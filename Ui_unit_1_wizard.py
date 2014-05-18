# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\charlottegraves\.qgis2\python\plugins\QGISforSchools\unit_1_wizard.ui'
#
# Created: Sun May 18 20:58:03 2014
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
        Wizard.resize(312, 551)
        Wizard.setAutoFillBackground(False)
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
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        Wizard.addPage(self.wizardPage1)
        self.wizardPage2 = QtGui.QWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.wizardPage2)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 40, 256, 41))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.lineEdit = QtGui.QLineEdit(self.wizardPage2)
        self.lineEdit.setGeometry(QtCore.QRect(30, 180, 171, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.BrowsepushButton = QtGui.QPushButton(self.wizardPage2)
        self.BrowsepushButton.setGeometry(QtCore.QRect(210, 180, 75, 23))
        self.BrowsepushButton.setObjectName(_fromUtf8("BrowsepushButton"))
        self.label_2 = QtGui.QLabel(self.wizardPage2)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 131, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.wizardPage2)
        self.label_3.setGeometry(QtCore.QRect(30, 230, 131, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.wizardPage2)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 250, 171, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.BrowsepushButton_2 = QtGui.QPushButton(self.wizardPage2)
        self.BrowsepushButton_2.setGeometry(QtCore.QRect(210, 250, 75, 23))
        self.BrowsepushButton_2.setObjectName(_fromUtf8("BrowsepushButton_2"))
        self.label_4 = QtGui.QLabel(self.wizardPage2)
        self.label_4.setGeometry(QtCore.QRect(30, 300, 131, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.BrowsepushButton_3 = QtGui.QPushButton(self.wizardPage2)
        self.BrowsepushButton_3.setGeometry(QtCore.QRect(210, 320, 75, 23))
        self.BrowsepushButton_3.setObjectName(_fromUtf8("BrowsepushButton_3"))
        self.lineEdit_3 = QtGui.QLineEdit(self.wizardPage2)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 320, 171, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        Wizard.addPage(self.wizardPage2)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(_translate("Wizard", "Unit 1 - Spatial Query", None))
        self.label.setText(_translate("Wizard", "Unit 1 - Spatial Query", None))
        self.textBrowser.setHtml(_translate("Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">*** Description ***</span></p></body></html>", None))
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


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Wizard = QtGui.QWizard()
    ui = Ui_Wizard()
    ui.setupUi(Wizard)
    Wizard.show()
    sys.exit(app.exec_())

