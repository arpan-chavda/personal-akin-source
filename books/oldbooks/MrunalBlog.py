#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return MrunalBlog

class MrunalBlog(BaseFeedBook):
    title                 = u'Mrunal.org'
    description           = u'Mrunal.org ebook'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    #mastheadfile          = "mh_lifeweek.gif"
    #coverfile             = "cv_lifeweek.jpg"
    oldest_article        = 7
    
    deliver_days          = ['Saturday']
    
    feeds = [
            (u'Current Feeds', 'http://mrunal.org/feed'),
           ]
    def fetcharticle(self, url, decoder):
        #每个URL都增加一个后缀full=y，如果有分页则自动获取全部分页
        url += '/print'
        return BaseFeedBook.fetcharticle(self,url,decoder)
        