# -*- coding:utf8 -*-

import os

class BatchRename():
    '''
    批量重命名文件夹中的图片文件
    '''
    def __init__(self):
        self.path = '/home/wangzhaowei/data/bishe/xml/xml12'
        self.group = 0

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 1
        for item in filelist:
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), '12'+item)
                print(dst)
                os.rename(src, dst)
                #print 'converting %s to %s ...' % (src, dst)
                i+=1

        #print 'total %d to rename & converted %d jpgs' % (total_num, i)

if __name__ == '__main__':

    demo = BatchRename()
    demo.rename()
