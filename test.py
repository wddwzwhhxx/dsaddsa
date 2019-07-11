# _*_coding:utf-8
import os
import json


input_json_path='/home/public/sulei/for_zhaowei/car_project_points'


if __name__=='__main__':
  filelist = os.listdir(input_json_path+'/manual_label')
  ftrainval = open(input_json_path + '/' + 'train_point.txt', 'w')
  count=0
  for file in filelist:
    print(count)
    count+=1
    # 读json 文件
    ftrainval.write(input_json_path+'/'+'images/'+file[:-5]+'||'+input_json_path+'/clb/'+file[:-9]+'.clb'+'\n')

