# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\charlottegraves\.qgis2\python\plugins\QGISforSchools\ui_qgisforschools.ui'
#
# Created: Sat Jun 21 17:37:51 2014
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

class Ui_QGISforSchools(object):
    def setupUi(self, QGISforSchools):
        QGISforSchools.setObjectName(_fromUtf8("QGISforSchools"))
        QGISforSchools.resize(403, 284)
        self.unit1 = QtGui.QRadioButton(QGISforSchools)
        self.unit1.setGeometry(QtCore.QRect(30, 110, 201, 17))
        self.unit1.setChecked(True)
        self.unit1.setObjectName(_fromUtf8("unit1"))
        self.unit2 = QtGui.QRadioButton(QGISforSchools)
        self.unit2.setGeometry(QtCore.QRect(30, 140, 161, 16))
        self.unit2.setObjectName(_fromUtf8("unit2"))
        self.unit3 = QtGui.QRadioButton(QGISforSchools)
        self.unit3.setGeometry(QtCore.QRect(30, 170, 82, 17))
        self.unit3.setObjectName(_fromUtf8("unit3"))
        self.label = QtGui.QLabel(QGISforSchools)
        self.label.setGeometry(QtCore.QRect(30, 20, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.buttonBox = QtGui.QDialogButtonBox(QGISforSchools)
        self.buttonBox.setGeometry(QtCore.QRect(210, 240, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_2 = QtGui.QLabel(QGISforSchools)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 231, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(QGISforSchools)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 301, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(QGISforSchools)
        QtCore.QMetaObject.connectSlotsByName(QGISforSchools)

    def retranslateUi(self, QGISforSchools):
        QGISforSchools.setWindowTitle(_translate("QGISforSchools", "QGISforSchools", None))
        self.unit1.setText(_translate("QGISforSchools", "Unit 1 - Population &&  Development", None))
        self.unit2.setText(_translate("QGISforSchools", "Unit 2 - Earthquakes", None))
        self.unit3.setText(_translate("QGISforSchools", "Unit 3", None))
        self.label.setText(_translate("QGISforSchools", "Welcome to QGIS for Schools!", None))
        self.label_2.setText(_translate("QGISforSchools", "Which unit would you like to open?", None))
        self.label_3.setText(_translate("QGISforSchools", "These tutorials use data which can be downloaded from:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    QGISforSchools = QtGui.QDialog()
    ui = Ui_QGISforSchools()
    ui.setupUi(QGISforSchools)
    QGISforSchools.show()
    sys.exit(app.exec_())

