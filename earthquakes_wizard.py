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
        QWizard.__init__(self, parent,  Qt.WindowStaysOnTopHint)
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

    @pyqtSignature("")
    def on_platesBrowseButton_clicked(self):
        """
        Open a File Browser Dialog - for the plate boundaries layer and put the filepath in the line edit 
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open plate_boundaries.shp','', 'Shapefiles (*.shp)')
        self.platesLineEdit.setText(inputFile)
   
    @pyqtSignature("")
    def on_eqBrowseButton_released(self):
        """
        Open a File Browser Dialog - for the earthquakes layer and put the filepath in the line edit 
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open earthquakes_2011.shp','', 'Shapefiles (*.shp)')
        self.eqLineEdit.setText(inputFile)

    @pyqtSignature("")
    def on_AddLayerButton_clicked(self):
        """
        Add the layers to the map canvas
        """
        countriesLineEdit = self.countriesLineEdit
        platesLineEdit = self.platesLineEdit
        eqLineEdit = self.eqLineEdit
        
        Countries = AddLayers().CheckAddLayers(countriesLineEdit,  "countries")
        plates = AddLayers().CheckAddLayers(platesLineEdit,  "plate_boundaries")
        earthquakes = AddLayers().CheckAddLayers(eqLineEdit,  "earthquakes")
        
        if Countries is not None:
            CountriesRenderer = Countries.rendererV2()
            CountriesSymbol = CountriesRenderer.symbol()
            CountriesSymbol.setColor(QColor('#31a354'))
            
        earthquakes.setCrs(QgsCoordinateReferenceSystem(4326,  QgsCoordinateReferenceSystem.EpsgCrsId))
        layerList = [Countries,  plates,  earthquakes]
        QgsMapLayerRegistry.instance().addMapLayers(layerList)
        iface.actionMapTips().trigger()
        
#*************************************** Page 3 *****************************************************************************

        
    @pyqtSignature("")
    def on_ChangeColourButton_clicked(self):
        """
        Allow the user to select a single colour for the Countries layer
        """
        colourManager().updateSingleColour("earthquakes")
        
    @pyqtSignature("QString")
    def on_StyleTypecomboBox_activated(self,  p0):
        """
        Enable or disable the column/colour ramp comboBoxes or the colour selection button depending on what style type is selected
        """
        style = self.StyleTypecomboBox.currentText()
        earthquakes = QgsMapLayerRegistry.instance().mapLayersByName("earthquakes")[0]
        
        if style == "Single Colour":
            self.ColourRampcomboBox.setEnabled(False)
            self.ColumncomboBox.setEnabled(False)
            self.colourRampLabel.setEnabled(False)
            self.columnLabel.setEnabled(False)
            self.ChangeColourButton.setEnabled(True)
            symbol = QgsSymbolV2.defaultSymbol(earthquakes.geometryType())
            earthquakes.setRendererV2(QgsSingleSymbolRendererV2(symbol))
            model = QStandardItemModel(0, 0)
            model.clear()
            self.earthquakeTableView.setModel(model)
            
        else:
            self.ColourRampcomboBox.setEnabled(True)
            self.ColumncomboBox.setEnabled(True)
            self.colourRampLabel.setEnabled(True)
            self.columnLabel.setEnabled(True)
            self.ChangeColourButton.setEnabled(False) 
            
            #Populate the countries column comboBox with the layer fields that you can style by
            self.ColumncomboBox.clear()
            fields = earthquakes.pendingFields()
            fieldList = []
            for field in fields:
                fieldList.append(field.name())
            self.ColumncomboBox.addItems(fieldList[1:4])

            #Populate the color ramp combobox with the names of the Color Brewer, color ramp schemes
            self.ColourRampcomboBox.clear()

            rampNames = QgsVectorColorBrewerColorRampV2.listSchemeNames()
        
            for name in rampNames:
                self.ColourRampcomboBox.addItem(name)
                
                
            #self.makeClassTable()
            tableViews = self.earthquakeTableView
            colourManager().setGraduatedColour("earthquakes",  self.ColumncomboBox,  self.ColourRampcomboBox,  5,  self.earthquakeTableView)
        
        
    @pyqtSignature("QString")
    def on_ColourRampcomboBox_activated(self,  p0):
        """
        classify the chosen field and colour each class based on the colour ramp selected
        """
        tableViews = self.earthquakeTableView
        colourManager().setGraduatedColour("earthquakes",  self.ColumncomboBox,  self.ColourRampcomboBox, 5, tableViews)



    @pyqtSignature("QString")
    def on_ColumncomboBox_activated(self,  p0):
        """
        Change classified values based on selected column
        """
        tableViews = self.earthquakeTableView
        colourManager().setGraduatedColour("earthquakes",  self.ColumncomboBox,  self.ColourRampcomboBox, 5, tableViews)

#*************************************** Page 4 *****************************************************************************

    @pyqtSignature("")
    def on_scaleCheckBox_clicked(self):
        """
        set the earthquake symbols to proportional or standard based on checkbox state
        """
        layer = QgsMapLayerRegistry.instance().mapLayersByName("countries")[0]
        state = self.countriesCheckBox.checkState()
        if state:
            return None
        else:
            return None
