import os
import xlrd

# 遍历指定目录，显示目录下的所有文件名
def eachFile(Dirpath):
    pathDir = os.listdir(Dirpath)
    """
    for file in pathDir:
        filepath = os.path.join(Dirpath,file)
        AllFileName.append(filepath)  #将文件名放到一个列表里
    """
    return pathDir

#遍历excel文件，对指定的ip段进行计数
def OperateExcelFile(filenamelist,Dirpath):
    CountList = []
    for file in filenamelist:
        path = os.path.join(Dirpath,file)
        work_book = xlrd.open_workbook(path)
        table = work_book.sheets()[0]  #获取表格
        nrows = table.nrows - 1  #获取该表格的有效行数
        IpPoul = table.col_values(1, start_rowx=1, end_rowx=nrows)  #将ip全部拿出来放到列表里，第一个参数指定哪一列数据，第二个参数指定从哪一行开始，第三个是结束行
        BussinessIPCount = 0
        for ip in IpPoul:
            Ipsplit = ip.split(".")   #将ip切片
            #print(Ipsplit[2])
            if(32<=int(Ipsplit[2])<=63):  #判断C类地址的大小
                BussinessIPCount  = BussinessIPCount + 1
        CountList.append(BussinessIPCount)
    return CountList

if __name__ == '__main__':
    Dirpath = 'D:\建信金科\业务终端统计测试'
    filelist = eachFile(Dirpath)
    #print(filelist)
    count = OperateExcelFile(filelist,Dirpath)
    cityname =  []
    #取分行的名字
    for f in filelist:
        city = f.split(".")[0]
        cityname.append(city)
    for(name, num) in zip(cityname, count):
        print(name + ":" + str(num))
