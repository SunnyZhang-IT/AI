# -*- coding: utf-8 -*-
import os
import struct
import numpy as np

# 读取数据集，以二维数组的方式返回图片信息和标签信息
def load_mnist(path, kind='train'):
    """Load MNIST data from `path`"""
    labels_path = os.path.join(path,
                               '%s-labels.idx1-ubyte'
                               % kind)
    images_path = os.path.join(path,
                               '%s-images.idx3-ubyte'
                               % kind)
    with open(labels_path, 'rb') as lbpath:
        magic, n = struct.unpack('>II',
                                 lbpath.read(8))
        labels = np.fromfile(lbpath,
                             dtype=np.uint8)

    with open(images_path, 'rb') as imgpath:
        magic, num, rows, cols = struct.unpack('>IIII',
                                               imgpath.read(16))
        images = np.fromfile(imgpath,
                             dtype=np.uint8).reshape(len(labels), 784)

    return images, labels

# 在终端打印某个图片的数据信息
def print_image(data, index):
    idx = 0;
    count = 0;
    for item in data[index]:
        if count % 28 == 0:
            print("")

        if item > 0:
            print("\033[7;31mY \033[0m", end="")
        else:
            print("0 ", end="")
        
        count += 1

def main():
    cur_path = os.getcwd()
    cur_path = os.path.join(cur_path, "..\data")
    imgs, labels = load_mnist(cur_path)
    print_image(imgs, 0)


if __name__ == "__main__":
    main()
