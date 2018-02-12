#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return Sblog

class Sblog(BaseFeedBook):
    title                 = u' Seniors Blog'
    description           = u' Seniors Blog ebook'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    #mastheadfile          = "mh_lifeweek.gif"
    #coverfile             = "cv_lifeweek.jpg"
    oldest_article        = 7
    
    deliver_days          = ['Saturday']
    
    feeds = [
            (u'Current Feeds', 'http://swapsushias.blogspot.com/feeds/posts/default?alt=rss', True),
           ]