# -*- coding: utf-8 -*-

"""
Module containing a class that deals with marker styling
"""
from PyQt4.QtGui import *
from PyQt4.QtSvg import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *



class MagicMarkers():
    """
    Class that deals with marker stuff
    """ 

    def viewSVGs(self,  graphicsView):
        
        svgPath = "C:/PROGRA~2/QGISVA~1/apps/qgis/svg"
        
        scene = QGraphicsScene()
        #item = QGraphicsItem()
        #graphicsView = MarkerDialog().SVGView
        graphicsView.setScene(scene)
        
        svgs = []
        
        svgNames = self.getSVGs()
        x = 0
        y = 0
        i = 0
        
        
        for name in svgNames:
            
            path = "C:/PROGRA~2/QGISVA~1/apps/qgis/svg"+ str(name)
            pic = QPixmap(path)
            pic.scaled(10, 10)
            x += 30
            i+= 1
            if i == 13:
                y+= 30
                x=0
                i = 0
            
            
            svgItem = scene.addPixmap(pic)
            svgItem.setScale(0.05)
            svgItem.setPos(x, y)
            svgItem.setFlags(svgItem.ItemIsSelectable)
            svgs.append((svgItem,  name))
        
        svgdict = dict(svgs)
        return svgdict,  scene


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
        
        return symbolNames
        
        
    def setSVG(self,  layerName, attribute, scene,  svgdict):
        
        Layer = QgsMapLayerRegistry.instance().mapLayersByName(layerName)[0]
        renderer = Layer.rendererV2()
        symbol = renderer.symbolForValue(attribute)
        selectedSvg = scene.selectedItems()[0]
        name = svgdict[selectedSvg]
        svgLayer = QgsSvgMarkerSymbolLayerV2(name)
        symbol.changeSymbolLayer(0, svgLayer)

        #QgsRendererCategoryV2(attribute, symbol ,  str(attribute)) 

        
        iface.mapCanvas().refresh()
        iface.legendInterface().refreshLayerSymbology(Layer)
        
        
        
        
