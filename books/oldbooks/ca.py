#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return ca

class ca(BaseFeedBook):
    title                 = u'Current Affairs'
    description           = u'v3 Current Affairs ebook'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    #mastheadfile          = "mh_lifeweek.gif"
    #coverfile             = "cv_lifeweek.jpg"
    oldest_article        = 7
    fulltext_by_readability = True
    deliver_days = ['Saturday']
    url_filters = [ 'http://www.jagranjosh.com/imported/images/E/Articles/.*.jpg' ]
    
    feeds = [
            (u'Jagran Josh', u'http://www.jagranjosh.com/rss/josh/current_affairs.xml'),(u'ForumIAS', u' http://my.forumias.com/feed/ '), (u'Seniors Blog', 'http://swapsushias.blogspot.com/feeds/posts/default?alt=rss', True),(u'ClearIAS', u'http://www.clearias.com/feed/ ') , (u'GKToday.in', u'http://feeds.feedburner.com/GeneralKnowledgeToday'), (u'Current Affairs', u'http://bestcurrentaffairs.com/w/feed/', True) ,]