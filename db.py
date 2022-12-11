import sqlite3


class BotDB:

    def __init__(self):
        self.conn = sqlite3.connect('Film.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

    # def add_comedy(self):
    #     self.cursor.execute('INSERT')
