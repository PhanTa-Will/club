from PySide6.QtWidgets import (QWidget,QLabel,QPushButton,QVBoxLayout,QComboBox
                               ,QHBoxLayout,QLineEdit,QMessageBox,QSpacerItem,QSizePolicy)
from PySide6.QtCore import QSize,Qt
from PySide6.QtGui import QIntValidator
from .utilities import create_home_btn,save_mem
from models import mem_list




class editpage(QWidget):
    def __init__(self,stack):
        super().__init__()
        self.stack = stack
        self.layout1 =QVBoxLayout()
        self.layout2 = QHBoxLayout()
        self.setLayout(self.layout1)
        
        self.label1 = QLabel("Enter member ID")
        self.line = QLineEdit()
        self.line.textChanged.connect(self.clear_widgets)
        self.line.setValidator(QIntValidator())
        self.find_btn = QPushButton("Find member")
        self.find_btn.setFixedSize(QSize(100,20))
        self.find_btn.clicked.connect(self.find)
        self.line.setPlaceholderText("Enter member ID")
        self.line.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        self.layout1.addLayout(self.layout2)
        self.layout2.addWidget(self.label1)
        self.layout2.addWidget(self.line)
        self.layout1.addWidget(self.find_btn,alignment=Qt.AlignmentFlag.AlignRight)
        self.spacer =QSpacerItem(20,40,QSizePolicy.Minimum,QSizePolicy.Expanding)
        self.layout1.addSpacerItem(self.spacer)
        home_btn = create_home_btn(self.stack)
        self.layout1.addWidget(home_btn)

        self.edit_widgets_list = []
    def find(self):
        if mem_list:
            text = self.line.text()
            self.edit_mem = None
            for i in mem_list:
                if i.idd == text :
                    self.line1 = QLineEdit(i.first_name)
                    self.line1.setPlaceholderText("First name")
                    self.line2 = QLineEdit(i.last_name)
                    self.line2.setPlaceholderText("Last name")
                    self.line3 = QLineEdit(i.idd)
                    self.line3.setEnabled(False)
                    self.line4 = QComboBox()
                    self.line4.addItems(["Inactive","Active"])
                    self.line4.setCurrentText(i.status)
                    self.line4.setPlaceholderText("Status")
                    edit_btn = QPushButton("Edit")
                    edit_btn.setFixedSize(QSize(100,30))
                    edit_btn.clicked.connect(self.edit)

                    index = self.layout1.indexOf(self.spacer)
                    for w in (edit_btn,self.line4,self.line3,self.line2,self.line1,):
                        self.layout1.insertWidget(index,w)
                        self.edit_widgets_list.append(w)

                    self.edit_mem = i
                    break

            if not self.edit_mem :
                self.msg2 = QMessageBox.critical(self,"Member not found","no member found with this ID")
                return
    def clear_widgets(self):
        for i in self.edit_widgets_list:
            i.setParent(None)
        self.edit_widgets_list.clear()
        

    def edit(self):
        
        edit_q = QMessageBox.question(self,"Edit member","Are you sure ?")
        
        if edit_q == QMessageBox.Yes :
            self.edit_mem.first_name = self.line1.text()
            self.edit_mem.last_name = self.line2.text()
            self.edit_mem.status = self.line4.currentText()
            save_mem()
            msg = QMessageBox.information(self,"Edit member","member edited successfully")
