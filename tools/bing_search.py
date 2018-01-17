#!/usr/bin/python
# -*- coding: utf-8 -*-
# ===========================================================
# bing搜索api封装
# ===========================================================
import os
import json
import urllib
from __init__ import debug_flag
from general_tools import write_file
from http_tools import gunzip, get, post
__author__ = 'rainp1ng'
bing_api_key = 'tVlMo0Nl9mCm0xMMtEFB1GFv2cXKcwUsvNVouFcyTqs'
html_path = 'html_files/bing/'
if __name__ != '__main__' and __name__ != 'bing_search':
    html_path = 'tools/' + html_path


def bing_search(query, pages=10, search_type='Web'):
    if os.path.exists('%ssearch_result_%s.html' % (html_path, query.replace('/', '_'))):
        res = open('%ssearch_result_%s.html' % (html_path, query.replace('/', '_')), 'rb').read()
        data = json.loads(res)
        return data['d']['results']
    query = urllib.quote(query)
    credentials = (':%s' % bing_api_key).encode('base64')[:-1]
    authorrization = 'Basic %s' % credentials
    search_url = 'https://api.datamarket.azure.com/Bing/Search/v1/' \
                 '%(search_type)s?Query=%%27%(query)s%%27&$top=%(number)s&$format=json' % \
    {
        'search_type': search_type, 'query': query, 'number': pages*10
    }
    headers = {
        'Authorization': authorrization,
    }
    res = gunzip(get(search_url, headers).read())
    write_file('%ssearch_result_%s.html' % (html_path, query.replace('/', '_')), res, True)
    data = json.loads(res)
    return data['d']['results']



