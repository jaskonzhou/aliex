import json
from urllib.request import urlopen, quote
import requests,csv
import pandas as pd

def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = 'pt7BONQkzlGaKhGB3F14AscwC2I4aYfn'
    add = quote(address)
    uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode() #将其他编码的字符串解码成unicode
    temp = json.loads(res) #对json数据进行解析
    return temp

file = open(r'E:\\scrapy\json\point.json','w') #建立json数据文件
with open(r'E:\\scrapy\json\区域均价.csv', 'r') as csvfile: #打开csv
    reader = csv.reader(csvfile)
    for line in reader: #读取csv里的数据
        # 忽略第一行
        if reader.line_num == 1: #由于第一行为变量名称，故忽略掉
            continue
            # line是个list，取得所有需要的值
        b = line[0].strip() #将第一列city读取出来并清除不需要字符
        c= line[1].strip()#将第二列price读取出来并清除不需要字符
        lng = getlnglat(b)['result']['location']['lng'] #采用构造的函数来获取经度
        lat = getlnglat(b)['result']['location']['lat'] #获取纬度
        str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":' + str(c) +'},'
        #print(str_temp) #也可以通过打印出来，把数据copy到百度热力地图api的相应位置上
        file.write(str_temp) #写入文档
file.close() #保存