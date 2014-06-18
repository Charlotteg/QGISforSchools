# -*- coding: utf-8 -*-

"""
Module implementing EarthquakesWizard.
"""
# Import the Python, PyQt and QGIS libraries
import ntpath
import numpy as np
import math

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

#Import other classes required here
from score import ScoreSystem
from colours import colourManager
from misc_classes import CitiesCustomSortingModel,  CountriesCustomSortingModel
from addlayers import AddLayers

from Ui_earthquakes_wizard import Ui_EQWizard

class EarthquakesWizard(QWizard, Ui_EQWizard):
    """
    Class defining the functionality of the earthquakes unit of the QGISforSchools Plugin 
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QWizard.__init__(self, parent)
        self.setupUi(self)
        
#*************************************** Page 2 *****************************************************************************
    @pyqtSignature("")
    def on_countriesBrowseButton_clicked(self):
        """
        Open a File Browser Dialog - for the countries layer and put the filepath in the line edit 
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open countries.shp','', 'Shapefiles (*.shp)')
        self.countriesLineEdit.setText(inputFile)
        
    def on_platesBrowseButton_clicked(self):
        """
        Open a File Browser Dialog - for the plateboundaries layer and put the filepath in the line edit 
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open plateboundaries.shp','', 'Shapefiles (*.shp)')
        self.countrieslineEdit.setText(inputFile)
    
    def on_eqBrowseButton_clicked(self):
        """
        Open a File Browser Dialog - for the plateboundaries layer and put the filepath in the line edit 
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open earthquakes.shp','', 'Shapefiles (*.shp)')
        self.countrieslineEdit.setText(inputFile)
        
    def on_AddCountriesLayerButton_clicked(self):
        """
        Add the layers to the map canvas
        """
        countrieslineEdit = self.countriesLineEdit
        platesLineEdit = self.platesLineEdit
        eqLineEdit = self.eqLineEdit
        
        Countries = AddLayers().CheckAddLayers(countrieslineEdit,  "countries")
        plates = AddLayers().CheckAddLayers(countrieslineEdit,  "plate")
        earthquakes = AddLayers().CheckAddLayers(eqLineEdit,  "earthquakes")
        
        if Countries is not None:
            CountriesRenderer = Countries.rendererV2()
            CountriesSymbol = CountriesRenderer.symbol()
            CountriesSymbol.setColor(QColor('#31a354'))
            
        
        QgsMapLayerRegistry.instance().addMapLayer(Countries) 
        QgsMapLayerRegistry.instance().addMapLayer(plates)
        QgsMapLayerRegistry.instance().addMapLayer(earthquakes)
        
        iface.actionMapTips().trigger()
        
        
