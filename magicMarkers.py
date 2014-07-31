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
    Class that deals with changing the marker
    """ 

    def viewSVGs(self,  graphicsView):
        """
        Get svgs and render them on the graphics view
        """ 
        
        svgPath = "C:/PROGRA~2/QGISVA~1/apps/qgis/svg"
        
        scene = QGraphicsScene()
        graphicsView.setScene(scene)
        
        svgs = []
        
        #get svg paths
        svgNames = self.getSVGs()
        x = 0
        y = 0
        i = 0
        
        
        for name in svgNames:
            
            #path = "C:/PROGRA~2/QGISVA~1/apps/qgis/svg"+ str(name)
            
            #create a pixmap from the SVG and get position for the graphics view
            path = name
            pic = QPixmap(path)
            pic.scaled(10, 10)
            x += 30
            i+= 1
            if i == 13:
                y+= 30
                x=0
                i = 0
            
            #add pixmap to the graphicsView
            svgItem = scene.addPixmap(pic)
            svgItem.setScale(0.05)
            svgItem.setPos(x, y)
            #allow the pixmap to be selected
            svgItem.setFlags(svgItem.ItemIsSelectable)
            svgs.append((svgItem,  name))
            
        #create a dictionary of SVGs so that the correct path can be found based on the pixmap selected
        svgdict = dict(svgs)
        return svgdict,  scene


    def getSVGs(self):
        """
        Get svgs from QGIS files
        """ 
        
#        svgPath = "C:/PROGRA~2/QGISVA~1/apps/qgis/svg" 
#        folders = os.listdir("C:/PROGRA~2/QGISVA~1/apps/qgis/svg")

        #get svg paths
        svgs = QgsSymbolLayerV2Utils.listSvgFiles()
        
        
#        print svgs
#        symbolNames = []
#        for folder in folders:
#            newPath = svgPath + "/"+str(folder)
#            svgFiles = os.listdir(newPath)
#            for file in svgFiles:
#                symbolName = "/"+str(folder)+"/"+str(file)
#                symbolNames.append(symbolName)
        
        return svgs
        
        
    def setSVG(self,  layerName, attribute, scene,  svgdict):
        """
        Set the layer symbol to the svg symbol chosen in the dialog
        """ 
        #get required information
        Layer = QgsMapLayerRegistry.instance().mapLayersByName(layerName)[0]
        renderer = Layer.rendererV2()
        #this is the line that causes problems with QGIS 2.4. Research into changes in API to update.
        symbol = renderer.symbolForValue(str(attribute))
        
        #look up SVG based on the picmap selected and set it as the new symbol
        selectedSvg = scene.selectedItems()[0]
        name = svgdict[selectedSvg]
        svgLayer = QgsSvgMarkerSymbolLayerV2(name)
        symbol.changeSymbolLayer(0, svgLayer)
        
        #Refresh the map canvas and legend
        iface.mapCanvas().refresh()
        iface.legendInterface().refreshLayerSymbology(Layer)
        
        
        
        
