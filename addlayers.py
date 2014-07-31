# -*- coding: utf-8 -*-

"""
Module containing a class that deals with adding layers to the canvas
"""
import ntpath

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from qgis.analysis import *

class AddLayers():
    """
    Class defining functionalities related to adding a layer to the map canvas
    """

    def CheckAddLayers(self, LineEditName,  LayerString): 
        """
        Performs checks to determine whether the layers to be added to the canvas:
        1. have not already been added
        2. have a file specified
        3. are valid
        4. are the correct layers
        
        """

        LayerFile = LineEditName.text()
        NewLayer = QgsVectorLayer(LayerFile,  LayerString,  'ogr')
        LayerAdded = QgsMapLayerRegistry.instance().mapLayersByName(LayerString)
           
        #set up message boxes
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
        #If the file selected does not contain the layer string, then the wrong shapefile has been selected and an error box is executed.
        elif LayerString not in LayerFile:
            msgBox.setText("You have chosen the wrong shapefile for " + LayerString + ".")
            msgBox.setInformativeText(" Please go back and select " + LayerString +".shp")
            msgBox.exec_()   
        #if there are no problems with the shapefile, then return it
        else:
                
            return NewLayer
           
    def CheckBufferLayer(self, inputComboBox,  filePathEdit,  distanceEdit,  progressBar=None): 
        """
        Checks that layer and buffer distance are valid, then creates a buffer of designated distance
        around the layer and returns it to the canvas
        """
          
        layerName = inputComboBox.currentText()
        layer = QgsMapLayerRegistry.instance().mapLayersByName(layerName)[0]
        
        #manual progress bar
        if progressBar is not None:
            progressBar.setValue(10)
        
        #use the specified file path to get the layer name
        newLayerFilePath = filePathEdit.text()
        newLayerSuffix =  ntpath.basename(newLayerFilePath)
        newLayerName = newLayerSuffix.split( '.')[0]
        
        distance = distanceEdit.text()
        
        if progressBar is not None:
            progressBar.setValue(20)
        
        #set up message box
        msgBox=QMessageBox()
        msgBox.setIcon(3)
        
        #check that a number has been typed into the distance box, provide an error box if not
        try:
            distFloat = float(distance)
        
        except ValueError:
            msgBox.setText("Could not create the layer")
            msgBox.setInformativeText(" Please make sure that you have typed a number into the distance box")
            msgBox.exec_()

        # buffer the given layer and save it at the chosen file path
        else:
            
            if progressBar is not None:
                progressBar.setValue(40)
        
            progress = QProgressDialog("Buffering Layer...",  "Cancel",  0,  100)
            analyser = QgsGeometryAnalyzer().buffer(layer,  newLayerFilePath,  distFloat,  False,  True,  -1,  progress)
            
            if progressBar is not None:
                progressBar.setValue(60)
        
            bufferLayer = QgsVectorLayer(newLayerFilePath,  newLayerName,  'ogr')
            

            if not newLayerFilePath:
                return None
            #If the file selected is not a valid layer, execute an error message box
            elif not bufferLayer.isValid():
                msgBox.setText("Could not create the layer")
                msgBox.setInformativeText(" Please make sure that you have used the Browse button to select a valid save location for the new layer")
                msgBox.exec_()
            #if there are no problems with the shapefile, then add it to the project
            else:
                QgsMapLayerRegistry.instance().addMapLayer(bufferLayer)
                if progressBar is not None:
                    progressBar.setValue(100)
        
        return newLayerName
    

    def clipLayer(self, inputComboBox, refComboBox, filePathEdit): 
        """ 
        Create a new vector layer from clipping two layers
        """
        #get layer names
        layerAName = inputComboBox.currentText()
        layerBName = refComboBox.currentText()
        
        #get layers
        layerA = QgsMapLayerRegistry.instance().mapLayersByName(layerAName)[0]
        layerB = QgsMapLayerRegistry.instance().mapLayersByName(layerBName)[0]
        
        #get filepath for new clipped layer
        newPath = filePathEdit.text()
        
        #show progress bar as clipping is done
        progress = QProgressDialog("Clipping Layer...",  "Cancel",  0,  100)
        
        #clip layer
        QgsOverlayAnalyzer().intersection(layerA,  layerB,  newPath, False,  progress)
        
        #get the name.shp
        newLayerSuffix =  ntpath.basename(newPath)
        #get the name without .shp
        newLayerName = newLayerSuffix.split( '.')[0]
        #create new layer
        newLayer = QgsVectorLayer(newPath,  newLayerName,  'ogr')
        
        return newLayer
        
        
