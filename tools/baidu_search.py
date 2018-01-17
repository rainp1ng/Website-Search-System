#!/usr/bin/python
# -*- coding: utf-8 -*-
# ===========================================================
# baidu搜索api封装
# ===========================================================
import re
import os
import json
import urllib
import traceback
from __init__ import debug_flag
from general_tools import write_file
from http_tools import gunzip, get
__author__ = 'rainp1ng'
html_path = 'html_files/baidu/'
if __name__ != '__main__' and __name__ != 'baidu_search':
    html_path = 'tools/' + html_path


def catch_div_content(content):
    index_div_start = content.find('<div')
    index_div_end = content.find('</div')
    while index_div_start < index_div_end:
        index_div_start = content.find('<div', index_div_start+len('<div'))
        index_div_end = content.find('</div', index_div_end+len('</div'))
    return index_div_end


def get_target_url(origin_url):
    try:
        return re.findall('window\.location\.replace\("([\s\S]+?)"\)', gunzip(get(origin_url).read()))[0]
    except Exception, e:
        traceback.print_exc()
        return origin_url


def get_result_list(crawl_content, key='<div class="result'):
    index = crawl_content.find(key)
    result_list = []
    while index != -1:
        crawl_content = crawl_content[index+len(key):].strip()
        index_div_end = catch_div_content(crawl_content)
        result_content = re.sub('<!--[^<>]+>', '', crawl_content[:index_div_end])
        final_content = result_content.strip()
        result_list.append(final_content)
        index = crawl_content.find(key)
    return result_list


def find_url_and_title(material):
    try:
        res = re.findall('<h3[\s\S]+?href\s{0,}=\s{0,}[\'"]([\s\S]+?)[\'"][\s\S]+?>([\s\S]+?)</a>', material)
        url, title = res[0]
        title = re.sub('<[\s\S]+?>', '', title)
        # url = get_target_url(url)
        return url, title
    except Exception, e:
        traceback.print_exc()
        return '', ''


def find_description(material):
    try:
        res = get_result_list(material, '<div class="c-abstract">')[0]
        res = re.sub('<[\s\S]+?>', '', res)
    except Exception, e:
        res = ''
    return res


def find_id(material):
    try:
        res = re.findall('\sid="(\d+)"', material)
        if len(res) == 1:
            return res[0]
        else:
            print '匹配了多个id，先取第一个，请修复! ids:',res
            return res[0]
    except Exception, e:
        traceback.print_exc()
        return ''


def find_elems(material):
    data = {}
    data['ID'] = find_id(material)
    data['Url'], data['Title'] = find_url_and_title(material)
    data['Description'] = find_description(material)
    return data


def batch_find_elems(result_materials):
    return map(find_elems, result_materials)


def baidu_search_single_search(query, page=0, search_type='Web'):
    query = urllib.quote(query)
    url = 'https://www.baidu.com/' \
          's?wd=%(query)s&rsv_spt=1&pn=%(from_record)s&' \
          'rsv_iqid=0xbf0fbc710099c56a&' \
          'issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&inputT=1647' % {
        'query': query,
        'from_record': page * 10,
    }
    res = gunzip(get(url).read())
    index = res.find('<div id="content_left">')
    result_materials = get_result_list(res[index:])
    result_list = batch_find_elems(result_materials)
    # [{'ID': ID, 'Title': Title, 'Url': Url, 'Description': Description}, ...]
    return result_list


def baidu_search(query, pages=10, search_type='Web'):
    if os.path.exists(u'%ssearch_result_%s.html' % (html_path, query.replace('/', '_'))):
        res = open(u'%ssearch_result_%s.html' % (html_path, query.replace('/', '_')), 'rb').read()
        data = json.loads(res)
        return data
    result_list = []
    for page in range(pages):
        result_list += baidu_search_single_search(query, page, search_type)
    res = json.dumps(result_list)
    write_file(u'%ssearch_result_%s.html' % (html_path, query.replace('/', '_')), res, True)
    return result_list


if __name__ == '__main__':
    print baidu_search('豆瓣')
