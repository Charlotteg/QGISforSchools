# -*- coding: utf-8 -*-

"""
Module containing a class that deals with changing the colour schemes of given layers
"""
import numpy as np

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

class AttributeTable():
    """
    Class that creates attribute tables for table views
    """
    def attributeTable(self, lyrComboBox,  tableView,  sorting= False):
        """
        populate the attribute table with data based on the layer chosen in the lyrcomboBox
        """

        lyrName = lyrComboBox.currentText()
        lyr = QgsMapLayerRegistry.instance().mapLayersByName(lyrName)[0]
        lyrFeats = lyr.getFeatures()
        
        featureArray = self.createFeatureArray(lyrFeats)
        shape = featureArray.shape
        rows = shape[0]
        cols = shape[1]
        
        model = QStandardItemModel(rows,  cols)
        
        self.setFieldNames(model,  lyr)
        
        for i in range(rows):
            for j in range(cols):
                if type(featureArray[i, j]) == QPyNullVariant:
                    item = QStandardItem("unknown")
                else:
                    item = QStandardItem(featureArray[i, j])
                model.setItem(i, j, item)
  
  
        tableView.setModel(model)
  
    
#        if sorting:
#            self.attributeTableView.setSortingEnabled(True)
#        
#        
#            if lyrName == "major_cities":
#                proxyModel = CitiesCustomSortingModel(self)
#                proxyModel.setSourceModel(model)
#                self.attributeTableView.setModel(proxyModel)
#                
#            else:
#                proxyModel = CountriesCustomSortingModel(self)
#                proxyModel.setSourceModel(model)
#                self.attributeTableView.setModel(proxyModel)
        

      #  selected = tableView.selectionModel().selectedRows()

   

    def createFeatureArray(self,  lyrFeats):
        """
        puts all of the attributes of the layer features into a 2d array, ready to be added to the model
        """        
        featIdlist = []
        fullFeatureList= []
        for feat in lyrFeats:
            if feat == NULL:
                feat = None
            featIdlist.append(feat.id())
            featAttributes = feat.attributes()
            fullFeatureList.extend(featAttributes)
        
        rows = len(featIdlist)
        cols = len(featAttributes)
    
        featArray = np.array([fullFeatureList])
        featArray2 = np.reshape(featArray, (rows, cols))
        return featArray2

    

    def setFieldNames(self, model,  lyr):
        """
        Set the column names for the attribute table
        """        
        fields = lyr.pendingFields()
        position = 0
        
        for field in fields:
            model.setHorizontalHeaderItem(position, QStandardItem(field.name()))
            position+=1
