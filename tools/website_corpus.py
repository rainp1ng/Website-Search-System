#!/usr/bin/python
# -*- coding:utf-8 -*-
################################################################
# 网站语料库处理
################################################################
import os
from bing_search import bing_search
from baidu_search import baidu_search
from jieba_split import split_word_only
from general_tools import write_file
from conf.website_conf import website_list
from __init__ import debug_flag
corpus_path = 'corpus_files/'
if __name__ != '__main__' and __name__ != 'website_corpus':
    corpus_path = 'tools/corpus_files/'


# 将搜索得到的摘要信息汇总
def get_corpus(func, website):
    result_list = func(website)
    content = ''
    for result in result_list:
        content += result['Description'] + '\n'
    return content


# 用baidu搜索获取语料信息
def get_corpus_by_baidu(website):
    return get_corpus(baidu_search, website[0])


# 用bing搜索获取语料信息
def get_corpus_by_bing(website):
    return get_corpus(bing_search, website[1])


# 获取单个网站的所有语料信息
def get_all_corpus(website):
    print '%s%s.txt' % (corpus_path, website[0])
    if os.path.exists(u'%s%s.txt' % (corpus_path, website[0])):
        return open(u'%s%s.txt' % (corpus_path, website[0]), 'rb').read()
    content = '%s\n%s' % (get_corpus_by_baidu(website), get_corpus_by_bing(website))
    split_words = split_word_only(content)
    write_file(u'%s%s.txt' % (corpus_path, website[0]), split_words, debug_flag)
    return split_words


# 获取所有网站的语料信息
def get_corpus_list(website_list):
    all_website_corpus = []
    for website in website_list:
        print website
        print website[0]
        print website[1]
        all_website_corpus.append(get_all_corpus(website))
    return all_website_corpus


if __name__ == '__main__':
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    get_corpus_list(website_list)
