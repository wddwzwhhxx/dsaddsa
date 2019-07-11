from PIL import Image
all_txt_path='/home/wangzhaowei/gitlab/mcdk/det/faster_rcnn/list/check.list'

result=[]
with open(all_txt_path, 'r') as f:
    for line in f:
        result.append(line.strip('\n'))
print result[0]
out_path='/home/wangzhaowei/images/'
for i in range(len(result)):
    image_path = '/data/m18_data/3MF_DATA/ORIGIN_IMAGE/'+ result[i]
    img = Image.open(image_path)
    save_path = out_path + str(i).zfill(6) + '.jpg'
    img.save(save_path)
    print (i)