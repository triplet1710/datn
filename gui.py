# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1208, 705)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(20, 20, 631, 491))
        self.label_img.setFrameShape(QtWidgets.QFrame.Box)
        self.label_img.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_img.setLineWidth(5)
        self.label_img.setText("")
        self.label_img.setObjectName("label_img")
        self.Button_start = QtWidgets.QPushButton(self.centralwidget)
        self.Button_start.setGeometry(QtCore.QRect(10, 560, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.Button_start.setFont(font)
        self.Button_start.setObjectName("Button_start")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(710, 100, 371, 261))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.Button_save = QtWidgets.QPushButton(self.groupBox)
        self.Button_save.setGeometry(QtCore.QRect(110, 180, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.Button_save.setFont(font)
        self.Button_save.setObjectName("Button_save")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 151, 29))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lable_nums = QtWidgets.QLabel(self.groupBox)
        self.lable_nums.setGeometry(QtCore.QRect(210, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.lable_nums.setFont(font)
        self.lable_nums.setObjectName("lable_nums")
        self.lable_weight = QtWidgets.QLabel(self.groupBox)
        self.lable_weight.setGeometry(QtCore.QRect(210, 50, 121, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.lable_weight.setFont(font)
        self.lable_weight.setObjectName("lable_weight")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(50, 130, 91, 29))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.qr_lable = QtWidgets.QLabel(self.groupBox)
        self.qr_lable.setGeometry(QtCore.QRect(210, 130, 131, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.qr_lable.setFont(font)
        self.qr_lable.setObjectName("qr_lable")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 172, 29))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(320, 50, 151, 29))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(630, 20, 49, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(690, 0, 891, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(710, 370, 371, 281))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 331, 32))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.Button_check = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Button_check.setFont(font)
        self.Button_check.setObjectName("Button_check")
        self.horizontalLayout_2.addWidget(self.Button_check)
        self.total_shrimp_lable = QtWidgets.QLabel(self.groupBox_2)
        self.total_shrimp_lable.setGeometry(QtCore.QRect(170, 140, 136, 29))
        self.total_shrimp_lable.setObjectName("total_shrimp_lable")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 140, 111, 29))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.total_weight_lable = QtWidgets.QLabel(self.groupBox_2)
        self.total_weight_lable.setGeometry(QtCore.QRect(170, 180, 136, 29))
        self.total_weight_lable.setObjectName("total_weight_lable")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 180, 101, 29))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.name_lable = QtWidgets.QLabel(self.groupBox_2)
        self.name_lable.setGeometry(QtCore.QRect(170, 100, 171, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.name_lable.setFont(font)
        self.name_lable.setObjectName("name_lable")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(60, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(30, 220, 101, 29))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.total_batch_lable = QtWidgets.QLabel(self.groupBox_2)
        self.total_batch_lable.setGeometry(QtCore.QRect(170, 220, 136, 29))
        self.total_batch_lable.setObjectName("total_batch_lable")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(700, 50, 421, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.Time_label = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Time_label.setFont(font)
        self.Time_label.setObjectName("Time_label")
        self.horizontalLayout_7.addWidget(self.Time_label)
        self.Date_label = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Date_label.setFont(font)
        self.Date_label.setObjectName("Date_label")
        self.horizontalLayout_7.addWidget(self.Date_label)
        self.button_exit = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(1120, 620, 71, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.button_exit.setFont(font)
        self.button_exit.setObjectName("button_exit")
        self.Button_stop = QtWidgets.QPushButton(self.centralwidget)
        self.Button_stop.setGeometry(QtCore.QRect(160, 560, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.Button_stop.setFont(font)
        self.Button_stop.setObjectName("Button_stop")
        self.lable_weight_2 = QtWidgets.QLabel(self.centralwidget)
        self.lable_weight_2.setGeometry(QtCore.QRect(420, 550, 121, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.lable_weight_2.setFont(font)
        self.lable_weight_2.setObjectName("lable_weight_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1208, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_start.setText(_translate("MainWindow", "Start"))
        self.groupBox.setTitle(_translate("MainWindow", "Measurement"))
        self.Button_save.setText(_translate("MainWindow", "Save"))
        self.label_4.setText(_translate("MainWindow", "Weight measured:"))
        self.lable_nums.setText(_translate("MainWindow", "-"))
        self.lable_weight.setText(_translate("MainWindow", "-"))
        self.label_9.setText(_translate("MainWindow", "ID_employee:"))
        self.qr_lable.setText(_translate("MainWindow", "-"))
        self.label_3.setText(_translate("MainWindow", "Number of shrimp:"))
        self.label_10.setText(_translate("MainWindow", "g"))
        self.label_2.setText(_translate("MainWindow", "Management Monitoring"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Report"))
        self.label_5.setText(_translate("MainWindow", "ID employee:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.Button_check.setText(_translate("MainWindow", "Check"))
        self.total_shrimp_lable.setText(_translate("MainWindow", "-"))
        self.label_7.setText(_translate("MainWindow", "total shrimp:"))
        self.total_weight_lable.setText(_translate("MainWindow", "-"))
        self.label_8.setText(_translate("MainWindow", "total weight:"))
        self.name_lable.setText(_translate("MainWindow", "-"))
        self.label_6.setText(_translate("MainWindow", "name:"))
        self.label_12.setText(_translate("MainWindow", "total batch:"))
        self.total_batch_lable.setText(_translate("MainWindow", "-"))
        self.label_11.setText(_translate("MainWindow", " Time :"))
        self.Time_label.setText(_translate("MainWindow", "-"))
        self.Date_label.setText(_translate("MainWindow", "-"))
        self.button_exit.setText(_translate("MainWindow", "EXIT"))
        self.Button_stop.setText(_translate("MainWindow", "stop"))
        self.lable_weight_2.setText(_translate("MainWindow", "-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())