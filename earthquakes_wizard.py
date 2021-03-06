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
from attributeTable import AttributeTable
from query import SpatialQuery
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
        #WindowStaysOnTopHint so that the plugin stays on top of the QGIS window when the user scrolls and pans the map etc.
        QWizard.__init__(self, parent,  Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        #initialise variables that are used in multiple functions
        self.score = 0
        self.magAnsClicks = 0
        self.distAnsClicks = 0
        self.numAnsClicks = 0
        self.eqAnsClicks = 0
        self.effAnsClicks = 0
        self.numAnsClicks2 = 0
        self.q1 = False
        self.q2 = False
        self.q3 = False
        self.q4 = False
        self.q5 = False
        self.q6 = False
        self.q7 = False
        self.scoreLabels = [self.Score_label,  self.Score_label_2,  self.Score_label_3,  self.Score_label_4,  self.Score_label_5,  self.Score_label_6,  self.Score_label_7,  self.Score_label_8,  self.Score_label_9,  self.Score_label_10,  self.Score_label_11,  self.Score_label_12,  self.Score_label_13]
        self.bufferLayer = None
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
        
        #Check the layers are valid
        Countries = AddLayers().CheckAddLayers(countriesLineEdit,  "countries")
        plates = AddLayers().CheckAddLayers(platesLineEdit,  "plate_boundaries")
        earthquakes = AddLayers().CheckAddLayers(eqLineEdit,  "earthquakes")
        
        #ensure the countries layer renders in a suitable colour
        if Countries is not None:
            CountriesRenderer = Countries.rendererV2()
            CountriesSymbol = CountriesRenderer.symbol()
            CountriesSymbol.setColor(QColor('#31a354'))
        
        #ensure that the correct CRS is set for the earthquakes layer
        if earthquakes is not None:
            earthquakes.setCrs(QgsCoordinateReferenceSystem(4326,  QgsCoordinateReferenceSystem.EpsgCrsId))
        
        #add layers and trigger map tips 'on'
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
            # Disable the categorised colour categories
            self.ColourRampcomboBox.setEnabled(False)
            self.ColumncomboBox.setEnabled(False)
            self.colourRampLabel.setEnabled(False)
            self.columnLabel.setEnabled(False)
            #enable the single colour button
            self.ChangeColourButton.setEnabled(True)
            #set the renderer to single symbol (i.e. all the same)
            symbol = QgsSymbolV2.defaultSymbol(earthquakes.geometryType())
            earthquakes.setRendererV2(QgsSingleSymbolRendererV2(symbol))
            #refresh the within-plugin legend
            model = QStandardItemModel(0, 0)
            model.clear()
            self.earthquakeTableView.setModel(model)
            
        else:
            #Enable the categorised colour categories
            self.ColourRampcomboBox.setEnabled(True)
            self.ColumncomboBox.setEnabled(True)
            self.colourRampLabel.setEnabled(True)
            self.columnLabel.setEnabled(True)
            # disable the single colour button
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
        #If checkbox is checked, then set proportional symbols based on the field chosen
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
        #turn off proportional symbols
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
        #set expression for proportional areas based on chosen field
        if field == "Magnitude":
            expression = "(Magnitude^3)/10"
        elif field == "latitude":
            expression = "abs(latitude)/5"
        else:
            expression = "abs(longitude)/5"
        #make symbols proportional
        colourManager().propSymbols(layer,  expression)
 
    @pyqtSignature("") 
    def on_checkAnswersMag_released(self):
        """
        check answers to q1 and add points if correct based on the number of answers already submitted
        """
        # log the number of times that the check answers button has been clicked
        self.magAnsClicks += 1
        #check answers and update score
        self.score,  self.q1 = ScoreSystem(self.score).checkAnswers(self.magAnsClicks,  self.twoFour,  self.q1,  1)
        ScoreSystem(self.score).updateScore(self.scoreLabels,  self.starView)


#*************************************** Page 5 *****************************************************************************

    @pyqtSignature("")
    def on_bufferBrowseButton_clicked(self):
        """
        Open a File Browser Dialog to select location to save new layer
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getSaveFileName(self, 'Save As','', 'Shapefiles (*.shp)')
        self.bufferLineEdit.setText(inputFile)

    
    @pyqtSignature("") 
    def on_bufferButton_clicked(self):
        """
        create buffer
        """
        self.bufferLayer = AddLayers().CheckBufferLayer(self.inputComboBox, self.bufferLineEdit,  self.distanceLineEdit)


#*************************************** Page 6 *****************************************************************************

    @pyqtSignature("") 
    def on_bufferColourButton_clicked(self):
        """
        change the colour of the buffer layer
        """
        #set up message box
        msgBox=QMessageBox()
        msgBox.setIcon(3)
        
        #If a buffer layer has been created, update the colours
        if self.bufferLayer is not None:
            colourManager().updateSingleColour(self.bufferLayer)
        #if not bring up a message box
        else:
            msgBox.setText("Could not re-colour the layer")
            msgBox.setInformativeText(" QGISforSchools cannot find the buffer layer. Try going back a step and making a new one.")
            msgBox.exec_()
        
        SpatialQuery().populateSrcBox(self.inputComboBox_2,  self.refComboBox)
        SpatialQuery().populateSrcBox(self.lyrComboBox)
        
    @pyqtSignature("") 
    def on_transparencyButton_clicked(self):
        """
        set transparency of the buffer layer
        """
        #get transparency percentage or 'alpha'
        alpha = self.alphaSpinBox.value()
        #if there is a buffer layer, change transparency
        if self.bufferLayer is not None:
            bufferLayer = QgsMapLayerRegistry.instance().mapLayersByName(self.bufferLayer)[0]
            bufferLayer.setLayerTransparency(alpha)
        else:
            pass
        
        #update map canvas and populate comboBox
        iface.mapCanvas().refresh()
        SpatialQuery().populateSrcBox(self.inputComboBox_2,  self.refComboBox)
        SpatialQuery().populateSrcBox(self.lyrComboBox)
        
    @pyqtSignature("") 
    def on_checkAnswersDist_clicked(self):
        """
        check answer to question 2 and assign points
        """
        # log the number of times that the check answers button has been clicked
        self.distAnsClicks += 1
        #check answers and update score
        self.score,  self.q2 = ScoreSystem(self.score).checkAnswers(self.distAnsClicks,  self.plates,  self.q2,  2)
        ScoreSystem(self.score).updateScore(self.scoreLabels,  self.starView)
        #update relevant combo boxes
        SpatialQuery().populateSrcBox(self.inputComboBox_2,  self.refComboBox)
        SpatialQuery().populateSrcBox(self.lyrComboBox)


#*************************************** Page 7 *****************************************************************************
    @pyqtSignature("QString")
    def on_inputComboBox_2_activated(self,  p0):
        """
        Populate the reference comboBox with all layers but the selected input layer and populate query comboBox
        """
        SpatialQuery().populateRefBox(self.inputComboBox_2,  self.refComboBox,  self.queryComboBox)
        SpatialQuery().populateSrcBox(self.lyrComboBox)
    

    @pyqtSignature("QString")
    def on_refComboBox_activated(self,  p0):
        """
        Populate the query combo box with options relevant to the input and reference layers chosen
        """
        SpatialQuery().populateSelBox(self.inputComboBox_2,  self.refComboBox,  self.queryComboBox)
        SpatialQuery().populateSrcBox(self.lyrComboBox)
        
        
    @pyqtSignature("") 
    def on_runQuery_clicked(self):
        """
        run the spatial query
        """
        SpatialQuery().startSpatialQuery(self.inputComboBox_2,  self.refComboBox,  self.queryComboBox,  self.newLayercheckBox,  self.queryLineEdit,  self.queryProgBar)
        #update combo box to including new layer
        SpatialQuery().populateSrcBox(self.lyrComboBox)
        #populate the attribute table
        AttributeTable().attributeTable(self.lyrComboBox, self.attribTableView)


    @pyqtSignature("") 
    def on_clearSelection_clicked(self):
        """
        clear selections
        """
        SpatialQuery().clearSelection()
    
    
    @pyqtSignature("") 
    def on_newLayercheckBox_clicked(self):
        """
        enable browse button and queryLineEdit
        """
        state = self.newLayercheckBox.checkState()
        
        if state:
            self.queryLineEdit.setEnabled(True)
            self.queryBrowseButton.setEnabled(True)
        else:
            self.queryLineEdit.setEnabled(False)
            self.queryBrowseButton.setEnabled(False)
    
    @pyqtSignature("") 
    def on_queryBrowseButton_clicked(self):
        """
        Open a File Browser Dialog to select location to save new layer
        """

        inputFile = QFileDialog.getSaveFileName(self, 'Save As','', 'Shapefiles (*.shp)')
        self.queryLineEdit.setText(inputFile)



#*************************************** Page 8 *****************************************************************************
    @pyqtSignature("QString")
    def on_lyrComboBox_activated(self,  p0):
        """
        fill the table view with an attribute table for that layer
        """
        AttributeTable().attributeTable(self.lyrComboBox, self.attribTableView)

    @pyqtSignature("") 
    def on_checkAnswersNum_clicked(self):
        """
        check answer to question 3 and assign points
        """
        # log the number of times that the check answers button has been clicked
        self.numAnsClicks += 1
        points = ScoreSystem(self.score).assignPoints(self.numAnsClicks)
        msgBox=QMessageBox()
        
        if self.numSpinBox.value() == 14736 and self.q3 == False:
            self.score += points
            self.q3 = True
            ScoreSystem(self.score).ansMsgBoxes(self.q3,  3)
            ScoreSystem(self.score).updateScore(self.scoreLabels,  self.starView)
        elif self.numSpinBox.value() == 14736 and self.q3 == True:
            msgBox.setText("Well done. Click Next to move on.")
            msgBox.exec_() 
        else:
            msgBox.setText("That is the wrong answer for question 3. Look at the attribute table and try again.")
            msgBox.exec_() 
            
#*************************************** Page 9 *****************************************************************************
    @pyqtSignature("") 
    def on_checkAnswersEQ_clicked(self):
        """
        check answer to questions 4 and 5 and assign points
        """
        # log the number of times that the check answers button has been clicked
        self.eqAnsClicks+= 1
        #check answers and update score
        self.score,  self.q4,  self.q5 = ScoreSystem(self.score).checkAnswers(self.eqAnsClicks,  self.epicentre,  self.q4,  4,  self.plateMovement,  self.q5,  5)
        ScoreSystem(self.score).updateScore(self.scoreLabels,  self.starView)
        
        #set check box names for next page
        
        layers = iface.legendInterface().layers()
        
        checkList = [self.lyrCheckBox,  self.lyrCheckBox_2,  self.lyrCheckBox_3,  self.lyrCheckBox_4,  self.lyrCheckBox_5]
        nameList = []
        
        for layer in layers:
            i = layers.index(layer)
            name = layer.name()
            if i <len(checkList):
                checkbox = checkList[i]
                checkbox.setText(name)

 
#*************************************** Page 10 *****************************************************************************

    def showHideLayers(self,  checkBox):
        """
        hide or show layer
        """
        #get layer name and checkbox toggle state
        layerName = checkBox.text()
        layer = QgsMapLayerRegistry.instance().mapLayersByName(layerName)[0]
        state = checkBox.checkState()
        legend = iface.legendInterface()
        
        #turn layer on and off
        if state:
            legend.setLayerVisible(layer,  True)
        else:
            legend.setLayerVisible(layer, False)


    @pyqtSignature("") 
    def on_lyrCheckBox_clicked(self):
        """
        hide or show layer
        """
        self.showHideLayers(self.lyrCheckBox)

    @pyqtSignature("") 
    def on_lyrCheckBox_2_clicked(self):
        """
        hide or show layer
        """
        self.showHideLayers(self.lyrCheckBox_2)

    @pyqtSignature("") 
    def on_lyrCheckBox_3_clicked(self):
        """
        hide or show layer
        """
        self.showHideLayers(self.lyrCheckBox_3)

    @pyqtSignature("") 
    def on_lyrCheckBox_4_clicked(self):
        """
        hide or show layer
        """
        self.showHideLayers(self.lyrCheckBox_4)
    
    @pyqtSignature("") 
    def on_lyrCheckBox_5_clicked(self):
        """
        hide or show layer
        """
        self.showHideLayers(self.lyrCheckBox_5)

    @pyqtSignature("") 
    def on_checkAnswersEffects_clicked(self):
        """
        check answer to questions 4 and 5 and assign points
        """
        # log the number of times that the check answers button has been clicked
        self.effAnsClicks+= 1
        #check answers and update score
        self.score,  self.q6 = ScoreSystem(self.score).checkAnswers(self.effAnsClicks,  self.shake,  self.q6,  6)
        ScoreSystem(self.score).updateScore(self.scoreLabels,  self.starView)
        SpatialQuery().populateSrcBox(self.inputComboBox_3)

#*************************************** Page 11 *****************************************************************************

    @pyqtSignature("")
    def on_equatorBrowseButton_clicked(self):
        """
        Open a File Browser Dialog - for the countries layer and put the filepath in the line edit 
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open equator.shp','', 'Shapefiles (*.shp)')
        self.equatorLineEdit.setText(inputFile)

    @pyqtSignature("")
    def on_AddLayerButton_2_clicked(self):
        """
        Add the equator to the map canvas
        """
        #Check the layers are valid
        equator = AddLayers().CheckAddLayers(self.equatorLineEdit,  "equator")
        #add the map layer if valid
        QgsMapLayerRegistry.instance().addMapLayer(equator)
        #populate boxes on the next page
        SpatialQuery().populateSrcBox(self.inputComboBox_3)
        SpatialQuery().populateSrcBox(self.inputComboBox_4,  self.refComboBox_2)
        
    @pyqtSignature("")
    def on_bufferBrowseButton_2_clicked(self):
        """
        Open a File Browser Dialog to select location to save new layer
        """
        inputFile = QFileDialog.getSaveFileName(self, 'Save As','', 'Shapefiles (*.shp)')
        self.bufferLineEdit_2.setText(inputFile)

    
    @pyqtSignature("") 
    def on_bufferButton_2_clicked(self):
        """
        create buffer
        """
        self.bufferLayer = AddLayers().CheckBufferLayer(self.inputComboBox_3, self.bufferLineEdit_2,  self.distanceLineEdit_2)


#*************************************** Page 12 *****************************************************************************

    @pyqtSignature("QString")
    def on_inputComboBox_4_activated(self,  p0):
        """
        Populate the reference comboBox with all layers but the selected input layer and populate query comboBox
        """
        SpatialQuery().populateRefBox(self.inputComboBox_4,  self.refComboBox_2,  self.queryComboBox_2)
#        SpatialQuery().populateSrcBox(self.lyrComboBox)
    

    @pyqtSignature("QString")
    def on_refComboBox_2_activated(self,  p0):
        """
        Populate the query combo box with options relevant to the input and reference layers chosen
        """
        SpatialQuery().populateSelBox(self.inputComboBox_4,  self.refComboBox_2,  self.queryComboBox_2)
        SpatialQuery().populateSrcBox(self.lyrComboBox_2)
        
        
    @pyqtSignature("") 
    def on_runQuery_2_clicked(self):
        """
        run the spatial query
        """
        SpatialQuery().startSpatialQuery(self.inputComboBox_4,  self.refComboBox_2,  self.queryComboBox_2,  self.newLayercheckBox_2,  self.queryLineEdit_2,  self.queryProgBar_2)
        #update combobox
        SpatialQuery().populateSrcBox(self.lyrComboBox_2)
        #update attribute table
        AttributeTable().attributeTable(self.lyrComboBox_2, self.attribTableView_2)


    @pyqtSignature("") 
    def on_clearSelection_2_clicked(self):
        """
        clear selections
        """
        SpatialQuery().clearSelection()
    
    
    @pyqtSignature("") 
    def on_newLayercheckBox_2_clicked(self):
        """
        enable browse button and queryLineEdit
        """
        state = self.newLayercheckBox_2.checkState()
        
        if state:
            self.queryLineEdit_2.setEnabled(True)
            self.queryBrowseButton_2.setEnabled(True)
        else:
            self.queryLineEdit_2.setEnabled(False)
            self.queryBrowseButton_2.setEnabled(False)
    
    @pyqtSignature("") 
    def on_queryBrowseButton_2_clicked(self):
        """
        Open a File Browser Dialog to select location to save new layer
        """

        inputFile = QFileDialog.getSaveFileName(self, 'Save As','', 'Shapefiles (*.shp)')
        self.queryLineEdit_2.setText(inputFile)

#*************************************** Page 13 *****************************************************************************

    @pyqtSignature("QString")
    def on_lyrComboBox_2_activated(self,  p0):
        """
        fill the table view with an attribute table for that layer
        """
        AttributeTable().attributeTable(self.lyrComboBox_2, self.attribTableView_2)

    @pyqtSignature("") 
    def on_checkAnswersNum_2_clicked(self):
        """
        check answer to question 7 and assign points
        """
        # log the number of times that the check answers button has been clicked
        self.numAnsClicks2 += 1
        points = ScoreSystem(self.score).assignPoints(self.numAnsClicks)
        msgBox=QMessageBox()
        
        #check for right answers and add points if correct. Alert user if wrong.
        if self.numSpinBox_2.value() == 4465 and self.q7 == False:
            self.score += points
            self.q7 = True
            ScoreSystem(self.score).ansMsgBoxes(self.q7,  7)
            ScoreSystem(self.score).updateScore(self.scoreLabels,  self.starView)
        elif self.numSpinBox_2.value() == 4465 and self.q7 == True:
            msgBox.setText("Well done. Click Next to move on.")
            msgBox.exec_() 
        else:
            msgBox.setText("That is the wrong answer for question 7. Look at the attribute table and try again.")
            msgBox.exec_() 

