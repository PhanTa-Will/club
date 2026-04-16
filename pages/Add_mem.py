from PySide6.QtWidgets import (QWidget,QPushButton,QVBoxLayout,QComboBox
                               ,QLineEdit,QMessageBox)
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import Signal
from .utilities import return_home,save_mem
from models import club_members,mem_list
import random





#Add mem page
class add_win(QWidget):
    home_help = return_home.go_home
    def __init__(self,stack):
        super().__init__()
        self.stack = stack #type : QStackWidget
        self.layout3 = QVBoxLayout()
        self.setLayout(self.layout3)
        self.setStyleSheet("background-color: white;")
        self.first_name = QLineEdit()
        self.first_name.setPlaceholderText("Enter first name")
        self.first_name.textChanged.connect(self.b_add_enable)

        self.last_name = QLineEdit()
        self.last_name.setPlaceholderText("Enter last name")
        self.last_name.textChanged.connect(self.b_add_enable)

        self.id = QLineEdit()
        
        while True:
            id_choice = str(random.randint(1, 100))
            duplicated = False
            for i in mem_list:
                if i.idd == id_choice:
                    duplicated = True
                    break
            if not duplicated:
                break
                
        self.id.setText(id_choice)
        self.id.setEnabled(False) 
        self.id.setValidator(QIntValidator())
        self.id.textChanged.connect(self.b_add_enable)

        self.status = QComboBox()
        self.status.addItems([ "Inactive","Active"])
        

        self.layout3.addWidget(self.first_name)
        self.layout3.addWidget(self.last_name)
        self.layout3.addWidget(self.id)
        self.layout3.addWidget(self.status)

        self.add_b = QPushButton("Add Member")
        self.add_b.setEnabled(False)
        self.add_b.clicked.connect(self.member_fun)
        self.layout3.addWidget(self.add_b)

        
        home_btn = return_home.create_home_btn(self,stack,self.home_help)
        self.layout3.addWidget(home_btn)

    def b_add_enable(self):
        if self.first_name.text() != "" and self.last_name.text() != "" and self.id.text() != "" :
            self.add_b.setEnabled(True)
        else :
            self.add_b.setEnabled(False)

    
    def member_fun(self):
            for i in mem_list:
                if int(i.idd )== int(self.id.text()) :
                    self.msg = QMessageBox.critical(self,"error","ID already exist in members")
                    self.id.setText("")
                    return
            first_name = self.first_name.text()
            last_name = self.last_name.text()
            id = self.id.text()
            status = self.status.currentText()
            mem = club_members(first_name,last_name,id,status)
            mem_list.append(mem)
            save_mem()
            self.stack.widget(0).count()
            self.stack.widget(2).display()
            if mem in mem_list :
                self.msg =QMessageBox.information(self,"Successfully Addation","Member added successfully")
            while True:
                self.id_choice = str(random.randint(1, 100))
                duplicated = False
                for i in mem_list:
                    if i.idd == self.id_choice:
                        duplicated = True
                        break
                if not duplicated:
                    break
            self.id.setText(self.id_choice)