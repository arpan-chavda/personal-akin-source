#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return Hindu

class Hindu(BaseFeedBook):
    title                 = u'The Hindu'
    description           = u'The Hindu newspaper ebook'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    #mastheadfile          = "th.jpg"
    #coverfile             = "cv_lifeweek.jpg"
    #mastheadfile          = "http://www.thehindu.com/template/1-0-1/gfx/logo.jpg"
    #coverfile             = "cv_lifeweek.jpg"
    fulltext_by_readability = True
    oldest_article        = 1
    keep_image = True
    
    feeds = [ (u'National', u'http://www.thehindu.com/news/national/?service=rss'), (u'International', u'http://www.thehindu.com/news/international/?service=rss'), (u'Lead', u'http://www.thehindu.com/opinion/lead/?service=rss'), (u'Columns', u'http://www.thehindu.com/opinion/columns/?service=rss'), (u'Editorial', u'http://www.thehindu.com/opinion/editorial/?service=rss'), (u'Letters', u'http://www.thehindu.com/opinion/letters/?service=rss'), (u'Op-Ed', u'http://www.thehindu.com/opinion/op-ed/?service=rss'), (u"Readers' Editor", u'http://www.thehindu.com/opinion/Readers-Editor/?service=rss'), (u'Energy & Environment', u'http://www.thehindu.com/sci-tech/energy-and-environment/?service=rss'), (u'ET-Environment', u'http://economictimes.indiatimes.com/rssfeeds/2647180.cms'), (u'Health', u'http://www.thehindu.com/sci-tech/health/?service=rss'), (u'Science', u'http://www.thehindu.com/sci-tech/science/?service=rss'), (u'Technology', u'http://www.thehindu.com/sci-tech/technology/?service=rss'), (u'Economy', u'http://www.thehindu.com/business/Economy/?service=rss'), (u'Sports', u'http://www.thehindu.com/sport/?service=rss'), (u'Industry', u'http://www.thehindu.com/business/Industry/?service=rss'), (u'Young World', u' http://www.thehindu.com/features/kids/?service=rss '),
           ]