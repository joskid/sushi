#!/usr/bin/env python
# coding: utf-8

import os
import sys
import tarfile
import shutil

from sushi.core import conf
from sushi.exceptions import *


class TemplatesManager(object):
	def __init__(self):
		pass

	def list(self):
		return os.listdir(conf.get('paths', 'sushi_templates'))

	def add(self, path):
		if not os.path.isfile(path):
			raise TemplatesManagerException('Template is not gzipped tar file')
		if not tarfile.is_tarfile(path):
			raise TemplatesManagerException('Template is not gzipped tar file')
		src = path
		dst = conf.get('paths', 'sushi_templates')

		# Open tarfile
		tar = tarfile.open(src, 'r:gz')
		if tarfile.is_tarfile(src):
			tar.extractall(dst)
		else:
			raise TemplatesManagerException('Template is not gzipped tar file')

	def delete(self, name):
		if name not in self.list():
			raise TemplatesManagerException('Template %s not installed' % name)
		dst = os.path.join(conf.get('paths', 'sushi_templates'), name)
		shutil.rmtree(dst)

	def get(self, name):
		if name not in self.list():
			raise TemplatesManagerException('Template %s not available' % name)
		return os.path.join(conf.get('paths', 'sushi_templates'), name)
