# -*- coding: utf-8 -*-

"""
Module implementing DockWidget.
"""

from PyQt4.QtGui import QDockWidget
from PyQt4.QtCore import pyqtSignature

from Ui_dock_widget import Ui_DockWidget

class DockWidget(QDockWidget, Ui_DockWidget):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDockWidget.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("QString")
    def on_comboBox_activated(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
