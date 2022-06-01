import sqlite3
import datetime

class DataBase:

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
    def get_time(self):
        return datetime.datetime.now().strftime("%d.%m.%Y")
    def get_toshkent(self):
        return self.cursor.execute("select * from namaz where Mintaqa='Toshkent' and Sana=?",(self.get_time(),)).fetchall()
    def get_andijon(self):
        return self.cursor.execute("select * from namaz where Mintaqa='Andijon' and Sana=?",(self.get_time(),)).fetchall()
    def get_buxoro(self):
        return self.cursor.execute("select * from namaz where Mintaqa='Buxoro' and Sana=?",(self.get_time(),)).fetchall()
    def get_guliston(self):
        return self.cursor.execute("select * from namaz where Mintaqa='Guliston' and Sana=?",(self.get_time(),)).fetchall()
    def get_samarqand(self):
        return self.cursor.execute("select * from namaz where Mintaqa='Samarqand' and Sana=?",(self.get_time(),)).fetchall()
    def get_namangan(self):
        return self.cursor.execute("select * from namaz where Mintaqa='Namangan' and Sana=?",(self.get_time(),)).fetchall()
    def get_navoi(self):
        return self.cursor.execute("select * from namaz where Mintaqa='Navoiy' and Sana=?",(self.get_time(),)).fetchall()
    def get_jizzax(self):
        return self.cursor.execute("select * from namaz where Mintaqa='Jizzax' and Sana=?",(self.get_time(),)).fetchall()
    def get_nukus(self):
        return self.cursor.execute("select * from namaz where Mintaqa='Nukus' and Sana=?",(self.get_time(),)).fetchall()
    def get_qarshi(self):
        return self.cursor.execute("select * from namaz where Mintaqa='Qarshi' and Sana=?",(self.get_time(),)).fetchall()
    def get_qoqon(self):
        return self.cursor.execute('select * from namaz where Mintaqa="Qo\'qon" and Sana=?',(self.get_time(),)).fetchall()
    def get_xiva(self):
        return self.cursor.execute("select * from namaz where Mintaqa='Xiva' and Sana=?",(self.get_time(),)).fetchall()
    def get_margilon(self):
        return self.cursor.execute('select * from namaz where Mintaqa="Marg\'ilon" and Sana=?',(self.get_time(),)).fetchall()

db = DataBase('data/dataNamaz.sqlite')
