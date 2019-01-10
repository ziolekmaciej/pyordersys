# ! /usr/bin/env python3
# -*- coding: utf-8 -*-

#
#  Created by Maciej Ziółkowski on 09.01.2019.
#  session
#

from db import DataBase
from log import Log
from messages import pref, sess
import getpass


class Session:
    def __init__(self):
        self.db = DataBase()
        self.log = Log()
        self.connection = 0
        self.cursor = None
        self.singed_in = False
        self.name = None
        self.id = None
        self.group = None

    def sign_in(self):
        login = input('Login: ').lower()
        print(login)
        self.log.write(pref['log'], sess['log_tr'] + login)
        password = getpass.getpass('Password: ')
        if self.connected_db():
            query = "SELECT id, group_id FROM users WHERE login=%s AND password=%s"
            self.cursor.execute(query, (login, password))
            result = self.cursor.fetchone()
            if result is not None:
                self.name = login.capitalize()
                self.id, self.group = result
                self.log.write(pref['log'], self.name + sess['log_ok'] + self.group)
                print(sess['ap_wl'] + self.name + sess['ap_an'])
            else:
                self.log.write(pref['war'], sess['log_er'] + login)

    def start(self):
        self.log.write(pref['log'], sess['ap_st'])
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
            query = "SELECT * FROM users WHERE login = %s"
            self.cursor.execute(query,(self.name.lower(),))
            for data in self.cursor:
                print(data)
        else:
            self.log.write(pref['war'], sess['db_no'])


