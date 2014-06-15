# -*- coding: utf-8 -*-

"""
Module implementing PopDevWizard.
"""
# Import the Python, PyQt and QGIS libraries
import ntpath
import numpy as np

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

#Import other classes required here
from misc_classes import CitiesCustomSortingModel,  CountriesCustomSortingModel
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
        #QWizard.__init__(self, parent)
        self.setupUi(self)
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
        
        Countries = self.CheckAddLayers(CountrieslineEdit,  "countries")
        
        
        if Countries is not None:
            CountriesRenderer = Countries.rendererV2()
            CountriesSymbol = CountriesRenderer.symbol()
            CountriesSymbol.setColor(QColor('#31a354'))
            
        
        return QgsMapLayerRegistry.instance().addMapLayer(Countries),  iface.actionMapTips().trigger()
        
    
    def CheckAddLayers(self, LineEditName,  LayerString): 
        """
        Performs checks to determine whether the layers to be added to the canvas:
        1. have not already been added
        2. have a file specified
        3. are valid
        4. are the correct layers
        
        Parameters: The name of the LineEdit that contains the filePath (LineEditName)
                        The string that you wish the layer to be called/shapefile name
        
        """

        LayerFile = LineEditName.text()
        NewLayer = QgsVectorLayer(LayerFile,  LayerString,  'ogr')
        LayerAdded = QgsMapLayerRegistry.instance().mapLayersByName(LayerString)
            
        msgBox=QMessageBox()
        msgBox.setIcon(3)
         
        #If the layer is already added, or the field has been left blank, do nothing
        if LayerAdded:
            return None
        elif not LayerFile:
            return None
        #If the file selected is not a vaild layer, execute an error message box
        elif not NewLayer.isValid():
            msgBox.setText("Could not load the " + LayerString + " layer")
            msgBox.setInformativeText(" Please make sure that you have used the Browse button to select " + LayerString +".shp")
            msgBox.exec_()
        elif LayerString not in LayerFile:
            msgBox.setText("You have chosen the wrong shapefile for " + LayerString + ".")
            msgBox.setInformativeText(" Please go back and select " + LayerString +".shp")
            msgBox.exec_()   
        else:
                
            return NewLayer 
            

#*************************************** Page 3 *****************************************************************************

        
    @pyqtSignature("")
    def on_ChangeColourButton_clicked(self):
        """
        Allow the user to select a single colour for the Countries layer
        """
        newColor = self.changeColour()
        
        Countries = QgsMapLayerRegistry.instance().mapLayersByName("countries")[0]
        CountriesRenderer = Countries.rendererV2()
        CountriesSymbol = CountriesRenderer.symbol()
        CountriesSymbol.setColor(newColor)
        
        #refresh the map and legend
        iface.mapCanvas().refresh()
        iface.legendInterface().refreshLayerSymbology(Countries)
        
    @pyqtSignature("")
    def changeColour(self):
        """
        Bring up the colour dialog box and return the selected colour
        """
        #Open the QColorDialog
        colorDialog = QColorDialog()
        colorDialog.exec_()
        
        #find & return selected colour
        colour = colorDialog.currentColor() 
        return colour
        
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
            #Populate the color ramp combobox with the names of the Color Brewer, color ramp schemes
            self.ColourRampcomboBox.clear()
            self.ColourRampcomboBox_2.clear()
            rampNames = QgsVectorColorBrewerColorRampV2.listSchemeNames()
            rampList = []
        
            for name in rampNames:
                #rampList.append(name)
                #colorRamp =QgsVectorColorBrewerColorRampV2.create()
                #rampIcon = QgsSymbolLayerV2Utils.colorRampPreviewIcon(colorRamp,  QSize(50, 16))
                self.ColourRampcomboBox.addItem(name)
                self.ColourRampcomboBox_2.addItem(name)
                self.ColourRampcomboBox_3.addItem(name)
                
                
            self.makeClassTable()
  
    @pyqtSignature("")
    def getAttributes(self, field):
        """
        get the sorted and deduplicated elements of the field passed
        """
        layer = QgsMapLayerRegistry.instance().mapLayersByName("countries")[0]

        feats = layer.getFeatures()
        
        fieldIndex = layer.fieldNameIndex(field)
        
        valueList = []
        
        for feat in feats:
            valueList.append(feat.attributes()[fieldIndex] )
        
        
        newValueList = sorted(set(valueList))
        
        return newValueList
        
        
    @pyqtSignature("QString")
    def on_ColourRampcomboBox_activated(self,  p0):
        """
        classify the chosen field and colour each class based on the colour ramp selected
        """
        self.changeColumnColor()
        
    def changeColumnColor(self):
        
        Countries = QgsMapLayerRegistry.instance().mapLayersByName("countries")[0]
        
        field = self.ColumncomboBox.currentText()
        colorScheme = self.ColourRampcomboBox.currentText()
        
        categories = self.getAttributes(field)
        numColors = len(categories)
        
        colors = QgsColorBrewerPalette.listSchemeColors(colorScheme, numColors )
        catList =[]
        
        for category in categories:
            colorIndex = categories.index(category)
            symbol = QgsSymbolV2.defaultSymbol(Countries.geometryType())
            symbol.setColor(colors[colorIndex])
            cat = QgsRendererCategoryV2(category, symbol ,  str(category))
            catList.append(cat)
        
        renderer = QgsCategorizedSymbolRendererV2(field, catList)
        
        Countries.setRendererV2(renderer)
        
        iface.mapCanvas().refresh()
        iface.legendInterface().refreshLayerSymbology(Countries)
        
        self.makeClassTable()


    @pyqtSignature("QString")
    def on_ColumncomboBox_activated(self,  p0):
        """
        Change classified values based on selected column
        """
        self.changeColumnColor()


    @pyqtSignature("")
    def makeClassTable(self):
        """
        make and show the table of classified field/ symbology
        """
        style = self.StyleTypecomboBox.currentText()
        field = self.ColumncomboBox.currentText()
        values = self.getAttributes(field)
        rows = len(values)
        cols = 2
        model = QStandardItemModel(rows,  cols) 
        model.setHorizontalHeaderItem(0, QStandardItem("Symbol"))
        model.setHorizontalHeaderItem(1, QStandardItem("Value"))
        icons = self.getIcons()

        
        for value in values:
            item = QStandardItem(value)
            row = values.index(value) 
            model.setItem(row,  1,  item)
            if row in range(len(icons)) :
                index = model.createIndex(row,  0)
                iconItem = QStandardItem(icons[row],  ' ') 
            #iconItem.setIcon(icons[row])
                #model.setData(index,  icons[0],  Qt.DecorationRole)
                model.setItem(row, 0,  iconItem)
                
        self.categoryTableView.setModel(model)
        self.categoryTableView_2.setModel(model)
        
    def getIcons(self):
        """
        make and return a list of Qicons from the symbols currently used to represent the countries layer
        """
        Countries = QgsMapLayerRegistry.instance().mapLayersByName("countries")[0]
        renderer = Countries.rendererV2()
        symbols = renderer.symbols()
        icons = []
        for symbol in symbols:
            icon = QgsSymbolLayerV2Utils.symbolPreviewIcon(symbol, QSize(50, 50))
            icons.append(icon)
            
        return icons
        
#*************************************** Page 4 *****************************************************************************

    def on_checkAnswersPop_released(self):
        """
        check answers and add points if correct based on the number of answers already submitted
        """
        self.popAnsClicks += 1
        points = self.assignPoints()
        
        if  self.mediumPop.isChecked() and self.usaPop.isChecked() and self.q1 == False and self.q2 == False:
            self.score += (2*points)
            self.q1 = True
            self.q2 = True
        elif self.mediumPop.isChecked() and self.q1 == False:
            self.score += points
            self.q1 = True
        elif self.usaPop.isChecked() and self.q2 == False:
            self.score += points
            self.q2 = True  
        else:
            self.score += 0
        
        self.ansMsgBoxes()
        self.updateScore()
        
    def assignPoints(self):
        """
        Assign a different number of points depending on the number of trials. i.e. 5 points for getting it right
        first time, 3 for getting it right second time and 1 point thereafter.
        """
        if self.popAnsClicks == 1:
            points = 5
        elif self.popAnsClicks == 2:
            points = 3
        else:
            points = 1

        return points
            

    def ansMsgBoxes(self):
        """
        show message boxes telling the user if they have got the questions right and informing them to move on
        or highlighting to the user which question they got wrong and telling them to try again.
        """
        msgBox=QMessageBox()
        if self.q1 == False and self.q2 == False:
            msgBox.setText("That is the wrong answer for question 1 and 2. Look at the map and try again.")
            msgBox.exec_() 
        elif self.q1 == False:
            msgBox.setText("That is the wrong answer for question 1. Look at the map and try again.")
            msgBox.exec_() 
        elif self.q2 == False:
            msgBox.setText("That is the wrong answer for question 2. Look at the map and try again.")
            msgBox.exec_() 
        else:
            msgBox.setText("Well done. Click Next to move on.")
            msgBox.exec_() 
            
    def updateScore(self):
        """
        update the score at the bottom of the window
        """
        self.Score_label.clear()
        self.Score_label_2.clear()
        self.Score_label_3.clear()
        self.Score_label_4.clear()
        self.Score_label_5.clear()
        self.Score_label_6.clear()
        self.Score_label_7.clear()
        self.Score_label_8.clear()
        self.Score_label_9.clear()
        self.Score_label.setText(str(self.score))
        self.Score_label_2.setText(str(self.score))
        self.Score_label_3.setText(str(self.score))
        self.Score_label_4.setText(str(self.score))
        self.Score_label_5.setText(str(self.score))
        self.Score_label_6.setText(str(self.score))
        self.Score_label_7.setText(str(self.score))
        self.Score_label_8.setText(str(self.score))
        self.Score_label_9.setText(str(self.score))
    
    
#*************************************** Page 5 *****************************************************************************    
    @pyqtSignature("")
    def on_ChangeColourButton_2_clicked(self):
        """
        Allow the user to select a single colour for the Countries layer
        """
        newColor = self.changeColour()
        
        Countries = QgsMapLayerRegistry.instance().mapLayersByName("countries")[0]
        CountriesRenderer = Countries.rendererV2()
        CountriesSymbol = CountriesRenderer.symbol()
        CountriesSymbol.setColor(newColor)
        
        #refresh the map and legend
        iface.mapCanvas().refresh()
        iface.legendInterface().refreshLayerSymbology(Countries)
        
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
            #symbol.setColor(QColor('#31a354'))
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
            #Populate the color ramp combobox with the names of the Color Brewer, color ramp schemes
            self.ColourRampcomboBox_2.clear()
            rampNames = QgsVectorColorBrewerColorRampV2.listSchemeNames()
            rampList = []
        
            for name in rampNames:
                #rampList.append(name)
                #colorRamp =QgsVectorColorBrewerColorRampV2.create()
                #rampIcon = QgsSymbolLayerV2Utils.colorRampPreviewIcon(colorRamp,  QSize(50, 16))
                self.ColourRampcomboBox_2.addItem(name)
                
                
            self.makeClassTable()
            self.makeClassTable2()

    @pyqtSignature("QString")
    def on_ColourRampcomboBox_2_activated(self,  p0):
        self.changeColumnColor2()
        
    def changeColumnColor2(self):
        """
        classify the chosen field and colour each class based on the colour ramp selected
        """
        Countries = QgsMapLayerRegistry.instance().mapLayersByName("countries")[0]
        
        field = self.ColumncomboBox_2.currentText()
        colorScheme = self.ColourRampcomboBox_2.currentText()
        
        categories = self.getAttributes(field)
        numColors = len(categories)
        
        colors = QgsColorBrewerPalette.listSchemeColors(colorScheme, numColors )
        catList =[]
        
        for category in categories:
            colorIndex = categories.index(category)
            symbol = QgsSymbolV2.defaultSymbol(Countries.geometryType())
            symbol.setColor(colors[colorIndex])
            cat = QgsRendererCategoryV2(category, symbol ,  str(category))
            catList.append(cat)
        
        renderer = QgsCategorizedSymbolRendererV2(field, catList)
        
        Countries.setRendererV2(renderer)
        
        iface.mapCanvas().refresh()
        iface.legendInterface().refreshLayerSymbology(Countries)
        
        self.makeClassTable()
        self.makeClassTable2()


    @pyqtSignature("QString")
    def on_ColumncomboBox_2_activated(self,  p0):
        """
        Change classified values based on selected column
        """
        self.changeColumnColor2()
        
    @pyqtSignature("")
    def makeClassTable2(self):
        """
        make and show the table of classified field/ symbology
        """
        style = self.StyleTypecomboBox_2.currentText()
        field = self.ColumncomboBox_2.currentText()
        values = self.getAttributes(field)
        rows = len(values)
        cols = 2
        model = QStandardItemModel(rows,  cols) 
        model.setHorizontalHeaderItem(0, QStandardItem("Symbol"))
        model.setHorizontalHeaderItem(1, QStandardItem("Value"))
        icons = self.getIcons()

        
        for value in values:
            item = QStandardItem(value)
            row = values.index(value) 
            model.setItem(row,  1,  item)
            if row in range(len(icons)) :
                index = model.createIndex(row,  0)
                iconItem = QStandardItem(icons[row],  ' ') 
            #iconItem.setIcon(icons[row])
                #model.setData(index,  icons[0],  Qt.DecorationRole)
                model.setItem(row, 0,  iconItem)
                
        self.categoryTableView.setModel(model)
        self.categoryTableView_2.setModel(model)
        
#*************************************** Page 6 *****************************************************************************    

    def on_checkAnswersDev_released(self):
        """
        check answers and add points if correct based on the number of answers already submitted
        """
        self.devAnsClicks += 1
        points = self.assignDevPoints()
        
        if  self.africa.isChecked() and self.ufi.isChecked() and self.q3 == False and self.q4 == False:
            self.score += (2*points)
            self.q3 = True
            self.q4 = True
        elif self.africa.isChecked() and self.q3 == False:
            self.score += points
            self.q3 = True
        elif self.ufi.isChecked() and self.q4 == False:
            self.score += points
            self.q4 = True  
        else:
            self.score += 0
        
        self.ansDevMsgBoxes()
        self.updateScore()
        
    def assignDevPoints(self):
        """
        Assign a different number of points depending on the number of trials. i.e. 5 points for getting it right
        first time, 3 for getting it right second time and 1 point thereafter.
        """
        if self.devAnsClicks == 1:
            points = 5
        elif self.devAnsClicks == 2:
            points = 3
        else:
            points = 1

        return points
        
    def ansDevMsgBoxes(self):
        """
        show message boxes telling the user if they have got the questions right and informing them to move on
        or highlighting to the user which question they got wrong and telling them to try again.
        """
        msgBox=QMessageBox()
        if self.q3 == False and self.q4 == False:
            msgBox.setText("That is the wrong answer for question 3 and 4. Look at the map and try again.")
            msgBox.exec_() 
        elif self.q3 == False:
            msgBox.setText("That is the wrong answer for question 3. Look at the map and try again.")
            msgBox.exec_() 
        elif self.q4 == False:
            msgBox.setText("That is the wrong answer for question 4. Look at the map and try again.")
            msgBox.exec_() 
        else:
            msgBox.setText("Well done. Click Next to move on.")
            msgBox.exec_() 
            
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
        
        obesityLayer = self.CheckAddLayers(obesitylineEdit,  "obesity")
        
        QgsMapLayerRegistry.instance().addMapLayer(obesityLayer)
        
        fields = obesityLayer.pendingFields()
        fieldList = []
        for field in fields:
            fieldList.append(field.name())
        self.obesityColumncomboBox.addItems(fieldList[10:])
    
#*************************************** Page 8 *****************************************************************************    


    @pyqtSignature("QString")
    def on_ColourRampcomboBox_3_activated(self,  p0):
        self.changeColumnColor3()
        self.changeObesityColumnColor()
        
    @pyqtSignature("QString")
    def on_obesityColumncomboBox_activated(self,  p0):
        """
        Change classified values based on selected column
        """
        self.changeColumnColor3()
        self.changeObesityColumnColor()
        
    @pyqtSignature("QString")
    def on_ColumncomboBox_3_activated(self,  p0):
        """
        Change classified values based on selected column
        """
        self.changeColumnColor3()
        self.changeObesityColumnColor()
        
    def changeColumnColor3(self):
        """
        classify the chosen field and colour each class based on the colour ramp selected
        """
        Countries = QgsMapLayerRegistry.instance().mapLayersByName("countries")[0]
        
        field = self.ColumncomboBox_3.currentText()
        colorScheme = self.ColourRampcomboBox_3.currentText()
        
        categories = self.getAttributes(field)
        numColors = len(categories)
        
        colors = QgsColorBrewerPalette.listSchemeColors(colorScheme, numColors )
        catList =[]
        
        for category in categories:
            colorIndex = categories.index(category)
            symbol = QgsSymbolV2.defaultSymbol(Countries.geometryType())
            symbol.setColor(colors[colorIndex])
            cat = QgsRendererCategoryV2(category, symbol ,  str(category))
            catList.append(cat)
        
        renderer = QgsCategorizedSymbolRendererV2(field, catList)
        
        Countries.setRendererV2(renderer)
        
        iface.mapCanvas().refresh()
        iface.legendInterface().refreshLayerSymbology(Countries)
        
        
    def changeObesityColumnColor(self):
        """
        classify the chosen field and colour each class based on the colour ramp selected
        """
 
        obesityLayer = QgsMapLayerRegistry.instance().mapLayersByName("obesity")[0]
        
        field = self.obesityColumncomboBox.currentText()
        colorScheme = self.ColourRampcomboBox_3.currentText()
        
        categories = self.getObesityAttributes(field)
        numColors = len(categories)
        
        colors = QgsColorBrewerPalette.listSchemeColors(colorScheme, numColors )
        catList =[]
        
        for category in categories:
            colorIndex = categories.index(category)
            symbol = QgsSymbolV2.defaultSymbol(obesityLayer.geometryType())
            symbol.setColor(colors[colorIndex])
            cat = QgsRendererCategoryV2(category, symbol ,  str(category))
            catList.append(cat)
        
        renderer = QgsCategorizedSymbolRendererV2(field, catList)
        
        obesityLayer.setRendererV2(renderer)
        
        iface.mapCanvas().refresh()
        iface.legendInterface().refreshLayerSymbology(obesityLayer)
        
        self.makeClassTable3()


    @pyqtSignature("")
    def makeClassTable3(self):
        """
        make and show the table of classified field/ symbology. This one has 3 columns: symbol, obesity value and income value
        """
        incomeField = self.ColumncomboBox_3.currentText()
        incomeValues = self.getAttributes(incomeField)
        obesityField = self.obesityColumncomboBox.currentText()
        obesityValues = self.getObesityAttributes(obesityField)
        rows = len(obesityValues)
        cols = 3
        model = QStandardItemModel(rows,  cols) 
        model.setHorizontalHeaderItem(0, QStandardItem("Symbol"))
        model.setHorizontalHeaderItem(1, QStandardItem("Obesity"))
        model.setHorizontalHeaderItem(2, QStandardItem("Income"))
        icons = self.getIcons()
        print obesityValues
        
        for value in obesityValues:
            item = QStandardItem(value)
            row = obesityValues.index(value) 
            model.setItem(row,  1,  item)
            if row in range(len(icons)) :
                index = model.createIndex(row,  0)
                iconItem = QStandardItem(icons[row],  ' ') 
                model.setItem(row, 0,  iconItem)
            if row in range(len(incomeValues)):
                incomeItem = QStandardItem(incomeValues[row])
                model.setItem(row, 2,  incomeItem)
                
        self.obesityTableView.setModel(model)
        
    @pyqtSignature("")
    def getObesityAttributes(self, field):
        """
        get the sorted and deduplicated elements of the field passed from the obesity layer
        """
        layer = QgsMapLayerRegistry.instance().mapLayersByName("obesity")[0]

        feats = layer.getFeatures()
        
        fieldIndex = layer.fieldNameIndex(field)
        
        valueList = []
        
        for feat in feats:
            valueList.append(feat.attributes()[fieldIndex] )
        
        
        newValueList = sorted(set(valueList))
        
        return newValueList
        
#*************************************** Page 9 *****************************************************************************    

    @pyqtSignature("")
    def on_countriesCheckBox_clicked(self):
        """
        hide or show the countries layer depending on the state of the checkbox
        """
        layer = QgsMapLayerRegistry.instance().mapLayersByName("countries")[0]
        state = self.countriesCheckBox.checkState()
        legend = iface.legendInterface()
        if state:
            legend.setLayerVisible(layer,  True)
        else:
            legend.setLayerVisible(layer, False)
    
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

    def on_checkAnswersObs_released(self):
        """
        check answers and add points if correct based on the number of answers already submitted
        """
        self.obsAnsClicks += 1
        points = self.assignObsPoints()
        
        if  self.hivhi.isChecked() and self.vLoOb.isChecked() and self.q5 == False and self.q6 == False:
            self.score += (2*points)
            self.q5 = True
            self.q6 = True
        elif self.hivhi.isChecked() and self.q5 == False:
            self.score += points
            self.q5 = True
        elif self.vLoOb.isChecked() and self.q6 == False:
            self.score += points
            self.q6 = True  
        else:
            self.score += 0
        
        self.ansObsMsgBoxes()
        self.updateScore()
        
    def assignObsPoints(self):
        """
        Assign a different number of points depending on the number of trials. i.e. 5 points for getting it right
        first time, 3 for getting it right second time and 1 point thereafter.
        """
        if self.obsAnsClicks == 1:
            points = 5
        elif self.obsAnsClicks == 2:
            points = 3
        else:
            points = 1

        return points
        
    def ansObsMsgBoxes(self):
        """
        show message boxes telling the user if they have got the questions right and informing them to move on
        or highlighting to the user which question they got wrong and telling them to try again.
        """
        msgBox=QMessageBox()
        if self.q5 == False and self.q6 == False:
            msgBox.setText("That is the wrong answer for question 5 and 6. Look at the map and try again.")
            msgBox.exec_() 
        elif self.q5 == False:
            msgBox.setText("That is the wrong answer for question 5. Look at the map and try again.")
            msgBox.exec_() 
        elif self.q6 == False:
            msgBox.setText("That is the wrong answer for question 6. Look at the map and try again.")
            msgBox.exec_() 
        else:
            msgBox.setText("Well done. Click Next to move on.")
            msgBox.exec_()   
  
#*************************************** Page 10*****************************************************************************      


    def on_checkAnswersPopDens_released(self):
        """
        check answers and add points if correct based on the number of answers already submitted
        """
        self.popDensAnsClicks += 1
        points = self.assignPopDensPoints()
        
        if  self.a.isChecked() and self.q7 == False:
            self.score += points
            self.q7 = True
        else:
            self.score += 0
        
        self.ansPopDensMsgBoxes()
        self.updateScore()
        
    def assignPopDensPoints(self):
        """
        Assign a different number of points depending on the number of trials. i.e. 5 points for getting it right
        first time, 3 for getting it right second time and 1 point thereafter.
        """
        if self.popDensAnsClicks == 1:
            points = 5
        elif self.popDensAnsClicks == 2:
            points = 3
        else:
            points = 1

        return points
        
    def ansPopDensMsgBoxes(self):
        """
        show message boxes telling the user if they have got the questions right and informing them to move on
        or highlighting to the user which question they got wrong and telling them to try again.
        """
        msgBox=QMessageBox()
    
        if self.q7 == False:
            msgBox.setText("That is the wrong answer for question 7. Look at the map and try again.")
            msgBox.exec_() 
        else:
            msgBox.setText("Well done. Click Next to move on.")
            msgBox.exec_()   
