#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return IRPOLICY

class IRPOLICY(BaseFeedBook):
    title                 = u'IR AND POLICY'
    description           = u'IR and POLICY of India'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    #mastheadfile          = "mh_lifeweek.gif"
    #coverfile             = "cv_lifeweek.jpg"
    fulltext_by_readability = True
    oldest_article        = 7
    
    deliver_days          = ['Saturday']
    
    feeds = [ (u'IDSA', 'http://idsa.in/rss.xml'), (u'PRS - Blog', 'http://www.prsindia.org/theprsblog/?feed=rss2'),
           ]