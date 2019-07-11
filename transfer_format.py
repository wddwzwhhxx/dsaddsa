# -*- coding:utf8 -*-
import os
all_txt_path='/share2/public/freespace_data/fisheye_car_wheel_line_head_tail/train_w_blank.txt'


all_result=[]
result=[]



def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        #print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        #print(path + ' 目录已存在')
        return False

def class_car_point(y1,x1,side1,head1,y2,x2,side2,head2):
    cls_a = 0
    cls_b = 0
    # 正面
    if side1 == 1 or side1 == 2:
        # a车头b车头
        if head1 == 1 and head2 == 1:
            if x1 > x2:
                cls_a = 1
                cls_b = 4
            else:
                cls_a = 4
                cls_b = 1
        # a车尾b车尾
        elif head1 == 2 and head2 == 2:
            if x1 > x2:
                cls_a = 3
                cls_b = 2
            else:
                cls_a = 2
                cls_b = 3
        else:
            cls_a = 255
            cls_b = 255
    # 侧面
    elif side1 == 3 or side1 == 4:
        # a车头b车尾
        if head1 == 1 and head2 == 2:
            if x1 > x2:
                cls_a = 4
                cls_b = 3
            else:
                cls_a = 1
                cls_b = 2
        # a车尾b车头
        elif head1 == 2 and head2 == 1:
            if x1 > x2:
                cls_a = 2
                cls_b = 1
            else:
                cls_a = 3
                cls_b = 4
        else:
            cls_a = 255
            cls_b = 255
    else:
        cls_a = 255
        cls_b = 255
    return cls_a,cls_b


def crop_point(y1,x1,side1,head1):
    crop_a=0
    if side1==1 or side1==3:
        crop_a=1
    elif side1==2 or side1==4:
        crop_a=2
    else:
        crop_a=255

    return crop_a

def class_head(side1,side2):
    if (side1 == 1 or side1 == 2 or side1 == 254) and (side2 == 1 or side2 == 2 or 254):
        side_a = 1
        side_b = 1
    elif (side1 == 3 or side1 == 4 or side2 == 255) and (side2 == 3 or side2 == 4 or 255):
        side_a = 2
        side_b = 2
    else:
        side_a = 255
        side_b = 255
    return side_a,side_b

if __name__ == '__main__':

    #mkdir('/home/wangzhaowei/hahahahaha/xixixixixi/aa')

    with open(all_txt_path, 'r') as f:
        for line in f:
            all_result.append(list(line.strip('\n').split('||')))
    fnew_clb = open('/home/wangzhaowei/data/new_clb.txt', 'w')

    for i in range(len(all_result)):
        image_path=all_result[i][0]
        fnew_clb.write(image_path+'||')
        clb_path=all_result[i][1]
        clb_name=list(clb_path.split('/'))[-1]
        clb_dir_path=clb_path[:-(len(clb_name))][:30]+'fisheye_car_wheel_line_orientation/'+clb_path[:-(len(clb_name))][30:]
        #print (clb_dir_path)

        fnew_clb.write(clb_dir_path+clb_name[:-3]+'newclb'+'\n')
        mkdir(clb_dir_path)
        result=[]
        #对于每张图
        ftrainval = open(clb_dir_path+clb_name[:-3]+'newclb', 'w')
        with open(clb_path, 'r') as f:
            for line in f:
                result.append(list(line.split('\n')))
        print(i)

        ftrainval.write(result[0][0]+'\n')
        for j in range(1,len(result)):
            cls_a=0
            cls_b=0
            crop_a=0
            crop_b=0
            y1=float(list(result[j][0].split(' '))[0])
            x1=float(list(result[j][0].split(' '))[1])
            side1=int(list(result[j][0].split(' '))[2])
            head1=int(list(result[j][0].split(' '))[3])

            y2=float(list(result[j][0].split(' '))[4])
            x2=float(list(result[j][0].split(' '))[5])
            side2=int(list(result[j][0].split(' '))[6])
            head2=int(list(result[j][0].split(' '))[7])
            cls_a,cls_b=class_car_point(y1,x1,side1,head1,y2,x2,side2,head2)
            crop_a=crop_point(y1,x1,side1,head1)
            crop_b=crop_point(y2,x2,side2,head2)
            if abs(cls_a-cls_b)==2:
                print('shit!')
            ftrainval.write(str(y1)+' '+str(x1)+' '+str(cls_a)+' '+str(crop_a)+' '+str(y2)+' '+str(x2)+' '+str(cls_b)+' '+str(crop_b)+'\n')
            #print(cls_a,cls_b,crop_a,crop_a)

    fnew_clb.close()











