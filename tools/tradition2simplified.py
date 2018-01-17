#!/usr/bin/python
# -*- coding: utf-8 -*-#coding=utf-8
# ===========================================================
# 分词功能封装
# ===========================================================
import pyopencc as opencc
__author__ = 'zhuyuping'


def t2s(sentences):
    cc = opencc.OpenCC('zht2zhs.ini')
    return cc.convert(sentences)


def s2t(sentences):
    cc = opencc.OpenCC('zhs2zht.ini')
    return cc.convert(sentences)


if __name__ == '__main__':
    print t2s('我')
