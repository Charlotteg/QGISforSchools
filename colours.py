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
    """
    Class that deals with all things colour, including changing single colours, categorised colours
    and making the colour display tables
    """

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
        
    def updateSingleColour(self,  layerName,  border=False):
        """
        Allow the user to select a single colour and update the map canvas and layer with the selected colour
        parameters: name of the layer that you wish to change the colour of
        """
        newColor = self.singleColourDialog()
        print newColor
        
        layer = QgsMapLayerRegistry.instance().mapLayersByName(layerName)[0]
        layerRenderer = layer.rendererV2()
        layerSymbol = layerRenderer.symbol()
        layerSymbol.setColor(newColor)
        feats = layer.getFeatures()
        feat = feats.next()
       
        if border:
            if feat.geometry().type() == 2:
                layerSymbol = QgsFillSymbolV2.createSimple({'color': newColor.name(),  'color_border': newColor.name()})
            elif feat.geometry().type == 0:
                layerSymbol = QgsMarkerSymbolV2.createSimple({'color': newColor.name(),  'color_border': newColor.name()})
            layerRenderer.setSymbol(layerSymbol)
        
        #refresh the map and legend
        iface.mapCanvas().refresh()
        iface.legendInterface().refreshLayerSymbology(layer)

        
    def changeColumnColor(self,  layerName,  ColumncomboBox,  ColourRampcomboBox,  tableViews = None):
        """
        Colour the layer by the selected categories specified in the field chosen in the ColumncomboBox.
        Colour scheme is determined by the current contents of the ColourRampcomboBox and the table views
        specified are updated with details of which colour is assigned to which category.
        
        Parameters: layer name, ColumncomboBox, ColourRampcomboBox, 
        table views (optional parameter, can pass a list or individual)
        """
        
        Layer = QgsMapLayerRegistry.instance().mapLayersByName(layerName)[0]
        
        if isinstance (ColumncomboBox, str) and isinstance(ColourRampcomboBox,  str):
            field = ColumncomboBox
            colorScheme = QgsVectorColorBrewerColorRampV2.listSchemeNames()[0]
        else:
            field = ColumncomboBox.currentText()
            colorScheme = ColourRampcomboBox.currentText()
        
        print colorScheme
        
        categories = self.getAttributes(field,  Layer)
        print categories
        numColors = len(categories)
        
        colors = QgsColorBrewerPalette.listSchemeColors(colorScheme, numColors)
        print colors
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
        
        if tableViews is not None:
            self.makeClassTable(Layer,  ColumncomboBox, tableViews)
            
    

    def setGraduatedColour(self,  layerName, ColumncomboBox,  ColourRampcomboBox, numColors,  tableViews = None):
        """
        Divide the field into 'pretty breaks' ranges and colour each range based on the colour scheme specified 
         by the current contents of the ColourRampcomboBox. The table views
        specified are updated with details of which colour is assigned to which range. 
        The number of ranges is suggested by the numColors value.
        
        Parameters: layer name, rangeList, ColumncomboBox, ColourRampcomboBox, numColors
        table views (optional parameter, can pass a list or individual)
        """
        
        Layer = QgsMapLayerRegistry.instance().mapLayersByName(layerName)[0]
        
        field = ColumncomboBox.currentText()
        colorScheme = ColourRampcomboBox.currentText()
        symbol = QgsSymbolV2.defaultSymbol(Layer.geometryType())
        
        if symbol is None:
            if Layer.geometryType() == QGis.Point:
                symbol = QgsMarkerSymbolV2()
        
        colorRamp = QgsVectorColorBrewerColorRampV2.create({'schemeName': str(colorScheme),  'colors': str(numColors)})
        renderer = QgsGraduatedSymbolRendererV2.createRenderer(Layer,  field,  numColors,  QgsGraduatedSymbolRendererV2.Pretty,  symbol,  colorRamp)
        Layer.setRendererV2(renderer)
        iface.mapCanvas().refresh()
        iface.legendInterface().refreshLayerSymbology(Layer)
        
        Labels = []
        for range in renderer.ranges():
            Labels.append(range.label())
            
        if tableViews is not None:
            self.makeClassTable(Layer,  ColumncomboBox,  tableViews,  Labels)
        
        
    def getAttributes(self, field,  layer):
        """
        get the sorted and deduplicated elements of the field passed
        
        parameters: layer and field that you wish to get the elements of
        
        returns: list of elements
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
        Layer = layer
        renderer = Layer.rendererV2()
        symbols = renderer.symbols()
        icons = []
        for symbol in symbols:
            if symbol.type() == 0:
                width = 10
                height = 10
            else:
                width = 50
                height = 50
            icon = QgsSymbolLayerV2Utils.symbolPreviewIcon(symbol, QSize(width, height))
            icons.append(icon)
            
        return icons
        



    def makeClassTable(self, layer, columncomboBox, tableViews,  graduatedLabels = None):
        """
        make the 2 column table of classified fields and symbology
        
        parameters: layer, columncomboBox to define field, table views to update
        """
        if isinstance (columncomboBox,  str):
            field = columncomboBox
        else:
            field = columncomboBox.currentText()
            
        if graduatedLabels is not None:
            values = graduatedLabels
        else:
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



    def make3ClassTable(self, layerName, otherLayerName,  ColumncomboBox, otherColumncomboBox, tableViews):
        """
        make and show the table of classified field/ symbology. 
        This one has 3 columns so can deal with 2 layers.
        
        Parameters: layer names of both layers, column combo boxes that determine 
        which field will be categorised and the relevant table views to be updated
        """
        layer = QgsMapLayerRegistry.instance().mapLayersByName(layerName)[0]
        otherLayer = QgsMapLayerRegistry.instance().mapLayersByName(otherLayerName)[0]
        field = ColumncomboBox.currentText()
        values = self.getAttributes(field,  layer)
        otherField = otherColumncomboBox.currentText()
        otherValues = self.getAttributes(otherField,  otherLayer)
        rows = len(otherValues)
        cols = 3
        model = QStandardItemModel(rows,  cols) 
        model.setHorizontalHeaderItem(0, QStandardItem("Symbol"))
        model.setHorizontalHeaderItem(1, QStandardItem(otherLayerName))
        model.setHorizontalHeaderItem(2, QStandardItem(layerName))
        icons = self.getIcons(layer)
        
        for value in otherValues:
            item = QStandardItem(value)
            row = otherValues.index(value) 
            model.setItem(row,  1,  item)
            if row in range(len(icons)) :
                index = model.createIndex(row,  0)
                iconItem = QStandardItem(icons[row],  ' ') 
                model.setItem(row, 0,  iconItem)
            if row in range(len(values)):
                iItem = QStandardItem(values[row])
                model.setItem(row, 2,  iItem)

        self.setTableViews(model,  tableViews)


    def setTableViews(self, model, tableViews):
        """
        show the table of classified fields and symbology in the given tableViews
        
        parameters: the model to update the table view with and the table view to update
        """
        if isinstance(tableViews,  list):
            for tableView in tableViews:
                tableView.setModel(model)
        else:
            tableViews.setModel(model)
            
            
    
    def propSymbols(self,  layer,  expression):
        """
        Set the size of the symbols based on the expression
        """
        
        renderer = layer.rendererV2()

        renderer.setSizeScaleField(expression)

        layer.setRendererV2(renderer)
        
        iface.mapCanvas().refresh()

