from PySide6.QtWidgets import QApplication,QStackedWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal
import sys
from models import *
from pages.utilities import *
load_mem()
from pages.home_page import win
from pages.Add_mem import add_win
from pages.view_mem import viewpage
# from pages.search_page import searchpage
# from pages.edit_page import editpage
# from pages.delete_page import deletepage


class app_win(QStackedWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Club Management")
        self.setWindowIcon(QIcon("icons/club"))
        self.setFixedSize(QSize(430,420))
        self.main_page = win(self)
        self.add_page = add_win(self)
        self.view_page = viewpage(self)
        # self.search_page = searchpage(self)
        # self.edit_page = editpage(self)
        # self.delete_page = deletepage(self)
                

        self.addWidget(self.main_page)
        self.addWidget(self.add_page)
        self.addWidget(self.view_page)
        # self.addWidget(self.search_page)
        # self.addWidget(self.edit_page)
        # self.addWidget(self.delete_page)
        
        self.main_page.go_main.connect(self.change_win_size)
        self.add_page.home_help.connect(self.original_size)

    def change_win_size(self):
        self.setFixedSize(QSize(430,300))
        self.setWindowTitle("Add member")

    def original_size(self):
        self.setFixedSize(QSize(430,420))
        self.setWindowTitle("Club Management")
        print("change")

app = QApplication(sys.argv)
window = app_win()
window.show()
app.exec()