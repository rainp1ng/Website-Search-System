#!/usr/bin/python
# -*- coding: utf-8 -*-
# ===========================================================
# 余弦相似度实现
# ===========================================================
import numpy as np


def get_cossimi(x, y):
    myx = x
    myy = y
    # myx = np.array(x)  # 将列表转化为数组，更好的数学理解是向量
    # myy = np.array(y)  # 将列表转化为数组，更好的数学理解是向量
    cos1 = np.sum(myx * myy)  # cos(a,b)=a*b/(|a|+|b|)
    # print 'cos1:', cos1
    cos21 = np.sqrt(sum(myx * myx))
    # print 'cos21:', cos21
    cos22 = np.sqrt(sum(myy * myy))
    # print 'cos22:', cos22
    return cos1 / (float(cos21 * cos22))


def batch_get_sort_scores(words_weight, website_list):
    question_wf = words_weight[len(words_weight) - 1]
    scores = []
    for i in range(len(website_list)):
        scores.append((website_list[i][0], get_cossimi(words_weight[i], question_wf)))
    return sorted(scores, key=lambda x: x[1], reverse=True)


def test():
    docs = [
        '我 今天 心情 很好，但是 看到 不想 看到 的 人 了',
        '我 今天 心情 很好，且 看到 想 看到 的 人 了',
        '我 今天 心情 很 不好，但是 看到 想 看到 的 人 了',
        '我 今天 心情 很 不好，且 看到 不想 看到 的 人 了',
        '我 今天 心情 很好，且 看到 想 看到 的 人 了'
    ]
    from tf_idf import tf_idf
    words, words_weight = tf_idf(docs)
    for i, x in enumerate(words_weight):
        print docs[i]
        for j, y in enumerate(words_weight[i]):
            print words[j], words_weight[i][j]
        print

    for i in range(0, 4):
        score = get_cossimi(words_weight[i], words_weight[4])
        print 'score', i, ':', score
        print


if __name__ == '__main__':

    # question = '我在哪里可以吃到海鲜意面'
    question = '怎么学好编程'

    from tf_idf import tf_idf, get_corpus_list
    from conf.website_conf import website_list
    website_corpus = get_corpus_list(website_list)
    from wikipedia_expansion import get_question_expansion_corpus
    # question_corpus = get_question_expansion_corpus(question)

    from jieba_split import split_word_only
    question_corpus = split_word_only(question)

    website_corpus.append(question_corpus)
    words, words_weight = tf_idf(website_corpus)
    scores = batch_get_sort_scores(words_weight, website_list)

    for i in scores:
        print i[0], ':', i[1]
