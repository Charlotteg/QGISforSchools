# -*- coding: utf-8 -*-

"""
Module implementing unit1wizard.
"""

from PyQt4.QtGui import QWizard
from PyQt4.QtCore import pyqtSignature

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
    
    @pyqtSignature("")
    def on___qt__passive_wizardbutton0_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on___qt__passive_wizardbutton1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
