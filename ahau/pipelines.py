# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from ahau.settings import FILE_PATH
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class AhauPipeline(object):
    def process_item(self, item, spider):
        if(spider.name=='ahau'):      
            with open(FILE_PATH + 'A.txt',"a+") as f:
                f.write(str(item['name']).strip().encode('utf-8')+',')
                f.write(item['url']+'\n')

        elif(spider.name=='page'):
            with open(FILE_PATH + 'B.txt',"a+") as f:
                f.write(str(item['title']).strip().encode('utf-8')+',')
                f.write(item['url']+'\n')
        elif(spider.name=='content'):
            with open(FILE_PATH + 'C.txt',"a+") as f:
                f.write(str(item['title']).encode('utf-8')+'\n')
     
        return item
