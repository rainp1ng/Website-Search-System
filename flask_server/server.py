#!/usr/bin/python
# -*- coding:utf-8 -*-
################################################################
# 服务器程序
################################################################
import json
import time
import sys
from flask import Flask, abort, render_template, redirect, send_from_directory, request, make_response
from flask.ext.bootstrap import Bootstrap
sys.path.append('..')
from tools.conf.website_conf import website_list, website_link
from tools.general_tools import get_top_n_website_scores


server = Flask(__name__)
bootstrap = Bootstrap(server)


def generate_result(scores):
    result_list = []
    for score in scores:
        result = {}
        result['website'] = score[0]
        result['score'] = '%.3f' % (score[1] * 100)
        result['link'] = website_link[score[0]][0]
        result['type'] = website_link[score[0]][1]
        result_list.append(result)
    return result_list  # sorted(result_list, key=lambda x: x['score'], reverse=True)


@server.route('/')
def hello():
    return render_template('index.html')


@server.route('/static/<path:path>')
def send_static_file(path):
    return send_from_directory('static', path)


# 前期演示用
STACKOVERFLOW = {'website': 'Stack Overflow', 'link': 'http://stackoverflow.com/', 'score': 88.7, 'type': '技术问答社区'}
ZHIHU = {'website': '知乎', 'link': 'http://www.zhihu.com/', 'score': 68.7, 'type': '技术生活问答社区'}
CSDN = {'website': 'CSDN', 'link': 'http://www.csdn.net/', 'score': 78.4, 'type': '技术讨论论坛'}
TIANYA = {'website': '天涯', 'link': 'http://www.tianya.cn/', 'score': 48.0, 'type': '闲聊网站论坛'}
HUASHENG = {'website': '华声论坛', 'link': 'http://bbs.voc.com.cn/', 'score': 58.2, 'type': '闲聊网站论坛'}  # rank: 0, 1, 2, 3, 4
HOOPCHINA = {'website': '虎扑中国', 'link': 'http://bbs.voc.com.cn/', 'score': 58.2, 'type': '闲聊网站论坛'}  # rank: 0, 1, 2, 3, 4
test = {
    '计算机': {'stat': '200', 'result': [ZHIHU, CSDN, STACKOVERFLOW]},
    'C++': {'stat': '200', 'result': [ZHIHU, CSDN, STACKOVERFLOW]},
    'JAVA': {'stat': '200', 'result': [ZHIHU, CSDN, STACKOVERFLOW]},
    '抢劫': {'stat': '200', 'result': [HUASHENG, ZHIHU, TIANYA]},
    '厨房': {'stat': '200', 'result': [HUASHENG, ZHIHU, TIANYA]},
    '花': {'stat': '200', 'result': [HUASHENG, ZHIHU, TIANYA]},
    '做饭': {'stat': '200', 'result': [HUASHENG, ZHIHU, TIANYA]},
}


@server.route('/search/<question>')
def ask_question(question):
    # words = split_word(question).strip().split(' ')
    # print words
    # time.sleep(1)
    # for i in test:
    #     for word in words:
    #         if word in i:
    #             test[i]['result'] = sorted(test[i]['result'], key=lambda x: x['score'], reverse=True)
    #             return json.dumps(test[i])
    try:
        scores = get_top_n_website_scores(question)
        result_list = generate_result(scores)
        return json.dumps({'stat': '200', 'result': result_list})
    except Exception, e:
        import traceback
        traceback.print_exc()
        return json.dumps({'stat': '404'})


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    server.run(host="localhost", port=8018, debug=True)
