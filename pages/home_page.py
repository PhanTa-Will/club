from PySide6.QtWidgets import (QWidget,QLabel,QPushButton,QVBoxLayout
                               ,QHBoxLayout,QStackedWidget,QApplication,QLineEdit,QLCDNumber,QSizePolicy)
from PySide6.QtCore import Qt,QSize,Signal
from PySide6.QtGui import QPixmap
from models import mem_list

#main Page
class win(QWidget):
    go_main = Signal()
    def __init__(self,stack):
        super().__init__()
        self.stack = stack #type: QStackedWidget
        
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setStyleSheet("background-color: yellow;")
# Labels
        welcome_msg = QLabel("Welcome to club Management app")
        welcome_msg.setStyleSheet("""color:red;
                                  font-size: 28px;
                                  font-weight: Bold;
                                  font-style: italic;""")
        image_lbl = QLabel()
        image_lbl.setPixmap(QPixmap("icons/club.png"))
        image_lbl.setScaledContents(True)
        image_lbl.lower()

        self.layout_v = QVBoxLayout()
        self.setLayout(self.layout_v)
        self.layout_v.addWidget(welcome_msg,0,alignment=Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)
        self.layout_v.addWidget(image_lbl)
        
        self.mem_count_lbl = QLabel("current members: ")
        self.mem_count_lbl.setStyleSheet("""font-size: 20px;
                                            font-style: italic;
                                            font-weight: Bold;""")
        self.mem_count_lbl.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Preferred)
        self.mem_count_line = QLCDNumber()
        self.mem_count_line.setDigitCount(3)
        self.mem_count_line.display(str(len(mem_list)))
        self.mem_count_line.setSegmentStyle(QLCDNumber.Filled)
        self.mem_count_line.setStyleSheet("color:red;")
        
        self.mem_count_line.setFixedSize(100,30)
        self.h_out = QHBoxLayout()
        self.h_out.addWidget(self.mem_count_lbl,0,alignment=Qt.AlignmentFlag.AlignVCenter|Qt.AlignmentFlag.AlignLeft)
        self.h_out.addWidget(self.mem_count_line,0,alignment=Qt.AlignmentFlag.AlignVCenter|Qt.AlignmentFlag.AlignRight)
        self.layout_v.addLayout(self.h_out)

       
        
        
# Main BUTTONS
        b1 = QPushButton("Add member")
        b1.clicked.connect(self.add_mem)
        b1.clicked.connect(lambda:self.go_main.emit())
        b2 = QPushButton("View members")
        b2.clicked.connect(self.view_mem)
        b3 = QPushButton("search member")
        b3.clicked.connect(self.search_mem)
        b4 = QPushButton("Exit")
        b4.clicked.connect(self.exit_b)

        self.layout_h = QHBoxLayout()
        button_list = [b1,b2,b3,b4]
        for b in button_list:
            self.layout_h.addWidget(b)
            b.setStyleSheet("font-size: 11px; font-weight:Bold; font-style:italic;")
        
        self.layout_v.addLayout(self.layout_h)

    def count(self):
        self.mem_count_line.display(str(len(mem_list)))
        
    def add_mem(self):
        self.stack.setCurrentIndex(1)
        
        

    def view_mem(self):
        self.stack.setCurrentIndex(2)
        self.stack.widget(2).display()
        
        
    def search_mem(self):
        self.stack.setCurrentIndex(3)
        
        
    def home(self):
        self.stack.setCurrentIndex(0)    

    def exit_b(self):
        QApplication.quit()

