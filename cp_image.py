from PIL import Image


input_txt = '/home/wangzhaowei/data/true_VOCdevkit/VOC2007/ImageSets/Main/train.txt'
save_txt= '/home/wangzhaowei/data/true_VOCdevkit/VOC2007/ImageSets/Main/train.xml'
result=[]


#new_txt=open('/home/wangzhaowei/data/new_check_all_list.txt','w')








####################
# 逐行修改txt




if __name__=='__main__':
    '''
    with open(input_txt, 'r') as f:
        for line in f:
            result.append(line.strip('\n'))
    for i in range(len(result)):
        print(i)
        img=Image.open(result[i])
        save_path='/home/wangzhaowei/data/ofo_data/all-image/'+str(i).zfill(6)+'.jpg'
        img.save(save_path)
    '''
    with open(input_txt, 'r') as f:
        for line in f:
            result.append(line.strip('\n'))
    #print (result[0])
    tss=open(save_txt,'w')
    for i in range(len(result)):
        a=result[i]+'.xml'
        print(a)
        tss.write(a+'\n')
        print (i+1)

