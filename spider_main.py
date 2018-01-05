# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 16:42:46 2018

@author: 59628
"""
import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
    def craw(self,root_url):
        self.urls.add_new_url(root_url)
        count=1
        while self.urls.has_new_url():
            new_url=self.urls.get_new_url()
            print("craw %d : %s" %(count,new_url))
            count=count+1
            html_cont=self.downloader.download(new_url)
            new_urls,new_data=self.parser.parse(new_url,html_cont)
            self.urls.add_new_urls(new_urls)
            self.outputer.collect_data(new_data)
            if count==50:
                break
            self.outputer.output_html()
if __name__=='__main__':
    root_url="https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)