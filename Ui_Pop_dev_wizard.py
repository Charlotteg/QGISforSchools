# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\charlottegraves\.qgis2\python\plugins\QGISforSchools\Pop_dev_wizard.ui'
#
# Created: Sat Jun 14 23:05:40 2014
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
        PopDevWizard.resize(293, 591)
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
        self.CountrieslineEdit.setGeometry(QtCore.QRect(20, 300, 171, 20))
        self.CountrieslineEdit.setObjectName(_fromUtf8("CountrieslineEdit"))
        self.CountriesBrowseButton = QtGui.QPushButton(self.wizardPage2)
        self.CountriesBrowseButton.setGeometry(QtCore.QRect(200, 300, 75, 23))
        self.CountriesBrowseButton.setObjectName(_fromUtf8("CountriesBrowseButton"))
        self.AddCountriesLayerButton = QtGui.QPushButton(self.wizardPage2)
        self.AddCountriesLayerButton.setGeometry(QtCore.QRect(20, 340, 251, 21))
        self.AddCountriesLayerButton.setObjectName(_fromUtf8("AddCountriesLayerButton"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.wizardPage2)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 390, 251, 71))
        self.textBrowser_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_3.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.label = QtGui.QLabel(self.wizardPage2)
        self.label.setGeometry(QtCore.QRect(150, 480, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.Score_label = QtGui.QLabel(self.wizardPage2)
        self.Score_label.setGeometry(QtCore.QRect(230, 482, 46, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Score_label.setFont(font)
        self.Score_label.setFrameShape(QtGui.QFrame.Panel)
        self.Score_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Score_label.setObjectName(_fromUtf8("Score_label"))
        self.textBrowser = QtGui.QTextBrowser(self.wizardPage2)
        self.textBrowser.setGeometry(QtCore.QRect(20, 30, 256, 261))
        self.textBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        PopDevWizard.addPage(self.wizardPage2)
        self.wizardPage3 = QtGui.QWizardPage()
        self.wizardPage3.setObjectName(_fromUtf8("wizardPage3"))
        self.categoryTableView = QtGui.QTableView(self.wizardPage3)
        self.categoryTableView.setGeometry(QtCore.QRect(20, 271, 256, 191))
        self.categoryTableView.setShowGrid(False)
        self.categoryTableView.setObjectName(_fromUtf8("categoryTableView"))
        self.Score_label_2 = QtGui.QLabel(self.wizardPage3)
        self.Score_label_2.setGeometry(QtCore.QRect(230, 482, 46, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Score_label_2.setFont(font)
        self.Score_label_2.setFrameShape(QtGui.QFrame.Box)
        self.Score_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Score_label_2.setObjectName(_fromUtf8("Score_label_2"))
        self.label_2 = QtGui.QLabel(self.wizardPage3)
        self.label_2.setGeometry(QtCore.QRect(150, 480, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.wizardPage3)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 271, 161))
        self.textBrowser_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_2.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.StyleTypecomboBox = QtGui.QComboBox(self.wizardPage3)
        self.StyleTypecomboBox.setGeometry(QtCore.QRect(30, 180, 111, 21))
        self.StyleTypecomboBox.setObjectName(_fromUtf8("StyleTypecomboBox"))
        self.StyleTypecomboBox.addItem(_fromUtf8(""))
        self.StyleTypecomboBox.addItem(_fromUtf8(""))
        self.ColourRampcomboBox = QtGui.QComboBox(self.wizardPage3)
        self.ColourRampcomboBox.setEnabled(False)
        self.ColourRampcomboBox.setGeometry(QtCore.QRect(150, 240, 111, 21))
        self.ColourRampcomboBox.setObjectName(_fromUtf8("ColourRampcomboBox"))
        self.ChangeColourButton = QtGui.QPushButton(self.wizardPage3)
        self.ChangeColourButton.setGeometry(QtCore.QRect(150, 180, 111, 21))
        self.ChangeColourButton.setObjectName(_fromUtf8("ChangeColourButton"))
        self.ColumncomboBox = QtGui.QComboBox(self.wizardPage3)
        self.ColumncomboBox.setEnabled(False)
        self.ColumncomboBox.setGeometry(QtCore.QRect(110, 210, 151, 20))
        self.ColumncomboBox.setObjectName(_fromUtf8("ColumncomboBox"))
        self.columnLabel = QtGui.QLabel(self.wizardPage3)
        self.columnLabel.setEnabled(False)
        self.columnLabel.setGeometry(QtCore.QRect(30, 210, 41, 16))
        self.columnLabel.setObjectName(_fromUtf8("columnLabel"))
        self.colourRampLabel = QtGui.QLabel(self.wizardPage3)
        self.colourRampLabel.setEnabled(False)
        self.colourRampLabel.setGeometry(QtCore.QRect(30, 240, 81, 16))
        self.colourRampLabel.setObjectName(_fromUtf8("colourRampLabel"))
        PopDevWizard.addPage(self.wizardPage3)
        self.wizardPage4 = QtGui.QWizardPage()
        self.wizardPage4.setObjectName(_fromUtf8("wizardPage4"))
        self.Score_label_3 = QtGui.QLabel(self.wizardPage4)
        self.Score_label_3.setGeometry(QtCore.QRect(230, 482, 46, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Score_label_3.setFont(font)
        self.Score_label_3.setFrameShape(QtGui.QFrame.Box)
        self.Score_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Score_label_3.setObjectName(_fromUtf8("Score_label_3"))
        self.label_3 = QtGui.QLabel(self.wizardPage4)
        self.label_3.setGeometry(QtCore.QRect(150, 480, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.vSmallPop = QtGui.QRadioButton(self.wizardPage4)
        self.vSmallPop.setGeometry(QtCore.QRect(60, 150, 161, 21))
        self.vSmallPop.setObjectName(_fromUtf8("vSmallPop"))
        self.mediumPop = QtGui.QRadioButton(self.wizardPage4)
        self.mediumPop.setGeometry(QtCore.QRect(60, 170, 161, 21))
        self.mediumPop.setObjectName(_fromUtf8("mediumPop"))
        self.smallPop = QtGui.QRadioButton(self.wizardPage4)
        self.smallPop.setGeometry(QtCore.QRect(60, 190, 161, 21))
        self.smallPop.setObjectName(_fromUtf8("smallPop"))
        self.largePop = QtGui.QRadioButton(self.wizardPage4)
        self.largePop.setGeometry(QtCore.QRect(60, 210, 161, 21))
        self.largePop.setObjectName(_fromUtf8("largePop"))
        self.norwayPop = QtGui.QRadioButton(self.wizardPage4)
        self.norwayPop.setGeometry(QtCore.QRect(60, 320, 161, 21))
        self.norwayPop.setObjectName(_fromUtf8("norwayPop"))
        self.brazilPop = QtGui.QRadioButton(self.wizardPage4)
        self.brazilPop.setGeometry(QtCore.QRect(60, 340, 161, 21))
        self.brazilPop.setObjectName(_fromUtf8("brazilPop"))
        self.francePop = QtGui.QRadioButton(self.wizardPage4)
        self.francePop.setGeometry(QtCore.QRect(60, 360, 161, 21))
        self.francePop.setObjectName(_fromUtf8("francePop"))
        self.usaPop = QtGui.QRadioButton(self.wizardPage4)
        self.usaPop.setGeometry(QtCore.QRect(60, 380, 161, 21))
        self.usaPop.setObjectName(_fromUtf8("usaPop"))
        self.checkAnswersPop = QtGui.QPushButton(self.wizardPage4)
        self.checkAnswersPop.setGeometry(QtCore.QRect(20, 440, 251, 21))
        self.checkAnswersPop.setObjectName(_fromUtf8("checkAnswersPop"))
        self.label_4 = QtGui.QLabel(self.wizardPage4)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.wizardPage4)
        self.label_5.setGeometry(QtCore.QRect(70, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.wizardPage4)
        self.label_6.setGeometry(QtCore.QRect(20, 50, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.wizardPage4)
        self.label_7.setGeometry(QtCore.QRect(20, 70, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.wizardPage4)
        self.label_8.setGeometry(QtCore.QRect(10, 260, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.wizardPage4)
        self.label_9.setGeometry(QtCore.QRect(10, 280, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        PopDevWizard.addPage(self.wizardPage4)

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
        self.Score_label_2.setText(_translate("PopDevWizard", "0", None))
        self.label_2.setText(_translate("PopDevWizard", "Your Score:", None))
        self.textBrowser_2.setHtml(_translate("PopDevWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Colour Schemes</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Using colour we can compare national characteristics like population. Experiment with the colour and column options below. Make sure that you choose </span><span style=\" font-size:10pt; font-weight:600; color:#00007f;\">Categorized</span><span style=\" font-size:10pt;\"> and the </span><span style=\" font-size:10pt; font-weight:600; color:#00007f;\">pop_group</span><span style=\" font-size:10pt;\"> column before you click </span><span style=\" font-size:10pt; font-weight:600; color:#00007f;\">Next</span><span style=\" font-size:10pt;\"> as this will help you with the following questions.</span></p></body></html>", None))
        self.StyleTypecomboBox.setItemText(0, _translate("PopDevWizard", "Single Colour", None))
        self.StyleTypecomboBox.setItemText(1, _translate("PopDevWizard", "Categorized", None))
        self.ChangeColourButton.setText(_translate("PopDevWizard", "Colour", None))
        self.columnLabel.setText(_translate("PopDevWizard", "Column:", None))
        self.colourRampLabel.setText(_translate("PopDevWizard", "Colour Ramp:", None))
        self.Score_label_3.setText(_translate("PopDevWizard", "0", None))
        self.label_3.setText(_translate("PopDevWizard", "Your Score:", None))
        self.vSmallPop.setText(_translate("PopDevWizard", "Very Small Population", None))
        self.mediumPop.setText(_translate("PopDevWizard", "Medium Population", None))
        self.smallPop.setText(_translate("PopDevWizard", "Small Population", None))
        self.largePop.setText(_translate("PopDevWizard", "Large Population", None))
        self.norwayPop.setText(_translate("PopDevWizard", "Norway, Russia and Australia", None))
        self.brazilPop.setText(_translate("PopDevWizard", "Brazil, Japan, Indonesia", None))
        self.francePop.setText(_translate("PopDevWizard", "France, Italy, Egypt", None))
        self.usaPop.setText(_translate("PopDevWizard", "USA, India, China", None))
        self.checkAnswersPop.setText(_translate("PopDevWizard", "Check my answers!", None))
        self.label_4.setText(_translate("PopDevWizard", "What population group does the UK fall into?", None))
        self.label_5.setText(_translate("PopDevWizard", "Question Time", None))
        self.label_6.setText(_translate("PopDevWizard", "Look at the map and answer the following", None))
        self.label_7.setText(_translate("PopDevWizard", "questions:", None))
        self.label_8.setText(_translate("PopDevWizard", "Which three countries fall int the \'very large", None))
        self.label_9.setText(_translate("PopDevWizard", "population\' category?", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PopDevWizard = QtGui.QWizard()
    ui = Ui_PopDevWizard()
    ui.setupUi(PopDevWizard)
    PopDevWizard.show()
    sys.exit(app.exec_())

