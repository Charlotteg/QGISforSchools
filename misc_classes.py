# -*- coding: utf-8 -*-

"""
Module with miscellaneous classes used in units
"""
import ntpath
import numpy as np

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

class CitiesCustomSortingModel(QSortFilterProxyModel):
    def lessThan(self,  left,  right):
        col = left.column()
        dataleft = left.data()
        dataright = right.data()
        
        if col > 2:
            dataleft = float(dataleft)
            dataright = float(dataright)
         
        lessthan = self.boolReturn(dataleft,  dataright)
        return lessthan
    
    def boolReturn(self,  dataleft,  dataright):
        if dataleft < dataright:
            return True
        else:
            return False
            
class CountriesCustomSortingModel(QSortFilterProxyModel):
    def lessThan(self,  left,  right):
        col = left.column()
        dataleft = left.data()
        dataright = right.data()
            
        if col == 4 or 5 or 6:
            dataleft = float(dataleft)
            dataright = float(dataright)
            
        lessthan = self.boolReturn(dataleft,  dataright)
        return lessthan
        
    def boolReturn(self,  dataleft,  dataright):
        if dataleft < dataright:
            return True
        else:
            return False
