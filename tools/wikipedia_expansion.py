#!/usr/bin/python
# -*- coding: utf-8 -*-#coding=utf-8
# ===========================================================
# 维基百科词义拓展功能封装
# ===========================================================
import wikipedia
__author__ = 'rainp1ng'


def get_content(page):
    # wikipedia.set_lang('zh')
    if '\n\n' in page.content:
        content = page.content.split('\n\n')[0]
    else:
        content = page.content.split('\r\n\r\n')[0]
    return content


def search(word):
    wikipedia.set_lang('zh')
    return wikipedia.page(word)


def expand(word):
    p = search(word)
    return get_content(p)


def main():
    wikipedia.set_lang('zh')
    print '===================================search========================================='
    s = wikipedia.search('NBA')
    for i in s:
        print i
    print '================================== page  ========================================='
    p = wikipedia.page('NBA')
    print p
    print '================================== title  ========================================='
    print p.title
    print '================================== url  ========================================='
    print p.url
    print '================================== content  ========================================='
    print p.content
    print '================================== link  ========================================='
    print p.links[0]

    t = wikipedia.summary('China', sentences=1)


if __name__ == '__main__':
    main()
    print search('朱德')
