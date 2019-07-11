save_dir='/home/wangzhaowei/data/ofo_data/result/'
input_dir='/home/wangzhaowei/data/ofo_data/all-image/'
input_txt_path='/home/wangzhaowei/data/test_save_dir/ofo_data.txt'
import cv2
import os

if __name__=='__main__':
    result=[]
    bboxs=[]
    ftrainval = open('/home/wangzhaowei/data/ofo_data/image_0.9_list.txt', 'w')

    #for filename in os.listdir(input_dir):
        # print(filename) #just for test
        # img is used to store the image data
        #img = cv2.imread(input_dir + "/" + filename)
        #count+=1

    with open(input_txt_path, 'r') as f:
        for line in f:
            result.append(list(line.split('\n')))
    #print result
    count=-1
    flag=0
    j=0
    for i in range(len(result)):
        print(len(result[i][0]))
        if len(result[i][0])==22:
            print (1)
            if count>=0:
                image = cv2.imread(input_dir + str(count).zfill(6) + '.jpg')
                flag=0
                for bbox in bboxs:
                    if float(bbox[4])>0.95:
                        flag+=1
                        #cv2.rectangle(image, (int(float(bbox[0])), int(float(bbox[1]))), (int(float(bbox[2])), int(float(bbox[3]))), (0, 204, 0), 2)
                if flag>0:
                    cv2.imwrite(save_dir + str(count).zfill(6) + '.jpg', image)
                    ftrainval.write('/home/public/wangzhaowei/ofo_data_0.9/'+str(count).zfill(6) + '.jpg'+'\n')
            bboxs=[]
            count += 1
        else:
            print(i)
            bboxs.append(list(result[i][0].split(' ')))
            #print (bboxs)
