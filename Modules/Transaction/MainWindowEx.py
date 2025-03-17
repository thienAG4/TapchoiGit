from PyQt6 import QtWidgets
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, QDialog
from FileFactory import FileFactory
from MainWindow import Ui_MainWindow
from MainWindow2 import Ui_MainWindow2
from chatbot import get_transactions

class Confirm(QDialog):
    def __init__(self):
        self.setWindowTitle("Notification")
        self.setFixedSize(400, 200)
        self.setStyleSheet("background-color: #0000FF; border-radius: 20px;")

        title_label = QLabel("<b>NOTIFICATION</b>")
        title_label.setFont(QFont("Arial", 12))
        title_label.setStyleSheet("color: black; text-align: center;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        message_label = QLabel("Deleted Transactions\nCannot Be Restored")
        message_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        message_label.setStyleSheet("color: white; text-align: center;")
        message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        cancel_button = QPushButton("CANCEL")
        cancel_button.setStyleSheet("background-color: navy; color: white; border: none; padding: 10px;")
        cancel_button.clicked.connect(self.reject)

        delete_button = QPushButton("DELETE")
        delete_button.setStyleSheet("background-color: navy; color: white; border: none; padding: 10px;")
        delete_button.clicked.connect(self.accept)

        button_layout = QHBoxLayout()
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(delete_button)

        layout = QVBoxLayout()
        layout.addWidget(title_label)
        layout.addWidget(message_label)
        layout.addLayout(button_layout)
        self.setLayout(layout)

class MainWindowEx(QMainWindow):

    def __init__(self):
        super().__init__()
        self.products = []
        self.selectedProduct = None
        self.fileFactory = FileFactory()
        self.Page1 = Ui_MainWindow()
        self.Transaction = Ui_MainWindow2()
        self.Page1.setupUi(self)
        self.setupUi()

    def setupUi(self):
        self.products = self.fileFactory.readData("./data/database.json", Product)
        self.loadDataIntoTableWidget()
        self.Page1.pushButton_Edit.clicked.connect(self.open_transaction)
        self.Page1.pushButton_Delete.clicked.connect(self.Delete)

    def open_transaction(self):
        self.Transaction_open = QMainWindow()
        self.Transaction.setupUi(self.Transaction_open)
        self.Transaction.pushButton_Transaction.clicked.connect(self.Save)
        self.Transaction.pushButton_Save.clicked.connect(self.processSave)
        self.Transaction_open.show()
        self.hide()

    def Save(self):
        self.show()
        self.Transaction_open.close()

    def loadDataIntoTableWidget(self):
         self.Page1.tableWidgetProduct.setRowCount(0)
         for product in self.products:
             row = self.Page1.tableWidgetProduct.rowCount()
             self.Page1.tableWidgetProduct.insertRow(row)
             self.Page1.tableWidgetProduct.setItem(row, 0, QTableWidgetItem(str(product.Categories)))
             self.Page1.tableWidgetProduct.setItem(row, 1, QTableWidgetItem(product.Details))
             self.Page1.tableWidgetProduct.setItem(row, 2, QTableWidgetItem(str(product.Amount)))
             self.Page1.tableWidgetProduct.setItem(row, 3, QTableWidgetItem(str(product.Date)))

    def Delete(self):
        current_row = self.Page1.tableWidgetProduct.currentRow()
        if current_row == 0:
            QMessageBox.warning(self, "Error", "Please select a row to delete")
            return

        dlg = Confirm()
        button = dlg.exec()
        if button == QDialog.DialogCode.Accepted:
            del self.products[current_row]
            self.Page1.tableWidgetProduct.removeRow(current_row)
            self.fileFactory.writeData("database.json", self.products)

    def processSave(self):
        Categories = "Food"
        if self.Transaction.radioButton_Transport.isChecked():
            Categories = "Transport"
        elif self.Transaction.radioButton_Medicine.isChecked():
            Categories = "Medicine"
        elif self.Transaction.radioButton_Groceries.isChecked():
            Categories = "Groceries"
        elif self.Transaction.radioButton_Gift.isChecked():
            Categories = "Gift"
        elif self.Transaction.radioButton_Savings.isChecked():
            Categories = "Savings"
        elif self.Transaction.radioButton_Entertainment.isChecked():
            Categories = "Entertainment"
        elif self.Transaction.radioButton_Rent.isChecked():
            Categories = "Rent"

        product = Product(Categories,self.Transaction.lineEdit_ExpenseTitle.text(), float(self.Transaction.lineEdit_Amount.text()), self.Transaction.lineEdit_Date.text())

        self.products.append(product)
        row = self.Page1.tableWidgetProduct.rowCount()

        self.Page1.tableWidgetProduct.insertRow(row)
        self.selectedProduct = product
        self.products[row] = self.selectedProduct

        self.Page1.tableWidgetProduct.setItem(row, 0, QTableWidgetItem(Categories))
        self.Page1.tableWidgetProduct.setItem(row, 1, QTableWidgetItem(product.Details))
        self.Page1.tableWidgetProduct.setItem(row, 2, QTableWidgetItem(str(product.Amount)))
        self.Page1.tableWidgetProduct.setItem(row, 3, QTableWidgetItem(str(product.Date)))
        self.fileFactory.writeData("./data/database.json", self.products)

    def get_total_expense(self):
        transactions = get_transactions()
        return sum([int(t["Amount"]) for t in transactions if
                    isinstance(t["Amount"], (int, float, str)) and str(t["Amount"]).isdigit()])

class Product:
    def __init__(self, Categories, Details, Amount, Date):
        self.Categories = Categories
        self.Details = Details
        self.Amount = Amount
        self.Date = Date

    def __str__(self):
        return f"{self.Categories} - {self.Details} - {self.Amount} - {self.Date}"

