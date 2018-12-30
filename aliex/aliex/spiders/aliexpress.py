# -*- coding: utf-8 -*-
import scrapy
from ..items import AliexItem
from pyquery import PyQuery

from scrapy.http import Request
import re

class AliexpressSpider(scrapy.Spider):
    name = 'aliexpress'
    allowed_domains = ['aliexpress.com']
    ROBOTSTXT_OBEY = False
    start_urls = ['https://www.aliexpress.com/category/200003482/dresses/1.html?site=glo&SortType=total_tranpro_desc&needQuery=n&tag='
                  #'https://www.aliexpress.com/category/200003482/dresses/'
                 ]



    def clean(s):
        """去除字符串两边的空格"""
        return s.strip() if s else ''


    def parse(self, response):
        item = AliexItem()
        jpy = PyQuery(response.text)
        li_list = jpy ('#list-items > li').items()
        for it in li_list:
                strname = it('div.right-block.util-clearfix > div > div.detail > h3 > a > span').text()
                strid = it.attr('qrdata')
                strid =re.findall(r"[|](.+?)[|]",strid)
                #print('strid',strid[0])

                strprice = it('div.right-block.util-clearfix > div > div.info.infoprice > span > span.value').text()
                stroder = it('div.right-block.util-clearfix > div > div.info.infoprice > div.rate-history > span.order-num > a > em').text()
                #print(strprice)
                if(it.find('img').attr('src')):
                    strjpg = r"https:" + it.find('img').attr('src')
                else:
                    strjpg = r"https:" + it.find('img').attr('image-src')
                item['productid'] = str(strid[0])
                item['name'] = strname
                item['price'] = strprice
                item['order'] = stroder
                item['picurl'] = str(strjpg)
                yield item
        if not li_list:
                return
        pn = response.meta.get('pn', 1)
        pn +=1
        if pn > 3:
            return

        url = 'https://www.aliexpress.com/category/200003482/dresses/{}.html?site=glo&SortType=total_tranpro_desc&needQuery=n&tag='.format(pn)
        print(url)
        yield Request(url,callback=self.parse,dont_filter=True)
        # pn = response.meta.get('pn',1)
        # pn +=1
        # if pn >5:
        #     return
        #
        # req = response.follow('category/200003482/dresses/{}.html?site=glo&SortType=total_tranpro_desc&needQuery=n&tag='.format(pn),
        #                       callback = self.parse,
        #                       meta = {'pn':pn}
        #                       )
        # yield req
#        strname = jpy('#list-items > li.list-item.list-item-first.util-clearfix.list-item-180 > div.right-block.util-clearfix > div > div.detail > h3 > a > span').text()


        pass
