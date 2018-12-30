import json,xlwt
def readExcel(file):
    with open(file,'r',encoding='utf8') as fr:
        data = json.load(fr) # 用json中的load方法，将json串转换成字典
    return data
def writeM():
    a = readExcel('mydata1.json')
    print(a)
    title = ["产品","价格","订单数"]
    book = xlwt.Workbook() # 创建一个excel对象
    sheet = book.add_sheet('Sheet1',cell_overwrite_ok=True) # 添加一个sheet页
    for i in range(len(title)): # 循环列
        sheet.write(0,i,title[i]) # 将title数组中的字段写入到0行i列中
    for line in a: #　循环字典
        print('line:',line)
        sheet.write(int(line),0,line) #　将line写入到第int(line)行，第0列中
        for i in range(len(a[line])):
            sheet.write(int(line),i+1,a[line][i])
    book.save('demo.xls')

if __name__ == '__main__':
    writeM()