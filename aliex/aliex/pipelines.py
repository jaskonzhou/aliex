# -*- coding: utf-8 -*-
import json
import codecs
import urllib.request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QtpjtPipeline(object):
    pass


class AliexPipeline(object):
    def process_item(self, item, spider):
        line = '{}\n'.format(json.dumps(dict(item), ensure_ascii=False))
        print(line)
        self.file.write(line)
        strname = item['name']
        print(strname)
        thispic = item['picurl']
        trueurl = thispic
        localpath = r'E:\scrapy\aliex\aliex\jpg'
        localpath = localpath + r'\\' + str(item['productid']) + '.jpg'
        urllib.request.urlretrieve(trueurl, filename=localpath)
        return item

    def __init__(self):
        self.file = codecs.open("mydata1.json", "wb", encoding="utf-8")
        pass


    def close_spider(self,spider):
        self.file.close()