# coding=UTF-8
import sys
from PIL import Image
from xml.dom import minidom
#import cv2
def make_xml(count,txt_path,out_path):
    img_name=str(i).zfill(6)+'.jpg'
    floder = 'VOC2007'
    result=[]
    with open(txt_path,'r') as f:
        for line in f:
            result.append(list(line.strip('\n').split(' ')))
    #print (result)
    w = int(result[0][1])
    h = int(result[0][0])
    d = 3
    # print w,h,d
    doc = minidom.Document()  # 创建DOM树对象

    annotation = doc.createElement('annotation')  # 创建子节点
    doc.appendChild(annotation)  # annotation作为doc树的子节点

    folder = doc.createElement('folder')
    folder.appendChild(doc.createTextNode(floder))  # 文本节点作为floder的子节点
    annotation.appendChild(folder)  # folder作为annotation的子节点

    filename = doc.createElement('filename')
    filename.appendChild(doc.createTextNode(img_name))
    annotation.appendChild(filename)

    source = doc.createElement('source')
    database = doc.createElement('database')
    database.appendChild(doc.createTextNode("Unknown"))
    source.appendChild(database)

    annotation.appendChild(source)

    size = doc.createElement('size')
    width = doc.createElement('width')
    width.appendChild(doc.createTextNode("%d" % w))
    size.appendChild(width)
    height = doc.createElement('height')
    height.appendChild(doc.createTextNode("%d" % h))
    size.appendChild(height)
    depth = doc.createElement('depth')
    depth.appendChild(doc.createTextNode("%d" % d))
    size.appendChild(depth)
    annotation.appendChild(size)
    segmented = doc.createElement('segmented')
    segmented.appendChild(doc.createTextNode("0"))
    annotation.appendChild(segmented)

    txtLabel = open(txt_path, 'r')
    boxes = result[1:]
    # print (boxes)
    for box in boxes:
        x_min = float(box[0])
        y_min = float(box[1])
        x_max = float(box[2]) + x_min
        y_max = float(box[3]) + y_min
        label=int(box[4])
        '''
        if x_min < 0:
            x_min = 1
        if y_min < 0:
            y_min = 1
        if x_max > 1279:
            x_max = 1279
        if y_max > 959:
            y_max = 959


        #elif x_max-x_min > 300 or y_max-y_min > 300:
            #continue
        if label==3:
            continue
        elif x_max-x_min<20 and y_max-y_min<20:
            continue
        '''
        #开始写xml文件
        object = doc.createElement('object')
        nm = doc.createElement('name')
        nm.appendChild(doc.createTextNode('car'))
        object.appendChild(nm)
        pose = doc.createElement('pose')
        pose.appendChild(doc.createTextNode("Unspecified"))
        object.appendChild(pose)
        truncated = doc.createElement('truncated')
        '''
        if label==2:
            truncated.appendChild(doc.createTextNode("1"))
        else:
            truncated.appendChild(doc.createTextNode("0"))
        '''
        object.appendChild(truncated)
        difficult = doc.createElement('difficult')
        '''
        if x_max-x_min < 40 and y_max-y_min < 40:
            difficult.appendChild(doc.createTextNode("1"))
        else:
            difficult.appendChild(doc.createTextNode("0"))
        '''
        object.appendChild(difficult)
        bndbox = doc.createElement('bndbox')
        xmin = doc.createElement('xmin')
        xmin.appendChild(doc.createTextNode(str(x_min)))
        bndbox.appendChild(xmin)
        ymin = doc.createElement('ymin')
        ymin.appendChild(doc.createTextNode(str(y_min)))
        bndbox.appendChild(ymin)
        xmax = doc.createElement('xmax')
        xmax.appendChild(doc.createTextNode(str(x_max)))
        bndbox.appendChild(xmax)
        ymax = doc.createElement('ymax')
        ymax.appendChild(doc.createTextNode(str(y_max)))
        bndbox.appendChild(ymax)
        object.appendChild(bndbox)
        annotation.appendChild(object)
        #开始存
        savefile = open(out_path, 'w')
        savefile.write(doc.toprettyxml())
    return count

def check_txt(txt_path):
    txt_res=[]
    num_good=0
    with open(txt_path,'r') as f:
        for line in f:
            txt_res.append(list(line.strip('\n').split(' ')))
    for i in range(int(txt_res[0][2])):
        x_min=float(txt_res[i+1][0])
        y_min=float(txt_res[i+1][1])
        x_max=x_min+float(txt_res[i+1][2])
        y_max=y_min+float(txt_res[i+1][3])
        label=int(txt_res[i+1][4])
        if x_min < 0:
            x_min = 1
        if y_min < 0:
            y_min = 1
        if x_max > 1279:
            x_max = 1279
        if y_max > 959:
            y_max = 959
        w=x_max-x_min
        h=y_max-y_min
        #elif w > 300 or h > 300:
        #    continue
        if label==3:
            continue
        elif w<20 and h<20:
            continue
        else:
            num_good+=1
    return num_good


if __name__=="__main__":
    result = []
    count = -1
    all_txt_path = '/share2/public/freespace_data/fisheye_car_bbox/test.txt'
    #得到文件的所有路径，存在result
    with open(all_txt_path, 'r') as f:
        for line in f:
            result.append(list(line.strip('\n').split('||')))
    for i in range(len(result)):
        #if count>100:
        #    break
        txt_path = result[i][1]
        #检查是不是有好的bbox
        #num_goodbbox=check_txt(txt_path)
        #if num_goodbbox==0:
        #    continue
        count+=1
        out_path = '/home/wangzhaowei/data/bbox_voc/Annotations/' + str(count).zfill(6) + '.xml'
        count = make_xml(count, txt_path, out_path)
        print ('{:d}'.format(count))


