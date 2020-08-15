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
        
                #��Ȼ�����ݼ���������1-255��ʾ��ɫ�������ΪY
                if res > 0 :
                    wf.write(" Y ")
                else:
                    wf.write(" 0 ")

                #����ͼƬ��28�У�����ڴ˽��л���
                if out_count % 28 == 0 :
                    wf.write("\n")

                cur_pos += strlen
                out_count += 1

trans_to_txt("../data/train-images.idx3-ubyte", "image.txt", 1)

