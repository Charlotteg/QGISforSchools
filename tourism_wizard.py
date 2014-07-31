# -*- coding: utf-8 -*-

"""
Module implementing TourismWizard.
"""

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
from query import SpatialQuery
from labels import Label
from magicMarkers import MagicMarkers
from marker_dialog import MarkerDialog

from Ui_tourism_wizard import Ui_TourismWizard

class TourismWizard(QWizard, Ui_TourismWizard):
    """
    Class documentation goes here.
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
        self.landAnsClicks = 0
        self.negAnsClicks = 0
        self.sustAnsClicks = 0
        self.accomAnsClicks = 0
        self.q1 = False
        self.q2 = False
        self.q3 = False
        self.q4 = False
        self.q5 = False
        self.q6 = False
        self.scoreLabels = [self.Score_label,  self.Score_label_2,  self.Score_label_3,  self.Score_label_4,  self.Score_label_5, self.Score_label_6,  self.Score_label_7,  self.Score_label_8,  self.Score_label_9,  self.Score_label_10]
        
       
#*************************************** Page 2 *****************************************************************************   
    @pyqtSignature("")
    def on_woodBrowseButton_clicked(self):
        """
        Open a File Browser Dialog - for the woodland layer
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open woodland.shp','', 'Shapefiles (*.shp)')
        self.woodLineEdit.setText(inputFile)
    
    @pyqtSignature("")
    def on_AddWoodLayer_clicked(self):
        """
        Add the woodland layer to the map canvas
        """
        woodLineEdit = self.woodLineEdit
        
        #Check the layer is valid
        woodland = AddLayers().CheckAddLayers(woodLineEdit,  "woodland")
        
        #ensure the woodland layer renders in purple!
        if woodland is not None:
            woodRenderer = woodland.rendererV2()
            woodSymbol = woodRenderer.symbol()
            woodSymbol.setColor(QColor('#cc33ff'))
            
        #add layer
        QgsMapLayerRegistry.instance().addMapLayer(woodland)

    @pyqtSignature("")
    def on_checkAnswersLand_released(self):
        """
        check answers and add points if correct based on the number of answers already submitted
        """
        # log the number of times that the check answers button has been clicked
        self.landAnsClicks += 1
        #check answers and update score
        self.score,  self.q1 = ScoreSystem(self.score,  6).checkAnswers(self.landAnsClicks,  self.landscapes,  self.q1,  1)
        ScoreSystem(self.score,  6).updateScore(self.scoreLabels,  self.starView)

#*************************************** Page 3 *****************************************************************************   

    @pyqtSignature("")
    def on_woodColourButton_clicked(self):
        """
        Allow the user to select a single colour for the woodland layer
        """
        colourManager().updateSingleColour("woodland",  True)

    @pyqtSignature("")
    def on_riverBrowseButton_clicked(self):
        """
        Open a File Browser Dialog - for the rivers layer
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open rivers.shp','', 'Shapefiles (*.shp)')
        self.riverLineEdit.setText(inputFile)
    
    @pyqtSignature("")
    def on_AddRiverLayer_clicked(self):
        """
        Add the river layer to the map canvas
        """
        riverLineEdit = self.riverLineEdit
        
        #Check the layer is valid
        rivers = AddLayers().CheckAddLayers(riverLineEdit,  "rivers")
        
        #add layer
        QgsMapLayerRegistry.instance().addMapLayer(rivers)


    @pyqtSignature("")
    def on_riverColourButton_clicked(self):
        """
        Allow the user to select a single colour for the rivers layer
        """
        colourManager().updateSingleColour("rivers")


    @pyqtSignature("")
    def on_applyRiverStyle_clicked(self):
        """
        Apply the style settings to the river layer
        """

        #get the information required
        rivers = QgsMapLayerRegistry.instance().mapLayersByName("rivers")[0]
        lineWidth = self.riverWidth.value()
        lineStyle = self.lineStyle.currentText()
        style = lineStyle.rsplit(' ',  1)[0]

        #Set line width
        riverRenderer = rivers.rendererV2()
        riverSymbol = riverRenderer.symbol()
        riverSymbol.setWidth(lineWidth)
        
        #get colour
        riverColor = riverSymbol.color().name()
        
        #set line style
        riverSymbol = QgsLineSymbolV2.createSimple({'color': riverColor,  'width': str(lineWidth),  'penstyle': style.lower()})
        riverRenderer.setSymbol(riverSymbol)
        
        #refresh map canvas and legend
        iface.mapCanvas().refresh()
        iface.legendInterface().refreshLayerSymbology(rivers)

#*************************************** Page 4 *****************************************************************************   

    @pyqtSignature("")
    def on_urbanBrowseButton_clicked(self):
        """
        Open a File Browser Dialog - for the buildings layer
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open buildings.shp','', 'Shapefiles (*.shp)')
        self.urbanLineEdit.setText(inputFile)
    
    @pyqtSignature("")
    def on_AddUrbanLayer_clicked(self):
        """
        Add the urban region layer to the map canvas
        """
        urbanLineEdit = self.urbanLineEdit
        #check layer is valid
        buildings = AddLayers().CheckAddLayers(urbanLineEdit,  "buildings")
        #add layer
        QgsMapLayerRegistry.instance().addMapLayer(buildings)

    @pyqtSignature("")
    def on_urbanColourButton_clicked(self):
        """
        Allow the user to select a single colour for the buildings layer
        """
        colourManager().updateSingleColour("buildings",  True)

    @pyqtSignature("")
    def on_checkAnswersNeg_released(self):
        """
        check answers and add points if correct based on the number of answers already submitted
        """
        # log the number of times that the check answers button has been clicked
        self.negAnsClicks += 1
        #check answers and update score
        self.score,  self.q2 = ScoreSystem(self.score,  6).checkAnswers(self.negAnsClicks,  self.environment,  self.q2,  2)
        ScoreSystem(self.score,  6).updateScore(self.scoreLabels,  self.starView)

#*************************************** Page 5 *****************************************************************************  

    @pyqtSignature("")
    def on_railBrowseButton_clicked(self):
        """
        Open a File Browser Dialog - for the rail lines layer
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open railway_line.shp','', 'Shapefiles (*.shp)')
        self.railLineEdit.setText(inputFile)
    
    @pyqtSignature("")
    def on_railStationBrowseButton_clicked(self):
        """
        Open a File Browser Dialog - for the railway stations layer
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open railway_station.shp','', 'Shapefiles (*.shp)')
        self.railStationLineEdit.setText(inputFile)

    @pyqtSignature("")
    def on_minorRdBrowseButton_clicked(self):
        """
        Open a File Browser Dialog - for the minor roads layer
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open minor_road.shp','', 'Shapefiles (*.shp)')
        self.minorRdLineEdit.setText(inputFile)

    @pyqtSignature("")
    def on_bRoadsBrowseButton_clicked(self):
        """
        Open a File Browser Dialog - for the B roads layer
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open b_road.shp','', 'Shapefiles (*.shp)')
        self.bRoadsLineEdit.setText(inputFile)

    @pyqtSignature("")
    def on_priRoadsBrowseButton_clicked(self):
        """
        Open a File Browser Dialog - for the primary roads layer
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open primary_road.shp','', 'Shapefiles (*.shp)')
        self.priRoadsLineEdit.setText(inputFile)

    @pyqtSignature("")
    def on_AddLayersButton_clicked(self):
        """
        Add the layers to the map canvas
        """
        #make sure that each layer is valid
        railway = AddLayers().CheckAddLayers(self.railLineEdit,  "railway_line")
        station = AddLayers().CheckAddLayers(self.railStationLineEdit,  "railway_station")
        minorRoad = AddLayers().CheckAddLayers(self.minorRdLineEdit,  "minor_road")
        bRoad = AddLayers().CheckAddLayers(self.bRoadsLineEdit,  "b_road")
        primaryRoad = AddLayers().CheckAddLayers(self.priRoadsLineEdit,  "primary_road")
        
        #add the layers to the map
        QgsMapLayerRegistry.instance().addMapLayer(railway)
        QgsMapLayerRegistry.instance().addMapLayer(minorRoad)
        QgsMapLayerRegistry.instance().addMapLayer(bRoad)
        QgsMapLayerRegistry.instance().addMapLayer(primaryRoad)
        QgsMapLayerRegistry.instance().addMapLayer(station)
        
        # populate the line layers box on the next page
        SpatialQuery().populateLineOnlyBox(self.lineLyrComboBox)

    
#*************************************** Page 6 *****************************************************************************  

    @pyqtSignature("")
    def on_lineColourButton_clicked(self):
        """
        Allow the user to select a single colour for the rivers layer
        """
        #get the layer name
        layerName = self.lineLyrComboBox.currentText()
        #update the colour of the layer symbols
        colourManager().updateSingleColour(layerName)

    @pyqtSignature("")
    def on_applyStyle_clicked(self):
        """
        Apply the style settings to the chosen layer
        """
        #get the information required
        layerName = self.lineLyrComboBox.currentText()
        layer = QgsMapLayerRegistry.instance().mapLayersByName(layerName)[0]
        lineWidth = self.lineWidth.value()
        lineStyle = self.styleComboBox.currentText()
        style = lineStyle.rsplit(' ',  1)[0]
        renderer = layer.rendererV2()
        rendererSymbol = renderer.symbol()
        color = rendererSymbol.color().name()
        
        #set line style
        rendererSymbol = QgsLineSymbolV2.createSimple({'color': color,  'width': str(lineWidth),  'penstyle': style.lower()})
        renderer.setSymbol(rendererSymbol)
    
        #refresh the map canvas and legend
        iface.mapCanvas().refresh()
        iface.legendInterface().refreshLayerSymbology(layer)

    @pyqtSignature("")
    def on_addLabels_clicked(self):
        """
        hide or show the labels based on checkbox state
        """
        state = self.addLabels.checkState()
        #if the checkbox is checked, add the names of the railway station as labels
        if state:
            Label().nameLabel("railway_station",  "NAME")
        #if not checked remove labels
        else:
            Label().removeLabel("railway_station")

    @pyqtSignature("")
    def on_labelFormat_clicked(self):
        """
        change style of labels
        """   
        Label().chooseLabel("railway_station",  "NAME")


    @pyqtSignature("")
    def on_stationColour_clicked(self):
        """
        Allow the user to select a single colour for the station points
        """
        colourManager().updateSingleColour("railway_station")

    @pyqtSignature("")
    def on_applyStationStyle_clicked(self):
        """
        Apply size
        """
        #get required information
        layer = QgsMapLayerRegistry.instance().mapLayersByName("railway_station")[0]
        size = self.stationSize.value()
        renderer = layer.rendererV2()
        rendererSymbol = renderer.symbol()
        #set new size
        rendererSymbol.setSize(size)
        
        #refresh map canvas and legend
        iface.mapCanvas().refresh()
        iface.legendInterface().refreshLayerSymbology(layer) 
        

#*************************************** Page 7 *****************************************************************************      

    @pyqtSignature("")
    def on_settlementBrowseButton_clicked(self):
        """
        Open a File Browser Dialog - for the settlement layer
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open settlement_names.shp','', 'Shapefiles (*.shp)')
        self.settlementLineEdit.setText(inputFile)

    @pyqtSignature("")
    def on_AddSettlementLayer_clicked(self):
        """
        Add label layer with transparent points and labels enabled
        """
        #check layer is valid
        labels = AddLayers().CheckAddLayers(self.settlementLineEdit,  "settlement_names")
        
        #if valid, make layer points appear invisible and apply labels
        if labels is not None:
            labelsRenderer = labels.rendererV2()
            labelsSymbol = labelsRenderer.symbol()
            color = QColor(0, 0, 0, 0)
            labelsSymbol.setColor(QColor(0, 0, 0, 0))
            labelsSymbol = QgsMarkerSymbolV2.createSimple({'color': '0,0,0,0',  'color_border': '0,0,0,0'})
            labelsRenderer.setSymbol(labelsSymbol)
       
        #add layer to map canvas
        QgsMapLayerRegistry.instance().addMapLayer(labels)
        #set labels to settlement names
        Label().nameLabel("settlement_names",  "NAME")
        

    @pyqtSignature("")
    def on_formatLabels_clicked(self):
        """
        bring up QFontDialog and set label style based on user choices
        """
        Label().chooseLabel("settlement_names",  "NAME")

    @pyqtSignature("")
    def on_checkAnswersSust_clicked(self):
        """
        check answers and add points if correct based on the number of answers already submitted
        """
        # log the number of times that the check answers button has been clicked
        self.sustAnsClicks += 1
        # check answers and update score
        self.score,  self.q3 = ScoreSystem(self.score,  6).checkAnswers(self.sustAnsClicks,  self.balance,  self.q3,  3)
        ScoreSystem(self.score,  6).updateScore(self.scoreLabels,  self.starView)

#*************************************** Page 8 *****************************************************************************   

    @pyqtSignature("")
    def on_attractionBrowseButton_clicked(self):
        """
        Open a File Browser Dialog - for the tourist attraction layer
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open tourist_attraction.shp','', 'Shapefiles (*.shp)')
        self.attractionLineEdit.setText(inputFile)

    @pyqtSignature("")
    def on_AddAttractionLayer_clicked(self):
        """
        add the tourist attraction layer to the mao
        """
        #check layer is valid
        attractions = AddLayers().CheckAddLayers(self.attractionLineEdit,  "tourist_attraction")
        # add layer to map canvas
        QgsMapLayerRegistry.instance().addMapLayer(attractions)
        
        #if valid, populate the combobox on the next page with types of attraction
        if attractions is not None:
            attractionTypes = colourManager().getAttributes("LEGEND",  attractions)
            self.fieldComboBox.addItems(attractionTypes)
            
            colorList = [QColor('#8dd3c7'), QColor('#ffffb3'), QColor('#bebada'), QColor('#fb8072'), QColor('#80b1d3'), QColor('#fdb462'), QColor('#b3de69'), QColor('#fccde5'), QColor('#d9d9d9'), QColor('#bc80bd'), QColor('#ccebc5'), QColor('#ffed6f'), QColor('#6699ff'),QColor('#ff1975'),QColor('#3399ff')]
            catList = []
            #apply a default colour scheme to the attractions based on attraction type
            for attraction in attractionTypes:
                colorIndex = attractionTypes.index(attraction)
                symbol = QgsSymbolV2.defaultSymbol(attractions.geometryType())
                symbol.setColor(colorList[colorIndex])
                cat = QgsRendererCategoryV2(attraction, symbol ,  str(attraction))
                catList.append(cat)
            
            renderer = QgsCategorizedSymbolRendererV2("LEGEND", catList)
            
            attractions.setRendererV2(renderer)
            
            #refresh map canvas and legend
            iface.mapCanvas().refresh()
            iface.legendInterface().refreshLayerSymbology(attractions)
            
            #make a legend table in the plugin
            colourManager().makeClassTable(attractions,  "LEGEND",  self.AttractionTableView)


    @pyqtSignature("")
    def on_checkAnswersEco_clicked(self):
        """
        check answers and add points if correct based on the number of answers already submitted
        """
        # log the number of times that the check answers button has been clicked
        self.sustAnsClicks += 1
        #check answers and update score
        self.score,  self.q4 = ScoreSystem(self.score,  6).checkAnswers(self.sustAnsClicks,  self.sustainable,  self.q4,  4)
        ScoreSystem(self.score,  6).updateScore(self.scoreLabels,  self.starView)


#*************************************** Page 9 *****************************************************************************     

    @pyqtSignature("")
    def on_getIcons_clicked(self):
        """
        Open the MarkerDialog
        """
        #get attribute that user wishes to change icon for
        attribute = self.fieldComboBox.currentText()
        
        #open marker dialog
        openDlg=MarkerDialog(attribute,  self.AttractionTableView)
        openDlg.show()
        result = openDlg.exec_()



#*************************************** Page 10 *****************************************************************************     

    @pyqtSignature("")
    def on_checkAnswersAccom_clicked(self):
        """
        check answers and add points if correct based on the number of answers already submitted
        """
        # log the number of times that the check answers button has been clicked
        self.accomAnsClicks += 1
        #check answers and update schore
        self.score,  self.q5,  self.q6 = ScoreSystem(self.score,  6).checkAnswers(self.accomAnsClicks,  self.nature,  self.q5,  5,  self.camp,  self.q6, 6)
        ScoreSystem(self.score,  6).updateScore(self.scoreLabels,  self.starView)


