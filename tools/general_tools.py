#!/usr/bin/python
# -*- coding: utf-8 -*-
# ===========================================================
# 逻辑功能封装
# ===========================================================
from __init__ import debug_flag


def move_repeat(l):
    new_l = []
    for i in l:
        if new_l.count(i) < 1:
             new_l.append(i)
    return new_l


def write_file(filename, content, debug_flag=False):
    if debug_flag:
        file = open(filename, 'wb')
        file.write(content)
        file.close()


def get_website_scores(question):
    from tf_idf import tf_idf
    from conf.website_conf import website_list
    from website_corpus import get_corpus_list
    # 获取网站的语料库
    corpus_list = get_corpus_list(website_list)
    words, word_weights = tf_idf(corpus_list)
    for i in range(len(word_weights)):
        for j in range(len(words)):
            print words[j], word_weights[i][j]


if __name__ == '__main__':
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    get_website_scores('我怎么才能学好C++')