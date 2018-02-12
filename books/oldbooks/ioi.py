#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return ioi

class ioi(BaseFeedBook):
    title                 = u'Insight On India'
    description           = u'v2 Insight On India ebook'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    #mastheadfile          = "mh_lifeweek.gif"
    #coverfile             = "cv_lifeweek.jpg"
    oldest_article        = 2
    deliver_days          = ['Sunday','Tuesday','Thursday','Saturday']
    url_filters = ['insightsonindia.com/.*(political|history|public|philosophy).*answer.*']
    
    feeds = [
            (u'Current Feeds', 'http://insightsonindia.com/feed/ ', True),
           ]