#!/usr/bin/python
# -*- coding: utf-8 -*-
# ===========================================================
# 百度百科词义拓展功能封装
# ===========================================================
import urllib
from http_tools import get, gunzip
__author__ = 'rainp1ng'


def search(word):
    search_url = 'https://baike.baidu.com/search/word?word=%s' % urllib.quote(word)
    response = get(search_url)
    content = response.read()
    headers = response.headers
    print content
    print
    print headers
    return content


if __name__ == '__main__':
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    search('爱情')