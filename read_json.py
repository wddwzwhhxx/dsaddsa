# _*_coding:utf-8
import os
import json


input_json_path='/home/public/sulei/for_zhaowei/car_project_points'



def add_txt(txt_path,count):
  #print('yes')
  with open(txt_path, 'r+') as f:
   content = f.read()
   f.seek(0, 0)
   f.write('960 1280'+' '+str(count)+'\n'+content)

if __name__=='__main__':
  filelist = os.listdir(input_json_path+'/manual_label')
  for file in filelist:
    #print(file)
    # 读json 文件
    with open(input_json_path+'/manual_label'+'/'+file, 'r') as load_f:
      #对于每张图片来说
      ftrainval = open(input_json_path+'/'+'clb/'+file[:-9]+'.clb', 'w')
      load_dict = json.load(load_f)
      count=0
      if load_dict['hard']==True:
        print ('hard')
        continue
      elif 'children' in load_dict:
        for i in range(len(load_dict['children'])):
          if 'points' in load_dict['children'][i]:
            if load_dict['children'][i]['data']['property'][0]=='ignoreline':
              points=list(load_dict['children'][i]['points'].split(' '))
              #print (points)
              for j in range(len(points)):
                count+=1
                ftrainval.write(list(points[j].split(','))[1]+' '+list(points[j].split(','))[0]+' '+'255'+'\n')
            else:
              points = list(load_dict['children'][i]['points'].split(' '))
              # print (points)
              for j in range(len(points)):
                count += 1
                ftrainval.write(list(points[j].split(','))[1] + ' ' + list(points[j].split(','))[0] + ' ' + '1' + '\n')

          else:
            if load_dict['children'][i]['data']['property'][0]=='ignore':
              count+=1
              ftrainval.write(str(load_dict['children'][i]['y'])+' '+str(load_dict['children'][i]['x'])+' 255'+'\n')
            else:
              count+=1
              ftrainval.write(str(load_dict['children'][i]['y'])+' '+str(load_dict['children'][i]['x'])+' 1'+'\n')
        ftrainval.close()
        add_txt(input_json_path+'/'+'clb/'+file[:-9]+'.clb',count)
      else:
        ftrainval.write('960 1280 0 '+'\n')
        ftrainval.close()
