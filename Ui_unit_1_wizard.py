# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\charlottegraves\.qgis2\python\plugins\QGISforSchools\unit_1_wizard.ui'
#
# Created: Sun May 18 17:17:11 2014
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
        self.label.setGeometry(QtCore.QRect(10, -20, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.wizardPage1)
        self.lineEdit.setGeometry(QtCore.QRect(50, 80, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.wizardPage1)
        self.pushButton.setGeometry(QtCore.QRect(170, 80, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        Wizard.addPage(self.wizardPage1)
        self.wizardPage2 = QtGui.QWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        Wizard.addPage(self.wizardPage2)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(_translate("Wizard", "Unit 1 - Spatial Query", None))
        self.label.setText(_translate("Wizard", "Unit 1 - Spatial Query", None))
        self.pushButton.setText(_translate("Wizard", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Wizard = QtGui.QWizard()
    ui = Ui_Wizard()
    ui.setupUi(Wizard)
    Wizard.show()
    sys.exit(app.exec_())

