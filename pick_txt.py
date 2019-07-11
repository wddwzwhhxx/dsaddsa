from PIL import Image
all_txt_path='/home/wangzhaowei/data/new_clb.txt'
my_txt_path='/home/wangzhaowei/data/'

result=[]

def select_md5(txt):
    a=list(txt.split('||'))[0]
    b=list(a.split('/'))[-1]
    output=list(b.split('_'))[-1]
    return output


if __name__== '__main__':

    with open(all_txt_path,'r') as f:
        for line in f:
            result.append(line.strip('\n'))

    ftrainval = open('/home/wangzhaowei/data/18000_clb.txt', 'w')
    for i in range(20000):
        ftrainval.write(result[i]+'\n')
        print (i)

    '''
    for i in range(1,9):
        res=[]
        with open(all_txt_path+str(i)+'.list', 'r') as f:
            for line in f:
                res.append(line.strip('\n'))

        for i in range(len(res)):
            name=res[i]
            ftrainval.write('/data/m18_data/3MF_DATA/ORIGIN_IMAGE'+name+'\n')
            print(i)
    '''
