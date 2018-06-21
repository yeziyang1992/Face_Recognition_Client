# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(1024, 768)
        widget.setMinimumSize(QtCore.QSize(1024, 768))
        widget.setMaximumSize(QtCore.QSize(1024, 768))
        self.label_camera = QtWidgets.QLabel(widget)
        self.label_camera.setEnabled(True)
        self.label_camera.setGeometry(QtCore.QRect(360, 40, 640, 480))
        self.label_camera.setMinimumSize(QtCore.QSize(640, 480))
        self.label_camera.setMaximumSize(QtCore.QSize(640, 480))
        self.label_camera.setText("")
        self.label_camera.setObjectName("label_camera")
        self.textEdit = QtWidgets.QTextEdit(widget)
        self.textEdit.setGeometry(QtCore.QRect(360, 550, 641, 181))
        self.textEdit.setObjectName("textEdit")
        self.graphicsView = QtWidgets.QGraphicsView(widget)
        self.graphicsView.setGeometry(QtCore.QRect(360, 40, 640, 480))
        self.graphicsView.setMinimumSize(QtCore.QSize(640, 480))
        self.graphicsView.setMaximumSize(QtCore.QSize(640, 480))
        self.graphicsView.setObjectName("graphicsView")
        self.label_2 = QtWidgets.QLabel(widget)
        self.label_2.setGeometry(QtCore.QRect(640, 20, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(widget)
        self.label_3.setGeometry(QtCore.QRect(630, 530, 111, 20))
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(widget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 430, 281, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_name = QtWidgets.QLabel(self.layoutWidget)
        self.label_name.setText("")
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 1, 1, 1)
        self.label_look = QtWidgets.QLabel(self.layoutWidget)
        self.label_look.setText("")
        self.label_look.setObjectName("label_look")
        self.gridLayout.addWidget(self.label_look, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_face = QtWidgets.QLabel(widget)
        self.label_face.setEnabled(True)
        self.label_face.setGeometry(QtCore.QRect(50, 210, 96, 96))
        self.label_face.setMinimumSize(QtCore.QSize(96, 96))
        self.label_face.setMaximumSize(QtCore.QSize(96, 96))
        self.label_face.setObjectName("label_face")
        self.textEdit_2 = QtWidgets.QTextEdit(widget)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 550, 281, 181))
        self.textEdit_2.setObjectName("textEdit_2")
        self.layoutWidget1 = QtWidgets.QWidget(widget)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 70, 281, 121))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_local_camera = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_local_camera.setObjectName("btn_local_camera")
        self.gridLayout_2.addWidget(self.btn_local_camera, 0, 0, 1, 1)
        self.btn_web_camera = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_web_camera.setObjectName("btn_web_camera")
        self.gridLayout_2.addWidget(self.btn_web_camera, 1, 0, 1, 1)
        self.btn_close = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_close.setObjectName("btn_close")
        self.gridLayout_2.addWidget(self.btn_close, 2, 0, 1, 1)
        self.btn_get_face = QtWidgets.QPushButton(widget)
        self.btn_get_face.setEnabled(True)
        self.btn_get_face.setGeometry(QtCore.QRect(230, 220, 91, 41))
        self.btn_get_face.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_get_face.setMaximumSize(QtCore.QSize(100, 60))
        self.btn_get_face.setObjectName("btn_get_face")
        self.btn_face_recognize = QtWidgets.QPushButton(widget)
        self.btn_face_recognize.setGeometry(QtCore.QRect(230, 280, 91, 41))
        self.btn_face_recognize.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_face_recognize.setMaximumSize(QtCore.QSize(16777215, 100))
        self.btn_face_recognize.setObjectName("btn_face_recognize")
        self.btn_new_face = QtWidgets.QPushButton(widget)
        self.btn_new_face.setGeometry(QtCore.QRect(50, 350, 80, 31))
        self.btn_new_face.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_new_face.setObjectName("btn_new_face")
        self.btn_debug = QtWidgets.QPushButton(widget)
        self.btn_debug.setGeometry(QtCore.QRect(230, 350, 91, 31))
        self.btn_debug.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_debug.setObjectName("btn_debug")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.label_2.setText(_translate("widget", "摄像头采集信息"))
        self.label_3.setText(_translate("widget", "调试信息显示窗口"))
        self.label_5.setText(_translate("widget", "    欧式距离:"))
        self.label.setText(_translate("widget", "    预测姓名:"))
        self.label_face.setText(_translate("widget", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; vertical-align:sub;\">人脸图片</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">说明：</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.初次使用软件，请确保model文件夹存有训练好的权重</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.初次使用请新建人脸数据，名字必须为英文字符</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3.欧式距离越大，代表越不相似，越小代表越相似</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">4.每次点击</span><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">人脸识别</span><span style=\" font-size:8pt;\">前都必须先</span><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">获取人脸</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">步骤：</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.打开本地摄像头或者网络摄像头</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.点击获取人脸</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3.点击人脸识别</span></p></body></html>"))
        self.btn_local_camera.setText(_translate("widget", "打开本地摄像头"))
        self.btn_web_camera.setText(_translate("widget", "打开网络摄像头"))
        self.btn_close.setText(_translate("widget", "关闭程序"))
        self.btn_get_face.setText(_translate("widget", "获取人脸"))
        self.btn_face_recognize.setText(_translate("widget", "人脸识别"))
        self.btn_new_face.setText(_translate("widget", "新建人脸数据"))
        self.btn_debug.setText(_translate("widget", "报错"))

