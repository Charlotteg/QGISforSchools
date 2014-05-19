# -*- coding: utf-8 -*-

"""
Module implementing unit1wizard.
"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *

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
        Open a File Browser Dialog - for the countries layer
        """
        # set the chosen file as the input for the FilePathLineEdit
        inputFile = QFileDialog.getOpenFileName(self, 'Open Cities.shp','', 'Shapefiles (*.shp)')
        self.FilePathlineEdit_2.setText(inputFile)

