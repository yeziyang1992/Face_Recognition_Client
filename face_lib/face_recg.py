import tensorflow as tf

from face_lib import my_api,inference


class Recognize:
    def __init__(self, margin=0.4):
        self.margin = margin        # 阈值
        self.siamese = inference.Siamese(96)
        self.sess = tf.Session()
        self.my_faces_path = './faces/'                # 人脸数据集目录
        self.model_ckpt = 'model/train_faces.model'    # 模型存放目录
        self.saver = tf.train.Saver()
        self.saver.restore(self.sess, self.model_ckpt)   # 加载模型
        self.max_num = 0
        self.names = None
        self.face_array = None

    def reload_data(self):
        self.max_num, self.names, self.face_array = my_api.get_triplet_data(self.my_faces_path)            # 加载人脸数据集

    def whose_face(self, test_data):
        face = [[] for n in range(self.max_num)]
        for i in range(self.max_num):
            for j, img in enumerate(self.face_array[i]):
                res = self.sess.run(self.siamese.look_like, feed_dict={
                    self.siamese.x1: [test_data],
                    self.siamese.x2: [img],
                    self.siamese.keep_f: 1.0})
                face[i].append(res)
        return face

    def get_face_id(self, face):
        new_list = []
        for n in range(self.max_num):
            face[n].sort()        # 排序
            new_list.append(face[n][0])
        min_data = min(new_list)
        if min_data < self.margin:     # 阈值为0.3
            face_id = new_list.index(min_data)
        else:
            face_id = None
        return face_id, min_data

# if __name__ == "__main__":
#     rec = Recognize()
#     rec.reload_data()
#     print(rec.names)
