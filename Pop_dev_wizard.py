# -*- coding: utf-8 -*-

"""
Module implementing PopDevWizard.
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
from Ui_Pop_dev_wizard import Ui_PopDevWizard

class PopDevWizard(QWizard, Ui_PopDevWizard):
    """
    Class defining the functionality of the Population & Development unit of the QGISforSchools Plugin
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        #WindowStaysOnTopHint so that the plugin stays on top of the QGIS window when the user scrolls and pans the map etc.
        QWizard.__init__(self, parent,  Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        #initialise variables that are used in multiple functions
        self.userPos = None
        self.popAnsClicks = 0
        self.devAnsClicks = 0
        self.obsAnsClicks = 0
        self.popDensAnsClicks = 0
        self.score = 0
        self.q1 = False
        self.q2 = False
        self.q3 = False
        self.q4 = False
        self.q5 = False
        self.q6 = False
        self.q7 = False
        self.scoreLabels = [self.Score_label,  self.Score_label_2,  self.Score_label_3,  self.Score_label_4,  self.Score_label_5, self.Score_label_6,  self.Score_label_7,  self.Score_label_8,  self.Score_label_9,  self.Score_label_10]
        
       
#*************************************** Page 2 *****************************************************************************
    @pyqtSignature("")
    def on_CountriesBrowseButton_clicked(self):
        """
        Open a File Browser Dialog - for the countries layer
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open Countries.shp','', 'Shapefiles (*.shp)')
        self.CountrieslineEdit.setText(inputFile)
        
    @pyqtSignature("")
    def on_AddCountriesLayerButton_clicked(self):
        """
        Add the layers to the map canvas
        """
        CountrieslineEdit = self.CountrieslineEdit
        
        Countries = AddLayers().CheckAddLayers(CountrieslineEdit,  "countries")
        
        if Countries is not None:
            CountriesRenderer = Countries.rendererV2()
            CountriesSymbol = CountriesRenderer.symbol()
            CountriesSymbol.setColor(QColor('#31a354'))
            
        
        return QgsMapLayerRegistry.instance().addMapLayer(Countries),  iface.actionMapTips().trigger()
        
            

#*************************************** Page 3 *****************************************************************************

        
    @pyqtSignature("")
    def on_ChangeColourButton_clicked(self):
        """
        Allow the user to select a single colour for the Countries layer
        """
        colourManager().updateSingleColour("countries")
        
    @pyqtSignature("QString")
    def on_StyleTypecomboBox_activated(self,  p0):
        """
        Enable or disable the column/colour ramp comboBoxes or the colour selection button depending on what style type is selected
        """
        style = self.StyleTypecomboBox.currentText()
        Countries = QgsMapLayerRegistry.instance().mapLayersByName("countries")[0]
        
        if style == "Single Colour":
            self.ColourRampcomboBox.setEnabled(False)
            self.ColumncomboBox.setEnabled(False)
            self.colourRampLabel.setEnabled(False)
            self.columnLabel.setEnabled(False)
            self.ChangeColourButton.setEnabled(True)
            symbol = QgsSymbolV2.defaultSymbol(Countries.geometryType())
            Countries.setRendererV2(QgsSingleSymbolRendererV2(symbol))
            model = QStandardItemModel(0, 0)
            model.clear()
            self.categoryTableView.setModel(model)
            
        else:
            self.ColourRampcomboBox.setEnabled(True)
            self.ColumncomboBox.setEnabled(True)
            self.colourRampLabel.setEnabled(True)
            self.columnLabel.setEnabled(True)
            self.ChangeColourButton.setEnabled(False) 
            #Populate the countries column comboBox with the layer fields that you can style by
            self.ColumncomboBox.clear()
            self.ColumncomboBox_2.clear()
            self.ColumncomboBox_3.clear()
            fields = Countries.pendingFields()
            fieldList = []
            for field in fields:
                fieldList.append(field.name())
            self.ColumncomboBox.addItems(fieldList[3:])
            self.ColumncomboBox_2.addItems(fieldList[3:])
            self.ColumncomboBox_3.addItems(fieldList[3:])
            
            self.ColumncomboBox_2.setCurrentIndex(2)
            #Populate the color ramp combobox with the names of the Color Brewer, color ramp schemes
            self.ColourRampcomboBox.clear()
            self.ColourRampcomboBox_2.clear()
            rampNames = QgsVectorColorBrewerColorRampV2.listSchemeNames()
        
            for name in rampNames:
                self.ColourRampcomboBox.addItem(name)
                self.ColourRampcomboBox_2.addItem(name)
                self.ColourRampcomboBox_3.addItem(name)
                
                
            #self.makeClassTable()
            tableViews = [self.categoryTableView,  self.categoryTableView_2]
            colourManager().makeClassTable(Countries,  self.ColumncomboBox, tableViews)
        
        
    @pyqtSignature("QString")
    def on_ColourRampcomboBox_activated(self,  p0):
        """
        classify the chosen field and colour each class based on the colour ramp selected
        """
        #self.changeColumnColor()
        tableViews = [self.categoryTableView,  self.categoryTableView_2]
        colourManager().changeColumnColor("countries",  self.ColumncomboBox,  self.ColourRampcomboBox,  tableViews)


    @pyqtSignature("QString")
    def on_ColumncomboBox_activated(self,  p0):
        """
        Change classified values based on selected column
        """
        tableViews = [self.categoryTableView,  self.categoryTableView_2]
        colourManager().changeColumnColor("countries",  self.ColumncomboBox,  self.ColourRampcomboBox,  tableViews)


        
#*************************************** Page 4 *****************************************************************************

    def on_checkAnswersPop_released(self):
        """
        check answers and add points if correct based on the number of answers already submitted
        """
        self.popAnsClicks += 1
        self.score,  self.q1,  self.q2 = ScoreSystem(self.score).checkAnswers(self.popAnsClicks,  self.mediumPop,  self.q1,  1,  self.usaPop,  self.q2,  2)
        ScoreSystem(self.score).updateScore(self.scoreLabels,  self.starView)
            
            
    
    
#*************************************** Page 5 *****************************************************************************    
    @pyqtSignature("")
    def on_ChangeColourButton_2_clicked(self):
        """
        Allow the user to select a single colour for the Countries layer
        """
        colourManager().updateSingleColour("countries")
        
    @pyqtSignature("QString")
    def on_StyleTypecomboBox_2_activated(self,  p0):
        """
        Enable or disable the column/colour ramp comboBoxes or the colour selection button depending on what style type is selected
        """
        style = self.StyleTypecomboBox_2.currentText()
        Countries = QgsMapLayerRegistry.instance().mapLayersByName("countries")[0]
        
        if style == "Single Colour":
            self.ColourRampcomboBox_2.setEnabled(False)
            self.ColumncomboBox_2.setEnabled(False)
            self.colourRampLabel_2.setEnabled(False)
            self.columnLabel_2.setEnabled(False)
            self.ChangeColourButton_2.setEnabled(True)
            symbol = QgsSymbolV2.defaultSymbol(Countries.geometryType())
            Countries.setRendererV2(QgsSingleSymbolRendererV2(symbol))
            model = QStandardItemModel(0, 0)
            model.clear()
            self.categoryTableView.setModel(model)
            
        else:
            self.ColourRampcomboBox_2.setEnabled(True)
            self.ColumncomboBox_2.setEnabled(True)
            self.colourRampLabel_2.setEnabled(True)
            self.columnLabel_2.setEnabled(True)
            self.ChangeColourButton_2.setEnabled(False) 
            #Populate the countries column comboBox with the layer fields that you can style by
            self.ColumncomboBox_2.clear()
            fields = Countries.pendingFields()
            fieldList = []
            for field in fields:
                fieldList.append(field.name())
            self.ColumncomboBox_2.addItems(fieldList[3:])
            self.ColumncomboBox_2.setCurrentIndex(2)
            #Populate the color ramp combobox with the names of the Color Brewer, color ramp schemes
            self.ColourRampcomboBox_2.clear()
            rampNames = QgsVectorColorBrewerColorRampV2.listSchemeNames()
            rampList = []
        
            for name in rampNames:
                self.ColourRampcomboBox_2.addItem(name)
                
                
            tableViews = [self.categoryTableView,  self.categoryTableView_2]
            colourManager().makeClassTable(Countries,  self.ColumncomboBox_2, tableViews)

    @pyqtSignature("QString")
    def on_ColourRampcomboBox_2_activated(self,  p0):
        tableViews = [self.categoryTableView,  self.categoryTableView_2]
        colourManager().changeColumnColor("countries",  self.ColumncomboBox_2,  self.ColourRampcomboBox_2,  tableViews)
        

    @pyqtSignature("QString")
    def on_ColumncomboBox_2_activated(self,  p0):
        """
        Change classified values based on selected column
        """
        tableViews = [self.categoryTableView,  self.categoryTableView_2]
        colourManager().changeColumnColor("countries",  self.ColumncomboBox_2,  self.ColourRampcomboBox_2,  tableViews)
        
#*************************************** Page 6 *****************************************************************************    

    @pyqtSignature("")
    def on_checkAnswersDev_released(self):
        """
        check answers and add points if correct based on the number of answers already submitted
        """
        
        self.devAnsClicks += 1
        self.score,  self.q3,  self.q4 = ScoreSystem(self.score).checkAnswers(self.devAnsClicks,  self.africa,  self.q3,  3,  self.ufi,  self.q4,  4)
        ScoreSystem(self.score).updateScore(self.scoreLabels,  self.starView)
            
#*************************************** Page 7 *****************************************************************************    

    @pyqtSignature("")
    def on_obesityBrowseButton_clicked(self):
        """
        Open a File Browser Dialog - for the countries layer
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open obesity.shp','', 'Shapefiles (*.shp)')
        self.obesitylineEdit.setText(inputFile)
        
    @pyqtSignature("")
    def on_AddObesityLayerButton_clicked(self):
        """
        Add the layers to the map canvas
        """
        obesitylineEdit = self.obesitylineEdit
        
        obesityLayer = AddLayers().CheckAddLayers(obesitylineEdit,  "obesity")
        
        QgsMapLayerRegistry.instance().addMapLayer(obesityLayer)
        
        fields = obesityLayer.pendingFields()
        fieldList = []
        for field in fields:
            fieldList.append(field.name())
        self.obesityColumncomboBox.addItems(fieldList[10:])
    
#*************************************** Page 8 *****************************************************************************    


    @pyqtSignature("QString")
    def on_ColourRampcomboBox_3_activated(self,  p0):

        colourManager().changeColumnColor("countries",  self.ColumncomboBox_3,  self.ColourRampcomboBox_3)
        colourManager().changeColumnColor("obesity",  self.obesityColumncomboBox,  self.ColourRampcomboBox_3)
        colourManager().make3ClassTable("countries",  "obesity",  self.ColumncomboBox_3,  self.obesityColumncomboBox,  self.obesityTableView)
        
    @pyqtSignature("QString")
    def on_obesityColumncomboBox_activated(self,  p0):
        """
        Change classified values based on selected column
        """
        colourManager().changeColumnColor("countries",  self.ColumncomboBox_3,  self.ColourRampcomboBox_3)
        colourManager().changeColumnColor("obesity",  self.obesityColumncomboBox,  self.ColourRampcomboBox_3)
        colourManager().make3ClassTable("countries",  "obesity",  self.ColumncomboBox_3,  self.obesityColumncomboBox,  self.obesityTableView)
        
    @pyqtSignature("QString")
    def on_ColumncomboBox_3_activated(self,  p0):
        """
        Change classified values based on selected column
        """
        colourManager().changeColumnColor("countries",  self.ColumncomboBox_3,  self.ColourRampcomboBox_3)
        colourManager().changeColumnColor("obesity",  self.obesityColumncomboBox,  self.ColourRampcomboBox_3)
        colourManager().make3ClassTable("countries",  "obesity",  self.ColumncomboBox_3,  self.obesityColumncomboBox,  self.obesityTableView)
        
#*************************************** Page 9 *****************************************************************************    
#check box has been removed but code kept in case it should be re-instated
#    @pyqtSignature("")
#    def on_countriesCheckBox_clicked(self):
#        """
#        hide or show the countries layer depending on the state of the checkbox
#        """
#        layer = QgsMapLayerRegistry.instance().mapLayersByName("countries")[0]
#        state = self.countriesCheckBox.checkState()
#        legend = iface.legendInterface()
#        if state:
#            legend.setLayerVisible(layer,  True)
#        else:
#            legend.setLayerVisible(layer, False)
    
    @pyqtSignature("")
    def on_obesityCheckBox_clicked(self):
        """
        hide or show the countries layer depending on the state of the checkbox
        """
        layer = QgsMapLayerRegistry.instance().mapLayersByName("obesity")[0]
        state = self.obesityCheckBox.checkState()
        legend = iface.legendInterface()
        if state:
            legend.setLayerVisible(layer,  True)
        else:
            legend.setLayerVisible(layer, False)

    @pyqtSignature("")
    def on_checkAnswersObs_released(self):
        """
        check answers and add points if correct based on the number of answers already submitted
        """
        self.obsAnsClicks += 1
        self.score,  self.q5,  self.q6 = ScoreSystem(self.score).checkAnswers(self.obsAnsClicks,  self.hivhi,  self.q5,  5,  self.vLoOb,  self.q6,  6)
        ScoreSystem(self.score).updateScore(self.scoreLabels,  self.starView) 
  
#*************************************** Page 10*****************************************************************************      


    @pyqtSignature("")
    def on_checkAnswersPopDens_released(self):
        """
        check answers and add points if correct based on the number of answers already submitted
        """
        self.popDensAnsClicks += 1
        
        self.score,  self.q7 = ScoreSystem(self.score).checkAnswers(self.popDensAnsClicks,  self.a,  self.q7,  7)
        ScoreSystem(self.score).updateScore(self.scoreLabels,  self.starView) 
        
