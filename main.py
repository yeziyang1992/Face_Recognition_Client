import sys
import time
import cv2
import os
import numpy as np
from PyQt5 import QtWidgets, QtCore, QtGui
from face_lib import align_dlib, face_recg
from face_lib.udp_recv import UdpGetVideo
# import helpers
from gui import Ui_widget


class MyDesignerShow(QtWidgets.QWidget, Ui_widget):
    _signal = QtCore.pyqtSignal(int)

    def __init__(self):
        super(MyDesignerShow, self).__init__()
        self.timer_camera = QtCore.QTimer()   # 本地摄像头定时器
        self.timer_udp_video = QtCore.QTimer()  # UDP获取视频定时器
        self.cap = cv2.VideoCapture()         # 获得摄像头对象
        self.CAM_NUM = 0                      # 获取摄像头编号
        self.time = time                      # 获取时间对象
        self.PREDICTOR_PATH = './face_lib/shape_predictor_68_face_landmarks.dat'  # 关键点提取模型路径
        self.my_align = align_dlib.AlignDlib(self.PREDICTOR_PATH)     # 获取人脸对齐对象
        self.pix = QtGui.QPixmap()           # 获取QPixmap对象
        self.pic_show = None
        self.face_photo = None               # 人脸图片
        self.face_recog = face_recg.Recognize()  # 获取人脸识别对象

        self.setupUi(self)                          # 加载窗体
        self.btn_close.clicked.connect(self.close)   # 关闭程序
        self.btn_local_camera.clicked.connect(self.get_local_camera)   # 打开本地相机
        self.btn_web_camera.clicked.connect(self.get_udp_video)       # 打开UDP视频数据
        self.btn_get_face.clicked.connect(self.get_face)              # 得到人脸图像
        self.btn_debug.clicked.connect(self.debug)                    # 报错
        self.btn_new_face.clicked.connect(self.new_face)                # 新建人脸数据
        self.btn_face_recognize.clicked.connect(self.face_recognize)           # 人脸识别

        self.timer_camera.timeout.connect(self.show_local_camera)  # 计时结束调用show_camera()方法
        self.timer_udp_video.timeout.connect(self.show_udp_video)  # 计时结束调用show_udp_video()方法

    # 获取本地摄像头视频
    def get_local_camera(self):
        if self.timer_udp_video.isActive():      # 查询网络摄像头是否打开
            QtWidgets.QMessageBox.warning(self, u"Warning", u"请先关闭网络摄像头", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)

        elif not self.timer_camera.isActive():
            flag = self.cap.open(self.CAM_NUM)
            if not flag:
                QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确", buttons=QtWidgets.QMessageBox.Ok,
                                                defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(30)     # 30ms刷新一次
                self.btn_local_camera.setText(u'关闭本地摄像头')

        else:
            self.timer_camera.stop()    # 定时器关闭
            self.cap.release()          # 摄像头释放
            self.label_camera.clear()   # 视频显示区域清屏
            self.graphicsView.show()
            self.btn_local_camera.setText(u'打开本地摄像头')

    def show_local_camera(self):
        flag, image = self.cap.read()
        self.pic_show = cv2.resize(image, (640, 480))
        self.pic_show = cv2.cvtColor(self.pic_show, cv2.COLOR_BGR2RGB)
        showimage = QtGui.QImage(self.pic_show.data, self.pic_show.shape[1], self.pic_show.shape[0], QtGui.QImage.Format_RGB888)
        self.graphicsView.close()
        self.label_camera.setPixmap(self.pix.fromImage(showimage))

    def get_udp_video(self):
        if self.timer_camera.isActive():      # 查询本地摄像头
            QtWidgets.QMessageBox.warning(self, u"Warning", u"请先关闭本地摄像头", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
        elif not self.timer_udp_video.isActive():
            self.time.sleep(1)
            self.udp_video = UdpGetVideo()  # 获取udp视频对象
            self.timer_udp_video.start(30)     # 10ms刷新一次
            self.btn_web_camera.setText(u'关闭网络摄像头')

        else:
            self.timer_udp_video.stop()    # 定时器关闭
            self.udp_video.close()         # udp视频接受关闭
            self.label_camera.clear()      # 视频显示区域清屏
            self.graphicsView.show()
            self.btn_web_camera.setText(u'打开网络摄像头')

    def show_udp_video(self):

        image = self.udp_video.receive()
        # 从内存缓存区中读取图像
        decimg = cv2.imdecode(image, 1)
        self.pic_show = cv2.resize(decimg, (640, 480))
        self.pic_show = cv2.cvtColor(self.pic_show, cv2.COLOR_BGR2RGB)
        showimage = QtGui.QImage(self.pic_show.data, self.pic_show.shape[1], self.pic_show.shape[0], QtGui.QImage.Format_RGB888)
        self.graphicsView.close()
        self.label_camera.setPixmap(self.pix.fromImage(showimage))

    def get_face(self):
        flag_cam = True
        if not self.timer_camera.isActive() and not self.timer_udp_video.isActive():      # 查询摄像头
            QtWidgets.QMessageBox.warning(self, u"Warning", u"请先打开摄像头", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
            flag_cam = False
        if flag_cam:
            pic = self.pic_show
            if pic is not None:
                # 使用dlib自带的frontal_face_detector作为我们的特征提取器
                face_align = self.my_align.align(96, pic)
                if face_align is None:
                    QtWidgets.QMessageBox.warning(self, u"Warning", u"没有检测到人脸", buttons=QtWidgets.QMessageBox.Ok,
                                                  defaultButton=QtWidgets.QMessageBox.Ok)
                else:
                    face_align = cv2.cvtColor(face_align, cv2.COLOR_RGB2BGR)  # 转为BGR图片
                    self.face_photo = face_align
                    face_align = cv2.cvtColor(face_align, cv2.COLOR_BGR2RGB)  # 转为RGB图片
                    showimage = QtGui.QImage(face_align.data, face_align.shape[1], face_align.shape[0],
                                             QtGui.QImage.Format_RGB888)
                    self.label_face.setPixmap(QtGui.QPixmap.fromImage(showimage))
            else:
                QtWidgets.QMessageBox.warning(self, u"Warning", u"没有检测到图片", buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)

    def face_recognize(self):
        if self.face_photo is None:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"请先获取人脸图片", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            self.face_recog.reload_data()         # 重载人脸数据集
            names = self.face_recog.names
            if len(names) < 1:
                QtWidgets.QMessageBox.warning(self, u"Warning", u"数据集为空！", buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                image_data = np.array(self.face_photo)
                image_data = image_data.astype('float32') / 255.0
                face_like = self.face_recog.whose_face(image_data)                    # 识别人脸
                for i in range(len(names)):
                    print('姓名：%s   欧式距离： %s' % (names[i], face_like[i]))
                    self.textEdit.append("姓名：" + str(names[i]) + "    欧式距离： " + str(face_like[i]))
                face_id, distance = self.face_recog.get_face_id(face_like)
                if face_id is not None:
                    self.label_name.setText(str(names[face_id]))
                else:
                    self.label_name.setText('unknown')
                self.label_look.setText(str(distance))

    def new_face(self):
        text, ok = QtWidgets.QInputDialog.getText(self, '英文字符！', '请输入你的英文名字：')
        if ok:
            print(text)
            if self.face_photo is not None:
                # 创建文件夹
                paths = './faces/' + text + '/'
                if not os.path.exists(paths):
                    os.makedirs(paths)
                    # 保存图片
                    s_time = time.ctime().replace(' ', '_').replace(':', '_')
                    cv2.imwrite(str(paths) + str(s_time) + '.jpg', self.face_photo)
                    self.textEdit.append("人脸已存放在 " + paths + ' 文件夹中！！')
                else:
                    QtWidgets.QMessageBox.warning(self, u"Warning", u"数据集中已有相同人名！",
                                                  buttons=QtWidgets.QMessageBox.Ok,
                                                  defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"输入错误", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)

    def debug(self):
        self.face_recog.reload_data()  # 重载人脸数据集
        num = self.face_recog.max_num
        file_names = self.face_recog.names
        print(file_names)
        if num > 0:
            result, ok = QtWidgets.QInputDialog.getItem(self, u"人脸数据校验", u"把人脸数据存入对应的文件夹中，可增加人脸识别的准确性。确定把图片存放在以下文件夹中吗？",
                                                        file_names, 1, False)
            if ok:
                if self.face_photo is not None:
                    # 保存图片
                    s_time = time.ctime().replace(' ', '_').replace(':', '_')
                    cv2.imwrite('./faces/' + result + '/' + str(s_time) + '.jpg', self.face_photo)
                    self.textEdit.append("已保存在./faces/" + result + '文件夹下!!')
        else:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"数据集为空,请新建人脸数据！", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)

    def closeEvent(self, event):
        ok = QtWidgets.QPushButton()
        cacel = QtWidgets.QPushButton()

        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u"关闭", u"是否关闭！")

        msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cacel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'确定')
        cacel.setText(u'取消')
        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            event.ignore()
        else:
            if self.cap.isOpened():
                self.cap.release()
            if self.timer_camera.isActive():
                self.timer_camera.stop()
            if self.timer_udp_video.isActive():
                self.timer_udp_video.stop()
            event.accept()


if __name__ == "__main__":
    if not os.path.exists("./faces"):
        os.makedirs("./faces")
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyDesignerShow()    # 创建实例
    myshow.show()           # 使用Qidget的show()方法
    sys.exit(app.exec_())

