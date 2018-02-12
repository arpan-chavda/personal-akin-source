#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook
from bs4 import BeautifulSoup

def getBook():
    return PIB

class PIB(BaseFeedBook):
    title                 = u'PIB'
    description           = u'The latest English Press Releases from Press Information Bureau Govt. Of India.'
    oldest_article        = 7
    deliver_days          = ['Saturday']
    feeds = [
            (u'Latest News', 'http://pib.nic.in/newsite/rssenglish.aspx'),
            ]
    #remove_ids = ['printID','pimage']
    def preprocess(self, content):
        soup = BeautifulSoup(content, "lxml")

        #get title text
        title_text = ''
        for tag in soup.find_all(attrs={"style":"text-align:center;font-weight: bold;"}):
            if tag.name == 'div':
                #tag.name = 'h2'
                for tg in tag.find_all(['br']):
                    tg.decompose()
                title_text = tag.get_text()
                tag.decompose()
                break

        #get time of article
        time_text = ''
        for tag in soup.find_all(attrs={"style":"text-align:right;font-size:80%;font-weight:lighter"}):
            if tag.name == 'div':
                time_text = tag.get_text()
                tag.decompose()
                break

        #get content of article
        content_text = ''
        for tag in soup.find_all(attrs={"style":"position:absolute;top:110px;text-align:justify"}):
            if tag.name == 'div':
                content_text = unicode(tag)
                #tag.decompose()
                break

        soup = None

        #rebuild a aricle
        ret_text = u"<html><head><title>%s</title></head><body> %s <br/> %s </body></html>" % (title_text,time_text,content_text)
        return ret_text