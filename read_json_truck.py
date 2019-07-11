# _*_coding:utf-8
import os
import sys
import json
import datetime


def ObjectId(s):
  return s


def parse(path):
  with open(path, 'r') as f:
    lines = [l.strip() for l in f.readlines()]
  labels = [eval(l) for l in lines]
  return labels
    #with open(save, 'w') as f:
    #json.dump(labels, f, indent=4)





input_json_path='/home/wangzhaowei/data/truck_200'
save_json_path='/home/wangzhaowei/data/truck_200/truck_150.json'



def transfer_format_2(y1,x1,cls_1,crop_1,y2,x2,cls_2,crop_2):
  #正面线
  if (cls_1 == 'right_front' and cls_2 == 'left_front') or (cls_1 == 'left_back' and cls_2 == 'right_back') or (cls_1 == 'right_back' and cls_2 == 'left_back') or (cls_1 == 'left_front' and cls_2 == 'right_front'):
    new_y1=y1
    new_x1=x1
    new_y2=y2
    new_x2=x2
    if crop_1=='truncate_point':
      new_cls1=2
    else:
      new_cls1=1
    if crop_2=='truncate_point':
      new_cls2=2
    else:
      new_cls2=1
    if cls_1=='right_front' or cls_1=='left_front':
      head1=1
      head2=1
    else:
      head1=2
      head2=2
  #侧面线 变
  elif (cls_1 == 'left_front' and cls_2 == 'left_back') or (cls_1 == 'right_front' and cls_2 == 'right_back'):
    new_y1=y2
    new_x1=x2
    new_y2=y1
    new_x2=x1
    if crop_2=='truncate_point':
      new_cls1=4
    else:
      new_cls1=3
    if crop_1=='truncate_point':
      new_cls2=4
    else:
      new_cls2=3
    head1=2
    head2=1
  #侧面线  不变
  elif (cls_1 == 'left_back' and cls_2 == 'left_front') or (cls_1 == 'right_back' and cls_2 == 'right_front'):
    new_y1=y1
    new_x1=x1
    new_y2=y2
    new_x2=x2
    if crop_1=='truncate_point':
      new_cls1=4
    else:
      new_cls1=3
    if crop_2=='truncate_point':
      new_cls2=4
    else:
      new_cls2=3
    head1=2
    head2=1
  #侧面线 变 有中点
  elif (cls_1 == 'left_front' and cls_2 == 'left_middle') or (cls_1 == 'right_front' and cls_2 == 'right_middle'):
    new_y1=y2
    new_x1=x2
    new_y2=y1
    new_x2=x1
    if crop_2=='truncate_point':
      new_cls1=4
    else:
      new_cls1=3
    if crop_1=='truncate_point':
      new_cls2=4
    else:
      new_cls2=3
    head1=3
    head2=1
  #侧面线 变 有中点
  elif (cls_1 == 'left_middle' and cls_2 == 'left_back') or (cls_1 == 'right_middle' and cls_2 == 'right_back'):
    new_y1=y2
    new_x1=x2
    new_y2=y1
    new_x2=x1
    if crop_2=='truncate_point':
      new_cls1=4
    else:
      new_cls1=3
    if crop_1=='truncate_point':
      new_cls2=4
    else:
      new_cls2=3
    head1=1
    head2=3
  else:
    print('搞错了')
    print (cls_1,cls_2)
    return 1




  return new_y1,new_x1,new_cls1,head1,new_y2,new_x2,new_cls2,head2


def transfer_format_more_2(point_num):
  new_point_num=[]
  point_first=point_num.pop(0)
  for i in range(len(point_num)-1):
    y1=point_num[i-1][0]
    x1=point_num[i-1][1]
    cls_1=point_num[i-1][2]
    crop_1=point_num[i-1][3]
    y2=point_num[i][0]
    x2=point_num[i][1]
    cls_2=point_num[i][2]
    crop_2=point_num[i][3]
    new_y1, new_x1, new_cls1, head1, new_y2, new_x2, new_cls2, head2 = transfer_format_2(y1,x1,cls_1,crop_1,y2,x2,cls_2,crop_2)
    new_point_num.append([new_y1, new_x1, new_cls1, head1, new_y2, new_x2, new_cls2, head2])
  return new_point_num


if __name__=='__main__':
  count=0
  filelist = os.listdir(input_json_path)
  for file in filelist:
    print(count)
    count+=1
    # 读json 文件
    json_path=input_json_path+'/'+file
    dict=parse(json_path)
    #print (dict)
    origin_path = list(dict[0]['origin_path'].split('FS_DATA'))[1]
    if 'children' in dict[0]['results'][0]['raw']:
      results=dict[0]['results'][0]['raw']['children']
    else:
      continue
    skip=dict[0]['results'][0]['raw']['skip']
    hard=dict[0]['results'][0]['raw']['hard']
    if skip or hard:
      continue
    #有几个就说明有几组线
    for i in range(len(results)):
      #对于每一组线来说
      class_line=results[i] #小字典

      #如果只有俩个点
      if len(class_line['children'])==2:
        point_1=class_line['children'][0]
        point_2=class_line['children'][1]
        new_y1,new_x1,new_cls1,head1,new_y2,new_x2,new_cls2,head2=transfer_format_2(point_1['y'],point_1['x'],point_1['data']['location'][0],point_1['data']['visibility'][0],
                              point_2['y'],point_2['x'],point_2['data']['location'][0],point_2['data']['visibility'][0])
        print(new_y1,new_x1,new_cls1,head1,new_y2,new_x2,new_cls2,head2)



      #如果多于俩个点
      else:
        point_num=[]
        for i in range(len(class_line['children'])):
          point_num.append([class_line['children'][i]['y'],class_line['children'][i]['x'],class_line['children'][i]['data']['location'][0],
                                    class_line['children'][i]['data']['visibility'][0]])
        new_point_num=transfer_format_more_2(point_num)
        for n in new_point_num:
          print(n)












