# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_IgmpSerV2(object):
    def setupUi(self, IgmpSerV2):
        IgmpSerV2.setObjectName(_fromUtf8("IgmpSerV2"))
        IgmpSerV2.resize(412, 431)
        self.centralwidget = QtGui.QWidget(IgmpSerV2)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.save_conf = QtGui.QPushButton(self.centralwidget)
        self.save_conf.setGeometry(QtCore.QRect(160, 360, 75, 23))
        self.save_conf.setObjectName(_fromUtf8("save_conf"))
        self.iface = QtGui.QComboBox(self.centralwidget)
        self.iface.setGeometry(QtCore.QRect(80, 20, 311, 22))
        self.iface.setObjectName(_fromUtf8("iface"))
        self.groupBox1 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox1.setGeometry(QtCore.QRect(10, 50, 391, 141))
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))
        self.label_inter = QtGui.QLabel(self.groupBox1)
        self.label_inter.setGeometry(QtCore.QRect(210, 20, 51, 16))
        self.label_inter.setObjectName(_fromUtf8("label_inter"))
        self.resp = QtGui.QLineEdit(self.groupBox1)
        self.resp.setGeometry(QtCore.QRect(60, 110, 113, 20))
        self.resp.setObjectName(_fromUtf8("resp"))
        self.multicast = QtGui.QLineEdit(self.groupBox1)
        self.multicast.setGeometry(QtCore.QRect(60, 50, 113, 20))
        self.multicast.setObjectName(_fromUtf8("multicast"))
        self.label_multicast = QtGui.QLabel(self.groupBox1)
        self.label_multicast.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.label_multicast.setObjectName(_fromUtf8("label_multicast"))
        self.send_pro = QtGui.QPushButton(self.groupBox1)
        self.send_pro.setGeometry(QtCore.QRect(230, 60, 75, 23))
        self.send_pro.setObjectName(_fromUtf8("send_pro"))
        self.dst_ip = QtGui.QLineEdit(self.groupBox1)
        self.dst_ip.setGeometry(QtCore.QRect(60, 80, 113, 20))
        self.dst_ip.setObjectName(_fromUtf8("dst_ip"))
        self.label_srcip = QtGui.QLabel(self.groupBox1)
        self.label_srcip.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.label_srcip.setObjectName(_fromUtf8("label_srcip"))
        self.label_dstip = QtGui.QLabel(self.groupBox1)
        self.label_dstip.setGeometry(QtCore.QRect(10, 80, 41, 16))
        self.label_dstip.setObjectName(_fromUtf8("label_dstip"))
        self.src_ip = QtGui.QLineEdit(self.groupBox1)
        self.src_ip.setGeometry(QtCore.QRect(60, 20, 113, 20))
        self.src_ip.setObjectName(_fromUtf8("src_ip"))
        self.interval = QtGui.QLineEdit(self.groupBox1)
        self.interval.setGeometry(QtCore.QRect(270, 20, 113, 20))
        self.interval.setText(_fromUtf8(""))
        self.interval.setObjectName(_fromUtf8("interval"))
        self.label_resp = QtGui.QLabel(self.groupBox1)
        self.label_resp.setGeometry(QtCore.QRect(10, 110, 51, 16))
        self.label_resp.setObjectName(_fromUtf8("label_resp"))
        self.save_conf.raise_()
        self.label_inter.raise_()
        self.resp.raise_()
        self.multicast.raise_()
        self.label_multicast.raise_()
        self.send_pro.raise_()
        self.dst_ip.raise_()
        self.label_srcip.raise_()
        self.label_dstip.raise_()
        self.src_ip.raise_()
        self.interval.raise_()
        self.label_resp.raise_()
        self.groupBox2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox2.setGeometry(QtCore.QRect(10, 210, 391, 141))
        self.groupBox2.setObjectName(_fromUtf8("groupBox2"))
        self.label_rate = QtGui.QLabel(self.groupBox2)
        self.label_rate.setGeometry(QtCore.QRect(210, 20, 51, 16))
        self.label_rate.setObjectName(_fromUtf8("label_rate"))
        self.rate = QtGui.QLineEdit(self.groupBox2)
        self.rate.setGeometry(QtCore.QRect(270, 20, 113, 20))
        self.rate.setObjectName(_fromUtf8("rate"))
        self.sport = QtGui.QLineEdit(self.groupBox2)
        self.sport.setGeometry(QtCore.QRect(60, 80, 113, 20))
        self.sport.setObjectName(_fromUtf8("sport"))
        self.data_dst = QtGui.QLineEdit(self.groupBox2)
        self.data_dst.setGeometry(QtCore.QRect(60, 50, 113, 20))
        self.data_dst.setObjectName(_fromUtf8("data_dst"))
        self.label_dst = QtGui.QLabel(self.groupBox2)
        self.label_dst.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.label_dst.setObjectName(_fromUtf8("label_dst"))
        self.send_udp = QtGui.QPushButton(self.groupBox2)
        self.send_udp.setGeometry(QtCore.QRect(230, 90, 75, 23))
        self.send_udp.setObjectName(_fromUtf8("send_udp"))
        self.dport = QtGui.QLineEdit(self.groupBox2)
        self.dport.setGeometry(QtCore.QRect(60, 110, 113, 20))
        self.dport.setObjectName(_fromUtf8("dport"))
        self.label_dport = QtGui.QLabel(self.groupBox2)
        self.label_dport.setGeometry(QtCore.QRect(10, 110, 51, 16))
        self.label_dport.setObjectName(_fromUtf8("label_dport"))
        self.label_src = QtGui.QLabel(self.groupBox2)
        self.label_src.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.label_src.setObjectName(_fromUtf8("label_src"))
        self.data_src = QtGui.QLineEdit(self.groupBox2)
        self.data_src.setGeometry(QtCore.QRect(60, 20, 113, 20))
        self.data_src.setObjectName(_fromUtf8("data_src"))
        self.label_sport = QtGui.QLabel(self.groupBox2)
        self.label_sport.setGeometry(QtCore.QRect(10, 80, 41, 16))
        self.label_sport.setObjectName(_fromUtf8("label_sport"))
        IgmpSerV2.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(IgmpSerV2)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        IgmpSerV2.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(IgmpSerV2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 412, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        IgmpSerV2.setMenuBar(self.menubar)
        self.action = QtGui.QAction(IgmpSerV2)
        self.action.setObjectName(_fromUtf8("action"))
        self.menuHelp.addAction(self.action)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(IgmpSerV2)
        QtCore.QMetaObject.connectSlotsByName(IgmpSerV2)

    def retranslateUi(self, IgmpSerV2):
        IgmpSerV2.setWindowTitle(_translate("IgmpSerV2", "WinMain", None))
        self.label.setText(_translate("IgmpSerV2", "选择网卡:", None))
        self.save_conf.setText(_translate("IgmpSerV2", "保存配置", None))
        self.groupBox1.setTitle(_translate("IgmpSerV2", "IGMP报文", None))
        self.label_inter.setText(_translate("IgmpSerV2", "发包间隔", None))
        self.label_multicast.setText(_translate("IgmpSerV2", "组播IP", None))
        self.send_pro.setText(_translate("IgmpSerV2", "发送", None))
        self.label_srcip.setText(_translate("IgmpSerV2", "源IP", None))
        self.label_dstip.setText(_translate("IgmpSerV2", "目的IP", None))
        self.label_resp.setText(_translate("IgmpSerV2", "Resp", None))
        self.groupBox2.setTitle(_translate("IgmpSerV2", "数据报文", None))
        self.label_rate.setText(_translate("IgmpSerV2", "发包间隔s", None))
        self.label_dst.setText(_translate("IgmpSerV2", "目的IP", None))
        self.send_udp.setText(_translate("IgmpSerV2", "发送", None))
        self.label_dport.setText(_translate("IgmpSerV2", "目的端口", None))
        self.label_src.setText(_translate("IgmpSerV2", "源IP", None))
        self.label_sport.setText(_translate("IgmpSerV2", "源端口", None))
        self.menuHelp.setTitle(_translate("IgmpSerV2", "help", None))
        self.action.setText(_translate("IgmpSerV2", "帮助信息", None))

