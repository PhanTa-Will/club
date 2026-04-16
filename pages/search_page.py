from PySide6.QtWidgets import (QWidget,QLabel,QPushButton,QVBoxLayout,QMessageBox
                               ,QHBoxLayout,QStackedWidget,QLineEdit,QSpacerItem,QSizePolicy,QTableWidget,QTableWidgetItem)
from PySide6.QtCore import QSize,Qt
from pages.utilities import create_home_btn
from models import mem_list





class searchpage(QWidget):
    def __init__(self,stack):
        super().__init__()
        self.stack = stack  #type: QStackedWidget
        self.setMinimumSize(QSize(320,300))
        self.layout5 = QVBoxLayout()
        self.setLayout(self.layout5)
        self.h_layout = QHBoxLayout()
        self.layout5.addLayout(self.h_layout)



        self.label = QLabel("search: ")
        self.l_search = QLineEdit()
        self.l_search.setPlaceholderText("Enter Name or ID")
        self.l_search.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.l_search.textChanged.connect(self.clear_search)
        self.h_layout.addWidget(self.label)
        self.h_layout.addWidget(self.l_search)

        self.search_btn = QPushButton("Search")
        self.search_btn.setFixedSize(QSize(150,30))
        self.search_btn.clicked.connect(self.search)
        self.layout5.addWidget(self.search_btn,0,alignment=Qt.AlignmentFlag.AlignRight)
        
        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)     #expanding area
        self.layout5.addSpacerItem(self.spacer)

        self.new_layout = QHBoxLayout()
        self.layout5.addLayout(self.new_layout)
        self.edit_btn = QPushButton("Edit member")
        self.edit_btn.clicked.connect(self.move_edit)
        self.delete_btn = QPushButton("Delete member")
        self.delete_btn.clicked.connect(self.move_delete)
        self.new_layout.addWidget(self.edit_btn)
        self.new_layout.addWidget(self.delete_btn)
        home_btn = create_home_btn(self.stack)
        self.layout5.addWidget(home_btn)

        self.search_list =[]
        
    def search(self):
        text = self.l_search.text()
        for label in self.search_list :
            label.setParent(None)
            label.deleteLater()             

        self.search_list.clear()
        search_result = []    
        for i in mem_list:
            if text in i.first_name or text in i.last_name or text == i.status or text == i.idd :
                search_result.append(i)
        if search_result:
            result_table = QTableWidget()
            result_table.setHorizontalHeaderLabels(["First name","Last name","ID","Status"])
            result_table.setColumnCount(4)
            result_table.setRowCount(len(search_result))
            result_table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
            for row,i in enumerate(search_result):
                result_table.setItem(row,0,QTableWidgetItem(i.first_name))
                result_table.setItem(row,1,QTableWidgetItem(i.last_name))
                result_table.setItem(row,2,QTableWidgetItem(i.idd))
                result_table.setItem(row,3,QTableWidgetItem(i.status))
            spacer_index = self.layout5.indexOf(self.spacer)
            self.layout5.insertWidget(spacer_index,result_table)
            self.search_list.append(result_table)
        if not search_result:
            msg = QMessageBox.critical(self,"failed","No members found") 
        
               
    def clear_search(self):
        self.search_btn.setEnabled(True)
        for i in self.search_list :
            i.setText("")

    def move_edit(self):
        self.stack.setCurrentIndex(4) 
    def move_delete(self):
        self.stack.setCurrentIndex(5)            


