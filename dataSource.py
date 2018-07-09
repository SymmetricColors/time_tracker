import sqlite3


# c.execute(''' create table dates(date text , startTime text , finishTime text, duration real,
#              project text , persianDate )''')

class DataSource():
    def __init__(self,dbname):
        self.conn = sqlite3.connect(dbname)
        self.c = self.conn.cursor()
    def get_data(self,projec_name):
        self.c.execute('select * from dates where project ==')
    def insert_data(self,date):
        self.c.execute('insert into dates values (?,?,?,?,?,? );',date)
        self.conn.commit()
        self.conn.close()
