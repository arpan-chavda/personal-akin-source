#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return EPW

class EPW(BaseFeedBook):
    title                 = u'Economical & Political Weekly'
    description           = u'EPW ebook'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    #mastheadfile          = "mh_lifeweek.gif"
    #coverfile             = "cv_lifeweek.jpg"
    fulltext_by_readability = True
    oldest_article        = 7
    
    deliver_days          = ['Saturday']
    
    feeds = [ (u'Editorial', ' http://www.epw.in/feed/editorials.xml '), (u'Commentary', ' http://www.epw.in/feed/commentary.xml'), (u'Perspective', ' http://www.epw.in/feed/perspectives.xml '), (u'Web Exclusive', 'http://www.epw.in/feed/web-exclusives.xml'),
           ] 



