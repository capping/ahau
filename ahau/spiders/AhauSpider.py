import scrapy
from ahau.items import AhauItem
from ahau.settings import BASE_URL

class AhauSpider(scrapy.Spider):
    name = "ahau"
    def start_requests(self):
        # start_urls = ['http://www.ahau.edu.cn/']
        start_urls = ['http://jgxy.ahau.edu.cn/']
        for url in start_urls:
            yield scrapy.Request(url=url,callback=self.paser)


    def paser(self, response):
        textlists = response.css("ul.venus-menu>li>a::text").extract()
        urllists = response.css("ul.venus-menu>li>a::attr(href)").extract()
        # textlists = response.css("div.smeunbottom.tab_erji1>dl>dd>a::text").extract()
        # urllists = response.css("div.smeunbottom.tab_erji1>dl>dd>a::attr(href)").extract()
   
        i = 0
        while(i<len(textlists)-1):
            pageitems = AhauItem()
            pageitems['name'] = textlists[i]
            pageitems['url'] = BASE_URL + urllists[i]
            i = i + 1
            yield pageitems
