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
        
        layers = iface.legendInterface().layers()
        
        nameList = []
        
        for layer in layers:
            name = layer.name()
            if name not in nameList:
                nameList.append(name)
            
        #return nameList
        
        inputbox.clear()
        if refbox is not None:
            refbox.clear()
        
        inputbox.addItems(nameList)
        if refbox is not None:
            refbox.addItems(nameList)
        
    def populateRefBox(self,  inputbox,  refbox,  querybox=None):
        """
        removes the selected source feature from the list of options for reference
        """
        inputLayerName = inputbox.currentText()
        
        layers = iface.legendInterface().layers()
        
        refList = []
        
        for layer in layers:
            name = layer.name()
            if name != inputLayerName:
                refList.append(name)
        
        refbox.clear()
        
        refbox.addItems(refList)
        
        if querybox is not None:
            self.populateSelBox(inputbox,  refbox,  querybox)
        

    def populateSelBox(self,  inputbox,  refbox, querybox):
        """
        populates the 'process' combobox with the correct options based on the source and reference features.
        """
        inputLayerName = inputbox.currentText()
        refLayerName = refbox.currentText()
        sLayer = QgsMapLayerRegistry.instance().mapLayersByName(inputLayerName)
        rLayer = QgsMapLayerRegistry.instance().mapLayersByName(refLayerName)
        
        Line2Line = ["crosses",  "equals",  "intersects",  "is disjoint to",  "overlaps",  "touches"]
        Line2Point = ["contains",  "intersects",  "is disjoint to"]
        Point2Point = ["equals",  "intersects",  "is disjoint to",  "overlaps"]
        Poly2Poly = ["contains",  "equals",  "intersects",  "is disjoint to",  "overlaps", "touches",  "is within"]
        Poly2Line = ["contains",  "intersects",  "is disjoint to"]
        Line2Poly = ["crosses",  "intersects",  "is disjoint to",  "touches",  "is within"]
        Point2Line =["crosses",  "intersects",  "is disjoint to",  "touches",  "is within"]
        Poly2Point = ["contains",  "intersects",  "is disjoint to"]
        Point2Poly = ["crosses",  "intersects",  "is disjoint to",  "touches", "is within"]
        
        sFeats = sLayer[0].getFeatures()
        sFeat = sFeats.next()
        sGeom = sFeat.geometry()
        sType = sGeom.type()
        
        rFeats = rLayer[0].getFeatures()
        rFeat = rFeats.next()
        rGeom = rFeat.geometry()
        rType = rGeom.type()
        
        querybox.clear()
        
        msgBox=QMessageBox()
        msgBox.setIcon(3)
        
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
        if progressBar is not None:
            progressBar.reset()
        
        sourceLayer = inputbox.currentText()
        
        if progressBar is not None:
            progressBar.setValue(5)
        
        newSelection = self.spatialQuery(inputbox,  refbox,  querybox,  progressBar)
        
        if progressBar is not None:
            progressBar.setValue(95)

        
        if newLayercheckBox.isChecked():
            
            self.makeNewLayer(sourceLayer,  newLayerEdit)
            layerFilePath = newLayerEdit.text()
            newLayerSuffix =  ntpath.basename(layerFilePath)
            newLayerName = newLayerSuffix.split( '.')[0]
            legendName = newLayerName.split(".")
            newLayer = QgsVectorLayer(layerFilePath,  legendName[0],  'ogr')
            
            if progressBar is not None:
                progressBar.setValue(100)
            
            return newSelection, QgsMapLayerRegistry.instance().addMapLayer(newLayer),  self.populateSrcBox(inputbox,  refbox) 
        else:
            if progressBar is not None:
                progressBar.setValue(100)
            return newSelection,  self.populateSrcBox(inputbox,  refbox)


    def spatialQuery(self, inputbox, refbox, querybox,  progressBar = None):
        """
        Compiles spatial query functions
        """
        
        srcLayer = inputbox.currentText()
        refLayer = refbox.currentText()
        selType = querybox.currentText()
        
        srcLayer = QgsMapLayerRegistry.instance().mapLayersByName(srcLayer)
        refLayer = QgsMapLayerRegistry.instance().mapLayersByName(refLayer)
        refFeats = refLayer[0].getFeatures()
        srcPoints = srcLayer[0].getFeatures()
        

        selectList = []
        
        if selType == "is disjoint to":
            selectList = self.srcDisjointRef(srcLayer, refLayer)
            
            
        else:
            progValue = 5
            for feat in refFeats:
                progValue+=1
                if progValue <= 90 and progressBar is not None:
                    progressBar.setValue(progValue)
                refGeom = feat.geometry()
                srcPoints = srcLayer[0].getFeatures(QgsFeatureRequest().setFilterRect(refGeom.boundingBox()))
                for point in srcPoints:
                    progValue +=1
                    
                    if progValue <= 90 and progressBar is not None:
                        progressBar.setValue(progValue)
                        
                        
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
                    
        return srcLayer[0].setSelectedFeatures(selectList)


    def srcDisjointRef(self, srcLayer, refLayer):
        """
        determines which source features are spatially unrelated to the reference features
        """
        srcPoints = srcLayer[0].getFeatures()
        refFeats = refLayer[0].getFeatures()
        
        selectList = []
        for point in srcPoints:
            selectList.append(point.id())

        selectList2 = []
        
        for feat in refFeats:
            refGeom = feat.geometry()
            srcPoints = srcLayer[0].getFeatures(QgsFeatureRequest().setFilterRect(refGeom.boundingBox()))
            for point in srcPoints:
                if point.geometry().intersects(refGeom):
                        selectList2.append(point.id())
        
        
        selectList3 = [id for id in selectList if id not in selectList2]        
        
        return selectList3
        

    def makeNewLayer(self,  sourceLayer,  filePathLineEdit):
        """
        Open a File Browser Dialog to select location to save new layer
        """ 
        SelectionLayer = QgsMapLayerRegistry.instance().mapLayersByName(sourceLayer)
        SelectedFeats = SelectionLayer[0].selectedFeatures()
        
        newLayerFilePath = filePathLineEdit.text()
        newLayerName =  ntpath.basename(newLayerFilePath)
        
        
        pendingFields = SelectionLayer[0].pendingFields()
        fieldNames = []
        for field in pendingFields:
            fieldNames.append(field.name())
        
        
        CRS = SelectionLayer[0].crs()
        
        
        SelectionType = SelectionLayer[0].wkbType()
        
        writer = QgsVectorFileWriter(newLayerFilePath,  "CP1250",  pendingFields,  SelectionType,  CRS,  "ESRI Shapefile")
        
        if writer.hasError() != QgsVectorFileWriter.NoError:
            msgBox=QMessageBox()
            msgBox.setIcon(3)
            msgBox.setText("Error when creating shapefile. Check that you have chosen a valid place to save it.")
            msgBox.exec_()

        
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
        layers = iface.legendInterface().layers()
        
        nameList = []
        
        for layer in layers:
            name = layer.name()
            feats = layer.getFeatures()
            feat = feats.next()
            if name not in nameList and feat.geometry().type() == 1:
                nameList.append(name)
        
        lineComboBox.clear()
        lineComboBox.addItems(nameList)
        
