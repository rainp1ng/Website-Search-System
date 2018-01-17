#!/usr/bin/python
# -*- coding: utf-8 -*-
# ===========================================================
# 主程序入口
# ===========================================================
import sys
from __init__ import debug_flag
from flask_server.server import server


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    server.run(port=8018, debug=debug_flag)
