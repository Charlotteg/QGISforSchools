# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\charlottegraves\.qgis2\python\plugins\QGISforSchools\earthquakes_wizard.ui'
#
# Created: Wed Jun 18 21:53:46 2014
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

class Ui_EQWizard(object):
    def setupUi(self, EQWizard):
        EQWizard.setObjectName(_fromUtf8("EQWizard"))
        EQWizard.setSizeGripEnabled(True)
        EQWizard.setWizardStyle(QtGui.QWizard.ModernStyle)
        EQWizard.setOptions(QtGui.QWizard.NoBackButtonOnStartPage)
        self.wizardPage1 = QtGui.QWizardPage()
        self.wizardPage1.setObjectName(_fromUtf8("wizardPage1"))
        self.IntrotextBrowser = QtGui.QTextBrowser(self.wizardPage1)
        self.IntrotextBrowser.setGeometry(QtCore.QRect(20, 30, 256, 481))
        self.IntrotextBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.IntrotextBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.IntrotextBrowser.setObjectName(_fromUtf8("IntrotextBrowser"))
        EQWizard.addPage(self.wizardPage1)
        self.wizardPage2 = QtGui.QWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        self.label_4 = QtGui.QLabel(self.wizardPage2)
        self.label_4.setGeometry(QtCore.QRect(20, 330, 131, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_3 = QtGui.QLabel(self.wizardPage2)
        self.label_3.setGeometry(QtCore.QRect(20, 260, 141, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.eqLineEdit = QtGui.QLineEdit(self.wizardPage2)
        self.eqLineEdit.setGeometry(QtCore.QRect(20, 350, 171, 20))
        self.eqLineEdit.setObjectName(_fromUtf8("eqLineEdit"))
        self.plateBrowseButton = QtGui.QPushButton(self.wizardPage2)
        self.plateBrowseButton.setGeometry(QtCore.QRect(200, 280, 75, 23))
        self.plateBrowseButton.setObjectName(_fromUtf8("plateBrowseButton"))
        self.label_2 = QtGui.QLabel(self.wizardPage2)
        self.label_2.setGeometry(QtCore.QRect(20, 190, 131, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.countriesLineEdit = QtGui.QLineEdit(self.wizardPage2)
        self.countriesLineEdit.setGeometry(QtCore.QRect(20, 210, 171, 20))
        self.countriesLineEdit.setObjectName(_fromUtf8("countriesLineEdit"))
        self.platesLineEdit = QtGui.QLineEdit(self.wizardPage2)
        self.platesLineEdit.setGeometry(QtCore.QRect(20, 280, 171, 20))
        self.platesLineEdit.setObjectName(_fromUtf8("platesLineEdit"))
        self.eqBrowseButton = QtGui.QPushButton(self.wizardPage2)
        self.eqBrowseButton.setGeometry(QtCore.QRect(200, 350, 75, 23))
        self.eqBrowseButton.setObjectName(_fromUtf8("eqBrowseButton"))
        self.AddLayerButton = QtGui.QPushButton(self.wizardPage2)
        self.AddLayerButton.setGeometry(QtCore.QRect(20, 400, 251, 21))
        self.AddLayerButton.setObjectName(_fromUtf8("AddLayerButton"))
        self.countriesBrowseButton = QtGui.QPushButton(self.wizardPage2)
        self.countriesBrowseButton.setGeometry(QtCore.QRect(200, 210, 75, 23))
        self.countriesBrowseButton.setObjectName(_fromUtf8("countriesBrowseButton"))
        self.label = QtGui.QLabel(self.wizardPage2)
        self.label.setGeometry(QtCore.QRect(150, 510, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.Score_label = QtGui.QLabel(self.wizardPage2)
        self.Score_label.setGeometry(QtCore.QRect(230, 512, 46, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Score_label.setFont(font)
        self.Score_label.setFrameShape(QtGui.QFrame.Panel)
        self.Score_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Score_label.setObjectName(_fromUtf8("Score_label"))
        self.label_5 = QtGui.QLabel(self.wizardPage2)
        self.label_5.setGeometry(QtCore.QRect(40, 430, 211, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.wizardPage2)
        self.label_6.setGeometry(QtCore.QRect(70, 450, 141, 21))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.wizardPage2)
        self.label_7.setGeometry(QtCore.QRect(90, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.wizardPage2)
        self.label_8.setGeometry(QtCore.QRect(20, 50, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.wizardPage2)
        self.label_9.setGeometry(QtCore.QRect(20, 70, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.wizardPage2)
        self.label_10.setGeometry(QtCore.QRect(20, 90, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.wizardPage2)
        self.label_11.setGeometry(QtCore.QRect(20, 110, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.wizardPage2)
        self.label_12.setGeometry(QtCore.QRect(20, 130, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        EQWizard.addPage(self.wizardPage2)
        self.wizardPage = QtGui.QWizardPage()
        self.wizardPage.setObjectName(_fromUtf8("wizardPage"))
        EQWizard.addPage(self.wizardPage)

        self.retranslateUi(EQWizard)
        QtCore.QMetaObject.connectSlotsByName(EQWizard)

    def retranslateUi(self, EQWizard):
        EQWizard.setWindowTitle(_translate("EQWizard", "Earthquakes", None))
        EQWizard.setWhatsThis(_translate("EQWizard", "Earthquakes", None))
        self.IntrotextBrowser.setWhatsThis(_translate("EQWizard", "Population & Development Intro", None))
        self.IntrotextBrowser.setHtml(_translate("EQWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#000000;\">Unit 2</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#000000;\">Earthquakes</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Earthquakes are the vibration of the Earth’s crust caused by the release of pressure that has built up due to the movements of tectonic plates. The size, or magnitude, of an earthquake can be measured on the Richter scale which is numbered from 0 – 10.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">In this unit you will explore the distribution of the earthquakes that took place in 2011. You will see how GIS can help you answer all sorts of spatial queries.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">You will be asked questions as you go. You will earn 5 points for getting the answer right first time, 3 for getting it right second time and 1 for getting it right any time thereafter.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.label_4.setText(_translate("EQWizard", "3. Add the earthquakes:", None))
        self.label_3.setText(_translate("EQWizard", "2. Add the plate boundaries:", None))
        self.plateBrowseButton.setText(_translate("EQWizard", "Browse", None))
        self.label_2.setText(_translate("EQWizard", "1. Add the countries layer:", None))
        self.eqBrowseButton.setText(_translate("EQWizard", "Browse", None))
        self.AddLayerButton.setText(_translate("EQWizard", "Add Layers!", None))
        self.countriesBrowseButton.setText(_translate("EQWizard", "Browse", None))
        self.label.setText(_translate("EQWizard", "Your Score:", None))
        self.Score_label.setText(_translate("EQWizard", "0", None))
        self.label_5.setText(_translate("EQWizard", "When the layers appear on the map", None))
        self.label_6.setText(_translate("EQWizard", "canvas, click Next.", None))
        self.label_7.setText(_translate("EQWizard", "Adding Layers", None))
        self.label_8.setText(_translate("EQWizard", "For this unit we will need three layers: ", None))
        self.label_9.setText(_translate("EQWizard", "countries.shp, plateboundaries.shp and", None))
        self.label_10.setText(_translate("EQWizard", "earthquakes.shp. Use the Browse", None))
        self.label_11.setText(_translate("EQWizard", "buttons below to select these layers from", None))
        self.label_12.setText(_translate("EQWizard", "the Earthquakes data file.", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EQWizard = QtGui.QWizard()
    ui = Ui_EQWizard()
    ui.setupUi(EQWizard)
    EQWizard.show()
    sys.exit(app.exec_())

