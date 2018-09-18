# -*- coding: cp936 -*-
import scrapy
import re
from ahau.items import AhauItem
from ahau.settings import FILE_PATH

class PageSpider(scrapy.Spider):
    name = "content"

    def start_requests(self):
        listfile = open(FILE_PATH + "B.txt","r")
        line = listfile.readline()
        while(line):
            (name,url)=line.split(',')
            request = scrapy.Request(url=url.strip(),callback=self.paser)
            line = listfile.readline()
            yield request
      


    def paser(self,response):
        
        titles = response.css("h3::text").extract()
        contents = response.css("div[align=left]").extract()
        pageitems = AhauItem()
        if titles:
            pageitems['title']=titles[0]
        if contents:
            pageitems['contents']=contents[0]
    
        yield pageitems