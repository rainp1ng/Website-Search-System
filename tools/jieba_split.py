#!/usr/bin/python
# -*- coding: utf-8 -*-#coding=utf-8
# ===========================================================
# 分词功能封装
# ===========================================================
import jieba
import jieba.posseg as pseg
from general_tools import write_file
from __init__ import debug_flag


def split_word(sentence, filename='', cut_all=True, show_nominal=False):
    split_words = ''
    if not show_nominal:
        word_list = jieba.cut(sentence, cut_all)
    else:
        word_list = pseg.cut(sentence, cut_all)
    for word in word_list:
        split_words += '%s ' % word
    if not filename == '':
        write_file(filename, split_words)
    return split_words


def split_word_only(sentence, filename='', cut_all=False, show_nominal=False):
    return split_word(sentence, filename, cut_all, show_nominal)