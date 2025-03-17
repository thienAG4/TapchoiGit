import json
import os
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QLineEdit, QLabel, QPushButton, QVBoxLayout, QDialog
from Modules.Sign_up.Sign_up import Ui_MainWindow
import sys
from Api.Signup_API import SignupAPI

class Sign_upEx(QMainWindow, Ui_MainWindow, SignupAPI):
    # def __init__(self):
    #     super().__init__()
    #     self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushRegister.clicked.connect(self.register)
        self.checkShowPassword.stateChanged.connect(self.show_password)

    def register(self):
        username = self.lineUserName.text().strip()
        password = self.linePassword.text().strip()
        confirm_password = self.lineConfirm.text().strip()
        signup_signal= self.check_user_signup(username=username, password=password,repassword=confirm_password)
        match signup_signal:
            case 1:
                QMessageBox.warning(self.MainWindow, "Error", "Error 1: Username or password is empty")
            case 2:
                QMessageBox.warning(self.MainWindow, "Error", "Error 2: Password is not the same")
            case 3:
                QMessageBox.warning(self.MainWindow, "Error", "Error 3: Username is already exist")
            case _:
                QMessageBox.warning(self.MainWindow, "Notification", "Successful registration")



    def show_password(self):
        if self.checkShowPassword.isChecked():
            self.linePassword.setEchoMode(QLineEdit.EchoMode.Normal)
            self.lineConfirm.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.linePassword.setEchoMode(QLineEdit.EchoMode.Password)
            self.lineConfirm.setEchoMode(QLineEdit.EchoMode.Password)

    def show(self):
        self.MainWindow.show()

