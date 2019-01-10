# ! /usr/bin/env python3
# -*- coding: utf-8 -*-

#
#  Created by Maciej Ziółkowski on 09.01.2019.
#  generate logs
#

import datetime


def log_file_path():
    file_name = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M")
    directory = 'logs/'
    file_format = '.log'
    return directory + file_name + file_format


def get_time():
    return datetime.datetime.now().strftime('%H:%M:%S') + ' '


class Log:
    def __init__(self):
        self.file_name = log_file_path()
        self.logfile = open(self.file_name, 'w')
        self.logfile.write('ORDERING SYSTEM BY MACIEJ ZIÓŁKOWSKI' + '\n\n')
        self.logfile.write('<-------  STARTING LOGGING  ------->' + '\n')
        self.logfile.close()

    def write(self, prefix, message):
        self.logfile = open(self.file_name, 'a')
        self.logfile.write(prefix + get_time() + message + '\n')
        self.logfile.close()



