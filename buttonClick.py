# -*- coding: utf-8 -*-

"""
Module implementing PopDevWizard.
"""
# Import the Python, PyQt and QGIS libraries
import ntpath
import numpy as np

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

#Import other classes required here

from Ui_Pop_dev_wizard import Ui_PopDevWizard

class clickButton(Ui_PopDevWizard):
    """
    Class monitoring the number of times a button is clicked
    """
    def __init__(self,  parent = None):
        """
        Constructor
        """
        self.clicks = 0
        

    def on_checkAnswersPop_clicked(self):
        self.clicks += 1
        return self.clicks
