# -*- coding: utf-8 -*-

"""
Module implementing unit1wizard.
"""
import ntpath
import numpy as np

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from Ui_unit_1_wizard import Ui_Unit1

class Unit1Wizard(QWizard, Ui_Unit1):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QWizard.__init__(self, parent,  Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.userPos = None
        
    def moveEvent(self,  event):
        self.userPos = event.pos()

    
    @pyqtSignature("")
    def on___qt__passive_wizardbutton1_clicked(self):
        """
        Slot documentation goes here.
        """
        self.populateSrcList()

    
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

#***************************************Unit 1 Wizard Page 2 *****************************************************************************
    @pyqtSignature("")
    def populateSrcList(self):
        """
        Populate source and reference feature ComboBoxes with the names of the currently loaded layers.
        """   
        #layers = QgsMapLayerRegistry.instance().mapLayers()
        layers = iface.legendInterface().layers()
        
        nameList = []
        
        for layer in layers:
            name = layer.name()
            if name not in nameList:
                nameList.append(name)
            
        #return nameList
        
        self.srcFeatcomboBox.clear()
        self.refFeatcomboBox.clear()
        self.lyrcomboBox.clear()
        
        self.srcFeatcomboBox.addItems(nameList)
        self.refFeatcomboBox.addItems(nameList)
        self.lyrcomboBox.addItems(nameList)
        
#    @pyqtSignature("")
#    def on_wizardPage3_completeChanged(self):
#        """
#        function description here
#        """
#        self.populateSrcList()

    @pyqtSignature("QString")
    def on_srcFeatcomboBox_activated(self,  p0):
        """
        removes the selected source feature from the list of options for reference
        """
        srcLayerName = self.srcFeatcomboBox.currentText()
        
        layers = iface.legendInterface().layers()
        
        refList = []
        
        for layer in layers:
            name = layer.name()
            if name != srcLayerName:
                refList.append(name)
        
        self.refFeatcomboBox.clear()
        
        #print refList
        
        self.refFeatcomboBox.addItems(refList)
        
        self.populateSelBox()
        

    @pyqtSignature("QString")
    def on_refFeatcomboBox_activated(self,  p0):
        
        self.populateSelBox()
        
    @pyqtSignature("")
    def populateSelBox(self):
        """
        populates the 'process' combobox with the correct options based on the source and reference features.
        """
        srcLayerName = self.srcFeatcomboBox.currentText()
        refLayerName = self.refFeatcomboBox.currentText()
        sLayer = QgsMapLayerRegistry.instance().mapLayersByName(srcLayerName)
        rLayer = QgsMapLayerRegistry.instance().mapLayersByName(refLayerName)
        
        Line2Line = ["cross",  "equal",  "intersect",  "are disjoint to",  "overlap",  "touch"]
        Line2Point = ["contain",  "intersect",  "are disjoint to"]
        Point2Point = ["equal",  "intersect",  "are disjoint to",  "overlap"]
        Poly2Poly = ["contain",  "equal",  "intersect",  "are disjoint to",  "overlap", "touch",  "are within"]
        Poly2Line = ["contain",  "intersect",  "are disjoint to"]
        Line2Poly = ["cross",  "intersect",  "are disjoint to",  "touch",  "are within"]
        Point2Line =["cross",  "intersect",  "are disjoint to",  "touch",  "are within"]
        Poly2Point = ["contain",  "intersect",  "are disjoint to"]
        Point2Poly = ["cross",  "intersect",  "are disjoint to",  "touch", "are within"]
        
        sFeats = sLayer[0].getFeatures()
        sFeat = sFeats.next()
        sGeom = sFeat.geometry()
        sType = sGeom.type()
        
        rFeats = rLayer[0].getFeatures()
        rFeat = rFeats.next()
        rGeom = rFeat.geometry()
        rType = rGeom.type()
        
        self.selTypecomboBox.clear()
        
        if sType == 0 and rType == 0:
            self.selTypecomboBox.addItems(Point2Point)
        elif sType == 0 and rType ==1:
            self.selTypecomboBox.addItems(Point2Line)
        elif sType == 1 and rType == 0:
            self.selTypecomboBox.addItems(Line2Point)
        elif sType == 0 and rType == 2:
            self.selTypecomboBox.addItems(Point2Poly)
        elif sType == 2 and rType == 0:
            self.selTypecomboBox.addItems(Poly2Point)
        elif sType == 1 and rType == 1:
            self.selTypecomboBox.addItems(Line2Line)
        elif sType == 1 and rType == 2:
            self.selTypecomboBox.addItems(Line2Poly)
        elif sType == 2 and rType == 1:
            self.selTypecomboBox.addItems(Poly2Line)
        elif sType == 2 and rType == 2:
            self.selTypecomboBox.addItems(Poly2Poly)
        else:
            #put a messagebox here
            print "problems!"
        
        
#*****************QUERY BUTTON CLICKED *********************************
    
    @pyqtSignature("")
    def on_queryButton_clicked(self):
        """
        function description here
        """


        #put an error message if no layers loaded
        sourceLayer = self.srcFeatcomboBox.currentText()
        referenceLayer = self.refFeatcomboBox.currentText()
        selectionType = self.selTypecomboBox.currentText()
        
        self.QueryprogressBar.setValue(33)

        newSelection = self.srcSpatialQuery(sourceLayer,  referenceLayer,  selectionType)

        
        if self.newLayercheckBox.isChecked():
            
            self.makeNewLayer(sourceLayer)
            layerFilePath = self.FilePathlineEdit_4.text()
            newLayerName =  ntpath.basename(layerFilePath)
            legendName = newLayerName.split(".")
            newLayer = QgsVectorLayer(layerFilePath,  legendName[0],  'ogr')
            
            return newSelection, QgsMapLayerRegistry.instance().addMapLayer(newLayer),  self.populateSrcList(),  self.QueryprogressBar.setValue(100)  
        else:
            return newSelection,  self.populateSrcList(),  self.QueryprogressBar.setValue(100)
            


# ********************************************************************************
    @pyqtSignature("")
    def srcWithinRef(self, srcLayer, refLayer):
        """
        determines which source features are within the reference features
        """
        srcLayer = QgsMapLayerRegistry.instance().mapLayersByName(srcLayer)
        refLayer = QgsMapLayerRegistry.instance().mapLayersByName(refLayer)
        
        refFeats = refLayer[0].getFeatures()

        
        selectList = []
        
        for feat in refFeats:
            refGeom = feat.geometry()
            srcPoints = srcLayer[0].getFeatures(QgsFeatureRequest().setFilterRect(refGeom.boundingBox()))
            for point in srcPoints:
                if point.geometry().within(refGeom):
                    selectList.append(point.id())
                    
        return selectList

           
    @pyqtSignature("")
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
            #srcPoints = srcLayer[0].getFeatures()
            for point in srcPoints:
                if point.geometry().intersects(refGeom):
                        selectList2.append(point.id())
        
        
        selectList3 = [id for id in selectList if id not in selectList2]        
        
        return selectList3

    @pyqtSignature("")
    def srcSpatialQuery(self, srcLayer, refLayer, selType):
        """
        Compiles spatial query functions
        """
        self.QueryprogressBar.reset()
        
        srcLayer = QgsMapLayerRegistry.instance().mapLayersByName(srcLayer)
        refLayer = QgsMapLayerRegistry.instance().mapLayersByName(refLayer)
        refFeats = refLayer[0].getFeatures()
        srcPoints = srcLayer[0].getFeatures()
        
        self.QueryprogressBar.setValue(66)

        selectList = []
        
        if selType == "are disjoint to":
            selectList = self.srcDisjointRef(srcLayer, refLayer)
            
            
        else:
        
            for feat in refFeats:
                
                refGeom = feat.geometry()
                srcPoints = srcLayer[0].getFeatures(QgsFeatureRequest().setFilterRect(refGeom.boundingBox()))
                for point in srcPoints:
                    if selType == "are within":
                        if point.geometry().within(refGeom):
                            selectList.append(point.id())
                    elif selType == "cross":
                        if point.geometry().crosses(refGeom):
                            selectList.append(point.id())
                    elif selType == "equal":
                        if point.geometry().equals(refGeom):
                            selectList.append(point.id())
                    elif selType == "intersect":
                        if point.geometry().intersects(refGeom):
                            selectList.append(point.id())
                    elif selType == "overlap":
                        if point.geometry().overlaps(refGeom):
                            selectList.append(point.id())
                    elif selType == "touches":
                        if point.geometry().touches(refGeom):
                            selectList.append(point.id())
                    else:
                        if point.geometry().contains(refGeom):
                            selectList.append(point.id())
                    
        return srcLayer[0].setSelectedFeatures(selectList)

#    @pyqtSignature("")
#    def srcSpatialQuery2(self, srcLayer, refLayer,  selType):
#        """
#        Doesn't work, use srcSpatialQuery1
#        """
#        srcLayer = QgsMapLayerRegistry.instance().mapLayersByName(srcLayer)
#        refLayer = QgsMapLayerRegistry.instance().mapLayersByName(refLayer)
#        refFeats = refLayer[0].getFeatures()
#        
#        selectList = []
#        
#        for feat in refFeats:
#            
#            refGeom = feat.geometry()
#            srcPoints = srcLayer[0].getFeatures(QgsFeatureRequest().setFilterRect(refGeom.boundingBox()))
#                
#                
#            for point in srcPoints:
#                if selType == "within":
#                    if point.geometry().within(refGeom):
#                        selectList.append(point.id())
#                elif selType == "cross":
#                    if point.geometry().crosses(refGeom):
#                        selectList.append(point.id())
#                elif selType == "equal":
#                    if point.geometry().equals(refGeom):
#                        selectList.append(point.id())
#                elif selType == "intersect":
#                    if point.geometry().intersects(refGeom):
#                        selectList.append(point.id())
#                elif selType == "are disjoint to":
#                    if point.geometry().disjoint(refGeom):
#                        selectList.append(point.id())
#                elif selType == "overlap":
#                    if point.geometry().overlaps(refGeom):
#                        selectList.append(point.id())
#                elif selType == "touches":
#                    if point.geometry().touches(refGeom):
#                        selectList.append(point.id())
#                else:
#                    if point.geometry().contains(refGeom):
#                        selectList.append(point.id())
#                    
#        return srcLayer[0].setSelectedFeatures(selectList)


    @pyqtSignature("")
    def on_clearSelectionButton_clicked(self):
        """
        Clears current selection
        """
        layers = iface.legendInterface().layers()
        
        for layer in layers:
            layer.removeSelection()
            
    
    @pyqtSignature("")
    def on_BrowsepushButton_4_clicked(self):
        """
        Open a File Browser Dialog to select location to save new layer
        """
#        if self.newLayercheckBox.isChecked():
#            self.FilePathlineEdit_4.setEnabled(True)
            
        inputFile = QFileDialog.getSaveFileName(self, 'Save As','', 'Shapefiles (*.shp)')
        self.FilePathlineEdit_4.setText(inputFile)
        
    @pyqtSignature("")
    def makeNewLayer(self,  sourceLayer):
        """
        Open a File Browser Dialog to select location to save new layer
        """ 
        SelectionLayer = QgsMapLayerRegistry.instance().mapLayersByName(sourceLayer)
        SelectedFeats = SelectionLayer[0].selectedFeatures()
        
        newLayerFilePath = self.FilePathlineEdit_4.text()
        newLayerName =  ntpath.basename(newLayerFilePath)
        
        print newLayerName
        
        pendingFields = SelectionLayer[0].pendingFields()
        fieldNames = []
        for field in pendingFields:
            fieldNames.append(field.name())
        
        print fieldNames
        
        CRS = SelectionLayer[0].crs()
        
        print CRS
        
        SelectionType = SelectionLayer[0].wkbType()
        
        writer = QgsVectorFileWriter(newLayerFilePath,  "CP1250",  pendingFields,  SelectionType,  CRS,  "ESRI Shapefile")
        
        if writer.hasError() != QgsVectorFileWriter.NoError:
            #print "Error when creating shapefile: ",  writer.errorMessage()
            msgBox=QMessageBox()
            msgBox.setIcon(3)
            msgBox.setText("Error when creating shapefile. Check that you have chosen a valid place to save it.")
            msgBox.exec_()

        
        for feat in SelectedFeats:
            writer.addFeature(feat)
        
#        newVectorLayer = QgsVectorLayer(newLayerFilePath,  newLayerName,  'ogr')
#        
#        print newVectorLayer
#        
#        return newVectorLayer


#***************************************Unit 1 Wizard Page 3 *****************************************************************************
  
    @pyqtSignature("")
    def on_openATButton_clicked(self):
        """
        description here
        """
        
        Layer = QgsMapLayerRegistry.instance().mapLayersByName("countries")
        dialog = QgsAttributeDialog(Layer)
        dialog.show()
        
    @pyqtSignature("QString")
    def on_lyrcomboBox_activated(self,  p0):
        """
        description here
        """
        
        
        
        lyrName = self.lyrcomboBox.currentText()
        lyr = QgsMapLayerRegistry.instance().mapLayersByName(lyrName)[0]
        lyrFeats = lyr.getFeatures()
        
        featureArray = self.createFeatureArray(lyrFeats)
        shape = featureArray.shape
        rows = shape[0]
        cols = shape[1]
        
        model = QStandardItemModel(rows,  cols)
        
        for i in range(rows):
            for j in range(cols):
                featAttribute = featureArray[i, j]
                if featAttribute == "Null":
                    item = QStandardItem("-")
                else:
                    item = QStandardItem(featAttribute)
                model.setItem(i, j, item)
        
        self.attributeTableView.setModel(model)
        
    @pyqtSignature("")
    def createFeatureArray(self,  lyrFeats):
        """
        description here
        """        
        featIdlist = []
        fullFeatureList= []
        for feat in lyrFeats:
            featIdlist.append(feat.id())
            featAttributes = feat.attributes()
            fullFeatureList.extend(featAttributes)
        
        rows = len(featIdlist)
        cols = len(featAttributes)
        
#        print cols
#        print rows
#        print len(fullFeatureList)
    
        featArray = np.array([fullFeatureList])
        featArray2 = np.reshape(featArray, (rows, cols))
        return featArray2
        
        

        
            


        
