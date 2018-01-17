#!/usr/bin/python
# -*- coding: utf-8 -*-#coding=utf-8
# ===========================================================
# 维基百科词义拓展功能封装
# ===========================================================
import os
import wikipedia
import traceback
from tradition2simplified import t2s
from jieba_split import split_word_only
from general_tools import write_file
from __init__ import debug_flag
__author__ = 'rainp1ng'
corpus_path = 'searched_questions/'
expanded_words_path = 'expanded_words/'
if __name__ != '__main__' and __name__ != 'wikipedia_expansion':
    corpus_path = 'tools/searched_questions/'
    expanded_words_path = 'tools/expanded_words/'


# 将wiki搜索结果的content取出
def get_content(page):
    # wikipedia.set_lang('zh')
    try:
        if '\n\n' in page.content:
            content = page.content.split('\n\n')[0]
        else:
            content = page.content.split('\r\n\r\n')[0]
        return content
    except Exception, e:
        traceback.print_exc()
        return page


# 使用维基百科api获取词的百科信息
def search(word):
    if debug_flag:
        print 'wiki searching ... '
    wikipedia.set_lang('zh')
    try:
        return wikipedia.page(word)
    except Exception, e:
        traceback.print_exc()
        print 'something wrong ... '
        return word


# 对词语进行拓展
def expand(word):
    file_path = u'%s%s' % (expanded_words_path, word)
    if os.path.exists(file_path):
        return open(file_path, 'rb').read()
    if debug_flag:
        print 'wiki expanding ... '
    p = search(word)
    content = get_content(p)
    write_file(file_path, content, True)
    return content


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


# 获取问题拓展后分词的语料库
def get_question_expansion_corpus(question):
    # file_path = u'%s%s' % (corpus_path, question)
    # if os.path.exists(file_path):
    #     return open(file_path, 'rb').read()
    words_list = split_word_only(question).split(' ')
    if debug_flag:
        sentence = u''
        for word in words_list:
            sentence += ' %s' % word
        print sentence
    expand_list = ''
    for word in words_list:
        if word.strip() == '':
            continue
        if debug_flag:
            print 'expanding %s ...' % word
        expand_sentences = '%s ' % t2s(expand(word))
        if debug_flag:
            print 'expansion:', expand_sentences
        expand_list += expand_sentences
    if debug_flag:
        print 'done expansion'
    expand_corpus = split_word_only(expand_list)
    # write_file(question, expand_corpus, True)
    return expand_corpus


if __name__ == '__main__':
    main()
    # s = u'haha哈哈'
    # ss = '%s ' % s
    # sss = '哈哈' + ss
    # print sss
    # print type(ss)
    # print ss
    # print type(s)
    # print s
    # exit(0)
    # expasion = search('C++')
    # print 'search done'
    # print 'expansion:', expasion
    # print 'content:', expasion.content
    # print 'done print'
    # expasion = expand('朱德')
    # print type(expasion)
    # print expasion
    # print get_question_expansion_corpus('我在哪里可以吃到海鲜意面')
    # wikipedia.set_lang('zh')
    # s = wikipedia.page('我')
    # print s
    # print s.title
    # print s.content
    # print s.url