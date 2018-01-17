#!/usr/bin/python
# -*- coding: utf-8 -*-
# ===========================================================
# 逻辑功能封装
# ===========================================================
from __init__ import debug_flag


# 核心函数，输入问题，得到最终得分前五的网站
def get_top_n_website_scores(question, n=5):
    from tf_idf import tf_idf, get_corpus_list
    from conf.website_conf import website_list
    from jieba_split import split_word_only
    from cosine import batch_get_sort_scores
    from wikipedia_expansion import get_question_expansion_corpus

    if debug_flag:
        print 'question:', question

    website_corpus = get_corpus_list(website_list)
    question_corpus = get_question_expansion_corpus(question)
    # question_corpus = split_word_only(question)
    website_corpus.append(question_corpus)
    words, words_weight = tf_idf(website_corpus)

    return batch_get_sort_scores(words_weight, website_list)[0:n]


# 废弃
def move_repeat(l):
    new_l = []
    for i in l:
        if new_l.count(i) < 1:
             new_l.append(i)
    return new_l


# 内容content保存成文件filename
def write_file(filename, content, debug_flag=False):
    if debug_flag:
        file = open(filename, 'wb')
        file.write(content)
        file.close()


#　废弃
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
    scores = get_top_n_website_scores('我怎么才能学好C++')
    for i in scores:
        print i[0], ':', i[1]