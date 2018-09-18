# -*- coding: cp936 -*-
import scrapy
import re
from ahau.items import AhauItem
from ahau.settings import FILE_PATH, BASE_URL

class PageSpider(scrapy.Spider):
    name = "page"

    def start_requests(self):
        listfile = open(FILE_PATH + "A.txt","r")
        line = listfile.readline()
        while(line):
            (name,url)=line.split(',')
            if(url.startswith("http")):
                domain = url.strip()
                request = scrapy.Request(url=domain,callback=self.paser)
                request.meta['url'] = domain
                yield request
            line = listfile.readline()


    def paser(self,response):
        
        textlists = response.css("dl>dd>a::text").extract()
        urllists = response.css("dl>dd>a::attr(href)").extract()
   
        i = 0
        while(i<len(textlists)-1):
            pageitems = AhauItem()
            pageitems['title'] = textlists[i]
            pageitems['url'] = BASE_URL + "/"+  urllists[i]
            i = i +1
            yield pageitems
