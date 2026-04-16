from PySide6.QtWidgets import (QWidget,QLabel,QVBoxLayout
                               ,QStackedWidget,QTableWidget,QTableWidgetItem)
from PySide6.QtCore import Qt
from .utilities import return_home
import models

class viewpage(QWidget):
    def __init__(self,stack):
        super().__init__()
        self.stack = stack   #type: QStackedWidget
        self.stack_widget = QStackedWidget()
        self.setMinimumSize(430,200)

        self.label = QLabel("member list is empty!!")
        self.members = QTableWidget()
        
        
        
        
        
        self.stack_widget.addWidget(self.label)
        

        self.layout4 = QVBoxLayout()
        self.setLayout(self.layout4)
        self.layout4.addWidget(self.stack_widget)

        home_btn = return_home.create_home_btn(self,stack,go_home="")
        self.layout4.addWidget(home_btn)
        

    def home(self):
        self.stack.setCurrentIndex(0)
        
    def display(self):
            if models.mem_list:
                self.members.setParent(None)
                self.members.deleteLater()
                self.members = QTableWidget()
                self.members.setColumnCount(4)
                self.members.setHorizontalHeaderLabels(["First Name","Last Name","ID","Status"])
                self.members.setRowCount(len(models.mem_list))
                self.stack_widget.addWidget(self.members)
                self.stack_widget.setCurrentWidget(self.members)
                for row,mem in enumerate(models.mem_list):
                    self.members.setItem(row,0,QTableWidgetItem(mem.first_name))
                    self.members.setItem(row,1,QTableWidgetItem(mem.last_name))
                    id_item = QTableWidgetItem(str(mem.idd))
                    id_item.setData(Qt.EditRole, int(mem.idd))
                    self.members.setItem(row,2,id_item)
                    self.members.setItem(row,3,QTableWidgetItem(mem.status))
                self.members.setSortingEnabled(True)
            else :
                 self.stack_widget.setCurrentWidget(self.label)