import sys
from PIL import Image
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


if __name__=='__main__':
    result=[]
    all_txt_path='/share2/public/freespace_data/fisheye_car_bbox/test.txt'
    with open(all_txt_path,'r') as f:
        for line in f:
            result.append(list(line.strip('\n').split('|')))
    count=-1
    for i in range(len(result)):
        image_path=result[i][0]
        txt_path=result[i][1]
        res=[]
        #num_goodbbox=check_txt(txt_path)
        #if num_goodbbox==0:
        #    continue
        count+=1
        img=Image.open(image_path)
        save_path='/home/wangzhaowei/data/bbox_voc/JPEGImages/'+str(count).zfill(6)+'.jpg'
        #save_path='/home/wangzhaowei/data/show_photo/'+str(count).zfill(6)+'.jpg'
        img.save(save_path)
        print ('{:d}'.format(i))