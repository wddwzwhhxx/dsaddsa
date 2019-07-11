import json
input_xml_list='/home/wangzhaowei/txt/train_image_message07.txt'
result=[]

current_path=None
dict={}
dict_result={}
count=0

def save_json(data,sp):
    with open(sp,'w') as outfile:
        json.dump(data,outfile,indent=4,sort_keys=False)

if __name__=='__main__':

    with open(input_xml_list, 'r') as f:
        for line in f:
            result.append(list(line.split('\n')))
    for i in range(len(result)):

        line_i=list(result[i][0].split(' '))
        image_path=line_i[0]

        width=int(line_i[1])
        height=int(line_i[2])
        x1=int(line_i[3])
        y1=int(line_i[4])
        x2=int(line_i[5])
        y2=int(line_i[6])
        conf=float(line_i[7])

        #应该储存格式了
        if image_path != current_path:
            print (count)
            if count!=0:
                save_json(dict,'/home/wangzhaowei/700000_json/'+'07'+str(count).zfill(6)+'.json')

            dict={}
            dict_result={}
            dict_result['cls_scores']=[[conf]]
            dict_result['cls_boxes']=[[x1,y1,x2,y2]]

            dict['imshape']=[height,width]
            dict['file_name']=image_path
            dict['result']=dict_result
            count += 1

            current_path=image_path
        else:
            dict_result['cls_scores'].append([conf])
            dict_result['cls_boxes'].append([x1,y1,x2,y2])

    save_json(dict,'/home/wangzhaowei/700000_json/'+'07'+str(count).zfill(6)+'.json')


