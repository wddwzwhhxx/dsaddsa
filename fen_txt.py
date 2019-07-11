
result=[]
input_xml_list='/share2/public/freespace_data/fisheye_car_wheel_line_mvp_head_tail/train_w_saic.txt'


if __name__=='__main__':
    with open(input_xml_list, 'r') as f:
        for line in f:
            result.append(list(line.split('\n')))

    train1 = open('/home/wangzhaowei/txt/train1.txt', 'w')
    train2 = open('/home/wangzhaowei/txt/train2.txt', 'w')
    train3 = open('/home/wangzhaowei/txt/train3.txt', 'w')
    train4 = open('/home/wangzhaowei/txt/train4.txt', 'w')
    train5 = open('/home/wangzhaowei/txt/train5.txt', 'w')
    train6 = open('/home/wangzhaowei/txt/train6.txt', 'w')
    train7 = open('/home/wangzhaowei/txt/train7.txt', 'w')


    for i in range(len(result)):
        if i <100000:
            train1.write(result[i][0]+'\n')
        elif i <200000:
            train2.write(result[i][0]+'\n')
        elif i<300000:
            train3.write(result[i][0]+'\n')
        elif i<400000:
            train4.write(result[i][0]+'\n')
        elif i<500000:
            train5.write(result[i][0]+'\n')
        elif i<600000:
            train6.write(result[i][0]+'\n')
        else:
            train7.write(result[i][0]+'\n')