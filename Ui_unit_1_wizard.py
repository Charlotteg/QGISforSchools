# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\charlottegraves\.qgis2\python\plugins\QGISforSchools\unit_1_wizard.ui'
#
# Created: Sat May 31 16:12:22 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Unit1(object):
    def setupUi(self, Unit1):
        Unit1.setObjectName(_fromUtf8("Unit1"))
        Unit1.setEnabled(True)
        Unit1.resize(324, 588)
        Unit1.setWhatsThis(_fromUtf8(""))
        Unit1.setAutoFillBackground(False)
        Unit1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        Unit1.setWizardStyle(QtGui.QWizard.AeroStyle)
        Unit1.setOptions(QtGui.QWizard.HelpButtonOnRight)
        self.wizardPage1 = QtGui.QWizardPage()
        self.wizardPage1.setObjectName(_fromUtf8("wizardPage1"))
        self.label = QtGui.QLabel(self.wizardPage1)
        self.label.setGeometry(QtCore.QRect(60, -20, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowser = QtGui.QTextBrowser(self.wizardPage1)
        self.textBrowser.setGeometry(QtCore.QRect(20, 70, 271, 401))
        self.textBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        Unit1.addPage(self.wizardPage1)
        self.wizardPage2 = QtGui.QWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.wizardPage2)
        self.textBrowser_2.setGeometry(QtCore.QRect(25, 20, 261, 131))
        self.textBrowser_2.setWhatsThis(_fromUtf8(""))
        self.textBrowser_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_2.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.FilePathlineEdit = QtGui.QLineEdit(self.wizardPage2)
        self.FilePathlineEdit.setGeometry(QtCore.QRect(30, 180, 171, 20))
        self.FilePathlineEdit.setObjectName(_fromUtf8("FilePathlineEdit"))
        self.BrowsepushButton = QtGui.QPushButton(self.wizardPage2)
        self.BrowsepushButton.setGeometry(QtCore.QRect(210, 180, 75, 23))
        self.BrowsepushButton.setObjectName(_fromUtf8("BrowsepushButton"))
        self.label_2 = QtGui.QLabel(self.wizardPage2)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 131, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.wizardPage2)
        self.label_3.setGeometry(QtCore.QRect(30, 230, 131, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.FilePathlineEdit_2 = QtGui.QLineEdit(self.wizardPage2)
        self.FilePathlineEdit_2.setGeometry(QtCore.QRect(30, 250, 171, 20))
        self.FilePathlineEdit_2.setObjectName(_fromUtf8("FilePathlineEdit_2"))
        self.BrowsepushButton_2 = QtGui.QPushButton(self.wizardPage2)
        self.BrowsepushButton_2.setGeometry(QtCore.QRect(210, 250, 75, 23))
        self.BrowsepushButton_2.setObjectName(_fromUtf8("BrowsepushButton_2"))
        self.label_4 = QtGui.QLabel(self.wizardPage2)
        self.label_4.setGeometry(QtCore.QRect(30, 300, 131, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.BrowsepushButton_3 = QtGui.QPushButton(self.wizardPage2)
        self.BrowsepushButton_3.setGeometry(QtCore.QRect(210, 320, 75, 23))
        self.BrowsepushButton_3.setObjectName(_fromUtf8("BrowsepushButton_3"))
        self.FilePathlineEdit_3 = QtGui.QLineEdit(self.wizardPage2)
        self.FilePathlineEdit_3.setGeometry(QtCore.QRect(30, 320, 171, 20))
        self.FilePathlineEdit_3.setObjectName(_fromUtf8("FilePathlineEdit_3"))
        self.AddLayerButton = QtGui.QPushButton(self.wizardPage2)
        self.AddLayerButton.setGeometry(QtCore.QRect(30, 380, 251, 21))
        self.AddLayerButton.setObjectName(_fromUtf8("AddLayerButton"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.wizardPage2)
        self.textBrowser_3.setGeometry(QtCore.QRect(30, 430, 251, 71))
        self.textBrowser_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_3.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        Unit1.addPage(self.wizardPage2)
        self.wizardPage_2 = QtGui.QWizardPage()
        self.wizardPage_2.setObjectName(_fromUtf8("wizardPage_2"))
        self.textBrowser_5 = QtGui.QTextBrowser(self.wizardPage_2)
        self.textBrowser_5.setGeometry(QtCore.QRect(10, 40, 281, 451))
        self.textBrowser_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_5.setObjectName(_fromUtf8("textBrowser_5"))
        self.label_9 = QtGui.QLabel(self.wizardPage_2)
        self.label_9.setGeometry(QtCore.QRect(70, -20, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        Unit1.addPage(self.wizardPage_2)
        self.wizardPage3 = QtGui.QWizardPage()
        self.wizardPage3.setObjectName(_fromUtf8("wizardPage3"))
        self.textBrowser_4 = QtGui.QTextBrowser(self.wizardPage3)
        self.textBrowser_4.setGeometry(QtCore.QRect(10, 20, 256, 91))
        self.textBrowser_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_4.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        self.queryButton = QtGui.QPushButton(self.wizardPage3)
        self.queryButton.setGeometry(QtCore.QRect(150, 450, 75, 23))
        self.queryButton.setObjectName(_fromUtf8("queryButton"))
        self.QueryprogressBar = QtGui.QProgressBar(self.wizardPage3)
        self.QueryprogressBar.setGeometry(QtCore.QRect(40, 420, 201, 21))
        self.QueryprogressBar.setProperty("value", 0)
        self.QueryprogressBar.setObjectName(_fromUtf8("QueryprogressBar"))
        self.clearSelectionButton = QtGui.QPushButton(self.wizardPage3)
        self.clearSelectionButton.setGeometry(QtCore.QRect(60, 450, 81, 21))
        self.clearSelectionButton.setObjectName(_fromUtf8("clearSelectionButton"))
        self.selTypecomboBox = QtGui.QComboBox(self.wizardPage3)
        self.selTypecomboBox.setGeometry(QtCore.QRect(110, 240, 91, 21))
        self.selTypecomboBox.setObjectName(_fromUtf8("selTypecomboBox"))
        self.selTypecomboBox.addItem(_fromUtf8(""))
        self.selTypecomboBox.addItem(_fromUtf8(""))
        self.selTypecomboBox.addItem(_fromUtf8(""))
        self.selTypecomboBox.addItem(_fromUtf8(""))
        self.refFeatcomboBox = QtGui.QComboBox(self.wizardPage3)
        self.refFeatcomboBox.setGeometry(QtCore.QRect(110, 190, 91, 21))
        self.refFeatcomboBox.setObjectName(_fromUtf8("refFeatcomboBox"))
        self.refFeatcomboBox.addItem(_fromUtf8(""))
        self.refFeatcomboBox.addItem(_fromUtf8(""))
        self.refFeatcomboBox.addItem(_fromUtf8(""))
        self.label_5 = QtGui.QLabel(self.wizardPage3)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 160, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_7 = QtGui.QLabel(self.wizardPage3)
        self.label_7.setGeometry(QtCore.QRect(20, 220, 130, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.srcFeatcomboBox = QtGui.QComboBox(self.wizardPage3)
        self.srcFeatcomboBox.setGeometry(QtCore.QRect(110, 140, 91, 21))
        self.srcFeatcomboBox.setObjectName(_fromUtf8("srcFeatcomboBox"))
        self.srcFeatcomboBox.addItem(_fromUtf8(""))
        self.srcFeatcomboBox.addItem(_fromUtf8(""))
        self.srcFeatcomboBox.addItem(_fromUtf8(""))
        self.label_8 = QtGui.QLabel(self.wizardPage3)
        self.label_8.setGeometry(QtCore.QRect(180, 270, 93, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_6 = QtGui.QLabel(self.wizardPage3)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 116, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.newLayergroupBox = QtGui.QGroupBox(self.wizardPage3)
        self.newLayergroupBox.setGeometry(QtCore.QRect(20, 300, 241, 101))
        self.newLayergroupBox.setObjectName(_fromUtf8("newLayergroupBox"))
        self.newLayercheckBox = QtGui.QCheckBox(self.newLayergroupBox)
        self.newLayercheckBox.setGeometry(QtCore.QRect(10, 30, 241, 17))
        self.newLayercheckBox.setObjectName(_fromUtf8("newLayercheckBox"))
        self.FilePathlineEdit_4 = QtGui.QLineEdit(self.newLayergroupBox)
        self.FilePathlineEdit_4.setEnabled(False)
        self.FilePathlineEdit_4.setGeometry(QtCore.QRect(10, 60, 131, 21))
        self.FilePathlineEdit_4.setObjectName(_fromUtf8("FilePathlineEdit_4"))
        self.BrowsepushButton_4 = QtGui.QPushButton(self.newLayergroupBox)
        self.BrowsepushButton_4.setEnabled(False)
        self.BrowsepushButton_4.setGeometry(QtCore.QRect(150, 60, 75, 23))
        self.BrowsepushButton_4.setObjectName(_fromUtf8("BrowsepushButton_4"))
        Unit1.addPage(self.wizardPage3)
        self.wizardPage = QtGui.QWizardPage()
        self.wizardPage.setObjectName(_fromUtf8("wizardPage"))
        Unit1.addPage(self.wizardPage)

        self.retranslateUi(Unit1)
        QtCore.QObject.connect(self.newLayercheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.FilePathlineEdit_4.setEnabled)
        QtCore.QObject.connect(self.newLayercheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.BrowsepushButton_4.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Unit1)

    def retranslateUi(self, Unit1):
        Unit1.setWindowTitle(_translate("Unit1", "Unit 1 - Spatial Query", None))
        self.label.setText(_translate("Unit1", "Unit 1 - Spatial Query", None))
        self.textBrowser.setHtml(_translate("Unit1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">*** Description - goals and steps ***</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">GIS not only allows you to make maps, but also helps you to answer questions about how layers are related. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">A </span><span style=\" font-size:10pt; font-style:italic;\">Spatial Query</span><span style=\" font-size:10pt;\"> investigates how layers are related in space. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">In this unit we/you are going to explore ....</span></p></body></html>", None))
        self.textBrowser_2.setHtml(_translate("Unit1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">***Explanation about adding data ***</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">To explore spatial relationships, we must first add the spatial data. This can be in the form of layers of points, lines or polygons that represent features like countries and cities.Use the Browse buttons below to select the countries.shp, cities.shp and equator.shp files, then click Add Layers! to add them to your map. ***too much!***</span></p></body></html>", None))
        self.BrowsepushButton.setText(_translate("Unit1", "Browse", None))
        self.label_2.setText(_translate("Unit1", "1. Add the countries layer:", None))
        self.label_3.setText(_translate("Unit1", "2. Add the cities layer:", None))
        self.BrowsepushButton_2.setText(_translate("Unit1", "Browse", None))
        self.label_4.setText(_translate("Unit1", "3. Add the equator:", None))
        self.BrowsepushButton_3.setText(_translate("Unit1", "Browse", None))
        self.AddLayerButton.setText(_translate("Unit1", "Add Layers!", None))
        self.textBrowser_3.setHtml(_translate("Unit1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">When you have added all three layers to the canvas, click Next.</span></p></body></html>", None))
        self.textBrowser_5.setHtml(_translate("Unit1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">We are now going to investigate the relationships between the countries, cities and equator through spatial query.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">On the next page is a form that can help you to phrase these kinds of queries. You can select, or make a new layer from, features in the source layer that are related in a particular way to the reference layer</span><span style=\" font-size:8pt;\">.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#00007f;\">Source Layer</span><span style=\" font-size:10pt;\"> - The layer you want to select features from</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#00007f;\">Reference Layer </span><span style=\" font-size:10pt; color:#000000;\">- The layer that the selection depends on </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#00007f;\">Relationship</span><span style=\" font-size:10pt; color:#000000;\"> - The way that the two layers may be related, e.g. contains (a country may contain an airport) or intersect (the equator may intersect some countries).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline; color:#000000;\">Example</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">Select all of the countries (source layer) that are intersected (relationship) by the equator(reference layer).</span></p></body></html>", None))
        self.label_9.setText(_translate("Unit1", "Spatial Queries", None))
        self.textBrowser_4.setHtml(_translate("Unit1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Experiment with the different options available to you by changing the source and reference layers and the type of relationship you are looking for and clicking Go! Then try making a new layer that only contains those countries that are intersected by the equator.</span></p></body></html>", None))
        self.queryButton.setText(_translate("Unit1", "Go!", None))
        self.clearSelectionButton.setText(_translate("Unit1", "Clear Selection", None))
        self.selTypecomboBox.setItemText(0, _translate("Unit1", "Intersect", None))
        self.selTypecomboBox.setItemText(1, _translate("Unit1", "Are Within", None))
        self.selTypecomboBox.setItemText(2, _translate("Unit1", "Contain", None))
        self.selTypecomboBox.setItemText(3, _translate("Unit1", "Are disjoint to", None))
        self.refFeatcomboBox.setItemText(0, _translate("Unit1", "countries", None))
        self.refFeatcomboBox.setItemText(1, _translate("Unit1", "major_Cities", None))
        self.refFeatcomboBox.setItemText(2, _translate("Unit1", "equator", None))
        self.label_5.setText(_translate("Unit1", "Select features from source layer", None))
        self.label_7.setText(_translate("Unit1", "Where the source features", None))
        self.srcFeatcomboBox.setItemText(0, _translate("Unit1", "countries", None))
        self.srcFeatcomboBox.setItemText(1, _translate("Unit1", "major_cities", None))
        self.srcFeatcomboBox.setItemText(2, _translate("Unit1", "equator", None))
        self.label_8.setText(_translate("Unit1", "the reference layer", None))
        self.label_6.setText(_translate("Unit1", "with the reference layer", None))
        self.newLayergroupBox.setTitle(_translate("Unit1", "New Layer", None))
        self.newLayercheckBox.setText(_translate("Unit1", "Make a new layer from the selection", None))
        self.BrowsepushButton_4.setText(_translate("Unit1", "Browse", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Unit1 = QtGui.QWizard()
    ui = Ui_Unit1()
    ui.setupUi(Unit1)
    Unit1.show()
    sys.exit(app.exec_())

