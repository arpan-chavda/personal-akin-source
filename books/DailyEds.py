#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
from base import BaseFeedBook

def getBook():
    return DailyEds

class DailyEds(BaseFeedBook):
    title                 = u'DailyEds'
    description           = u'Personal UPSC Daily News Articles Compilation'
#    now                   = datetime.datetime.now()
    # Set category.
#    category = 'newspaper'
    # Set publisher and publication type.
#    publisher = now.strftime("%d-%b-%y")
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 50
    oldest_article        = 1
    mastheadfile          = "mh-dailyeds.gif"
    coverfile             = "cv_dailyeds.jpg"
    network_timeout       = 80
#    fetch_img_via_ssl     = False
    fulltext_by_readability = True
#    conversion_options = { 'comment' : description, 'tags' : category, 'publisher' : publisher, 'language' : language, 'smarten_punctuation' : True }

    deliver_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    feeds = [
(u'The Hindu Op-Ed', 'http://www.thehindu.com/opinion/?service=rss'),
(u'Indian Exp Op-Ed', 'http://indianexpress.com/section/opinion/feed/'),
(u'Livemint Op-Ed', 'http://www.livemint.com/rss/opinion'),
(u'BLine Op-Ed', 'http://www.thehindubusinessline.com/opinion/feeder/default.rss'),
(u'Tribune Op-Ed', 'http://www.tribuneindia.com/rss/feed.aspx?cat_id=34&mid=70'),
(u'HT Op-Ed', 'https://www.hindustantimes.com/rss/opinion/rssfeed.xml'),
(u'Scroll.in Articles', 'http://arpan.space/tinyrss/public.php?op=rss&id=-1029&key=vgdufo5a76c06b60ee6'),
(u'Scroll.in Pulse', 'http://arpan.space/tinyrss/public.php?op=rss&id=-1032&key=y36w9z5a76c0a0b962e'),
(u'TOI Blogs', 'https://blogs.timesofindia.indiatimes.com/feed/defaultrss'),
(u'Mrunal.org', 'http://mrunal.org/feed'),
(u'ORF Online', 'http://www.orfonline.org/feed/?post_type=research&withoutcomments=1'),]