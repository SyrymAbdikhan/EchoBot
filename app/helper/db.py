
import sqlite3


class DB:
    def __init__(self, file='storage.db'):
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()
        self.init()
    
    def init(self):
        self.cur.execute('create table if not exists users (id int, chat_id int)')
        self.con.commit()
    
    def insert(self, user_id, chat_id):
        self.cur.execute('insert into users values (?, ?)', (user_id, chat_id))
        self.con.commit()

    def update(self, user_id, chat_id):
        self.cur.execute('update users set chat_id=? where id=?', (chat_id, user_id))
        self.con.commit()

    def select(self, user_id):
        self.cur.execute('select * from users where id=?', (user_id,))
        self.con.commit()

        res = self.cur.fetchone()
        if res is None:
            return []
        return list(res)

    def select_all(self):
        self.cur.execute('select * from users')
        self.con.commit()
        return self.cur.fetchall()
    
    def delete(self, user_id):
        self.cur.execute('delete from users where id=?', (user_id,))
        self.con.commit()
    
    def close(self):
        self.con.close()
