from PIL import Image
import os
import cv2
all_txt_path='/home/wangzhaowei/data/new_clb.txt'

result=[]

num_list=[[772.496,384.411], [ 864.506,430.117], [1141.84,616.785]]
if __name__== '__main__':
    img = cv2.imread('/data/m18_data/YSG_DATA/IMAGES/20190619_17.25--19.35_night_5/camera_test_b03/12776.jpg')
    for i in range(len(num_list)):
        cv2.circle(img, (int(num_list[i][0]), int(num_list[i][1])), 2, (255, 0, 255), 1)
    cv2.imwrite('/home/wangzhaowei/vis.jpg', img)
    '''
    with open(all_txt_path,'r') as f:
        for line in f:
            result.append(line.strip('\n').split('||'))


    for i in range(200,400):
        image_path=result[i][0]
        img=cv2.imread(image_path)
        clb_path=result[i][1]
        clb_name=list(clb_path.split('/'))[-1]
        save_path='/home/wangzhaowei/data/vis_image_point/'+clb_name[:-6]+'jpg'
        #print (save_path)
        res=[]

        print(i)
        with open(clb_path, 'r') as f:
            for line in f:
                res.append(line.strip('\n'))
        #print (res)

        for i in range(1,len(res)):

            y1=float(list(res[i].split(' '))[0])
            x1=float(list(res[i].split(' '))[1])
            class1=float(list(res[i].split(' '))[2])
            head1=int(list(res[i].split(' '))[3])
            y2=float(list(res[i].split(' '))[4])
            x2=float(list(res[i].split(' '))[5])
            class2=float(list(res[i].split(' '))[6])
            if class1==1:
                cv2.circle(img, (int(x1),int(y1)), 2, (255,255,255), 1)
                #cv2.putText(img, str(i)+'|'+str(class1), (int(x1),int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            if class1==2:
                cv2.circle(img, (int(x1), int(y1)), 2, (0, 255, 0), 1)
                #cv2.putText(img, str(i)+'|'+str(class1), (int(x1),int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            if class1 == 3:
                cv2.circle(img, (int(x1), int(y1)), 2, (255, 0, 0), 1)
                #cv2.putText(img, str(i)+'|'+str(class1), (int(x1),int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            if class1 == 4:
                cv2.circle(img, (int(x1), int(y1)), 2, (0, 0, 255), 1)
                #cv2.putText(img, str(i)+'|'+str(class1), (int(x1),int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            if head1 ==1:
                cv2.line(img, (int(x1),int(y1)), (int(x2),int(y2)), (0,0,255), 1, 8)
            elif head1 ==2 :
                cv2.line(img, (int(x1),int(y1)), (int(x2),int(y2)), (0,255,0), 1, 8)
            else:
                cv2.line(img, (int(x1),int(y1)), (int(x2),int(y2)), (255,255,255), 1, 8)



        cv2.imwrite(save_path,img)
    '''
