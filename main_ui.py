# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Jun 29 23:25:23 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(944, 675)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.MasterLine = QtGui.QSlider(self.centralwidget)
        self.MasterLine.setGeometry(QtCore.QRect(800, 220, 23, 301))
        self.MasterLine.setMaximum(127)
        self.MasterLine.setProperty("value", 0)
        self.MasterLine.setOrientation(QtCore.Qt.Vertical)
        self.MasterLine.setProperty("channel", 0)
        self.MasterLine.setProperty("parameter", 0)
        self.MasterLine.setObjectName(_fromUtf8("MasterLine"))
        self.MasterLineLcd = QtGui.QLCDNumber(self.centralwidget)
        self.MasterLineLcd.setGeometry(QtCore.QRect(780, 590, 64, 23))
        self.MasterLineLcd.setObjectName(_fromUtf8("MasterLineLcd"))
        self.masterLabel = QtGui.QLabel(self.centralwidget)
        self.masterLabel.setGeometry(QtCore.QRect(760, 550, 111, 21))
        self.masterLabel.setStyleSheet(_fromUtf8(""))
        self.masterLabel.setObjectName(_fromUtf8("masterLabel"))
        self.wave1Label = QtGui.QLabel(self.centralwidget)
        self.wave1Label.setGeometry(QtCore.QRect(330, 540, 111, 21))
        self.wave1Label.setStyleSheet(_fromUtf8(""))
        self.wave1Label.setObjectName(_fromUtf8("wave1Label"))
        self.Wave1 = QtGui.QSlider(self.centralwidget)
        self.Wave1.setGeometry(QtCore.QRect(370, 220, 23, 301))
        self.Wave1.setMaximum(127)
        self.Wave1.setProperty("value", 0)
        self.Wave1.setOrientation(QtCore.Qt.Vertical)
        self.Wave1.setProperty("channel", 0)
        self.Wave1.setProperty("parameter", 0)
        self.Wave1.setObjectName(_fromUtf8("Wave1"))
        self.Wave1Lcd = QtGui.QLCDNumber(self.centralwidget)
        self.Wave1Lcd.setGeometry(QtCore.QRect(350, 590, 64, 23))
        self.Wave1Lcd.setObjectName(_fromUtf8("Wave1Lcd"))
        self.outputDevicesList = QtGui.QComboBox(self.centralwidget)
        self.outputDevicesList.setGeometry(QtCore.QRect(210, 20, 311, 23))
        self.outputDevicesList.setObjectName(_fromUtf8("outputDevicesList"))
        self.Mic1 = QtGui.QSlider(self.centralwidget)
        self.Mic1.setGeometry(QtCore.QRect(150, 220, 23, 301))
        self.Mic1.setMaximum(127)
        self.Mic1.setProperty("value", 0)
        self.Mic1.setOrientation(QtCore.Qt.Vertical)
        self.Mic1.setProperty("channel", 0)
        self.Mic1.setProperty("parameter", 0)
        self.Mic1.setObjectName(_fromUtf8("Mic1"))
        self.Mic1Lcd = QtGui.QLCDNumber(self.centralwidget)
        self.Mic1Lcd.setGeometry(QtCore.QRect(130, 590, 64, 23))
        self.Mic1Lcd.setObjectName(_fromUtf8("Mic1Lcd"))
        self.mic1Label = QtGui.QLabel(self.centralwidget)
        self.mic1Label.setGeometry(QtCore.QRect(110, 540, 111, 21))
        self.mic1Label.setStyleSheet(_fromUtf8(""))
        self.mic1Label.setObjectName(_fromUtf8("mic1Label"))
        self.Mic1Pan = QtGui.QDial(self.centralwidget)
        self.Mic1Pan.setGeometry(QtCore.QRect(140, 150, 50, 64))
        self.Mic1Pan.setMaximum(127)
        self.Mic1Pan.setProperty("value", 0)
        self.Mic1Pan.setSliderPosition(0)
        self.Mic1Pan.setWrapping(False)
        self.Mic1Pan.setObjectName(_fromUtf8("Mic1Pan"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 180, 57, 14))
        self.label.setObjectName(_fromUtf8("label"))
        self.Mic1PanLcd = QtGui.QLCDNumber(self.centralwidget)
        self.Mic1PanLcd.setGeometry(QtCore.QRect(130, 130, 64, 23))
        self.Mic1PanLcd.setObjectName(_fromUtf8("Mic1PanLcd"))
        self.Mic2Pan = QtGui.QDial(self.centralwidget)
        self.Mic2Pan.setGeometry(QtCore.QRect(250, 150, 50, 64))
        self.Mic2Pan.setMaximum(127)
        self.Mic2Pan.setProperty("value", 0)
        self.Mic2Pan.setSliderPosition(0)
        self.Mic2Pan.setWrapping(False)
        self.Mic2Pan.setObjectName(_fromUtf8("Mic2Pan"))
        self.Mic2 = QtGui.QSlider(self.centralwidget)
        self.Mic2.setGeometry(QtCore.QRect(260, 220, 23, 301))
        self.Mic2.setMaximum(127)
        self.Mic2.setProperty("value", 0)
        self.Mic2.setOrientation(QtCore.Qt.Vertical)
        self.Mic2.setProperty("channel", 0)
        self.Mic2.setProperty("parameter", 0)
        self.Mic2.setObjectName(_fromUtf8("Mic2"))
        self.Mic2Lcd = QtGui.QLCDNumber(self.centralwidget)
        self.Mic2Lcd.setGeometry(QtCore.QRect(240, 590, 64, 23))
        self.Mic2Lcd.setObjectName(_fromUtf8("Mic2Lcd"))
        self.mic2Label = QtGui.QLabel(self.centralwidget)
        self.mic2Label.setGeometry(QtCore.QRect(220, 540, 111, 21))
        self.mic2Label.setStyleSheet(_fromUtf8(""))
        self.mic2Label.setObjectName(_fromUtf8("mic2Label"))
        self.Mic2PanLcd = QtGui.QLCDNumber(self.centralwidget)
        self.Mic2PanLcd.setGeometry(QtCore.QRect(240, 130, 64, 23))
        self.Mic2PanLcd.setObjectName(_fromUtf8("Mic2PanLcd"))
        self.Wave2 = QtGui.QSlider(self.centralwidget)
        self.Wave2.setGeometry(QtCore.QRect(480, 220, 23, 301))
        self.Wave2.setMaximum(127)
        self.Wave2.setProperty("value", 0)
        self.Wave2.setOrientation(QtCore.Qt.Vertical)
        self.Wave2.setProperty("channel", 0)
        self.Wave2.setProperty("parameter", 0)
        self.Wave2.setObjectName(_fromUtf8("Wave2"))
        self.Wave2Lcd = QtGui.QLCDNumber(self.centralwidget)
        self.Wave2Lcd.setGeometry(QtCore.QRect(460, 590, 64, 23))
        self.Wave2Lcd.setObjectName(_fromUtf8("Wave2Lcd"))
        self.wave1Label_2 = QtGui.QLabel(self.centralwidget)
        self.wave1Label_2.setGeometry(QtCore.QRect(440, 540, 111, 21))
        self.wave1Label_2.setStyleSheet(_fromUtf8(""))
        self.wave1Label_2.setObjectName(_fromUtf8("wave1Label_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 191, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.masterLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">MASTER</span></p></body></html>", None))
        self.wave1Label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">WAVE1</span></p></body></html>", None))
        self.mic1Label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">MIC1/GUITAR</span></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "PAN", None))
        self.mic2Label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">MIC2</span></p></body></html>", None))
        self.wave1Label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">WAVE2</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "Control Change Device:", None))

