# Form implementation generated from reading ui file 'D:\KTLT_DOANCK\Category.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Category(object):
    def setupUi(self, Category):
        Category.setObjectName("Category")
        Category.resize(1097, 778)
        Category.setSizeIncrement(QtCore.QSize(0, 0))
        Category.setAutoFillBackground(False)
        Category.setStyleSheet("background-color: rgb(255, 255, 255);")
        Category.setIconSize(QtCore.QSize(25, 25))
        Category.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(parent=Category)
        self.centralwidget.setObjectName("centralwidget")
        self.Icon_menu = QtWidgets.QLabel(parent=self.centralwidget)
        self.Icon_menu.setGeometry(QtCore.QRect(20, 21, 25, 25))
        self.Icon_menu.setText("")
        self.Icon_menu.setPixmap(QtGui.QPixmap("D:\\KTLT_DOANCK\\images/home/Icon_Menu.png"))
        self.Icon_menu.setObjectName("Icon_menu")
        self.label_menu = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_menu.setGeometry(QtCore.QRect(77, 21, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(18)
        self.label_menu.setFont(font)
        self.label_menu.setStyleSheet("color: rgb(52, 60, 106);")
        self.label_menu.setObjectName("label_menu")
        self.pushButton_home = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_home.setGeometry(QtCore.QRect(32, 89, 158, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.pushButton_home.sizePolicy().hasHeightForWidth())
        self.pushButton_home.setSizePolicy(sizePolicy)
        self.pushButton_home.setMinimumSize(QtCore.QSize(158, 25))
        self.pushButton_home.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setToolTip("")
        self.pushButton_home.setStyleSheet("color: rgb(177, 177, 177);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\KTLT_DOANCK\\images/home/Icon_Home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_home.setIcon(icon)
        self.pushButton_home.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_home.setShortcut("")
        self.pushButton_home.setCheckable(False)
        self.pushButton_home.setAutoRepeat(False)
        self.pushButton_home.setAutoDefault(False)
        self.pushButton_home.setObjectName("pushButton_home")
        self.pushButton_category = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_category.setGeometry(QtCore.QRect(32, 195, 158, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.pushButton_category.sizePolicy().hasHeightForWidth())
        self.pushButton_category.setSizePolicy(sizePolicy)
        self.pushButton_category.setMinimumSize(QtCore.QSize(158, 26))
        self.pushButton_category.setSizeIncrement(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_category.setFont(font)
        self.pushButton_category.setStyleSheet("color: rgb(24, 20, 243);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\KTLT_DOANCK\\images/category/Icon_Category.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_category.setIcon(icon1)
        self.pushButton_category.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_category.setShortcut("")
        self.pushButton_category.setAutoRepeat(False)
        self.pushButton_category.setObjectName("pushButton_category")
        self.pushButton_transaction = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_transaction.setGeometry(QtCore.QRect(32, 142, 158, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_transaction.sizePolicy().hasHeightForWidth())
        self.pushButton_transaction.setSizePolicy(sizePolicy)
        self.pushButton_transaction.setMinimumSize(QtCore.QSize(158, 25))
        self.pushButton_transaction.setSizeIncrement(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_transaction.setFont(font)
        self.pushButton_transaction.setStyleSheet("color: rgb(177, 177, 177);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\KTLT_DOANCK\\images/home/Icon_Transaction.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_transaction.setIcon(icon2)
        self.pushButton_transaction.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_transaction.setShortcut("")
        self.pushButton_transaction.setCheckable(False)
        self.pushButton_transaction.setAutoRepeat(False)
        self.pushButton_transaction.setObjectName("pushButton_transaction")
        self.pushButton_account = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_account.setGeometry(QtCore.QRect(32, 248, 158, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.pushButton_account.sizePolicy().hasHeightForWidth())
        self.pushButton_account.setSizePolicy(sizePolicy)
        self.pushButton_account.setMinimumSize(QtCore.QSize(158, 25))
        self.pushButton_account.setSizeIncrement(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_account.setFont(font)
        self.pushButton_account.setStyleSheet("color: rgb(177, 177, 177);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("D:\\KTLT_DOANCK\\images/home/Icon_Account.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_account.setIcon(icon3)
        self.pushButton_account.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_account.setShortcut("")
        self.pushButton_account.setCheckable(False)
        self.pushButton_account.setAutoRepeat(False)
        self.pushButton_account.setObjectName("pushButton_account")
        self.label_CATEGORY = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_CATEGORY.setGeometry(QtCore.QRect(249, 29, 127, 34))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(17)
        self.label_CATEGORY.setFont(font)
        self.label_CATEGORY.setStyleSheet("color: rgb(52, 60, 106);")
        self.label_CATEGORY.setObjectName("label_CATEGORY")
        self.Icon_mybalance = QtWidgets.QLabel(parent=self.centralwidget)
        self.Icon_mybalance.setGeometry(QtCore.QRect(283, 95, 70, 70))
        self.Icon_mybalance.setMinimumSize(QtCore.QSize(70, 70))
        self.Icon_mybalance.setText("")
        self.Icon_mybalance.setPixmap(QtGui.QPixmap("D:\\KTLT_DOANCK\\images/home/Icon_MyBalance.png"))
        self.Icon_mybalance.setObjectName("Icon_mybalance")
        self.lineEdit_mybalance = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_mybalance.setGeometry(QtCore.QRect(373, 128, 120, 32))
        self.lineEdit_mybalance.setObjectName("lineEdit_mybalance")
        self.label_mybalance = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_mybalance.setGeometry(QtCore.QRect(373, 100, 108, 20))
        self.label_mybalance.setMinimumSize(QtCore.QSize(108, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(12)
        self.label_mybalance.setFont(font)
        self.label_mybalance.setStyleSheet("color: rgb(113, 142, 191);")
        self.label_mybalance.setObjectName("label_mybalance")
        self.Icon_income = QtWidgets.QLabel(parent=self.centralwidget)
        self.Icon_income.setGeometry(QtCore.QRect(534, 94, 70, 70))
        self.Icon_income.setMinimumSize(QtCore.QSize(70, 70))
        self.Icon_income.setText("")
        self.Icon_income.setPixmap(QtGui.QPixmap("D:\\KTLT_DOANCK\\images/home/Icon_Income.png"))
        self.Icon_income.setObjectName("Icon_income")
        self.lineEdit_expense = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_expense.setGeometry(QtCore.QRect(882, 128, 117, 32))
        self.lineEdit_expense.setMinimumSize(QtCore.QSize(117, 32))
        self.lineEdit_expense.setObjectName("lineEdit_expense")
        self.label_expense = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_expense.setGeometry(QtCore.QRect(882, 100, 108, 20))
        self.label_expense.setMinimumSize(QtCore.QSize(88, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(12)
        self.label_expense.setFont(font)
        self.label_expense.setStyleSheet("color: rgb(113, 142, 191);")
        self.label_expense.setObjectName("label_expense")
        self.Icon_expense = QtWidgets.QLabel(parent=self.centralwidget)
        self.Icon_expense.setGeometry(QtCore.QRect(794, 96, 70, 70))
        self.Icon_expense.setMinimumSize(QtCore.QSize(70, 70))
        self.Icon_expense.setText("")
        self.Icon_expense.setPixmap(QtGui.QPixmap("D:\\KTLT_DOANCK\\images/home/Icon_Expenses.png"))
        self.Icon_expense.setObjectName("Icon_expense")
        self.lineEdit_income = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_income.setGeometry(QtCore.QRect(627, 126, 117, 32))
        self.lineEdit_income.setMinimumSize(QtCore.QSize(117, 32))
        self.lineEdit_income.setObjectName("lineEdit_income")
        self.label_income = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_income.setGeometry(QtCore.QRect(627, 98, 108, 20))
        self.label_income.setMinimumSize(QtCore.QSize(88, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(12)
        self.label_income.setFont(font)
        self.label_income.setStyleSheet("color: rgb(113, 142, 191);")
        self.label_income.setObjectName("label_income")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(249, 190, 810, 91))
        self.label.setMinimumSize(QtCore.QSize(810, 90))
        self.label.setStyleSheet("background-color: rgb(231, 237, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.radioButton_food = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_food.setGeometry(QtCore.QRect(316, 199, 73, 50))
        self.radioButton_food.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.radioButton_food.setStyleSheet("background-color: rgb(231, 237, 255);")
        self.radioButton_food.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("D:\\KTLT_DOANCK\\images/category/Icon_Food.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.radioButton_food.setIcon(icon4)
        self.radioButton_food.setIconSize(QtCore.QSize(50, 50))
        self.radioButton_food.setObjectName("radioButton_food")
        self.radioButton_transport = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_transport.setGeometry(QtCore.QRect(393, 199, 73, 50))
        self.radioButton_transport.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.radioButton_transport.setStyleSheet("background-color: rgb(231, 237, 255);")
        self.radioButton_transport.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("D:\\KTLT_DOANCK\\images/category/Icon_Transport.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.radioButton_transport.setIcon(icon5)
        self.radioButton_transport.setIconSize(QtCore.QSize(50, 50))
        self.radioButton_transport.setObjectName("radioButton_transport")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(323, 258, 41, 14))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(231, 237, 255);\n"
"color: rgb(9, 48, 48);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(388, 258, 71, 14))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(231, 237, 255);\n"
"color: rgb(9, 48, 48);")
        self.label_3.setObjectName("label_3")
        self.radioButton_medicine = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_medicine.setGeometry(QtCore.QRect(470, 199, 73, 50))
        self.radioButton_medicine.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.radioButton_medicine.setStyleSheet("background-color: rgb(231, 237, 255);")
        self.radioButton_medicine.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("D:\\KTLT_DOANCK\\images/category/Icon_Medicine.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.radioButton_medicine.setIcon(icon6)
        self.radioButton_medicine.setIconSize(QtCore.QSize(50, 50))
        self.radioButton_medicine.setObjectName("radioButton_medicine")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(471, 258, 64, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(231, 237, 255);\n"
"color: rgb(9, 48, 48);")
        self.label_9.setObjectName("label_9")
        self.radioButton_groceries = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_groceries.setGeometry(QtCore.QRect(548, 199, 73, 50))
        self.radioButton_groceries.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.radioButton_groceries.setStyleSheet("background-color: rgb(231, 237, 255);")
        self.radioButton_groceries.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("D:\\KTLT_DOANCK\\images/category/Icon_Groceries.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.radioButton_groceries.setIcon(icon7)
        self.radioButton_groceries.setIconSize(QtCore.QSize(50, 50))
        self.radioButton_groceries.setObjectName("radioButton_groceries")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(548, 258, 69, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(231, 237, 255);\n"
"color: rgb(9, 48, 48);")
        self.label_10.setObjectName("label_10")
        self.radioButton_rent = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_rent.setGeometry(QtCore.QRect(625, 199, 73, 50))
        self.radioButton_rent.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.radioButton_rent.setStyleSheet("background-color: rgb(231, 237, 255);")
        self.radioButton_rent.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("D:\\KTLT_DOANCK\\images/category/Icon_Rent.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.radioButton_rent.setIcon(icon8)
        self.radioButton_rent.setIconSize(QtCore.QSize(50, 50))
        self.radioButton_rent.setObjectName("radioButton_rent")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(639, 258, 35, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(231, 237, 255);\n"
"color: rgb(9, 48, 48);")
        self.label_11.setObjectName("label_11")
        self.radioButton_gifts = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_gifts.setGeometry(QtCore.QRect(702, 199, 73, 50))
        self.radioButton_gifts.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.radioButton_gifts.setStyleSheet("background-color: rgb(231, 237, 255);")
        self.radioButton_gifts.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("D:\\KTLT_DOANCK\\images/category/Icon_Gifts.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.radioButton_gifts.setIcon(icon9)
        self.radioButton_gifts.setIconSize(QtCore.QSize(50, 50))
        self.radioButton_gifts.setObjectName("radioButton_gifts")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(714, 258, 32, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(231, 237, 255);\n"
"color: rgb(9, 48, 48);")
        self.label_12.setObjectName("label_12")
        self.radioButton_saving = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_saving.setGeometry(QtCore.QRect(784, 199, 73, 50))
        self.radioButton_saving.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.radioButton_saving.setStyleSheet("background-color: rgb(231, 237, 255);")
        self.radioButton_saving.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("D:\\KTLT_DOANCK\\images/category/Icon_Saving.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.radioButton_saving.setIcon(icon10)
        self.radioButton_saving.setIconSize(QtCore.QSize(50, 50))
        self.radioButton_saving.setObjectName("radioButton_saving")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(785, 258, 47, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(231, 237, 255);\n"
"color: rgb(9, 48, 48);")
        self.label_13.setObjectName("label_13")
        self.radioButton_entertainment = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_entertainment.setGeometry(QtCore.QRect(864, 199, 73, 50))
        self.radioButton_entertainment.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.radioButton_entertainment.setStyleSheet("background-color: rgb(231, 237, 255);")
        self.radioButton_entertainment.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("D:\\KTLT_DOANCK\\images/category/Icon_Entertainment.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.radioButton_entertainment.setIcon(icon11)
        self.radioButton_entertainment.setIconSize(QtCore.QSize(50, 50))
        self.radioButton_entertainment.setObjectName("radioButton_entertainment")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(846, 258, 100, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(231, 237, 255);\n"
"color: rgb(9, 48, 48);")
        self.label_14.setObjectName("label_14")
        self.radioButton_more = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_more.setGeometry(QtCore.QRect(938, 199, 73, 50))
        self.radioButton_more.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.radioButton_more.setStyleSheet("background-color: rgb(231, 237, 255);")
        self.radioButton_more.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("D:\\KTLT_DOANCK\\images/category/Icon_More.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.radioButton_more.setIcon(icon12)
        self.radioButton_more.setIconSize(QtCore.QSize(50, 50))
        self.radioButton_more.setObjectName("radioButton_more")
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(953, 258, 47, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(231, 237, 255);\n"
"color: rgb(9, 48, 48);")
        self.label_15.setObjectName("label_15")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(249, 295, 465, 407))
        self.label_4.setStyleSheet("background-color: rgb(231, 237, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton_addexpenses = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_addexpenses.setGeometry(QtCore.QRect(397, 643, 180, 45))
        self.pushButton_addexpenses.setStyleSheet("background-color: rgb(231, 237, 255);")
        self.pushButton_addexpenses.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("D:\\KTLT_DOANCK\\images/category/Button_AddExpenses.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_addexpenses.setIcon(icon13)
        self.pushButton_addexpenses.setIconSize(QtCore.QSize(180, 45))
        self.pushButton_addexpenses.setObjectName("pushButton_addexpenses")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(260, 300, 451, 331))
        self.groupBox.setObjectName("groupBox")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.groupBox)
        self.scrollArea.setGeometry(QtCore.QRect(150, 100, 1, 1))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 16, 16))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.table_expenses = QtWidgets.QTableWidget(parent=self.groupBox)
        self.table_expenses.setGeometry(QtCore.QRect(20, 40, 381, 192))
        self.table_expenses.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 170, 255);")
        self.table_expenses.setObjectName("table_expenses")
        self.table_expenses.setColumnCount(3)
        self.table_expenses.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.table_expenses.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_expenses.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_expenses.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_expenses.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_expenses.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_expenses.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_expenses.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_expenses.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_expenses.setHorizontalHeaderItem(2, item)
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(730, 295, 328, 407))
        self.label_5.setStyleSheet("background-color: rgb(234, 232, 241);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        Category.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Category)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1097, 26))
        self.menubar.setObjectName("menubar")
        Category.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Category)
        self.statusbar.setObjectName("statusbar")
        Category.setStatusBar(self.statusbar)

        self.retranslateUi(Category)
        QtCore.QMetaObject.connectSlotsByName(Category)

    def retranslateUi(self, Category):
        _translate = QtCore.QCoreApplication.translate
        Category.setWindowTitle(_translate("Category", "MainWindow"))
        self.label_menu.setText(_translate("Category", "Menu"))
        self.pushButton_home.setText(_translate("Category", "Home"))
        self.pushButton_category.setText(_translate("Category", "Category"))
        self.pushButton_transaction.setText(_translate("Category", "Transaction"))
        self.pushButton_account.setText(_translate("Category", "Account"))
        self.label_CATEGORY.setText(_translate("Category", "Category"))
        self.lineEdit_mybalance.setText(_translate("Category", "0"))
        self.label_mybalance.setText(_translate("Category", "My Balance"))
        self.lineEdit_expense.setText(_translate("Category", "0"))
        self.label_expense.setText(_translate("Category", "Expense"))
        self.lineEdit_income.setText(_translate("Category", "0"))
        self.label_income.setText(_translate("Category", "Income"))
        self.label_2.setText(_translate("Category", "Food"))
        self.label_3.setText(_translate("Category", "Transport"))
        self.label_9.setText(_translate("Category", "Medicine"))
        self.label_10.setText(_translate("Category", "Groceries"))
        self.label_11.setText(_translate("Category", "Rent"))
        self.label_12.setText(_translate("Category", "Gifts"))
        self.label_13.setText(_translate("Category", "Saving"))
        self.label_14.setText(_translate("Category", "Entertainment"))
        self.label_15.setText(_translate("Category", "More"))
        self.groupBox.setTitle(_translate("Category", "GroupBox"))
        item = self.table_expenses.horizontalHeaderItem(0)
        item.setText(_translate("Category", "Date"))
        item = self.table_expenses.horizontalHeaderItem(1)
        item.setText(_translate("Category", "Category"))
        item = self.table_expenses.horizontalHeaderItem(2)
        item.setText(_translate("Category", "Amount"))
