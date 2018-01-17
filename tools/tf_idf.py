#!/usr/bin/python
# -*- coding: utf-8 -*-
# ===========================================================
# tf-idf词语权重计算封装
# ===========================================================
import json
from __init__ import debug_flag
from general_tools import write_file
from bing_search import bing_search
from jieba_split import split_word
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer


def tf_idf(split_words_list):
    vectorizer = CountVectorizer()  # 将词语生成词频矩阵的类
    transformer = TfidfTransformer()  # 计算词语权重的类
    words_frequency = vectorizer.fit_transform(split_words_list)
    tfidf = transformer.fit_transform(words_frequency)
    words = vectorizer.get_feature_names()  # 获取不重复的所有词语
    words_weight = tfidf.toarray()  # 词语权重
    # for i in range(len(words_weight)):
    #     for j in range(len(word_list)):
    #         print word_list[j], words_weight[i][j]
    return words, words_weight


if __name__ == '__main__':
    docs = [
        '我 今天 心情 很好，但是 看到 不想 看到 的 人 了',
        '我 今天 心情 很好，且 看到 想 看到 的 人 了',
        '我 今天 心情 很 不好，但是 看到 想 看到 的 人 了',
        '我 今天 心情 很 不好，且 看到 不想 看到 的 人 了',
    ]
    words, words_weight = tf_idf(docs)
    for i, x in enumerate(words_weight):
        for j, y in enumerate(words_weight[i]):
            print words_weight[i][j]

