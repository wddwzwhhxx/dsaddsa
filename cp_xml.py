import os
import os.path
import shutil
import time,  datetime
new_result=[]
result=[]
input_xml_list='/home/wangzhaowei/pycharm/centernet/CenterNet/data/voc/VOCdevkit/VOC2007/ImageSets/Main/train_xml.txt'

def moveFileto(sourceDir,  targetDir):
    shutil.copy(sourceDir,  targetDir)

if __name__=='__main__':
    with open(input_xml_list, 'r') as f:
        for line in f:
            result.append(list(line.split('\n')))
    for i in range(len(result)):
        new_result.append(result[i][0])

   # ftrainval = open('/home/wangzhaowei/data/my_xml.txt', 'w')
    for i in range(0,20000):
        a='/home/wangzhaowei/data/VOCdevkit/VOC2007/Annotations/'
        b='/home/wangzhaowei/data/VOCdevkit/VOC2007/annotations_test/'
        if (str(i).zfill(6)+'.xml') in new_result:
            moveFileto(a+str(i).zfill(6)+'.xml',b+str(i).zfill(6)+'.xml')
            print(i)


