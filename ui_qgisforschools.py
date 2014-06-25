# -*- coding: utf-8 -*-

"""
Module implementing QGISforSchools introduction page.
"""
#Import the Python, Qt and QGIS libraries
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *

from Ui_ui_qgisforschools import Ui_QGISforSchools
from unit_1_wizard import Unit1Wizard
from Ui_Pop_dev_wizard import Ui_PopDevWizard
from Pop_dev_wizard import PopDevWizard
from earthquakes_wizard import EarthquakesWizard
from tourism_wizard import TourismWizard

class QGISforSchoolsDialog(QDialog, Ui_QGISforSchools):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent,  Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.unit=1
    
    @pyqtSignature("bool")
    def on_unit1_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.unit=1
    
    @pyqtSignature("bool")
    def on_unit2_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.unit=2
    
    @pyqtSignature("bool")
    def on_unit3_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.unit=3
    
    @pyqtSignature("")
    def on_buttonBox_accepted(self):
        """
        Open the correct unit wizard based on the selection made
        """
        msgBox=QMessageBox()
        msgBox.setIcon(3)
        
        self.close()
        if self.unit==1:
            openWizard=PopDevWizard()
            openWizard.show()
            result = openWizard.exec_()
        elif self.unit==2:
            openWizard = TourismWizard()
            openWizard.show()
            result = openWizard.exec_()
        else:
            openWizard=EarthquakesWizard()
            openWizard.show()
            result = openWizard.exec_()
    
    @pyqtSignature("")
    def on_buttonBox_rejected(self):
        """
        Close the window when cancel is clicked
        """
        self.close()
    
#    @pyqtSignature("int")
#    def on_questions_stateChanged(self, p0):
#        """
#        Slot documentation goes here.
#        """
#        # TODO: not implemented yet
#        raise NotImplementedError
