#!/usr/bin/python
# -*- coding: utf-8 -*-
# ===========================================================
# 网站配置表
# ===========================================================


website_list = [
    ('新浪微博', 'site:weibo.com', '综合性UGC社区'),     # ALL
    ('知乎', 'site:www.zhihu.com', '综合性问答社区'),       # ALL, IT
    ('CSDN', 'site:csdn.net', '技术论坛'),          # IT
    ('华声', 'site:bbs.voc.com.cn', '综合性论坛'),                    # ALL
    ('人人网', 'site:www.renren.com', '学生UGC社区'),                   # ALL
    ('威锋网', 'site:www.feng.com', '数码产品论坛'),                   # PHONE
    ('虎扑体育论坛', 'site:bbs.hupu.com', '体育论坛'),      # SPORT
    ('天涯', 'site:www.tianya.cn', '综合性UGC社区'),           # ALL
    ('百度贴吧', 'site:tieba.baidu.com', '综合性论坛'),       # ALL
    ('宠物中国', 'site:www.chinapet.com', '宠物论坛'),      # PET
    ('吉他中国', 'site:bbs.guitarchina.com', '音乐论坛'),   # MUSIC, GUITAR
    ('高校魔术网', 'site:www.collegemagic.cn', '学生魔术论坛'),  # MAGIC
    ('魔术吧', 'site:www.magic8.cn', '魔术论坛'),              # MAGIC
    ('开源中国', 'site:www.oschina.net', '技术论坛'),           # IT
    ('懂球帝', 'site:www.dongqiudi.com', '体育UGC社区'),          # SPORT, FOOTBALL
    ('豆瓣', 'site:www.douban.com', '综合性UGC社区'),              # ALL
    ('新浪体育论坛', 'site:forum.sports.sina.com.cn', '体育论坛'),    # SPORT
    ('精英乒乓论坛', 'site:www.pingpang.info/bbs', '体育论坛'),       # SPORT, PINGPONG
    ('箱鼓论坛', 'site:www.cajon.cn', '音乐论坛'),              # MUSIC, CAJON
    ('安卓巴士', 'site:android.apkbus.com', '技术论坛'),        # IT
    ('eoe社区', 'site:www.eoeandroid.com', '技术论坛'),         # IT
    ('Cocoa China', 'site:www.cocoachina.com/bbs', '技术论坛'),     # IT
    ('虾米', 'site:www.xiami.com', '音乐社区'),               # MUSIC
    ('天使动漫', 'site:www.tsdm.net', '动漫论坛'),            # CARTOON
    ('动漫花园', 'site:www.dmhy.org', '动漫论坛'),            # CARTOON
    ('Linux时代', 'site:linux.chinaunix.net', '技术论坛'),            # IT
    ('Linux中国', 'site:linux.cn', '技术论坛'),            # IT
]


website_link = {}
for website in website_list:
    website_link[website[0]] = (website[1].replace('site:', ''), website[2])
