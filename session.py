# ! /usr/bin/env python3
# -*- coding: utf-8 -*-

#
#  Created by Maciej Ziółkowski on 09.01.2019.
#  session
#
from db import DataBase


class Session:
    def __init__(self):
        self.db = DataBase()
        self.connection = 0
        self.cursor = None

    def start(self):
        self.connection = self.db.connect()
        if self.connection == 1:
            self.cursor = self.db.connection.cursor()
            print("Connected to db")
        else:
            print("Error with db, error number = ", self.connection)

    def end(self):
        if self.connection == 1:
            self.cursor = None
            self.db.disconnect()
            print("Disconnected from db")
        else:
            print("I was not connected to db")

    def show_rows(self):
        query = "SELECT * FROM users"
        self.cursor.execute(query)
        for data in self.cursor:
            print(data[0:2])




