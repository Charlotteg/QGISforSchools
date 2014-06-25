# -*- coding: utf-8 -*-

"""
Module containing a class that deals with marker styling
"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *



class MagicMarkers():
    """
    Class that deals with marker stuff
    """ 
    def viewSVGs(self,  graphicsView):
        
        scene = QGraphicsScene()
        #item = QGraphicsItem()
        #graphicsView = MarkerDialog().SVGView
        graphicsView.setScene(scene)
        
        #item = QGraphicsSvgItem('C:/PROGRA~2/QGISVA~1/apps/qgis/svg/crosses/Star1.svg')
        
        starPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'os.pardir', 'apps/qgis/svg/crosses/Star1.svg'))
        
        
        print path
        #scene.addItem(item)

    def getSVGs(self):
        svgPath = "C:/PROGRA~2/QGISVA~1/apps/qgis/svg" 
        folders = os.listdir("C:/PROGRA~2/QGISVA~1/apps/qgis/svg")
        symbolNames = []
        for folder in folders:
            newPath = svgPath + "/"+str(folder)
            svgFiles = os.listdir(newPath)
            for file in svgFiles:
                symbolName = "/"+str(folder)+"/"+str(file)
                symbolNames.append(symbolName)
        
        #return symbolNames
        
        print os.getcwd()
        
        
    def setSVG(self,  layerName):
        Layer = QgsMapLayerRegistry.instance().mapLayersByName("tourist_attraction")[0]
        renderer = Layer.rendererV2()
        symbol = renderer.symbol()
        svgLayer = QgsSvgMarkerSymbolLayerV2("/arrows/Arrow_01.svg")
        symbol.changeSymbolLayer(0, svgLayer)
        iface.mapCanvas().refresh()
        iface.legendInterface().refreshLayerSymbology(Layer)
