# ! /usr/bin/env python3
# -*- coding: utf-8 -*-

#
#  Created by Maciej Ziółkowski on 09.01.2019.
#  session
#

from db import DataBase
from log import Log
from messages import pref, sess

class Session:
    def __init__(self):
        self.db = DataBase()
        self.log = Log()
        self.connection = 0
        self.cursor = None

    def start(self):
        self.connection = self.db.connect()
        if self.connected_db():
            self.cursor = self.db.connection.cursor()
            self.log.write(pref['log'], sess['db_ok'])
        else:
            self.log.write(pref['err'], sess['db_er'] + str(self.connection))

    def connected_db(self):
        return self.connection == 1

    def end(self):
        if self.connected_db():
            self.cursor = None
            self.db.disconnect()
            self.log.write(pref['log'], sess['db_dc'])
        else:
            self.log.write(pref['war'], sess['db_no'])

    def show_rows(self):
        if self.connected_db():
            self.log.write(pref['log'], sess['db_do'])
            query = "SELECT * FROM users"
            self.cursor.execute(query)
            for data in self.cursor:
                for cell in data:
                    print(cell , end=' ')
                print()
        else:
            self.log.write(pref['war'], sess['db_no'])




