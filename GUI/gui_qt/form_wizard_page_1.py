# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wizard_page_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(809, 432)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(350, 10, 451, 411))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 30, 431, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.excelFileName = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.excelFileName.setReadOnly(True)
        self.excelFileName.setObjectName("excelFileName")
        self.horizontalLayout_3.addWidget(self.excelFileName)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 160, 431, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.open_excel_compare_file = QtWidgets.QToolButton(self.horizontalLayoutWidget_5)
        self.open_excel_compare_file.setObjectName("open_excel_compare_file")
        self.horizontalLayout_5.addWidget(self.open_excel_compare_file)
        self.compare_file = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.compare_file.setReadOnly(True)
        self.compare_file.setObjectName("compare_file")
        self.horizontalLayout_5.addWidget(self.compare_file)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 431, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_checkMode = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_checkMode.setObjectName("checkBox_checkMode")
        self.horizontalLayout.addWidget(self.checkBox_checkMode)
        self.checkBox_both = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_both.setGeometry(QtCore.QRect(360, 119, 86, 41))
        self.checkBox_both.setObjectName("checkBox_both")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 210, 431, 191))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.tree_widget_box = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.tree_widget_box.setContentsMargins(0, 0, 0, 0)
        self.tree_widget_box.setObjectName("tree_widget_box")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 10, 191, 21))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_source = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_source.setObjectName("label_source")
        self.horizontalLayout_13.addWidget(self.label_source)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 130, 271, 21))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_check_mode = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_check_mode.setObjectName("label_check_mode")
        self.horizontalLayout_15.addWidget(self.label_check_mode)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 10, 281, 371))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 261, 351))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_dbtype = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.lineEdit_dbtype.setObjectName("lineEdit_dbtype")
        self.horizontalLayout_6.addWidget(self.lineEdit_dbtype)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_dbtype = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_dbtype.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_dbtype.setObjectName("label_dbtype")
        self.horizontalLayout_17.addWidget(self.label_dbtype)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_17)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_dbhost = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_dbhost.setObjectName("lineEdit_dbhost")
        self.horizontalLayout_7.addWidget(self.lineEdit_dbhost)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_dbHost = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_dbHost.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_dbHost.setObjectName("label_dbHost")
        self.horizontalLayout_18.addWidget(self.label_dbHost)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_18)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEdit_dbuser = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_dbuser.setObjectName("lineEdit_dbuser")
        self.horizontalLayout_8.addWidget(self.lineEdit_dbuser)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_dbUser = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_dbUser.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_dbUser.setObjectName("label_dbUser")
        self.horizontalLayout_19.addWidget(self.label_dbUser)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_19)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_dbpass = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_dbpass.setObjectName("lineEdit_dbpass")
        self.horizontalLayout_9.addWidget(self.lineEdit_dbpass)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_dbPass = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_dbPass.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_dbPass.setObjectName("label_dbPass")
        self.horizontalLayout_20.addWidget(self.label_dbPass)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_20)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEdit_dbbase = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_dbbase.setObjectName("lineEdit_dbbase")
        self.horizontalLayout_10.addWidget(self.lineEdit_dbbase)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_dbBase = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_dbBase.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_dbBase.setObjectName("label_dbBase")
        self.horizontalLayout_21.addWidget(self.label_dbBase)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_21)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdit_dbport = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_dbport.setObjectName("lineEdit_dbport")
        self.horizontalLayout_11.addWidget(self.lineEdit_dbport)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_dbPort = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_dbPort.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_dbPort.setObjectName("label_dbPort")
        self.horizontalLayout_23.addWidget(self.label_dbPort)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_23)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_chose_loadMode = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_chose_loadMode.setObjectName("comboBox_chose_loadMode")
        self.horizontalLayout_2.addWidget(self.comboBox_chose_loadMode)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_loadMode = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_loadMode.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_loadMode.setObjectName("label_loadMode")
        self.horizontalLayout_24.addWidget(self.label_loadMode)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_24)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(20, 390, 281, 31))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 251, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.checkBox_Dictionary = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox_Dictionary.setObjectName("checkBox_Dictionary")
        self.horizontalLayout_12.addWidget(self.checkBox_Dictionary)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.open_excel_compare_file.setText(_translate("Form", "..."))
        self.checkBox_checkMode.setText(_translate("Form", "Check mode"))
        self.checkBox_both.setText(_translate("Form", "Both"))
        self.label_source.setText(_translate("Form", "Source excel file name:"))
        self.label_check_mode.setText(_translate("Form", "Check table name:"))
        self.label_dbtype.setText(_translate("Form", "dbtype"))
        self.label_dbHost.setText(_translate("Form", "dbHost"))
        self.label_dbUser.setText(_translate("Form", "dbUser"))
        self.label_dbPass.setText(_translate("Form", "dbPass"))
        self.label_dbBase.setText(_translate("Form", "dbBase"))
        self.label_dbPort.setText(_translate("Form", "dbPort"))
        self.label_loadMode.setText(_translate("Form", "Load Mode"))
        self.checkBox_Dictionary.setText(_translate("Form", "Dictionary"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
