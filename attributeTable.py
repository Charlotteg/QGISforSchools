# -*- coding: utf-8 -*-

"""
Module containing a class that deals with creating an attrubute table
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
        #get all required information
        lyrName = lyrComboBox.currentText()
        lyr = QgsMapLayerRegistry.instance().mapLayersByName(lyrName)[0]
        lyrFeats = lyr.getFeatures()
        
        #get array of attributes
        featureArray = self.createFeatureArray(lyrFeats)
        shape = featureArray.shape
        rows = shape[0]
        cols = shape[1]
        
        #set up the model for the table view
        model = QStandardItemModel(rows,  cols)
        
        self.setFieldNames(model,  lyr)
        
        #load data into the model, dealing with NULL values
        for i in range(rows):
            for j in range(cols):
                if type(featureArray[i, j]) == QPyNullVariant:
                    item = QStandardItem("unknown")
                else:
                    item = QStandardItem(featureArray[i, j])
                model.setItem(i, j, item)
  
  
        tableView.setModel(model)
  
#       below is the beginnings of support for sorting the tables     
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
        #add features to the attribute list
        for feat in lyrFeats:
            if feat == NULL:
                feat = None
            featIdlist.append(feat.id())
            featAttributes = feat.attributes()
            fullFeatureList.extend(featAttributes)
            
        #get size of attribute table
        rows = len(featIdlist)
        cols = len(featAttributes)
    
        #create an array af attributes and return it
        featArray = np.array([fullFeatureList])
        featArray2 = np.reshape(featArray, (rows, cols))
        return featArray2

    

    def setFieldNames(self, model,  lyr):
        """
        Set the column names for the attribute table
        """  
        #get the fields
        fields = lyr.pendingFields()
        position = 0
        
        #set column names
        for field in fields:
            model.setHorizontalHeaderItem(position, QStandardItem(field.name()))
            position+=1
