import os
import random

trainval_percent = 0.95
train_percent = 0.95
xmlfilepath = '/home/wangzhaowei/data/VOCdevkit/VOC2007/Annotations'
txtsavepath = '/home/wangzhaowei/data/VOCdevkit/VOC2007/ImageSets/Main'
total_xml = os.listdir(xmlfilepath)

num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)
trainval= random.sample(list,tv)
train=random.sample(trainval,tr)

ftrainval = open('/home/wangzhaowei/data/VOCdevkit/VOC2007/ImageSets/Main/trainval.txt', 'w')
ftrainval_xml=open('/home/wangzhaowei/data/VOCdevkit/VOC2007/ImageSets/Main/trainval_xml.txt', 'w')
ftest = open('/home/wangzhaowei/data/VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'w')
ftest_xml = open('/home/wangzhaowei/data/VOCdevkit/VOC2007/ImageSets/Main/test_xml.txt', 'w')

ftrain = open('/home/wangzhaowei/data/VOCdevkit/VOC2007/ImageSets/Main/train.txt', 'w')
ftrain_xml = open('/home/wangzhaowei/data/VOCdevkit/VOC2007/ImageSets/Main/train_xml.txt', 'w')

fval = open('/home/wangzhaowei/data/VOCdevkit/VOC2007/ImageSets/Main/val.txt', 'w')
fval_xml = open('/home/wangzhaowei/data/VOCdevkit/VOC2007/ImageSets/Main/val_xml.txt', 'w')


for i  in list:
    name=total_xml[i][:-4]
    if i in trainval:
        ftrainval.write(name+'\n')
        ftrainval_xml.write(name+'.xml'+'\n')
        if i in train:
            ftrain.write(name+'\n')
            ftrain_xml.write(name+'.xml'+'\n')

        else:
            fval.write(name+'\n')
            fval_xml.write(name+'.xml'+'\n')

    else:
        ftest.write(name+'\n')
        ftest_xml.write(name+'.xml'+'\n')


ftrainval.close()
ftrain.close()
fval.close()
ftest .close()
