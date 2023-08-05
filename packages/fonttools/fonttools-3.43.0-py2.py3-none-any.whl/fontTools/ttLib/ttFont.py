from __future__ import print_function, division, absolute_import
from fontTools.misc import xmlWriter
from fontTools.misc.py23 import *
from fontTools.misc.loggingTools import deprecateArgument
from fontTools.ttLib import TTLibError
from fontTools.ttLib.sfnt import SFNTReader, SFNTWriter
import os
import logging
import itertools

log = logging.getLogger(__name__)

class TTFont(object):

	"""The main font object. It manages file input and output, and offers
	a convenient way of accessing tables.
	Tables will be only decompiled when necessary, ie. when they're actually
	accessed. This means that simple operations can be extremely fast.
	"""

	def __init__(self, file=None, res_name_or_index=None,
			sfntVersion="\000\001\000\000", flavor=None, checkChecksums=False,
			verbose=None, recalcBBoxes=True, allowVID=False, ignoreDecompileErrors=False,
			recalcTimestamp=True, fontNumber=-1, lazy=None, quiet=None,
			_tableCache=None):

		"""The constructor can be called with a few different arguments.
		When reading a font from disk, 'file' should be either a pathname
		pointing to a file, or a readable file object.

		It we're running on a Macintosh, 'res_name_or_index' maybe an sfnt
		resource name or an sfnt resource index number or zero. The latter
		case will cause TTLib to autodetect whether the file is a flat file
		or a suitcase. (If it's a suitcase, only the first 'sfnt' resource
		will be read!)

		The 'checkChecksums' argument is used to specify how sfnt
		checksums are treated upon reading a file from disk:
			0: don't check (default)
			1: check, print warnings if a wrong checksum is found
			2: check, raise an exception if a wrong checksum is found.

		The TTFont constructor can also be called without a 'file'
		argument: this is the way to create a new empty font.
		In this case you can optionally supply the 'sfntVersion' argument,
		and a 'flavor' which can be None, 'woff', or 'woff2'.

		If the recalcBBoxes argument is false, a number of things will *not*
		be recalculated upon save/compile:
			1) 'glyf' glyph bounding boxes
			2) 'CFF ' font bounding box
			3) 'head' font bounding box
			4) 'hhea' min/max values
			5) 'vhea' min/max values
		(1) is needed for certain kinds of CJK fonts (ask Werner Lemberg ;-).
		Additionally, upon importing an TTX file, this option cause glyphs
		to be compiled right away. This should reduce memory consumption
		greatly, and therefore should have some impact on the time needed
		to parse/compile large fonts.

		If the recalcTimestamp argument is false, the modified timestamp in the
		'head' table will *not* be recalculated upon save/compile.

		If the allowVID argument is set to true, then virtual GID's are
		supported. Asking for a glyph ID with a glyph name or GID that is not in
		the font will return a virtual GID.   This is valid for GSUB and cmap
		tables. For SING glyphlets, the cmap table is used to specify Unicode
		values for virtual GI's used in GSUB/GPOS rules. If the gid N is requested
		and does not exist in the font, or the glyphname has the form glyphN
		and does not exist in the font, then N is used as the virtual GID.
		Else, the first virtual GID is assigned as 0x1000 -1; for subsequent new
		virtual GIDs, the next is one less than the previous.

		If ignoreDecompileErrors is set to True, exceptions raised in
		individual tables during decompilation will be ignored, falling
		back to the DefaultTable implementation, which simply keeps the
		binary data.

		If lazy is set to True, many data structures are loaded lazily, upon
		access only.  If it is set to False, many data structures are loaded
		immediately.  The default is lazy=None which is somewhere in between.
		"""

		for name in ("verbose", "quiet"):
			val = locals().get(name)
			if val is not None:
				deprecateArgument(name, "configure logging instead")
			setattr(self, name, val)

		self.lazy = lazy
		self.recalcBBoxes = recalcBBoxes
		self.recalcTimestamp = recalcTimestamp
		self.tables = {}
		self.reader = None

		# Permit the user to reference glyphs that are not int the font.
		self.last_vid = 0xFFFE # Can't make it be 0xFFFF, as the world is full unsigned short integer counters that get incremented after the last seen GID value.
		self.reverseVIDDict = {}
		self.VIDDict = {}
		self.allowVID = allowVID
		self.ignoreDecompileErrors = ignoreDecompileErrors

		if not file:
			self.sfntVersion = sfntVersion
			self.flavor = flavor
			self.flavorData = None
			return
		if not hasattr(file, "read"):
			closeStream = True
			# assume file is a string
			if res_name_or_index is not None:
				# see if it contains 'sfnt' resources in the resource or data fork
				from . import macUtils
				if res_name_or_index == 0:
					if macUtils.getSFNTResIndices(file):
						# get the first available sfnt font.
						file = macUtils.SFNTResourceReader(file, 1)
					else:
						file = open(file, "rb")
				else:
					file = macUtils.SFNTResourceReader(file, res_name_or_index)
			else:
				file = open(file, "rb")
		else:
			# assume "file" is a readable file object
			closeStream = False
			file.seek(0)

		if not self.lazy:
			# read input file in memory and wrap a stream around it to allow overwriting
			file.seek(0)
			tmp = BytesIO(file.read())
			if hasattr(file, 'name'):
				# save reference to input file name
				tmp.name = file.name
			if closeStream:
				file.close()
			file = tmp
		self._tableCache = _tableCache
		self.reader = SFNTReader(file, checkChecksums, fontNumber=fontNumber)
		self.sfntVersion = self.reader.sfntVersion
		self.flavor = self.reader.flavor
		self.flavorData = self.reader.flavorData

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		self.close()

	def close(self):
		"""If we still have a reader object, close it."""
		if self.reader is not None:
			self.reader.close()

	def save(self, file, reorderTables=True):
		"""Save the font to disk. Similarly to the constructor,
		the 'file' argument can be either a pathname or a writable
		file object.
		"""
		if not hasattr(file, "write"):
			if self.lazy and self.reader.file.name == file:
				raise TTLibError(
					"Can't overwrite TTFont when 'lazy' attribute is True")
			closeStream = True
			file = open(file, "wb")
		else:
			# assume "file" is a writable file object
			closeStream = False

		tmp = BytesIO()

		writer_reordersTables = self._save(tmp)

		if (reorderTables is None or writer_reordersTables or
				(reorderTables is False and self.reader is None)):
			# don't reorder tables and save as is
			file.write(tmp.getvalue())
			tmp.close()
		else:
			if reorderTables is False:
				# sort tables using the original font's order
				tableOrder = list(self.reader.keys())
			else:
				# use the recommended order from the OpenType specification
				tableOrder = None
			tmp.flush()
			tmp2 = BytesIO()
			reorderFontTables(tmp, tmp2, tableOrder)
			file.write(tmp2.getvalue())
			tmp.close()
			tmp2.close()

		if closeStream:
			file.close()

	def _save(self, file, tableCache=None):
		"""Internal function, to be shared by save() and TTCollection.save()"""

		if self.recalcTimestamp and 'head' in self:
			self['head']  # make sure 'head' is loaded so the recalculation is actually done

		tags = list(self.keys())
		if "GlyphOrder" in tags:
			tags.remove("GlyphOrder")
		numTables = len(tags)
		# write to a temporary stream to allow saving to unseekable streams
		writer = SFNTWriter(file, numTables, self.sfntVersion, self.flavor, self.flavorData)

		done = []
		for tag in tags:
			self._writeTable(tag, writer, done, tableCache)

		writer.close()

		return writer.reordersTables()

	def saveXML(self, fileOrPath, newlinestr=None, **kwargs):
		"""Export the font as TTX (an XML-based text file), or as a series of text
		files when splitTables is true. In the latter case, the 'fileOrPath'
		argument should be a path to a directory.
		The 'tables' argument must either be false (dump all tables) or a
		list of tables to dump. The 'skipTables' argument may be a list of tables
		to skip, but only when the 'tables' argument is false.
		"""

		writer = xmlWriter.XMLWriter(fileOrPath, newlinestr=newlinestr)
		self._saveXML(writer, **kwargs)
		writer.close()

	def _saveXML(self, writer,
		     writeVersion=True,
		     quiet=None, tables=None, skipTables=None, splitTables=False,
		     splitGlyphs=False, disassembleInstructions=True,
		     bitmapGlyphDataFormat='raw'):

		if quiet is not None:
			deprecateArgument("quiet", "configure logging instead")

		self.disassembleInstructions = disassembleInstructions
		self.bitmapGlyphDataFormat = bitmapGlyphDataFormat
		if not tables:
			tables = list(self.keys())
			if "GlyphOrder" not in tables:
				tables = ["GlyphOrder"] + tables
			if skipTables:
				for tag in skipTables:
					if tag in tables:
						tables.remove(tag)
		numTables = len(tables)

		if writeVersion:
			from fontTools import version
			version = ".".join(version.split('.')[:2])
			writer.begintag("ttFont", sfntVersion=repr(tostr(self.sfntVersion))[1:-1],
					ttLibVersion=version)
		else:
			writer.begintag("ttFont", sfntVersion=repr(tostr(self.sfntVersion))[1:-1])
		writer.newline()

		# always splitTables if splitGlyphs is enabled
		splitTables = splitTables or splitGlyphs

		if not splitTables:
			writer.newline()
		else:
			path, ext = os.path.splitext(writer.filename)
			fileNameTemplate = path + ".%s" + ext

		for i in range(numTables):
			tag = tables[i]
			if splitTables:
				tablePath = fileNameTemplate % tagToIdentifier(tag)
				tableWriter = xmlWriter.XMLWriter(tablePath,
						newlinestr=writer.newlinestr)
				tableWriter.begintag("ttFont", ttLibVersion=version)
				tableWriter.newline()
				tableWriter.newline()
				writer.simpletag(tagToXML(tag), src=os.path.basename(tablePath))
				writer.newline()
			else:
				tableWriter = writer
			self._tableToXML(tableWriter, tag, splitGlyphs=splitGlyphs)
			if splitTables:
				tableWriter.endtag("ttFont")
				tableWriter.newline()
				tableWriter.close()
		writer.endtag("ttFont")
		writer.newline()

	def _tableToXML(self, writer, tag, quiet=None, splitGlyphs=False):
		if quiet is not None:
			deprecateArgument("quiet", "configure logging instead")
		if tag in self:
			table = self[tag]
			report = "Dumping '%s' table..." % tag
		else:
			report = "No '%s' table found." % tag
		log.info(report)
		if tag not in self:
			return
		xmlTag = tagToXML(tag)
		attrs = dict()
		if hasattr(table, "ERROR"):
			attrs['ERROR'] = "decompilation error"
		from .tables.DefaultTable import DefaultTable
		if table.__class__ == DefaultTable:
			attrs['raw'] = True
		writer.begintag(xmlTag, **attrs)
		writer.newline()
		if tag == "glyf":
			table.toXML(writer, self, splitGlyphs=splitGlyphs)
		else:
			table.toXML(writer, self)
		writer.endtag(xmlTag)
		writer.newline()
		writer.newline()

	def importXML(self, fileOrPath, quiet=None):
		"""Import a TTX file (an XML-based text format), so as to recreate
		a font object.
		"""
		if quiet is not None:
			deprecateArgument("quiet", "configure logging instead")

		if "maxp" in self and "post" in self:
			# Make sure the glyph order is loaded, as it otherwise gets
			# lost if the XML doesn't contain the glyph order, yet does
			# contain the table which was originally used to extract the
			# glyph names from (ie. 'post', 'cmap' or 'CFF ').
			self.getGlyphOrder()

		from fontTools.misc import xmlReader

		reader = xmlReader.XMLReader(fileOrPath, self)
		reader.read()

	def isLoaded(self, tag):
		"""Return true if the table identified by 'tag' has been
		decompiled and loaded into memory."""
		return tag in self.tables

	def has_key(self, tag):
		if self.isLoaded(tag):
			return True
		elif self.reader and tag in self.reader:
			return True
		elif tag == "GlyphOrder":
			return True
		else:
			return False

	__contains__ = has_key

	def keys(self):
		keys = list(self.tables.keys())
		if self.reader:
			for key in list(self.reader.keys()):
				if key not in keys:
					keys.append(key)

		if "GlyphOrder" in keys:
			keys.remove("GlyphOrder")
		keys = sortedTagList(keys)
		return ["GlyphOrder"] + keys

	def __len__(self):
		return len(list(self.keys()))

	def __getitem__(self, tag):
		tag = Tag(tag)
		try:
			return self.tables[tag]
		except KeyError:
			if tag == "GlyphOrder":
				table = GlyphOrder(tag)
				self.tables[tag] = table
				return table
			if self.reader is not None:
				import traceback
				log.debug("Reading '%s' table from disk", tag)
				data = self.reader[tag]
				if self._tableCache is not None:
					table = self._tableCache.get((Tag(tag), data))
					if table is not None:
						return table
				tableClass = getTableClass(tag)
				table = tableClass(tag)
				self.tables[tag] = table
				log.debug("Decompiling '%s' table", tag)
				try:
					table.decompile(data, self)
				except:
					if not self.ignoreDecompileErrors:
						raise
					# fall back to DefaultTable, retaining the binary table data
					log.exception(
						"An exception occurred during the decompilation of the '%s' table", tag)
					from .tables.DefaultTable import DefaultTable
					file = StringIO()
					traceback.print_exc(file=file)
					table = DefaultTable(tag)
					table.ERROR = file.getvalue()
					self.tables[tag] = table
					table.decompile(data, self)
				if self._tableCache is not None:
					self._tableCache[(Tag(tag), data)] = table
				return table
			else:
				raise KeyError("'%s' table not found" % tag)

	def __setitem__(self, tag, table):
		self.tables[Tag(tag)] = table

	def __delitem__(self, tag):
		if tag not in self:
			raise KeyError("'%s' table not found" % tag)
		if tag in self.tables:
			del self.tables[tag]
		if self.reader and tag in self.reader:
			del self.reader[tag]

	def get(self, tag, default=None):
		try:
			return self[tag]
		except KeyError:
			return default

	def setGlyphOrder(self, glyphOrder):
		self.glyphOrder = glyphOrder

	def getGlyphOrder(self):
		try:
			return self.glyphOrder
		except AttributeError:
			pass
		if 'CFF ' in self:
			cff = self['CFF ']
			self.glyphOrder = cff.getGlyphOrder()
		elif 'post' in self:
			# TrueType font
			glyphOrder = self['post'].getGlyphOrder()
			if glyphOrder is None:
				#
				# No names found in the 'post' table.
				# Try to create glyph names from the unicode cmap (if available)
				# in combination with the Adobe Glyph List (AGL).
				#
				self._getGlyphNamesFromCmap()
			else:
				self.glyphOrder = glyphOrder
		else:
			self._getGlyphNamesFromCmap()
		return self.glyphOrder

	def _getGlyphNamesFromCmap(self):
		#
		# This is rather convoluted, but then again, it's an interesting problem:
		# - we need to use the unicode values found in the cmap table to
		#   build glyph names (eg. because there is only a minimal post table,
		#   or none at all).
		# - but the cmap parser also needs glyph names to work with...
		# So here's what we do:
		# - make up glyph names based on glyphID
		# - load a temporary cmap table based on those names
		# - extract the unicode values, build the "real" glyph names
		# - unload the temporary cmap table
		#
		if self.isLoaded("cmap"):
			# Bootstrapping: we're getting called by the cmap parser
			# itself. This means self.tables['cmap'] contains a partially
			# loaded cmap, making it impossible to get at a unicode
			# subtable here. We remove the partially loaded cmap and
			# restore it later.
			# This only happens if the cmap table is loaded before any
			# other table that does f.getGlyphOrder()  or f.getGlyphName().
			cmapLoading = self.tables['cmap']
			del self.tables['cmap']
		else:
			cmapLoading = None
		# Make up glyph names based on glyphID, which will be used by the
		# temporary cmap and by the real cmap in case we don't find a unicode
		# cmap.
		numGlyphs = int(self['maxp'].numGlyphs)
		glyphOrder = [None] * numGlyphs
		glyphOrder[0] = ".notdef"
		for i in range(1, numGlyphs):
			glyphOrder[i] = "glyph%.5d" % i
		# Set the glyph order, so the cmap parser has something
		# to work with (so we don't get called recursively).
		self.glyphOrder = glyphOrder

		# Make up glyph names based on the reversed cmap table. Because some
		# glyphs (eg. ligatures or alternates) may not be reachable via cmap,
		# this naming table will usually not cover all glyphs in the font.
		# If the font has no Unicode cmap table, reversecmap will be empty.
		if 'cmap' in self:
			reversecmap = self['cmap'].buildReversed()
		else:
			reversecmap = {}
		useCount = {}
		for i in range(numGlyphs):
			tempName = glyphOrder[i]
			if tempName in reversecmap:
				# If a font maps both U+0041 LATIN CAPITAL LETTER A and
				# U+0391 GREEK CAPITAL LETTER ALPHA to the same glyph,
				# we prefer naming the glyph as "A".
				glyphName = self._makeGlyphName(min(reversecmap[tempName]))
				numUses = useCount[glyphName] = useCount.get(glyphName, 0) + 1
				if numUses > 1:
					glyphName = "%s.alt%d" % (glyphName, numUses - 1)
				glyphOrder[i] = glyphName

		if 'cmap' in self:
			# Delete the temporary cmap table from the cache, so it can
			# be parsed again with the right names.
			del self.tables['cmap']
			self.glyphOrder = glyphOrder
			if cmapLoading:
				# restore partially loaded cmap, so it can continue loading
				# using the proper names.
				self.tables['cmap'] = cmapLoading

	@staticmethod
	def _makeGlyphName(codepoint):
		from fontTools import agl  # Adobe Glyph List
		if codepoint in agl.UV2AGL:
			return agl.UV2AGL[codepoint]
		elif codepoint <= 0xFFFF:
			return "uni%04X" % codepoint
		else:
			return "u%X" % codepoint

	def getGlyphNames(self):
		"""Get a list of glyph names, sorted alphabetically."""
		glyphNames = sorted(self.getGlyphOrder())
		return glyphNames

	def getGlyphNames2(self):
		"""Get a list of glyph names, sorted alphabetically,
		but not case sensitive.
		"""
		from fontTools.misc import textTools
		return textTools.caselessSort(self.getGlyphOrder())

	def getGlyphName(self, glyphID, requireReal=False):
		try:
			return self.getGlyphOrder()[glyphID]
		except IndexError:
			if requireReal or not self.allowVID:
				# XXX The ??.W8.otf font that ships with OSX uses higher glyphIDs in
				# the cmap table than there are glyphs. I don't think it's legal...
				return "glyph%.5d" % glyphID
			else:
				# user intends virtual GID support
				try:
					glyphName = self.VIDDict[glyphID]
				except KeyError:
					glyphName  ="glyph%.5d" % glyphID
					self.last_vid = min(glyphID, self.last_vid )
					self.reverseVIDDict[glyphName] = glyphID
					self.VIDDict[glyphID] = glyphName
				return glyphName

	def getGlyphID(self, glyphName, requireReal=False):
		if not hasattr(self, "_reverseGlyphOrderDict"):
			self._buildReverseGlyphOrderDict()
		glyphOrder = self.getGlyphOrder()
		d = self._reverseGlyphOrderDict
		if glyphName not in d:
			if glyphName in glyphOrder:
				self._buildReverseGlyphOrderDict()
				return self.getGlyphID(glyphName)
			else:
				if requireReal:
					raise KeyError(glyphName)
				elif not self.allowVID:
					# Handle glyphXXX only
					if glyphName[:5] == "glyph":
						try:
							return int(glyphName[5:])
						except (NameError, ValueError):
							raise KeyError(glyphName)
				else:
					# user intends virtual GID support
					try:
						glyphID = self.reverseVIDDict[glyphName]
					except KeyError:
						# if name is in glyphXXX format, use the specified name.
						if glyphName[:5] == "glyph":
							try:
								glyphID = int(glyphName[5:])
							except (NameError, ValueError):
								glyphID = None
						if glyphID is None:
							glyphID = self.last_vid -1
							self.last_vid = glyphID
						self.reverseVIDDict[glyphName] = glyphID
						self.VIDDict[glyphID] = glyphName
					return glyphID

		glyphID = d[glyphName]
		if glyphName != glyphOrder[glyphID]:
			self._buildReverseGlyphOrderDict()
			return self.getGlyphID(glyphName)
		return glyphID

	def getReverseGlyphMap(self, rebuild=False):
		if rebuild or not hasattr(self, "_reverseGlyphOrderDict"):
			self._buildReverseGlyphOrderDict()
		return self._reverseGlyphOrderDict

	def _buildReverseGlyphOrderDict(self):
		self._reverseGlyphOrderDict = d = {}
		glyphOrder = self.getGlyphOrder()
		for glyphID in range(len(glyphOrder)):
			d[glyphOrder[glyphID]] = glyphID

	def _writeTable(self, tag, writer, done, tableCache=None):
		"""Internal helper function for self.save(). Keeps track of
		inter-table dependencies.
		"""
		if tag in done:
			return
		tableClass = getTableClass(tag)
		for masterTable in tableClass.dependencies:
			if masterTable not in done:
				if masterTable in self:
					self._writeTable(masterTable, writer, done, tableCache)
				else:
					done.append(masterTable)
		done.append(tag)
		tabledata = self.getTableData(tag)
		if tableCache is not None:
			entry = tableCache.get((Tag(tag), tabledata))
			if entry is not None:
				log.debug("reusing '%s' table", tag)
				writer.setEntry(tag, entry)
				return
		log.debug("writing '%s' table to disk", tag)
		writer[tag] = tabledata
		if tableCache is not None:
			tableCache[(Tag(tag), tabledata)] = writer[tag]

	def getTableData(self, tag):
		"""Returns raw table data, whether compiled or directly read from disk.
		"""
		tag = Tag(tag)
		if self.isLoaded(tag):
			log.debug("compiling '%s' table", tag)
			return self.tables[tag].compile(self)
		elif self.reader and tag in self.reader:
			log.debug("Reading '%s' table from disk", tag)
			return self.reader[tag]
		else:
			raise KeyError(tag)

	def getGlyphSet(self, preferCFF=True):
		"""Return a generic GlyphSet, which is a dict-like object
		mapping glyph names to glyph objects. The returned glyph objects
		have a .draw() method that supports the Pen protocol, and will
		have an attribute named 'width'.

		If the font is CFF-based, the outlines will be taken from the 'CFF ' or
		'CFF2' tables. Otherwise the outlines will be taken from the 'glyf' table.
		If the font contains both a 'CFF '/'CFF2' and a 'glyf' table, you can use
		the 'preferCFF' argument to specify which one should be taken. If the
		font contains both a 'CFF ' and a 'CFF2' table, the latter is taken.
		"""
		glyphs = None
		if (preferCFF and any(tb in self for tb in ["CFF ", "CFF2"]) or
		   ("glyf" not in self and any(tb in self for tb in ["CFF ", "CFF2"]))):
			table_tag = "CFF2" if "CFF2" in self else "CFF "
			glyphs = _TTGlyphSet(self,
			    list(self[table_tag].cff.values())[0].CharStrings, _TTGlyphCFF)

		if glyphs is None and "glyf" in self:
			glyphs = _TTGlyphSet(self, self["glyf"], _TTGlyphGlyf)

		if glyphs is None:
			raise TTLibError("Font contains no outlines")

		return glyphs

	def getBestCmap(self, cmapPreferences=((3, 10), (0, 6), (0, 4), (3, 1), (0, 3), (0, 2), (0, 1), (0, 0))):
		"""Return the 'best' unicode cmap dictionary available in the font,
		or None, if no unicode cmap subtable is available.

		By default it will search for the following (platformID, platEncID)
		pairs:
			(3, 10), (0, 6), (0, 4), (3, 1), (0, 3), (0, 2), (0, 1), (0, 0)
		This can be customized via the cmapPreferences argument.
		"""
		return self["cmap"].getBestCmap(cmapPreferences=cmapPreferences)


class _TTGlyphSet(object):

	"""Generic dict-like GlyphSet class that pulls metrics from hmtx and
	glyph shape from TrueType or CFF.
	"""

	def __init__(self, ttFont, glyphs, glyphType):
		self._glyphs = glyphs
		self._hmtx = ttFont['hmtx']
		self._vmtx = ttFont['vmtx'] if 'vmtx' in ttFont else None
		self._glyphType = glyphType

	def keys(self):
		return list(self._glyphs.keys())

	def has_key(self, glyphName):
		return glyphName in self._glyphs

	__contains__ = has_key

	def __getitem__(self, glyphName):
		horizontalMetrics = self._hmtx[glyphName]
		verticalMetrics = self._vmtx[glyphName] if self._vmtx else None
		return self._glyphType(
			self, self._glyphs[glyphName], horizontalMetrics, verticalMetrics)

	def __len__(self):
		return len(self._glyphs)

	def get(self, glyphName, default=None):
		try:
			return self[glyphName]
		except KeyError:
			return default

class _TTGlyph(object):

	"""Wrapper for a TrueType glyph that supports the Pen protocol, meaning
	that it has .draw() and .drawPoints() methods that take a pen object as
	their only argument. Additionally there are 'width' and 'lsb' attributes,
	read from the 'hmtx' table.

	If the font contains a 'vmtx' table, there will also be 'height' and 'tsb'
	attributes.
	"""

	def __init__(self, glyphset, glyph, horizontalMetrics, verticalMetrics=None):
		self._glyphset = glyphset
		self._glyph = glyph
		self.width, self.lsb = horizontalMetrics
		if verticalMetrics:
			self.height, self.tsb = verticalMetrics
		else:
			self.height, self.tsb = None, None

	def draw(self, pen):
		"""Draw the glyph onto Pen. See fontTools.pens.basePen for details
		how that works.
		"""
		self._glyph.draw(pen)

	def drawPoints(self, pen):
		# drawPoints is only implemented for _TTGlyphGlyf at this time.
		raise NotImplementedError()

class _TTGlyphCFF(_TTGlyph):
	pass

class _TTGlyphGlyf(_TTGlyph):

	def draw(self, pen):
		"""Draw the glyph onto Pen. See fontTools.pens.basePen for details
		how that works.
		"""
		glyfTable = self._glyphset._glyphs
		glyph = self._glyph
		offset = self.lsb - glyph.xMin if hasattr(glyph, "xMin") else 0
		glyph.draw(pen, glyfTable, offset)

	def drawPoints(self, pen):
		"""Draw the glyph onto PointPen. See fontTools.pens.pointPen
		for details how that works.
		"""
		glyfTable = self._glyphset._glyphs
		glyph = self._glyph
		offset = self.lsb - glyph.xMin if hasattr(glyph, "xMin") else 0
		glyph.drawPoints(pen, glyfTable, offset)


class GlyphOrder(object):

	"""A pseudo table. The glyph order isn't in the font as a separate
	table, but it's nice to present it as such in the TTX format.
	"""

	def __init__(self, tag=None):
		pass

	def toXML(self, writer, ttFont):
		glyphOrder = ttFont.getGlyphOrder()
		writer.comment("The 'id' attribute is only for humans; "
				"it is ignored when parsed.")
		writer.newline()
		for i in range(len(glyphOrder)):
			glyphName = glyphOrder[i]
			writer.simpletag("GlyphID", id=i, name=glyphName)
			writer.newline()

	def fromXML(self, name, attrs, content, ttFont):
		if not hasattr(self, "glyphOrder"):
			self.glyphOrder = []
			ttFont.setGlyphOrder(self.glyphOrder)
		if name == "GlyphID":
			self.glyphOrder.append(attrs["name"])


def getTableModule(tag):
	"""Fetch the packer/unpacker module for a table.
	Return None when no module is found.
	"""
	from . import tables
	pyTag = tagToIdentifier(tag)
	try:
		__import__("fontTools.ttLib.tables." + pyTag)
	except ImportError as err:
		# If pyTag is found in the ImportError message,
		# means table is not implemented.  If it's not
		# there, then some other module is missing, don't
		# suppress the error.
		if str(err).find(pyTag) >= 0:
			return None
		else:
			raise err
	else:
		return getattr(tables, pyTag)


def getTableClass(tag):
	"""Fetch the packer/unpacker class for a table.
	Return None when no class is found.
	"""
	module = getTableModule(tag)
	if module is None:
		from .tables.DefaultTable import DefaultTable
		return DefaultTable
	pyTag = tagToIdentifier(tag)
	tableClass = getattr(module, "table_" + pyTag)
	return tableClass


def getClassTag(klass):
	"""Fetch the table tag for a class object."""
	name = klass.__name__
	assert name[:6] == 'table_'
	name = name[6:] # Chop 'table_'
	return identifierToTag(name)


def newTable(tag):
	"""Return a new instance of a table."""
	tableClass = getTableClass(tag)
	return tableClass(tag)


def _escapechar(c):
	"""Helper function for tagToIdentifier()"""
	import re
	if re.match("[a-z0-9]", c):
		return "_" + c
	elif re.match("[A-Z]", c):
		return c + "_"
	else:
		return hex(byteord(c))[2:]


def tagToIdentifier(tag):
	"""Convert a table tag to a valid (but UGLY) python identifier,
	as well as a filename that's guaranteed to be unique even on a
	caseless file system. Each character is mapped to two characters.
	Lowercase letters get an underscore before the letter, uppercase
	letters get an underscore after the letter. Trailing spaces are
	trimmed. Illegal characters are escaped as two hex bytes. If the
	result starts with a number (as the result of a hex escape), an
	extra underscore is prepended. Examples:
		'glyf' -> '_g_l_y_f'
		'cvt ' -> '_c_v_t'
		'OS/2' -> 'O_S_2f_2'
	"""
	import re
	tag = Tag(tag)
	if tag == "GlyphOrder":
		return tag
	assert len(tag) == 4, "tag should be 4 characters long"
	while len(tag) > 1 and tag[-1] == ' ':
		tag = tag[:-1]
	ident = ""
	for c in tag:
		ident = ident + _escapechar(c)
	if re.match("[0-9]", ident):
		ident = "_" + ident
	return ident


def identifierToTag(ident):
	"""the opposite of tagToIdentifier()"""
	if ident == "GlyphOrder":
		return ident
	if len(ident) % 2 and ident[0] == "_":
		ident = ident[1:]
	assert not (len(ident) % 2)
	tag = ""
	for i in range(0, len(ident), 2):
		if ident[i] == "_":
			tag = tag + ident[i+1]
		elif ident[i+1] == "_":
			tag = tag + ident[i]
		else:
			# assume hex
			tag = tag + chr(int(ident[i:i+2], 16))
	# append trailing spaces
	tag = tag + (4 - len(tag)) * ' '
	return Tag(tag)


def tagToXML(tag):
	"""Similarly to tagToIdentifier(), this converts a TT tag
	to a valid XML element name. Since XML element names are
	case sensitive, this is a fairly simple/readable translation.
	"""
	import re
	tag = Tag(tag)
	if tag == "OS/2":
		return "OS_2"
	elif tag == "GlyphOrder":
		return tag
	if re.match("[A-Za-z_][A-Za-z_0-9]* *$", tag):
		return tag.strip()
	else:
		return tagToIdentifier(tag)


def xmlToTag(tag):
	"""The opposite of tagToXML()"""
	if tag == "OS_2":
		return Tag("OS/2")
	if len(tag) == 8:
		return identifierToTag(tag)
	else:
		return Tag(tag + " " * (4 - len(tag)))



# Table order as recommended in the OpenType specification 1.4
TTFTableOrder = ["head", "hhea", "maxp", "OS/2", "hmtx", "LTSH", "VDMX",
				"hdmx", "cmap", "fpgm", "prep", "cvt ", "loca", "glyf",
				"kern", "name", "post", "gasp", "PCLT"]

OTFTableOrder = ["head", "hhea", "maxp", "OS/2", "name", "cmap", "post",
				"CFF "]

def sortedTagList(tagList, tableOrder=None):
	"""Return a sorted copy of tagList, sorted according to the OpenType
	specification, or according to a custom tableOrder. If given and not
	None, tableOrder needs to be a list of tag names.
	"""
	tagList = sorted(tagList)
	if tableOrder is None:
		if "DSIG" in tagList:
			# DSIG should be last (XXX spec reference?)
			tagList.remove("DSIG")
			tagList.append("DSIG")
		if "CFF " in tagList:
			tableOrder = OTFTableOrder
		else:
			tableOrder = TTFTableOrder
	orderedTables = []
	for tag in tableOrder:
		if tag in tagList:
			orderedTables.append(tag)
			tagList.remove(tag)
	orderedTables.extend(tagList)
	return orderedTables


def reorderFontTables(inFile, outFile, tableOrder=None, checkChecksums=False):
	"""Rewrite a font file, ordering the tables as recommended by the
	OpenType specification 1.4.
	"""
	inFile.seek(0)
	outFile.seek(0)
	reader = SFNTReader(inFile, checkChecksums=checkChecksums)
	writer = SFNTWriter(outFile, len(reader.tables), reader.sfntVersion, reader.flavor, reader.flavorData)
	tables = list(reader.keys())
	for tag in sortedTagList(tables, tableOrder):
		writer[tag] = reader[tag]
	writer.close()


def maxPowerOfTwo(x):
	"""Return the highest exponent of two, so that
	(2 ** exponent) <= x.  Return 0 if x is 0.
	"""
	exponent = 0
	while x:
		x = x >> 1
		exponent = exponent + 1
	return max(exponent - 1, 0)


def getSearchRange(n, itemSize=16):
	"""Calculate searchRange, entrySelector, rangeShift.
	"""
	# itemSize defaults to 16, for backward compatibility
	# with upstream fonttools.
	exponent = maxPowerOfTwo(n)
	searchRange = (2 ** exponent) * itemSize
	entrySelector = exponent
	rangeShift = max(0, n * itemSize - searchRange)
	return searchRange, entrySelector, rangeShift
