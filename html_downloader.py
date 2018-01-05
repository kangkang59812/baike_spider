# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 16:43:38 2018

@author: 59628
"""
import urllib
from urllib.parse import quote 
import string
class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None
        url_=quote(url,safe= string.printable)
        response=urllib.request.urlopen(url_)
        if response.getcode()!=200:
            return None
        return response.read()