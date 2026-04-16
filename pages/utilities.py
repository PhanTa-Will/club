from PySide6.QtWidgets import QPushButton,QWidget
from PySide6.QtCore import QSize,Signal
from PySide6.QtGui import QIcon
import json 
import os
import models
import sqlite3

def save_mem():
    file = sqlite3.connect("member.db")
    cur = file.cursor()

    cur.execute("DROP TABLE IF EXISTS members")

    # إنشاء الجدول لو مش موجود فقط
    cur.execute("""
    CREATE TABLE IF NOT EXISTS members(
        firstname TEXT,
        lastname TEXT,
        id TEXT,
        status TEXT
    )
    """)

   

    new_list = []
    if models.mem_list:
        for mem in models.mem_list:
            new_list.append((mem.first_name, mem.last_name, mem.idd, mem.status))

        cur.executemany("INSERT INTO members VALUES (?,?,?,?)", new_list)
    
    file.commit()
    file.close()
    print("mem saved successfully")
    
    
def load_mem():

    file = sqlite3.connect("member.db")
    cur = file.cursor()

    # 1) التأكد من أن جدول members موجود
    cur.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name='members'
    """)
    table_exists = cur.fetchone()

    if not table_exists:
        models.models.mem_list = []   # الجدول مش موجود → رجّع ليست فاضية
        file.close()
        return

    # 2) قراءة البيانات من الجدول
    cur.execute("SELECT firstname, lastname, id, status FROM members")
    rows = cur.fetchall()

    # 3) تفريغ الليست قبل إعادة التحميل
    models.mem_list = []

    # 4) تحويل كل صف إلى instance
    for first, last, idd, status in rows:
        mem = models.club_members(first, last, idd, status)
        models.mem_list.append(mem)

    file.close()
    print("mem loaded successfully")
    print(models.mem_list)


class return_home(QWidget):
    go_home = Signal()
    def __init__(self):
        super().__init__()
    def create_home_btn(self,stack,go_home):
        home_btn = QPushButton()                       #return Home Button
        home_btn.setFixedSize(25,25)
        home_btn.setIcon(QIcon("icons/club.png"))
        home_btn.setIconSize(QSize(30,30))
        home_btn.setToolTip("return Home")
        def home():
            stack.setCurrentIndex(0)
            if go_home:
                self.go_home.emit()
                
        home_btn.clicked.connect(home)
        return home_btn