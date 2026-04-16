from PySide6.QtWidgets import (QWidget,QLabel,QPushButton,QVBoxLayout
                               ,QHBoxLayout,QLineEdit,QMessageBox)
from PySide6.QtCore import QSize,Qt
from PySide6.QtGui import QIntValidator
from .utilities import create_home_btn,save_mem
from models import mem_list


class deletepage(QWidget):
    def __init__(self,stack):
            super().__init__()
            self.stack = stack
            self.layout1 =QVBoxLayout()
            self.layout2 = QHBoxLayout()
            self.setLayout(self.layout1)
            
            self.label1 = QLabel("Enter member ID")
            self.line = QLineEdit()
            self.line.setValidator(QIntValidator())
            self.delete_btn = QPushButton("Delete member")
            self.delete_btn.clicked.connect(self.delete)
            self.line.setPlaceholderText("Enter member ID")
            self.line.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            
            self.layout1.addLayout(self.layout2)
            self.layout2.addWidget(self.label1)
            self.layout2.addWidget(self.line)
            self.layout1.addWidget(self.delete_btn)
            self.layout1.addStretch(10)




            home_btn = create_home_btn(self.stack)
            self.layout1.addWidget(home_btn)
    def delete(self):
        if mem_list:
            text = self.line.text()
            found = None
            for i in mem_list:
                if i.idd == text :
                    mem_list.remove(i)
                    save_mem()
                    self.stack.widget(2).display()
                    self.stack.widget(0).count()
                    self.msg1 = QMessageBox.information(self,"Delete member","Member deleted successfully")
                    found = i
                    break
            if not found :
                self.msg2 = QMessageBox.critical(self,"Failed delete","no member found with this ID")
        else :
            self.msg2 = QMessageBox.critical(self,"Failed delete","Member list is Empty")
        