# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\charlottegraves\.qgis2\python\plugins\QGISforSchools\Pop_dev_wizard.ui'
#
# Created: Thu Jun 12 16:48:09 2014
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

class Ui_PopDevWizard(object):
    def setupUi(self, PopDevWizard):
        PopDevWizard.setObjectName(_fromUtf8("PopDevWizard"))
        PopDevWizard.resize(295, 591)
        PopDevWizard.setSizeGripEnabled(True)
        PopDevWizard.setWizardStyle(QtGui.QWizard.ModernStyle)
        PopDevWizard.setOptions(QtGui.QWizard.NoBackButtonOnStartPage)
        self.wizardPage1 = QtGui.QWizardPage()
        self.wizardPage1.setObjectName(_fromUtf8("wizardPage1"))
        self.IntrotextBrowser = QtGui.QTextBrowser(self.wizardPage1)
        self.IntrotextBrowser.setGeometry(QtCore.QRect(20, 30, 256, 481))
        self.IntrotextBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.IntrotextBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.IntrotextBrowser.setObjectName(_fromUtf8("IntrotextBrowser"))
        PopDevWizard.addPage(self.wizardPage1)
        self.wizardPage2 = QtGui.QWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        self.CountrieslineEdit = QtGui.QLineEdit(self.wizardPage2)
        self.CountrieslineEdit.setGeometry(QtCore.QRect(20, 340, 171, 20))
        self.CountrieslineEdit.setObjectName(_fromUtf8("CountrieslineEdit"))
        self.CountriesBrowseButton = QtGui.QPushButton(self.wizardPage2)
        self.CountriesBrowseButton.setGeometry(QtCore.QRect(200, 340, 75, 23))
        self.CountriesBrowseButton.setObjectName(_fromUtf8("CountriesBrowseButton"))
        self.AddCountriesLayerButton = QtGui.QPushButton(self.wizardPage2)
        self.AddCountriesLayerButton.setGeometry(QtCore.QRect(20, 380, 251, 21))
        self.AddCountriesLayerButton.setObjectName(_fromUtf8("AddCountriesLayerButton"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.wizardPage2)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 430, 251, 71))
        self.textBrowser_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_3.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.pushButton = QtGui.QPushButton(self.wizardPage2)
        self.pushButton.setGeometry(QtCore.QRect(20, 500, 61, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.wizardPage2)
        self.label.setGeometry(QtCore.QRect(160, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.Score_label = QtGui.QLabel(self.wizardPage2)
        self.Score_label.setGeometry(QtCore.QRect(240, 12, 46, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Score_label.setFont(font)
        self.Score_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Score_label.setObjectName(_fromUtf8("Score_label"))
        self.textBrowser = QtGui.QTextBrowser(self.wizardPage2)
        self.textBrowser.setGeometry(QtCore.QRect(20, 60, 256, 261))
        self.textBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        PopDevWizard.addPage(self.wizardPage2)

        self.retranslateUi(PopDevWizard)
        QtCore.QMetaObject.connectSlotsByName(PopDevWizard)

    def retranslateUi(self, PopDevWizard):
        PopDevWizard.setWindowTitle(_translate("PopDevWizard", "Population and Development", None))
        PopDevWizard.setToolTip(_translate("PopDevWizard", "Population and Development", None))
        PopDevWizard.setWhatsThis(_translate("PopDevWizard", "Population and Development", None))
        self.IntrotextBrowser.setWhatsThis(_translate("PopDevWizard", "Population & Development Intro", None))
        self.IntrotextBrowser.setHtml(_translate("PopDevWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#000000;\">Unit 1</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#000000;\">Global Population &amp; Development</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Maps can help you to visually compare countries\' characteristics whether they are physical ones like area or number of cities, or ones that you can\'t see, like population, national income or development.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> A normal paper map would probably just display one or two of these aspects, but a system like QGIS can display many and can be manipulated very easily. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">In this unit you will explore the differences in the global distribution of population, income and development by changing the colour schemes of a map of the world.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">You will be asked questions as you go. You will earn </span><span style=\" font-size:11pt; font-weight:600; color:#aa007f;\">5</span><span style=\" font-size:10pt;\"> points for getting the answer right first time, </span><span style=\" font-size:11pt; font-weight:600; color:#aa007f;\">3</span><span style=\" font-size:10pt; font-weight:600; color:#aa007f;\"> </span><span style=\" font-size:10pt;\">for getting it right second time and </span><span style=\" font-size:11pt; font-weight:600; color:#aa007f;\">1</span><span style=\" font-size:10pt;\"> for getting it right the final time.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p></body></html>", None))
        self.CountriesBrowseButton.setText(_translate("PopDevWizard", "Browse", None))
        self.AddCountriesLayerButton.setText(_translate("PopDevWizard", "Add Countries!", None))
        self.textBrowser_3.setHtml(_translate("PopDevWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">When the map of the world appears on the map canvas, click Next.</span></p></body></html>", None))
        self.pushButton.setText(_translate("PopDevWizard", "Help", None))
        self.label.setText(_translate("PopDevWizard", "Your Score:", None))
        self.Score_label.setText(_translate("PopDevWizard", "0", None))
        self.textBrowser.setHtml(_translate("PopDevWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Adding Layers</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">In every GIS project, you have to start by adding data to the map canvas. We are going to start by adding the countries of the world.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Click the </span><span style=\" font-size:10pt; font-weight:600; color:#00007f;\">Browse</span><span style=\" font-size:10pt;\"> button below and navigate to the </span><span style=\" font-size:10pt; font-weight:600; color:#00007f;\">Population &amp; Development</span><span style=\" font-size:10pt;\"> data folder and choose </span><span style=\" font-size:10pt; font-weight:600; color:#00007f;\">countries.shp</span><span style=\" font-size:10pt;\">.</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PopDevWizard = QtGui.QWizard()
    ui = Ui_PopDevWizard()
    ui.setupUi(PopDevWizard)
    PopDevWizard.show()
    sys.exit(app.exec_())

