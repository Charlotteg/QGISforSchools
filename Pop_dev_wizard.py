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
    
    @pyqtSignature("")
    def on___qt__passive_wizardbutton0_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
    
    @pyqtSignature("")
    def on___qt__passive_wizardbutton1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
    
    @pyqtSignature("")
    def on_wizardPage1_completeChanged(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
    
    @pyqtSignature("")
    def on_wizardPage2_completeChanged(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
    
    @pyqtSignature("")
    def on___qt__passive_wizardbutton5_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
        
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
            

        return QgsMapLayerRegistry.instance().addMapLayer(Countries)
        
    
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
#    @pyqtSignature("")
#    def on_wizardPage2_completeChanged(self):
#        """
#        Slot documentation goes here.
#        """
#        Countries = QgsMapLayerRegistry.instance().mapLayersByName("countries")[0]
#        fields = Countries.pendingFields()
#        fieldList = []
#        self.ColumncomboBox.clear()
#        for field in fields:
#            fieldList.append(field.name())
#        print fieldList
#        self.ColumncomboBox.addItems(fieldList)
        
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
            #symbol.setColor(QColor('#31a354'))
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
            fields = Countries.pendingFields()
            fieldList = []
            for field in fields:
                fieldList.append(field.name())
            self.ColumncomboBox.addItems(fieldList[3:])
            #Populate the color ramp combobox with the names of the Color Brewer, color ramp schemes
            self.ColourRampcomboBox.clear()
            rampNames = QgsVectorColorBrewerColorRampV2.listSchemeNames()
            rampList = []
        
            for name in rampNames:
                rampList.append(name)
                colorRamp =QgsVectorColorBrewerColorRampV2.create()
                rampIcon = QgsSymbolLayerV2Utils.colorRampPreviewIcon(colorRamp,  QSize(50, 16))
                self.ColourRampcomboBox.addItem( name)
                
                
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
        self.makeClassTable()
        

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
            if len(icons)>1 :
                index = model.createIndex(row,  0)
                iconItem = QStandardItem(icons[row],  ' ') 
            #iconItem.setIcon(icons[row])
                #model.setData(index,  icons[0],  Qt.DecorationRole)
                model.setItem(row, 0,  iconItem)
                
        self.categoryTableView.setModel(model)
        
    def getIcons(self):
        Countries = QgsMapLayerRegistry.instance().mapLayersByName("countries")[0]
        renderer = Countries.rendererV2()
        symbols = renderer.symbols()
        print "symbols:"
        print symbols
        icons = []
        for symbol in symbols:
            icon = QgsSymbolLayerV2Utils.symbolPreviewIcon(symbol, QSize(50, 50))
            icons.append(icon)
            
        return icons

            
        


