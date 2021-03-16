import mysql.connector as ms


class DBConnect:
    def __init__(self):
        self.con = ms.connect(host='localhost', user='Kyser',
                              password='Sarthak1', database='user')
        self.cur = self.con.cursor()

    def insert(self, query,values):
        self.cur.execute(query,values)
        self.con.commit()

    def delete(self, query,values):
        self.cur.execute(query,values)
        self.con.commit()
    def select(self,query,values):
        self.cur.execute(query,values)
        self.con.commit()

    def update(self,query,values):
        self.cur.execute(query,values)
        self.con.commit()

    def read(self, query,values):
        self.cur.execute(query,values)
        self.con.commit()




