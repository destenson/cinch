#------------------------------------------------------------------------------#
# Copyright (c) 2014 Los Alamos National Security, LLC
# All rights reserved.
#------------------------------------------------------------------------------#

import sys
import string
from collections import OrderedDict

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#

class Chapter():

	"""
	"""

	def __init__(self, title):

		"""
		"""

		self._title = title
		self._content = []

	# __init__

	def append(self, content):

		"""
		"""

		self._content.append(content)

	# append

	def print_content(self):

		"""
		"""

		for line in self._content:
			sys.stdout.write(line)
		# for

	# print

	def str_content(self):
		# Don't use any seperator
		return string.join(self._content, '')
	# str_content

#------------------------------------------------------------------------------#
# Document class
#------------------------------------------------------------------------------#

class Document():

	"""
	"""

	def __init__(self, title):

		"""
		"""

		self._chapters = OrderedDict()
		self._title = title

	# __init__

	def title(self):
		return self._title
	# title

	def chapter(self, title):

		"""
		"""

		if not title in self._chapters:
			self._chapters[title] = Chapter(title)

		return self._chapters[title]
	# chapter

	def chapters(self):
		return self._chapters
	# chapters

	def add_chapter(self, title, obj=None):
		if obj:
			self._chapters[title] = obj
		elif not title in self._chapters:
			self._chapters[title] = Chapter(title)
	# add_chapter			
		
	def delete_chapter(self, title):
		del self._chapters[title]

	def print_content(self):
		for chapter in self._chapters:
			self._chapters[chapter].print_content()
	# print_content

	def write(self, output):
		with open(output, 'w+') as f:
			for chapter in self._chapters:
				f.write(self._chapters[chapter].str_content())
	# write

# Document
