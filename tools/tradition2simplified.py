#!/usr/bin/python
# -*- coding: utf-8 -*-#coding=utf-8
# ===========================================================
# 分词功能封装
# ===========================================================
import opencc
__author__ = 'zhuyuping'


def t2s(sentences):
    cc = opencc.OpenCC('t2s')
    return cc.convert(sentences)


def s2t(sentences):
    cc = opencc.OpenCC('s2t')
    return cc.convert(sentences)
