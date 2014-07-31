# -*- coding: utf-8 -*-

"""
Module containing a class that deals with spatial queries and related functions.
"""
import ntpath

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

class SpatialQuery():
    """
    Class that runs spatial queries etc.
    """
    def populateSrcBox(self,  inputbox,  refbox=None):
        """
        Populates the input and reference combo box if given, with all the layers currently loaded
        """
        #get all layers
        layers = iface.legendInterface().layers()
        
        nameList = []
        
        #ensure each layer is only added once
        for layer in layers:
            name = layer.name()
            if name not in nameList:
                nameList.append(name)
            
        #return nameList
        
        #clear current contents of comboBoxes
        inputbox.clear()
        if refbox is not None:
            refbox.clear()
        
        #add the layer names to the comboBox
        inputbox.addItems(nameList)
        if refbox is not None:
            refbox.addItems(nameList)
        
    def populateRefBox(self,  inputbox,  refbox,  querybox=None):
        """
        removes the selected source feature from the list of options for reference
        """
        #get selected input layer
        inputLayerName = inputbox.currentText()
        #get layers
        layers = iface.legendInterface().layers()
        
        refList = []
        #create list of all layers except the input layer
        for layer in layers:
            name = layer.name()
            if name != inputLayerName:
                refList.append(name)
        
        #clear current contents
        refbox.clear()
        
        #add new names
        refbox.addItems(refList)
        
        #if a querybox has been passed, populate it
        if querybox is not None:
            self.populateSelBox(inputbox,  refbox,  querybox)
        

    def populateSelBox(self,  inputbox,  refbox, querybox):
        """
        populates the 'process' combobox with the correct options based on the source and reference features.
        """
        #get selected input and reference layer names
        inputLayerName = inputbox.currentText()
        refLayerName = refbox.currentText()
        #get selected input and reference layers
        sLayer = QgsMapLayerRegistry.instance().mapLayersByName(inputLayerName)
        rLayer = QgsMapLayerRegistry.instance().mapLayersByName(refLayerName)
        
        #options for each possible combination of layer types
        Line2Line = ["crosses",  "equals",  "intersects",  "is disjoint to",  "overlaps",  "touches"]
        Line2Point = ["contains",  "intersects",  "is disjoint to"]
        Point2Point = ["equals",  "intersects",  "is disjoint to",  "overlaps"]
        Poly2Poly = ["contains",  "equals",  "intersects",  "is disjoint to",  "overlaps", "touches",  "is within"]
        Poly2Line = ["contains",  "intersects",  "is disjoint to"]
        Line2Poly = ["crosses",  "intersects",  "is disjoint to",  "touches",  "is within"]
        Point2Line =["crosses",  "intersects",  "is disjoint to",  "touches",  "is within"]
        Poly2Point = ["contains",  "intersects",  "is disjoint to"]
        Point2Poly = ["crosses",  "intersects",  "is disjoint to",  "touches", "is within"]
        
        #get type of features to be selected
        sFeats = sLayer[0].getFeatures()
        sFeat = sFeats.next()
        sGeom = sFeat.geometry()
        sType = sGeom.type()
        
        #get reference feature type
        rFeats = rLayer[0].getFeatures()
        rFeat = rFeats.next()
        rGeom = rFeat.geometry()
        rType = rGeom.type()
        
        #clear querybox of current contents
        querybox.clear()
        
        #set up message boxes
        msgBox=QMessageBox()
        msgBox.setIcon(3)
        
        #populate querybox with different options based on the source and reference layer types
        if sType == 0 and rType == 0:
            querybox.addItems(Point2Point)
        elif sType == 0 and rType ==1:
            querybox.addItems(Point2Line)
        elif sType == 1 and rType == 0:
            querybox.addItems(Line2Point)
        elif sType == 0 and rType == 2:
            querybox.addItems(Point2Poly)
        elif sType == 2 and rType == 0:
            querybox.addItems(Poly2Point)
        elif sType == 1 and rType == 1:
            querybox.addItems(Line2Line)
        elif sType == 1 and rType == 2:
            querybox.addItems(Line2Poly)
        elif sType == 2 and rType == 1:
            querybox.addItems(Poly2Line)
        elif sType == 2 and rType == 2:
            querybox.addItems(Poly2Poly)
        else:
            msgBox.setText("Oops! There was a problem")
            msgBox.setInformativeText("Please make sure that you have selected a valid layer")
            msgBox.exec_()
            


    def startSpatialQuery (self,  inputbox,  refbox,  querybox,  newLayercheckBox,  newLayerEdit,  progressBar = None):
        """
        sets up the variables for, and runs, the spatial query formulated by the user
        """
        #Reset manual querybar (update this to QProgressDialog if possible)
        if progressBar is not None:
            progressBar.reset()
        
        #get name of source layer
        sourceLayer = inputbox.currentText()
        
        #increment progress bar
        if progressBar is not None:
            progressBar.setValue(5)
        
        #run spatial query
        newSelection = self.spatialQuery(inputbox,  refbox,  querybox,  progressBar)
        
        #increment progress bar
        if progressBar is not None:
            progressBar.setValue(95)

        #create a new layer if the user has selected this
        if newLayercheckBox.isChecked():
            
            self.makeNewLayer(sourceLayer,  newLayerEdit)
            layerFilePath = newLayerEdit.text()
            newLayerSuffix =  ntpath.basename(layerFilePath)
            newLayerName = newLayerSuffix.split( '.')[0]
            legendName = newLayerName.split(".")
            newLayer = QgsVectorLayer(layerFilePath,  legendName[0],  'ogr')
            
            #increment progress bar
            if progressBar is not None:
                progressBar.setValue(100)
            
            #add new layer to the map canvas and update relevant comboBoxes
            return newSelection, QgsMapLayerRegistry.instance().addMapLayer(newLayer),  self.populateSrcBox(inputbox,  refbox) 
        else:
            #increment progress bar
            if progressBar is not None:
                progressBar.setValue(100)
            #highlight selected features
            return newSelection,  self.populateSrcBox(inputbox,  refbox)


    def spatialQuery(self, inputbox, refbox, querybox,  progressBar = None):
        """
        Compiles spatial query functions
        """
        #get source layer, reference layer and type of query
        srcLayer = inputbox.currentText()
        refLayer = refbox.currentText()
        selType = querybox.currentText()
        
        #get layers
        srcLayer = QgsMapLayerRegistry.instance().mapLayersByName(srcLayer)
        refLayer = QgsMapLayerRegistry.instance().mapLayersByName(refLayer)
        #get features
        refFeats = refLayer[0].getFeatures()
        srcPoints = srcLayer[0].getFeatures()
        

        selectList = []
        
        #separate as does not rely on boundingbox
        if selType == "is disjoint to":
            selectList = self.srcDisjointRef(srcLayer, refLayer)
            
            
        else:
            progValue = 5
            for feat in refFeats:
                progValue+=1
                #increment progress bar by 1 each iteration - Causes progress bar to stick at 90% IMPROVE.
                if progValue <= 90 and progressBar is not None:
                    progressBar.setValue(progValue)
                #get the geometry of the reference feature
                refGeom = feat.geometry()
                #get features in bounding rectangle of the geom
                srcPoints = srcLayer[0].getFeatures(QgsFeatureRequest().setFilterRect(refGeom.boundingBox()))
                for point in srcPoints:
                    progValue +=1
                    #increment progress bar by 1 each iteration - Causes progress bar to stick at 90% IMPROVE.
                    if progValue <= 90 and progressBar is not None:
                        progressBar.setValue(progValue)
                        
                    #for the selected query type, append the feature if it satsfies the requirement
                    if selType == "is within":
                        if point.geometry().within(refGeom):
                            selectList.append(point.id())
                    elif selType == "crosses":
                        if point.geometry().crosses(refGeom):
                            selectList.append(point.id())
                    elif selType == "equals":
                        if point.geometry().equals(refGeom):
                            selectList.append(point.id())
                    elif selType == "intersects":
                        if point.geometry().intersects(refGeom):
                            selectList.append(point.id())
                    elif selType == "overlaps":
                        if point.geometry().overlaps(refGeom):
                            selectList.append(point.id())
                    elif selType == "touches":
                        if point.geometry().touches(refGeom):
                            selectList.append(point.id())
                    else:
                        if point.geometry().contains(refGeom):
                            selectList.append(point.id())
        
        #select the features based on the list of features that satisfy the query requirement
        return srcLayer[0].setSelectedFeatures(selectList)


    def srcDisjointRef(self, srcLayer, refLayer):
        """
        determines which source features are spatially unrelated to the reference features
        """
        #get features
        srcPoints = srcLayer[0].getFeatures()
        refFeats = refLayer[0].getFeatures()
        
        #get a list of ids
        selectList = []
        for point in srcPoints:
            selectList.append(point.id())

        selectList2 = []
        
        #get list of features that intersect the reference features
        for feat in refFeats:
            refGeom = feat.geometry()
            srcPoints = srcLayer[0].getFeatures(QgsFeatureRequest().setFilterRect(refGeom.boundingBox()))
            for point in srcPoints:
                if point.geometry().intersects(refGeom):
                        selectList2.append(point.id())
        
        #create a list that is all but those features that intersect
        selectList3 = [id for id in selectList if id not in selectList2]        
        
        #return list
        return selectList3
        

    def makeNewLayer(self,  sourceLayer,  filePathLineEdit):
        """
        Open a File Browser Dialog to select location to save new layer
        """ 
        #get source layer
        SelectionLayer = QgsMapLayerRegistry.instance().mapLayersByName(sourceLayer)
        #get selected features
        SelectedFeats = SelectionLayer[0].selectedFeatures()
        
        #get file path and new layer name
        newLayerFilePath = filePathLineEdit.text()
        newLayerName =  ntpath.basename(newLayerFilePath)
        
        #carry attributes over to new layer
        pendingFields = SelectionLayer[0].pendingFields()
        fieldNames = []
        for field in pendingFields:
            fieldNames.append(field.name())
        
        #ensure the new layer has the same crs
        CRS = SelectionLayer[0].crs()
        
        #determine what type the layer is
        SelectionType = SelectionLayer[0].wkbType()
        
        #write the new layer to file
        writer = QgsVectorFileWriter(newLayerFilePath,  "CP1250",  pendingFields,  SelectionType,  CRS,  "ESRI Shapefile")
        
        #catch errors
        if writer.hasError() != QgsVectorFileWriter.NoError:
            msgBox=QMessageBox()
            msgBox.setIcon(3)
            msgBox.setText("Error when creating shapefile. Check that you have chosen a valid place to save it.")
            msgBox.exec_()

        #add each feature to the new layer
        for feat in SelectedFeats:
            writer.addFeature(feat)
            

    def clearSelection(self):
        """
        Clears current selection
        """
        layers = iface.legendInterface().layers()
        
        for layer in layers:
            layer.removeSelection()

    def populateLineOnlyBox(self,  lineComboBox):
        """
        populates the given box with only layers that have line geometries
        """   
        #get all layers
        layers = iface.legendInterface().layers()
        
        nameList = []
        
        #append only names of line layers
        for layer in layers:
            name = layer.name()
            feats = layer.getFeatures()
            feat = feats.next()
            if name not in nameList and feat.geometry().type() == 1:
                nameList.append(name)
                
        #clear current comboBox contents
        lineComboBox.clear()
        #add names of line layers
        lineComboBox.addItems(nameList)
        
