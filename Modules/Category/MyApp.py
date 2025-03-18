# from PyQt6.QtWidgets import QApplication
# from CategoryEx import MainWindowExt
# app = QApplication([])
#
# main_window = MainWindowExt()
# main_window.show()
#
# app.exec()


import sys
from PyQt6.QtWidgets import QApplication
from CategoryEx import MainWindowExt

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindowExt()
    main_window.show()
    sys.exit(app.exec())
