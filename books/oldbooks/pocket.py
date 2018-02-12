#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return pocket

class pocket(BaseFeedBook):
    title                 = u'My Pocket Feeds'
    description           = u' Pocket ebook'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    #mastheadfile          = "mh_lifeweek.gif"
    #coverfile             = "cv_lifeweek.jpg"
    oldest_article        = 100
    #deliver_days          = ['Saturday']
    fulltext_by_readability = False
    
    #如果为True则使用instapaper服务先清理网页，否则直接连URL下载网页内容
    #instapaper的服务很赞，能将一个乱七八糟的网页转换成只有正文内容的网页
    #但是缺点就是不太稳定，经常连接超时，建议设置为False
    #这样你需要自己编程清理网页，建议使用下面的keep_only_tags[]工具
    fulltext_by_instapaper = False
    feeds = [
            (u'Current Feeds', 'http://getpocket.com/users/arpanchavdaeng/feed/read'),
           ]