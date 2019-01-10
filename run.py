# ! /usr/bin/env python3
# -*- coding: utf-8 -*-

#
#  Created by Maciej Ziółkowski on 09.01.2019.
#  running script
#

from session import Session

if __name__ == "__main__":
    session = Session()
    session.start()
    session.sign_in()
    session.show_rows()

