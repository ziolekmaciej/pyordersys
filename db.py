# ! /usr/bin/env python3
# -*- coding: utf-8 -*-

#
#  Created by Maciej Ziółkowski on 09.01.2019.
#  db connection
#
import mysql.connector
from config_db import config


class DataBase:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**config)
            return 1
        except mysql.connector.Error as err:
            return err.errno

    def disconnect(self):
        self.connection.close()
