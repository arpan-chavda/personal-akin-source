#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return IE

class IE(BaseFeedBook):
    title                 = u'Indian Express'
    description           = u'Indian Express newspaper ebook'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    #mastheadfile          = "ie.jpg"
    #coverfile             = "cv_lifeweek.jpg"
    oldest_article        = 1
    
    feeds = [ (u'Opinion', u'http://indianexpress.com/section/opinion/feed', True), (u'Economy', u'http://indianexpress.com/section/economy/feed/ ', True), (u'Science', u'http://indianexpress.com/section/science/feed/', True), (u'Climate Change', u'http://indianexpress.com/section/world/climate-change/feed', True), #(u'Letters', u'http://syndication.indianexpress.com/rss/40/letters-to-editor.xml'), #(u'Art & Culture', u'http://syndication.indianexpress.com/rss/1229/art---culture.xml'), #(u'Sunday Stories', u'http://syndication.indianexpress.com/rss/723/sunday-stories.xml') ,
           ]