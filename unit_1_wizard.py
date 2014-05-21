# -*- coding: utf-8 -*-

"""
Module implementing unit1wizard.
"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from Ui_unit_1_wizard import Ui_Wizard

class Unit1Wizard(QWizard, Ui_Wizard):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QWizard.__init__(self, parent)
        self.setupUi(self)
    
    #@pyqtSignature("")
    #def on___qt__passive_wizardbutton1_clicked(self):
     #   """
      #  Slot documentation goes here.
       # """
        # TODO: not implemented yet
        #raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
        
        
    @pyqtSignature("")
    def on_BrowsepushButton_clicked(self):
        """
        Open a File Browser Dialog - for the countries layer
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open Countries.shp','', 'Shapefiles (*.shp)')
        self.FilePathlineEdit.setText(inputFile)
        
    @pyqtSignature("")
    def on_BrowsepushButton_2_clicked(self):
        """
        Open a File Browser Dialog - for the cities layer
        """
        # set the chosen file as the input for the FilePathLineEdit_2
        inputFile = QFileDialog.getOpenFileName(self, 'Open Cities.shp','', 'Shapefiles (*.shp)')
        self.FilePathlineEdit_2.setText(inputFile)
    
    @pyqtSignature("")
    def on_BrowsepushButton_3_clicked(self):
        """
        Open a File Browser Dialog - for the equator layer
        """
        # set the chosen file as the input for the FilePathLineEdit_3
        inputFile = QFileDialog.getOpenFileName(self, 'Open Equator.shp','', 'Shapefiles (*.shp)')
        self.FilePathlineEdit_3.setText(inputFile)
        
 
    @pyqtSignature("")
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
        
        if LayerAdded:
            return None
        elif not LayerFile:
            return None
        elif not NewLayer.isValid():
            msgBox.setText("Could not load the " + LayerString + " layer")
            msgBox.exec_()
        elif LayerString not in LayerFile:
            msgBox.setText("You have chosen the wrong shapefile for " + LayerString + ".")
            msgBox.setInformativeText(" Please go back and select " + LayerString +".shp")
            msgBox.exec_()   
        else:
            return NewLayer            

    @pyqtSignature("")
    def on_AddLayerButton_clicked(self):
        """
        Add the layers to the map canvas
        """
        FilePathlineEdit = self.FilePathlineEdit
        FilePathlineEdit_2 = self.FilePathlineEdit_2
        FilePathLineEdit_3 = self.FilePathlineEdit_3
        
        Countries = self.CheckAddLayers(FilePathlineEdit,  "countries")
        Cities = self.CheckAddLayers(FilePathlineEdit_2,  "major_cities")
        Equator = self.CheckAddLayers(FilePathLineEdit_3,  "equator")
        
        return QgsMapLayerRegistry.instance().addMapLayer(Countries), QgsMapLayerRegistry.instance().addMapLayer(Cities), QgsMapLayerRegistry.instance().addMapLayer(Equator) 


    @pyqtSignature("")
    def populateSrcList(self):
        """
        function description here
        """   
        #layers = QgsMapLayerRegistry.instance().mapLayers()
        layers = iface.legendInterface().layers()
        
        nameList = []
        
        for layer in layers:
            name = layer.name()
            nameList.append(name)
            
        print nameList
            
    
    
    @pyqtSignature("")
    def on_queryButton_clicked(self):
        """
        function description here
        """
        sourceLayer = self.sourceFeatcomboBox.currentText()
        referenceLayer = self.refFeatcomboBox.currentText()
        
        newSelection = self.srcWithinRef(sourceLayer, referenceLayer)
        print self.populateSrcList()
        print sourceLayer
        print referenceLayer
        return newSelection
       
    @pyqtSignature("")
    def srcWithinRef(self, srcLayer, refLayer):
        """
        function description here
        """
        srcLayer = QgsMapLayerRegistry.instance().mapLayersByName(srcLayer)
        refLayer = QgsMapLayerRegistry.instance().mapLayersByName(refLayer)
        
        print srcLayer
        print refLayer
        #if srcLayer[0].geometryType() == 2:
        polyFeats = refLayer[0].getFeatures()
        print polyFeats
        
        selectList = []
        
        for feat in polyFeats:
            polyGeom = feat.geometry()
            srcPoints = srcLayer[0].getFeatures(QgsFeatureRequest().setFilterRect(polyGeom.boundingBox()))
            for point in srcPoints:
                if point.geometry().within(polyGeom):
                    selectList.append(point.id())
                    
        return srcLayer[0].setSelectedFeatures(selectList)
        print selectList
            

