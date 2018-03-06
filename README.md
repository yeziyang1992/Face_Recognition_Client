### 客户端界面
![](http://ww1.sinaimg.cn/mw690/006IYRZEly1fp331vehs7j30sj0m574b.jpg)
___
### 使用说明
1. 点击“打开本地摄像头”按钮，在“摄像头采集信息”栏目中即会显示摄像头采集到的信息。
2. 点击“打开网络摄像头”按钮，在“摄像头采集信息”栏目中即会显示通过WIFI传输到的视频信息。传输协议是UDP，目的是显示树莓派采集到的视频。
3. 在打开摄像头后，才可点击“人脸识别”按钮，点击后会显示采集后的人脸图片，会在人脸图片下方显示预测的姓名和相似度。相似度其实代表相似距离，值越小，表示越相似。相似距离大于一定距离，其姓名会显示为unknown。
4. 文字显示框会显示采集图片与已存数据集中图片的相似距离。
5. 点击“报错”功能按钮，把误识的人脸存入对应的人脸数据集中。例如：数据集中有5种人脸，分别标号为1、2、3、4、5，采集人脸其实为5号，却被误识为1、2、3、4或者unknown，这时点击“报错”按钮，把采集人脸存为5号人脸文件夹中即可。
___
### 代码思路
1. 开发环境
   * 开发平台：win10
   * 开发软件：PyCharm
   * 界面开发：PyQt5
2. 项目结构
   ![](http://ww1.sinaimg.cn/mw690/006IYRZEly1fp344pfejbj30b00dzt95.jpg)
3. 文档说明
    1. face_lib文件夹
        * align_dlib.py文件：主要进行人脸对齐。
        * face_recg.py文件： 进行人脸识别，其中阈值为20，可根据相应情况进行修改。
        * my.api.py文件： 自己写的各种函数方法。
        * udp_recv.py文件：包含进行udp协议传输视频的类。
    2. faces文件夹
        每一个类别的文件夹其命名规则是  数字_姓名，数字要连续，姓名是英文。每一个类别中可以有多张图片，但数量过多，识别过慢。
    3. model文件夹
        存放你训练的模型。
    4. gui.py文件
        一些界面相关的函数。
    5. inference.py文件
        神经网络函数。
    6. main.py文件
```python
    def get_face(self):
        flag_cam = True
        if not self.timer_camera.isActive() and not self.timer_udp_video.isActive():      # 查询摄像头
            QtWidgets.QMessageBox.warning(self, u"Warning", u"请先打开摄像头", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
            flag_cam = False
        if flag_cam:
            pic = self.pic_show
            self.face_recog.restore_data()
            if pic is not None:
                # 使用dlib自带的frontal_face_detector作为我们的特征提取器
                face_align = self.my_align.align(96, pic)
                if face_align is None:
                    QtWidgets.QMessageBox.warning(self, u"Warning", u"没有检测到人脸", buttons=QtWidgets.QMessageBox.Ok,
                                                  defaultButton=QtWidgets.QMessageBox.Ok)
                else:
                    face_align = cv2.cvtColor(face_align, cv2.COLOR_RGB2BGR)  # 转为BGR图片
                    self.pic_pre = face_align
                    # face_align = cv2.cvtColor(face_align, cv2.COLOR_BGR2RGB)  # 转为RGB图片
                    image_data = np.array(face_align)
                    image_data = image_data.astype('float32') / 255.0
                    face_like = self.face_recog.whose_face(image_data)                    # 识别人脸
                    for i in range(4):
                        print('%s: %s' % (i, face_like[i]))
                        self.textEdit.append(str(i))
                        self.textEdit.append(str(face_like[i]))
                    face_id, distance = self.face_recog.get_face_id(face_like)
                    if face_id is not None:
                        self.label_name.setText(str(self.names[face_id]))
                    else:
                        self.label_name.setText('unknown')
                    self.label_look.setText(str(distance))
                    face_align = cv2.cvtColor(face_align, cv2.COLOR_BGR2RGB)  # 转为RGB图片
                    showimage = QtGui.QImage(face_align.data, face_align.shape[1], face_align.shape[0],
                                            QtGui.QImage.Format_RGB888)
                    self.label_face.setPixmap(QtGui.QPixmap.fromImage(showimage))
            else:
                QtWidgets.QMessageBox.warning(self, u"Warning", u"没有检测到图片", buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
```
    
    重点说说这个函数，首先查询摄像头是否打开，如果打开了，就获取当前显示的一帧当作照片，然后检测是否有人脸，检测了人脸后分别与数据集中的人脸进行一一比对，然后输出相似距离最低的姓名。
    注意：如下程序中的4代表faces文件夹中的人脸标签数，可自行修改。
    
```python
 for i in range(4):
    print('%s: %s' % (i, face_like[i]))
    self.textEdit.append(str(i))
    self.textEdit.append(str(face_like[i]))
face_id, distance = self.face_recog.get_face_id(face_like)
```
