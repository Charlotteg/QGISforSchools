# -*- coding: utf-8 -*-

"""
Module implementing MarkerDialog.
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from magicMarkers import MagicMarkers
from colours import colourManager

from Ui_marker_dialog import Ui_Dialog


class MarkerDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, attribute, tableView,  parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.svgDict = None
        self.scene = None
        self.attribute = attribute
        self.tableView = tableView
        self.svgDict,  self.scene = MagicMarkers().viewSVGs(self.SVGView)
    
    @pyqtSignature("")
    def on_buttonBox_accepted(self):
        """
        Slot documentation goes here.
        """
        if self.svgDict != None:
            MagicMarkers().setSVG("tourist_attraction", self.attribute , self.scene,  self.svgDict)
            attractions = QgsMapLayerRegistry.instance().mapLayersByName("tourist_attraction")[0]
            colourManager().makeClassTable(attractions,  "LEGEND",  self.tableView)

        self.close()
    
    @pyqtSignature("")
    def on_buttonBox_rejected(self):
        """
        Slot documentation goes here.
        """
        self.close()
    
    @pyqtSignature("QString")
    def on_comboBox_activated(self, p0):
        """
        Slot documentation goes here.
        """
        self.svgDict,  self.scene = MagicMarkers().viewSVGs(self.SVGView)
