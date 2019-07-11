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
        if w < 40 and h < 40:
            continue
        #elif w > 300 or h > 300:
        #    continue
        elif label==3:
            continue
        else:
            num_good+=1
    return num_good


if __name__=="__main__":
    result = []
    res=[]
    count = 0
    all_txt_path = '/share2/public/freespace_data/fisheye_car_bbox/train.txt'
    ftrainval = open('/share2/public/freespace_data/fisheye_car_bbox/my_train.txt', 'w')
    #得到文件的所有路径，存在result
    with open(all_txt_path, 'r') as f:
        for line in f:
            result.append(list(line.strip('\n').split('||')))
    with open(all_txt_path, 'r') as f:
        for line_1 in f:
            res.append(line_1.strip('\n'))
    for i in range(len(result)):
        txt_path = result[i][1]
        a=check_txt(txt_path)
        name=res[i]
        print (name)
        if a==0:
            continue
        else:
            ftrainval.write(name+'\n')
            count+=1
            print(count)
    ftrainval.close()

