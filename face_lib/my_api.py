import os
import cv2
import numpy as np
import itertools
size = 96


# 读取文件夹中的视频目录
def read_video_names(path, video_names):
    for filename in os.listdir(path):
        if filename.endswith('.avi'):
            filename = path + '/' + filename
            video_names.append(filename)


# 读取文件夹中的图片目录
def read_pic_names(path):
    num = 0
    pic_names = []
    names = []
    for filename in os.listdir(path):
        pic_names.append(filename)
        names.append(filename.split('_')[-1])
        num = num + 1
    return num, pic_names, names


# 读取文件夹中的图片目录
def read_photo_names(path, photo_names):
    for filename in os.listdir(path):
        photo_names.append(path+'/'+filename)


# 改变图片的亮度与对比度
def relight(img, light=1, bias=0):
    w = img.shape[1]
    h = img.shape[0]
    # image = []
    for i in range(0,w):
        for j in range(0,h):
            for c in range(3):
                tmp = int(img[j,i,c]*light + bias)
                if tmp > 255:
                    tmp = 255
                elif tmp < 0:
                    tmp = 0
                img[j, i, c] = tmp
    return img


# 获取图像的边界
def get_padding_size(img):
    h, w, _ = img.shape
    top, bottom, left, right = (0, 0, 0, 0)
    longest = max(h, w)
    if w < longest:
        tmp = longest - w
        # //表示整除符号
        left = tmp // 2
        right = tmp - left
    elif h < longest:
        tmp = longest - h
        top = tmp // 2
        bottom = tmp - top
    else:
        pass
    return top, bottom, left, right


# 读取一个文件夹 把标签存放在labs,把图片存放在imgs中
# 函数返回labs, imgs
def read_data(path, h=size, w=size):
    labs = []
    imgs = []
    for filename in os.listdir(path):
        for img_name in os.listdir(path+filename):
            if img_name.endswith('.jpg'):
                path_name = path+filename + '/' + img_name
                img = cv2.imread(path_name)
                top, bottom, left, right = get_padding_size(img)
                # 将图片放大， 扩充图片边缘部分
                img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0])
                img = cv2.resize(img, (h, w))
                labs.append(filename)
                imgs.append(img)
    return labs, imgs


# 函数返回人脸标签数, 人脸数组
def get_triplet_data(path):
    names = []
    num = len(os.listdir(path))             # 获取人脸标签数
    face_array = [[] for n in range(num)]   # 初始化二维数组
    for i, filename in enumerate(os.listdir(path)):
        for img_name in os.listdir(path+filename):
            if img_name.endswith('.jpg'):
                path_name = path+filename + '/' + img_name
                img = cv2.imread(path_name)
                img = np.array(img)
                face_array[i].append(img.astype('float32') / 255.0)
        names.append(filename)
    return num, names, face_array


def generate_train_data(image_array, num):
    per_data = []
    total_data = []
    for i in range(num):
        if len(image_array[i]) == 1:            # 一个标签只有一种照片的情况
            per_data.clear()
            per_data.append(image_array[i][0])
            per_data.append(image_array[i][0])   # 加2次 防止图片只有一张时，无法形成三元组
            for n in range(num):
                if n == i:                       # 防止出现3张图片都属于同一类
                    break
                for data in image_array[n]:
                    per_data.append(data)
                    total_data.append(tuple(per_data))   # 添加一个三元组数据集
                    per_data.pop()

        elif len(image_array[i]) >= 2:              # 一个标签只有多种照片的情况
            for data_list in itertools.combinations(image_array[i], 2):
                per_data.clear()
                per_data.append(list(data_list)[0])
                per_data.append(list(data_list)[1])
                for n in range(num):
                    if n != i:                       # 防止出现3张图片都属于同一类
                        for data in image_array[n]:
                            per_data.append(data)
                            total_data.append(tuple(per_data))   # 添加一个三元组数据集
                            per_data.pop()

    return total_data


def get_anc_pos_neg_data(train_data, num):
    train_anc = []
    train_pos = []
    train_neg = []
    for i in range(num):
        # 参数：图片数据的总数，图片的高、宽、通道
        anchor, positive, negative = train_data[i]
        train_anc.append(anchor)
        train_pos.append(positive)
        train_neg.append(negative)
    return train_anc, train_pos, train_neg


# 获取图片的文件夹名字集合，存放在lab_name
# 把文件夹名字即标签转化为数字，存放在lab_full
# 函数返回标签数,人脸名称，labs
def get_num_lab(l_np_lab):
    names = []
    labs = []
    # 获取图片的文件夹名字集合，存放在lab_name
    for lab in l_np_lab:
        if lab not in names:
            names.append(lab)
    max_num = len(names)
    # 把文件夹名字即标签转化为数字
    for lab in l_np_lab:
        lab = lab.split('_')[0]
        labs.append(int(lab))
    return max_num, names, labs



