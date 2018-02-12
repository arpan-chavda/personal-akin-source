#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return frontline

class frontline(BaseFeedBook):
    title                 = u'Frontline'
    description           = u'Frontline magazine ebook'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "fl.jpg"
    #coverfile             = "cv_lifeweek.jpg"
    oldest_article        = 7
    #max_articles_per_feed = 7
    #deliver_days          = ['Sunday','Tuesday','Thursday','Saturday']
    fulltext_by_readability = True
    keep_image = True
    feeds = [
            (u'Recent Articles', 'http://www.frontline.in/?service=rss'),
           ]
    #def fetcharticle(self, url, decoder):
        #每个URL都增加一个后缀full=y，如果有分页则自动获取全部分页
        #url += '?css=print'
        #return BaseFeedBook.fetcharticle(self,url,decoder)