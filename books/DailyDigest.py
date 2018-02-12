#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
from base import BaseFeedBook

def getBook():
    return DailyDigest

class DailyDigest(BaseFeedBook):
    title                 = u'DailyDigest'
    description           = u'Personal UPSC Daily Current Compilation'
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
    mastheadfile          = "mh_dailydigest.gif"
    coverfile             = "cv_dailydigest.jpg"
    network_timeout       = 80
    fetch_img_via_ssl     = False
    fulltext_by_readability = True
#    conversion_options = { 'comment' : description, 'tags' : category, 'publisher' : publisher, 'language' : language, 'smarten_punctuation' : True }

    deliver_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    feeds = [
(u'Insights DCA', 'http://www.insightsonindia.com/category/current-events-2/feed'),
(u'Insights Editorial', 'http://www.insightsonindia.com/category/editorials/feed'),
(u'Insights Synopsis', 'http://www.insightsonindia.com/category/secure-synopsis/feed'),
(u'Insights SECURE', 'http://morss.it/www.insightsonindia.com/category/secure-2018/feed'),
(u'Insights AIR', 'http://www.insightsonindia.com/category/air-spotlight/feed'),
(u'Insights RSTV', 'http://www.insightsonindia.com/category/rajya-sabha-videos/feed'),
(u'IASbaba DCA', 'https://iasbaba.com/category/iasbabas-daily-current-affairs/feed'),
(u'IASbaba TLP', 'https://iasbaba.com/category/tlp-upsc-mains-answer-writing/feed'),
(u'IASbaba RSTV', 'https://iasbaba.com/category/the-big-picture-rstv/feed'),
(u'IASbaba AIR', 'https://iasbaba.com/category/all-india-radio/feed'),
(u'IASbaba PIB', 'https://iasbaba.com/category/iasbabas-press-information-bureau/feed'),
(u'CivilsDaily', 'http://www.civilsdaily.com/current-affairs/feed'),]