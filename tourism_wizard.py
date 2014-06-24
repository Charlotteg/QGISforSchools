# -*- coding: utf-8 -*-

"""
Module implementing TourismWizard.
"""

import ntpath
import numpy as np
import math

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

#Import other classes required here
from score import ScoreSystem
from colours import colourManager
from misc_classes import CitiesCustomSortingModel,  CountriesCustomSortingModel
from addlayers import AddLayers

from Ui_tourism_wizard import Ui_TourismWizard

class TourismWizard(QWizard, Ui_TourismWizard):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QWizard.__init__(self, parent,  Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.score = 0
        self.q1 = False
        self.q2 = False
        self.q3 = False
        self.q4 = False
        self.q5 = False
        self.q6 = False
        self.scoreLabels = [self.Score_label,  self.Score_label_2,  self.Score_label_3,  self.Score_label_4,  self.Score_label_5, self.Score_label_6,  self.Score_label_7,  self.Score_label_8,  self.Score_label_9,  self.Score_label_10]
        
       
#*************************************** Page 2 *****************************************************************************   
    @pyqtSignature("")
    def on_AddWoodLayer_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
