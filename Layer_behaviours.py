# -*- coding: utf-8 -*-
"""
Module containing a class that holds typical layer behaviours that are used throughout the wizards
"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *

class TypicalLayers():
     """
     Class documentation goes here.
     """
     def __init__(self, LayerName):
        """
        Constructor
        """
        self.LayerName=LayerName
        

