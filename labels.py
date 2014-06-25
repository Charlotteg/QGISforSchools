# -*- coding: utf-8 -*-

"""
Module containing a class that deals with labelling

"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *  

class Label():
    """
    Class that deals with vector layer labels
    """
    
    def nameLabel(self,  layerName,  fieldName,  fontFamily = "Arial",  fontSize = 8, fontWeight = 50,  fontItalic = False, fontUnderline = False,  fontStrikeout = False,  ):
        
        layer = QgsMapLayerRegistry.instance().mapLayersByName(layerName)[0]
        layer.setCustomProperty("labeling",  "pal")
        layer.setCustomProperty("labeling/enabled",  "True")
        layer.setCustomProperty("labeling/fieldName",  fieldName)
        layer.setCustomProperty("labeling/fontFamily",  fontFamily)
        layer.setCustomProperty("labeling/fontSize",  str(fontSize))
        layer.setCustomProperty("labeling/fontWeight",  str(fontWeight))
        layer.setCustomProperty("labeling/fontItalic",  str(fontItalic))
        layer.setCustomProperty("labeling/fontUnderline",  str(fontUnderline))
        layer.setCustomProperty("labeling/fontStrikeout",  str(fontStrikeout))
        layer.setCustomProperty
        
        iface.mapCanvas().refresh()

    def chooseLabel(self,  layerName,  fieldName):
        
        fontBox = QFontDialog()
        fontBox.exec_()
        newFont = fontBox.currentFont()
        family = newFont.family()
        size = newFont.pointSize()
        weight = newFont.weight()
        underline = newFont.underline()
        italic = newFont.italic()
        strike = newFont.strikeOut()
        
        
        self.nameLabel(layerName,  fieldName,  family,  size,  weight,  italic,  underline, strike)


    def removeLabel(self,  layerName):
        
        layer = QgsMapLayerRegistry.instance().mapLayersByName(layerName)[0]
        layer.setCustomProperty("labeling/enabled",  "False")
        iface.mapCanvas().refresh()
