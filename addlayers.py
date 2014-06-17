# -*- coding: utf-8 -*-

"""
Module containing a class that deals with adding layers to the canvas
"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

class AddLayers():
    """
    Class defining functionalities pertaining to adding a layer to the map canvas
    """

    def CheckAddLayers(self, LineEditName,  LayerString): 
        """
        Performs checks to determine whether the layers to be added to the canvas:
        1. have not already been addedp
        2. have a file specified
        3. are valid
        4. are the correct layers
        
        Parameters: The name of the LineEdit that contains the filePath (LineEditName)
                        The string that you wish the layer to be called in the legend/shapefile name.This string must be in the shapefile name for the layer to load.
        
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
        #If the file selected does not contain the layer string, then the wrong shapefile has been selected and an error box is executed.
        elif LayerString not in LayerFile:
            msgBox.setText("You have chosen the wrong shapefile for " + LayerString + ".")
            msgBox.setInformativeText(" Please go back and select " + LayerString +".shp")
            msgBox.exec_()   
        #if there are no problems with the shapefile, then return it
        else:
                
            return NewLayer 
