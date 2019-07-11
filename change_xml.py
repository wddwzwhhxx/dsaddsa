# coding=utf-8
import os
import os.path
import xml.dom.minidom

path = "/home/wangzhaowei/data/bishe/xml/xml4"
files = os.listdir(path)  # 得到文件夹下所有文件名称
count=0
for xmlFile in files:  # 遍历文件夹
    if not os.path.isdir(xmlFile):  # 判断是否是文件夹,不是文件夹才打开
        print(xmlFile)

        # 将获取的xml文件名送入到dom解析
        dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))  # 输入xml文件具体路径
        root = dom.documentElement
        # 获取标签<name>以及<folder>的值
        filename = root.getElementsByTagName('filename')
        #folder = root.getElementsByTagName('folder')

        # 对每个xml文件的多个同样的属性值进行修改。此处将每一个<name>属性修改为plane,每一个<folder>属性修改为VOC2007
        for i in range(len(filename)):
            print (filename[i].firstChild.data)
            filename[i].firstChild.data = '04'+filename[i].firstChild.data
            print (filename[i].firstChild.data)

# 将属性存储至xml文件中
        with open(os.path.join(path, xmlFile), 'w') as fh:
            dom.writexml(fh)
            print('已写入')
        count+=1