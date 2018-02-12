#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return ioi2

class ioi2(BaseFeedBook):
    title                 = u'2Insight On India'
    description           = u'v2 Insight On India ebook'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    #mastheadfile          = "mh_lifeweek.gif"
    #coverfile             = "cv_lifeweek.jpg"
    oldest_article        = 2
    keep_only_tags = [dict(name='h1', attrs={'class':'entry-title'}),dict(name='div', attrs={'class':'entry-content'}),]
    remove_ids = ['jp-post-flair','pc1','addshare',]
    remove_classes = ['wpcnt','entry-links',] # haha.mx

    deliver_days          = ['Sunday','Tuesday','Thursday','Saturday']
    url_filters = ['insightsonindia.com/.*(political|history|public|philosophy).*answer.*']
    
    feeds = [
            (u'Current Feeds', 'http://insightsonindia.com/feed/ ', True),
           ]