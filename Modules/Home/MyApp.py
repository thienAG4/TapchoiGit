from PyQt6.QtWidgets import QApplication, QMainWindow
from Home_Ext import HomeExt

app=QApplication([])
myWindow=HomeExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()