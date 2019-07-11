# _*_coding:utf-8
import os

pic_path = "/home/wangzhaowei/res18_stage5_fg_bg/result"


def rename():
    piclist = os.listdir(pic_path)
    total_num = len(piclist)

    i = 1
    for pic in piclist:
        if pic.endswith(".jpg"):
            old_path = os.path.join(os.path.abspath(pic_path), pic)
            new_path = os.path.join(os.path.abspath(pic_path), str(i).zfill(6)+'.jpg')

            os.renames(old_path, new_path)
            print u"把原图片命名格式：" + old_path + u"转换为新图片命名格式：" + new_path
            # print "把原图片路径：%s,转换为新图片路径：%s" %(old_path,new_path)
            i = i + 1

    print "总共" + str(total_num) + "张图片被重命名为:" "000001.jpg~" + '000' + format(str(i - 1), '0>3') + ".jpg形式"


rename()

