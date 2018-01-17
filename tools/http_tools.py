#!/usr/bin/python
# -*- coding: utf-8 -*-
# ===========================================================
# http请求功能封装
# ===========================================================
import re
import gzip
import urllib
import urllib2
import traceback
from __init__ import debug_flag
from StringIO import StringIO


class Response(object):
    def __init__(self, content):
        self.message = content

    def read(self):
        return self.message


def get(url, option_headers={}, timeout=15, try_time=7):
    if debug_flag:
        print url
    headers = set_host(get_headers(), url)
    for option in option_headers:
        headers[option] = option_headers[option]
    success = False
    res = Response("Running out time !")
    c = 0
    while not success and c < try_time:
        try:
            req = urllib2.Request(url, headers=headers)
            res = urllib2.urlopen(req, timeout=timeout)
            success = True
        except Exception, e:
            success = False
            traceback.print_exc()
            c += 1
    return res


def post(url, data, option_headers={}, timeout=15, try_time=7):
    if debug_flag:
        print url
    data_urlencode = urllib.urlencode(data)
    headers = set_host(get_headers(), url)
    if headers != '':
        for option in option_headers:
            headers[option] = option_headers[option]
    success = False
    res = Response("Running out time !")
    c = 0
    while not success and c < try_time:
        try:
            req = urllib2.Request(url, data_urlencode, headers=headers)
            res = urllib2.urlopen(req, timeout=timeout)
            success = True
        except Exception, e:
            success = False
            traceback.print_exc()
            c += 1
    return res


def gunzip(content):
    return gzip.GzipFile(fileobj=StringIO(content)).read()


def get_headers():
        return {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip,deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cache-Control": "max-age=0",
        }


def set_host(headers, url):
        host = re.findall('https?://([^/]+)/', url)
        if len(host) > 0:
            headers['Host'] = host[0]
        else:
            headers['Host'] = 'weibo.com'
        return headers