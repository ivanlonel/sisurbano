# -*- coding: utf-8 -*-

"""
***************************************************************************
    ZHelpers.py
    ---------------------
    Date                 : September 2019
    Copyright            : (C) 2019 by Llactalab
    Email                : fastuller88 at gmail dot com
***************************************************************************
"""

__author__ = 'Johnatan Astudillo'
__date__ = 'July 2019'
__copyright__ = '(C) 2019, Llactalab'

import os
from qgis.gui import QgisInterface
from qgis.utils import iface
from qgis.core import QgsProcessing
import processing      
from .Zettings import *
from .ZProcesses import *

from qgis.core import QgsVectorLayer


# def getCurrentPath(self):
# 	folder = ''
# 	layers = iface.mapCanvas().layers() 
# 	for layer in layers: 
# 		# feedback.pushConsoleInfo(str((layer)))
# 		# feedback.pushConsoleInfo(str(layer.name()))
# 		nameLayer = layer.name()
# 		path =   layer.source()
# 		folder =  path.split(nameLayer)[0]
# 		folder = os.path.join(folder, 'SIS-OUTPUTS')
# 		folderExists = os.path.exists(folder)
# 		if not folderExists:
# 			os.makedirs(folder)
# 	return folder


def getCurrentPath(self, createFolder = True):
	folder = ''
	# layers = iface.mapCanvas().layers() 
	try:
		# layer = layers[len(layers) - 1]
		layer = iface.activeLayer()
		nameLayer = layer.name()
		path =   layer.source()
		folder =  path.split(nameLayer)[0]
		folder = os.path.join(folder, 'SIS-OUTPUTS')
		folderExists = os.path.exists(folder)
		if not folderExists and createFolder:
			os.makedirs(folder)

	except Exception as e:
		return ''
	else:
		pass
	finally:
		return folder

def getPath():
	folder = ''
	try:
		layer = iface.activeLayer()
		nameLayer = layer.name()
		path =   layer.source()
		folder =  path.split(nameLayer)[0]	
	except Exception as e:
		print(e)
	else:
		pass
	finally:
		return folder		

# def getCurrentPath(self):
# 	layers = iface.mapCanvas().layers() 
# 	layer = layers[0]
# 	folder = ''
# 	nameLayer = layer.name()
# 	sourceIn = iface.mapCanvas().currentLayer().name()
# 	folder = os.path.dirname(sourceIn)
# 	folder = os.path.join(folder, 'SIS-OUTPUTS')
# 	folderExists = os.path.exists(folder)
# 	if not folderExists:
# 		os.makedirs(folder)
# 	return folder

# def getCurrentPath(self):
# 	folder = ''
# 	sourceIn = self.iface.activeLayer().source()
# 	folder = os.path.dirname(sourceIn)
# 	folder = os.path.join(folder, 'SIS-OUTPUTS')
# 	folderExists = os.path.exists(folder)
# 	if not folderExists:
# 		os.makedirs(folder)
# 	return folder


def buildFullPathName(path, name):
	split = path.split('SIS-OUTPUTS')
	lenSplit = len(split)
	# print(lenSplit)
	if lenSplit > 2:
		path = split[0] + "SIS-OUTPUTS"
	# print(path)
	return os.path.join(path, name)
	# return os.path.join('', name)


def getPossibleAttrName():
	nameIndex = ''
	try:
		layerName = iface.activeLayer().name()
		nameIndex = exploreNames(layerName)
		return 
	except Exception as e:
		nameIndex = ''
	else:
		pass
	finally:
		return nameIndex

def exploreNames(name):
	result = ''
	for key in NAMES_INDEX:
		nameIndex = NAMES_INDEX[key][0]
		nameIndex = nameIndex.lower()
		name = name.lower()
		split = name.split(nameIndex)
		lenSplit = len(split)
		if lenSplit >= 2:
			result = nameIndex
	return result 


def getMaxMin(attr=''):
	values = 0, 0
	try:
		# pathLayer = iface.activeLayer().source()
		# layer = QgsVectorLayer(pathLayer, 'shape', "ogr")
		# isValid = isValidLayer(layer)
		# # if(isValidLayer):		
		# values = ''
		layer = iface.activeLayer()
		idx = layer.fields().indexFromName(attr)
		max = layer.maximumValue(idx)
		min = layer.minimumValue(idx)
		values = min, max
	except Exception as e:
		print(e)
		values = 0, 0	
	else:
		pass
	finally:
		return values		


def nameWithOuputExtension(name):
	return name + '.shp'


def isExistFile(path):
	return os.path.exists(path)


# def isValidLayer(layer):
#     if not layer.isValid():
#         print(layer.name(), "layer invalid.")
#         return False
#     else:
#         print(layer.name(), "layer valid.") 
#         return True

