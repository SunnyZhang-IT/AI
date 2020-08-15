# -*- coding: UTF-8 -*-
def trans_to_txt(train_file, txt_file, index):
     
    with open(train_file, 'rb') as sf:
        with open(txt_file, "w") as wf:
            offset = 16 + (28*28*index)
            cur_pos = offset
            count = 28*28
            strlen = 1 
            out_count = 1
            while cur_pos < offset+count:
                sf.seek(cur_pos)
                data = sf.read(strlen)
                res = int(data[0])
        
                #虽然在数据集中像素是1-255表示颜色，这里简化为Y
                if res > 0 :
                    wf.write(" Y ")
                else:
                    wf.write(" 0 ")

                #由于图片是28列，因此在此进行换行
                if out_count % 28 == 0 :
                    wf.write("\n")

                cur_pos += strlen
                out_count += 1

trans_to_txt("../data/train-images.idx3-ubyte", "image.txt", 1)

