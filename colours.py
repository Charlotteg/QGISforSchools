# -*- coding: utf-8 -*-

"""
Module containing a class that deals with changing the colour schemes of given layers
"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

class colourManager():

    def singleColourDialog(self):
        """
        Bring up the colour dialog box and return the selected colour
        """
        #Open the QColorDialog
        colorDialog = QColorDialog()
        colorDialog.exec_()
        
        #find & return selected colour
        colour = colorDialog.currentColor() 
        return colour
        
    def updateSingleColour(self,  layerName):
        """
        Allow the user to select a single colour
        """
        newColor = self.singleColourDialog()
        
        layer = QgsMapLayerRegistry.instance().mapLayersByName(layerName)[0]
        layerRenderer = layer.rendererV2()
        layerSymbol = layerRenderer.symbol()
        layerSymbol.setColor(newColor)
        
        #refresh the map and legend
        iface.mapCanvas().refresh()
        iface.legendInterface().refreshLayerSymbology(layer)

        
    def changeColumnColor(self,  layerName,  ColumncomboBox,  ColourRampcomboBox,  tableViews):
        
        Layer = QgsMapLayerRegistry.instance().mapLayersByName(layerName)[0]
        
        field = ColumncomboBox.currentText()
        colorScheme = ColourRampcomboBox.currentText()
        
        categories = self.getAttributes(field,  Layer)
        numColors = len(categories)
        
        colors = QgsColorBrewerPalette.listSchemeColors(colorScheme, numColors)
        catList =[]
        
        for category in categories:
            colorIndex = categories.index(category)
            symbol = QgsSymbolV2.defaultSymbol(Layer.geometryType())
            symbol.setColor(colors[colorIndex])
            cat = QgsRendererCategoryV2(category, symbol ,  str(category))
            catList.append(cat)
        
        renderer = QgsCategorizedSymbolRendererV2(field, catList)
        
        Layer.setRendererV2(renderer)
        
        iface.mapCanvas().refresh()
        iface.legendInterface().refreshLayerSymbology(Layer)
        
        self.makeClassTable(Layer,  ColumncomboBox, tableViews)
        
    def getAttributes(self, field,  layer):
        """
        get the sorted and deduplicated elements of the field passed
        """

        feats = layer.getFeatures()
        
        fieldIndex = layer.fieldNameIndex(field)
        
        valueList = []
        
        for feat in feats:
            valueList.append(feat.attributes()[fieldIndex] )
        
        
        newValueList = sorted(set(valueList))
        
        return newValueList
        
    def getIcons(self,  layer):
        """
        make and return a list of Qicons from the symbols currently used to represent the given layer
        """
        Countries = layer
        renderer = Countries.rendererV2()
        symbols = renderer.symbols()
        icons = []
        for symbol in symbols:
            icon = QgsSymbolLayerV2Utils.symbolPreviewIcon(symbol, QSize(50, 50))
            icons.append(icon)
            
        return icons
        

    def makeClassTable(self, layer, columncomboBox, tableViews):
        """
        make the table of classified fields and symbology
        """
        field = columncomboBox.currentText()
        values = self.getAttributes(field,  layer)
        rows = len(values)
        cols = 2
        model = QStandardItemModel(rows,  cols) 
        model.setHorizontalHeaderItem(0, QStandardItem("Symbol"))
        model.setHorizontalHeaderItem(1, QStandardItem("Value"))
        icons = self.getIcons(layer)

        
        for value in values:
            item = QStandardItem(value)
            row = values.index(value) 
            model.setItem(row,  1,  item)
            if row in range(len(icons)) :
                index = model.createIndex(row,  0)
                iconItem = QStandardItem(icons[row],  ' ') 
                model.setItem(row, 0,  iconItem)
                
        self.setTableViews(model,  tableViews)
                
    def setTableViews(self, model, tableViews):
        """
        show the table of classified fields and symbology in the given tableViews
        """
        if isinstance(tableViews,  list):
            for tableView in tableViews:
                tableView.setModel(model)
        else:
            tableViews.setModel(model)
        
