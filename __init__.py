# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QGISforSchools
                                 A QGIS plugin
 Plugin for use in UK schools
                             -------------------
        begin                : 2014-05-18
        copyright            : (C) 2014 by Charlotte Graves/ University of Edinburgh
        email                : charlottergraves@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load QGISforSchools class from file QGISforSchools
    from qgisforschools import QGISforSchools
    return QGISforSchools(iface)
