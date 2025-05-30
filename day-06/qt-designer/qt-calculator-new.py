# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt-calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import uic
import sys


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(891, 659)
        self.calcButton = QtWidgets.QPushButton(Dialog)
        self.calcButton.setGeometry(QtCore.QRect(330, 370, 291, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.calcButton.setFont(font)
        self.calcButton.setObjectName("calcButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 75, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(140, 150, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.input1 = QtWidgets.QLineEdit(Dialog)
        self.input1.setGeometry(QtCore.QRect(330, 70, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input1.setFont(font)
        self.input1.setObjectName("input1")
        self.input2 = QtWidgets.QLineEdit(Dialog)
        self.input2.setGeometry(QtCore.QRect(330, 150, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input2.setFont(font)
        self.input2.setObjectName("input2")
        self.addRadio = QtWidgets.QRadioButton(Dialog)
        self.addRadio.setGeometry(QtCore.QRect(330, 240, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addRadio.setFont(font)
        self.addRadio.setObjectName("addRadio")
        self.subRadio = QtWidgets.QRadioButton(Dialog)
        self.subRadio.setGeometry(QtCore.QRect(330, 270, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.subRadio.setFont(font)
        self.subRadio.setObjectName("subRadio")
        self.mulRadio = QtWidgets.QRadioButton(Dialog)
        self.mulRadio.setGeometry(QtCore.QRect(330, 300, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mulRadio.setFont(font)
        self.mulRadio.setObjectName("mulRadio")
        self.divRadio = QtWidgets.QRadioButton(Dialog)
        self.divRadio.setGeometry(QtCore.QRect(330, 330, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.divRadio.setFont(font)
        self.divRadio.setObjectName("divRadio")
        self.re = QtWidgets.QLabel(Dialog)
        self.re.setGeometry(QtCore.QRect(140, 540, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.re.setFont(font)
        self.re.setObjectName("re")
        self.resultLabel = QtWidgets.QLabel(Dialog)
        self.resultLabel.setGeometry(QtCore.QRect(330, 530, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.resultLabel.setFont(font)
        self.resultLabel.setObjectName("resultLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.calcButton.clicked.connect(self.calculate)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.calcButton.setText(_translate("Dialog", "Calculate"))
        self.label.setText(_translate("Dialog", "Operand A"))
        self.label_3.setText(_translate("Dialog", "Operand B"))
        self.addRadio.setText(_translate("Dialog", "Add"))
        self.subRadio.setText(_translate("Dialog", "Subtract"))
        self.mulRadio.setText(_translate("Dialog", "Multiply"))
        self.divRadio.setText(_translate("Dialog", "Divide"))
        self.re.setText(_translate("Dialog", "Result:"))
        self.resultLabel.setText(_translate("Dialog", "0"))

    def calculate(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())

            if self.addRadio.isChecked():
                result = num1 + num2
            elif self.subRadio.isChecked():
                result = num1 - num2
            elif self.mulRadio.isChecked():
                result = num1 * num2
            elif self.divRadio.isChecked():
                if num2 != 0:
                    result = num1 / num2
                else:
                    raise ValueError("Cannot divide by zero")
            else:
                result = "Select an operation"

            self.resultLabel.setText(f"{result}")

        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
