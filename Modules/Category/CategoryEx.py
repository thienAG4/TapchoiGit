import json
import os

from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QDialog, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from Category import Ui_Category
from Category_Addexpenses import Ui_add

class Confirm(QDialog):
    def __init__(self, message, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Notification")
        self.setFixedSize(400, 200)  # Kích thước cửa sổ
        self.setStyleSheet("background-color: #1814F3; border-radius: 50px;")  # Nền xanh & bo góc

        # Tiêu đề "NOTIFICATION"
        title_label = QLabel("<b>CONFIRM</b>")
        title_label.setFont(QFont("Arial", 16))
        title_label.setStyleSheet("color: white; text-align: center;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Nội dung thông báo
        message_label = QLabel(message)
        message_label.setFont(QFont("Arial", 13, QFont.Weight.Bold))
        message_label.setStyleSheet("color: white; text-align: center;")
        message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Nút Yes
        cancel_button = QPushButton("YES")
        cancel_button.setStyleSheet("background-color: navy; color: white; border: none; padding: 10px;")
        cancel_button.clicked.connect(self.accept)  # Xác nhận

        # Nút No
        confirm_button = QPushButton("NO")
        confirm_button.setStyleSheet("background-color: navy; color: white; border: none; padding: 10px;")
        confirm_button.clicked.connect(self.reject)  # Đóng cửa sổ

        # Layout cho nút
        button_layout = QHBoxLayout()
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(confirm_button)

        # Layout chính
        layout = QVBoxLayout()
        layout.addWidget(title_label)
        layout.addWidget(message_label)
        layout.addLayout(button_layout)

        self.setLayout(layout)


class MainWindowExt(QMainWindow):
    def __init__(self):
        super().__init__()
        self.category = Ui_Category()
        self.add_expenses = Ui_add()

        self.category.setupUi(self)
        self.setup_table()
        self.setup_signals()
        self.load_expense_history()

    def setup_table(self):
        """Cấu hình bảng để hiển thị dữ liệu từ expenses.json"""
        self.category.table_expenses.setColumnCount(4)
        self.category.table_expenses.setHorizontalHeaderLabels(["Date", "Category", "Details", "Amount"])

    def setup_signals(self):
        """Kết nối các nút với các chức năng tương ứng"""
        self.category.pushButton_addexpenses.clicked.connect(self.show_add_expenses)
        self.category.radioButton_transport.toggled.connect(self.filter_transport_data)
        self.category.radioButton_medicine.toggled.connect(self.filter_medicine_data)
        self.category.radioButton_groceries.toggled.connect(self.filter_groceries_data)
        self.category.radioButton_rent.toggled.connect(self.filter_rent_data)

    def show_add_expenses(self):
        self.add_expenses_window = QMainWindow()
        self.add_expenses.setupUi(self.add_expenses_window)
        self.add_expenses.pushButton_save.clicked.connect(self.show_category)
        self.add_expenses_window.show()
        self.hide()

    def show_category(self):
        """Hiển thị dialog xác nhận trước khi quay lại danh sách chi tiêu"""
        dialog = Confirm("Do you really want to save these changes?",self)
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            self.show()
            self.add_expenses_window.close()
            self.load_expense_history()
        else:
            # Nếu chọn Cancel, không làm gì cả
            pass

    def load_expense_history(self, category_filter=None):
        """Đọc dữ liệu từ expenses.json và hiển thị trên bảng"""
        try:
            with open("data/expenses.json", "r", encoding="utf-8") as file:
                expenses = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            expenses = []

        if category_filter:
            expenses = [exp for exp in expenses if exp["category"] == category_filter]

        self.category.table_expenses.setRowCount(len(expenses))
        for row, expense in enumerate(expenses):
            self.category.table_expenses.setItem(row, 0, QTableWidgetItem(expense.get("date", "N/A")))
            self.category.table_expenses.setItem(row, 1, QTableWidgetItem(expense.get("category", "N/A")))
            self.category.table_expenses.setItem(row, 2, QTableWidgetItem(expense.get("details", "N/A")))
            self.category.table_expenses.setItem(row, 3, QTableWidgetItem(str(expense.get("amount", "0"))))

    def filter_food_data(self):
        if self.category.radioButton_food.isChecked():
            self.load_expense_history(category_filter="Food")
        else:
            self.load_expense_history()

    def filter_transport_data(self):
        """Lọc dữ liệu chỉ hiển thị các khoản chi thuộc 'Transport'"""
        if self.category.radioButton_transport.isChecked():
            self.load_expense_history(category_filter="Transport")
        else:
            self.load_expense_history()

    def filter_medicine_data(self):
        """Lọc dữ liệu chỉ hiển thị các khoản chi thuộc 'Medicine'"""
        if self.category.radioButton_medicine.isChecked():
            self.load_expense_history(category_filter="Medicine")
        else:
            self.load_expense_history()

    def filter_groceries_data(self):
        """Lọc dữ liệu chỉ hiển thị các khoản chi thuộc 'Groceries'"""
        if self.category.radioButton_groceries.isChecked():
            self.load_expense_history(category_filter="Groceries")
        else:
            self.load_expense_history()

    def filter_rent_data(self):
        """Lọc dữ liệu chỉ hiển thị các khoản chi thuộc 'Rent'"""
        if self.category.radioButton_rent.isChecked():
            self.load_expense_history(category_filter="Rent")
        else:
            self.load_expense_history()





