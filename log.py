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
    return datetime.datetime.now().strftime('%H:%M') + ' '


class Log:
    def __init__(self):
        self.logfile = open(log_file_path(), 'w')
        self.logfile.write('<---  STARTING LOGGING  --->' + '\n')

    def __del__(self):
        if not self.logfile.closed:
            self.end()

    def end(self):
        self.logfile.close()

    def write(self, prefix, message):
        self.logfile.write(prefix + get_time() + message + '\n')



