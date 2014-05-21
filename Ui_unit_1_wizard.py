# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\charlottegraves\.qgis2\python\plugins\QGISforSchools\unit_1_wizard.ui'
#
# Created: Wed May 21 12:53:03 2014
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

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName(_fromUtf8("Wizard"))
        Wizard.resize(316, 557)
        Wizard.setWhatsThis(_fromUtf8(""))
        Wizard.setAutoFillBackground(False)
        Wizard.setWizardStyle(QtGui.QWizard.AeroStyle)
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
        Wizard.addPage(self.wizardPage1)
        self.wizardPage2 = QtGui.QWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.wizardPage2)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 40, 256, 41))
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
        Wizard.addPage(self.wizardPage2)
        self.wizardPage = QtGui.QWizardPage()
        self.wizardPage.setObjectName(_fromUtf8("wizardPage"))
        self.textBrowser_4 = QtGui.QTextBrowser(self.wizardPage)
        self.textBrowser_4.setGeometry(QtCore.QRect(30, 20, 256, 171))
        self.textBrowser_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_4.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        self.queryButton = QtGui.QPushButton(self.wizardPage)
        self.queryButton.setGeometry(QtCore.QRect(120, 410, 75, 23))
        self.queryButton.setObjectName(_fromUtf8("queryButton"))
        self.layoutWidget = QtGui.QWidget(self.wizardPage)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 140, 141, 151))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.refFeatcomboBox = QtGui.QComboBox(self.layoutWidget)
        self.refFeatcomboBox.setObjectName(_fromUtf8("refFeatcomboBox"))
        self.refFeatcomboBox.addItem(_fromUtf8(""))
        self.refFeatcomboBox.addItem(_fromUtf8(""))
        self.refFeatcomboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.refFeatcomboBox, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.sourceFeatcomboBox = QtGui.QComboBox(self.layoutWidget)
        self.sourceFeatcomboBox.setObjectName(_fromUtf8("sourceFeatcomboBox"))
        self.sourceFeatcomboBox.addItem(_fromUtf8(""))
        self.sourceFeatcomboBox.addItem(_fromUtf8(""))
        self.sourceFeatcomboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.sourceFeatcomboBox, 0, 1, 1, 1)
        self.selTypecomboBox = QtGui.QComboBox(self.layoutWidget)
        self.selTypecomboBox.setObjectName(_fromUtf8("selTypecomboBox"))
        self.selTypecomboBox.addItem(_fromUtf8(""))
        self.selTypecomboBox.addItem(_fromUtf8(""))
        self.selTypecomboBox.addItem(_fromUtf8(""))
        self.selTypecomboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.selTypecomboBox, 1, 1, 1, 1)
        self.QueryprogressBar = QtGui.QProgressBar(self.wizardPage)
        self.QueryprogressBar.setGeometry(QtCore.QRect(100, 340, 118, 23))
        self.QueryprogressBar.setProperty("value", 24)
        self.QueryprogressBar.setObjectName(_fromUtf8("QueryprogressBar"))
        Wizard.addPage(self.wizardPage)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(_translate("Wizard", "Unit 1 - Spatial Query", None))
        self.label.setText(_translate("Wizard", "Unit 1 - Spatial Query", None))
        self.textBrowser.setHtml(_translate("Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">*** Description - goals and steps ***</span></p></body></html>", None))
        self.textBrowser_2.setHtml(_translate("Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">***Explanation about adding data ***</span></p></body></html>", None))
        self.BrowsepushButton.setText(_translate("Wizard", "Browse", None))
        self.label_2.setText(_translate("Wizard", "1. Add the countries layer:", None))
        self.label_3.setText(_translate("Wizard", "2. Add the cities layer:", None))
        self.BrowsepushButton_2.setText(_translate("Wizard", "Browse", None))
        self.label_4.setText(_translate("Wizard", "3. Add the equator:", None))
        self.BrowsepushButton_3.setText(_translate("Wizard", "Browse", None))
        self.AddLayerButton.setText(_translate("Wizard", "Add Layers!", None))
        self.textBrowser_3.setHtml(_translate("Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">When you have added all three layers to the canvas, click Next.</span></p></body></html>", None))
        self.textBrowser_4.setHtml(_translate("Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">***Info about spatial query. Instructions***</span></p></body></html>", None))
        self.queryButton.setText(_translate("Wizard", "Go!", None))
        self.label_6.setText(_translate("Wizard", "that", None))
        self.label_7.setText(_translate("Wizard", "the", None))
        self.refFeatcomboBox.setItemText(0, _translate("Wizard", "countries", None))
        self.refFeatcomboBox.setItemText(1, _translate("Wizard", "major_Cities", None))
        self.refFeatcomboBox.setItemText(2, _translate("Wizard", "equator", None))
        self.label_5.setText(_translate("Wizard", "Select the", None))
        self.sourceFeatcomboBox.setItemText(0, _translate("Wizard", "countries", None))
        self.sourceFeatcomboBox.setItemText(1, _translate("Wizard", "major_cities", None))
        self.sourceFeatcomboBox.setItemText(2, _translate("Wizard", "equator", None))
        self.selTypecomboBox.setItemText(0, _translate("Wizard", "Intersects", None))
        self.selTypecomboBox.setItemText(1, _translate("Wizard", "Is Within", None))
        self.selTypecomboBox.setItemText(2, _translate("Wizard", "Contains", None))
        self.selTypecomboBox.setItemText(3, _translate("Wizard", "Is disjoint to", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Wizard = QtGui.QWizard()
    ui = Ui_Wizard()
    ui.setupUi(Wizard)
    Wizard.show()
    sys.exit(app.exec_())

