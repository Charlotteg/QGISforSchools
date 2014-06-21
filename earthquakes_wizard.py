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
from qgis.analysis import *

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
        self.score = 0
        self.magAnsClicks = 0
        self.q1 = False
        self.scoreLabels = [self.Score_label,  self.Score_label_2,  self.Score_label_3]
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
        layer = QgsMapLayerRegistry.instance().mapLayersByName("earthquakes")[0]
        field = self.scaleComboBox.currentText()
        state = self.scaleCheckBox.checkState()
        if state:
            self.scaleComboBox.setEnabled(True)
            self.label_17.setEnabled(True)
            self.label_16.setEnabled(True)
            if field == "Magnitude":
                expression = "(Magnitude^3)/10"
            elif field == "latitude":
                expression = "abs(latitude)/5"
            else:
                expression = "abs(longitude)/5"
            colourManager().propSymbols(layer,  expression)
        else:
            colourManager().propSymbols(layer,  "2")
            self.scaleComboBox.setEnabled(False)
            self.label_17.setEnabled(False)
            self.label_16.setEnabled(False)

    @pyqtSignature("QString")
    def on_scaleComboBox_activated(self,  p0):
        """
        scale earthquake symbols  based on the field chosen in scaleComboBox
        """
        layer = QgsMapLayerRegistry.instance().mapLayersByName("earthquakes")[0]
        field = self.scaleComboBox.currentText()
        if field == "Magnitude":
            expression = "(Magnitude^3)/10"
        elif field == "latitude":
            expression = "abs(latitude)/5"
        else:
            expression = "abs(longitude)/5"
        colourManager().propSymbols(layer,  expression)
 
    @pyqtSignature("") 
    def on_checkAnswersMag_released(self):
        """
        check answers and add points if correct based on the number of answers already submitted
        """
        
        self.magAnsClicks += 1
        self.score,  self.q1 = ScoreSystem(self.score).checkAnswers(self.magAnsClicks,  self.twoFour,  self.q1,  1)
        ScoreSystem(self.score).updateScore(self.scoreLabels)


#*************************************** Page 5 *****************************************************************************

    @pyqtSignature("")
    def on_bufferBrowseButton_clicked(self):
        """
        Open a File Browser Dialog to select location to save new layer
        """
        
        inputFile = QFileDialog.getSaveFileName(self, 'Save As','', 'Shapefiles (*.shp)')
        self.bufferLineEdit.setText(inputFile)

    
    @pyqtSignature("") 
    def on_bufferButton_clicked(self):
        """
        create buffer
        """
        AddLayers().CheckBufferLayer(self.inputComboBox, self.bufferLineEdit,  self.distanceLineEdit,  self.bufferProgressBar)


#*************************************** Page 6 *****************************************************************************

    @pyqtSignature("") 
    def on_transparencyButton_clicked(self):
        earthquakes = QgsMapLayerRegistry.instance().mapLayersByName("earthquakes")[0]
        plates = QgsMapLayerRegistry.instance().mapLayersByName("earthquakes")[0]
        countries = QgsMapLayerRegistry.instance().mapLayersByName("earthquakes")[0]
        layers = QgsMapLayerRegistry.instance().mapLayers()
        for layer in layers:
            if layer != earthquakes and layer != plates and layer != countries:
               bufferLayer = layer
        alpha = self.alphaSlider.value()
        bufferLayer.setLayerTransparency(alpha)
        print "yo"

