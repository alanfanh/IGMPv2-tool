# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_IgmpSerV2(object):
    def setupUi(self, IgmpSerV2):
        if not IgmpSerV2.objectName():
            IgmpSerV2.setObjectName(u"IgmpSerV2")
        IgmpSerV2.resize(412, 431)
        IgmpSerV2.setMinimumSize(QSize(412, 431))
        IgmpSerV2.setMaximumSize(QSize(412, 431))
        self.action = QAction(IgmpSerV2)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(IgmpSerV2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 54, 12))
        self.save_conf = QPushButton(self.centralwidget)
        self.save_conf.setObjectName(u"save_conf")
        self.save_conf.setGeometry(QRect(160, 360, 75, 23))
        self.iface = QComboBox(self.centralwidget)
        self.iface.setObjectName(u"iface")
        self.iface.setGeometry(QRect(80, 20, 311, 22))
        self.groupBox1 = QGroupBox(self.centralwidget)
        self.groupBox1.setObjectName(u"groupBox1")
        self.groupBox1.setGeometry(QRect(10, 50, 391, 141))
        self.label_inter = QLabel(self.groupBox1)
        self.label_inter.setObjectName(u"label_inter")
        self.label_inter.setGeometry(QRect(210, 20, 51, 16))
        self.resp = QLineEdit(self.groupBox1)
        self.resp.setObjectName(u"resp")
        self.resp.setGeometry(QRect(60, 110, 113, 20))
        self.multicast = QLineEdit(self.groupBox1)
        self.multicast.setObjectName(u"multicast")
        self.multicast.setGeometry(QRect(60, 50, 113, 20))
        self.label_multicast = QLabel(self.groupBox1)
        self.label_multicast.setObjectName(u"label_multicast")
        self.label_multicast.setGeometry(QRect(10, 50, 41, 16))
        self.send_pro = QPushButton(self.groupBox1)
        self.send_pro.setObjectName(u"send_pro")
        self.send_pro.setGeometry(QRect(230, 60, 75, 23))
        self.dst_ip = QLineEdit(self.groupBox1)
        self.dst_ip.setObjectName(u"dst_ip")
        self.dst_ip.setGeometry(QRect(60, 80, 113, 20))
        self.label_srcip = QLabel(self.groupBox1)
        self.label_srcip.setObjectName(u"label_srcip")
        self.label_srcip.setGeometry(QRect(10, 20, 31, 16))
        self.label_dstip = QLabel(self.groupBox1)
        self.label_dstip.setObjectName(u"label_dstip")
        self.label_dstip.setGeometry(QRect(10, 80, 41, 16))
        self.src_ip = QLineEdit(self.groupBox1)
        self.src_ip.setObjectName(u"src_ip")
        self.src_ip.setGeometry(QRect(60, 20, 113, 20))
        self.interval = QLineEdit(self.groupBox1)
        self.interval.setObjectName(u"interval")
        self.interval.setGeometry(QRect(270, 20, 113, 20))
        self.label_resp = QLabel(self.groupBox1)
        self.label_resp.setObjectName(u"label_resp")
        self.label_resp.setGeometry(QRect(10, 110, 51, 16))
        self.groupBox2 = QGroupBox(self.centralwidget)
        self.groupBox2.setObjectName(u"groupBox2")
        self.groupBox2.setGeometry(QRect(10, 210, 391, 141))
        self.label_rate = QLabel(self.groupBox2)
        self.label_rate.setObjectName(u"label_rate")
        self.label_rate.setGeometry(QRect(210, 20, 51, 16))
        self.rate = QLineEdit(self.groupBox2)
        self.rate.setObjectName(u"rate")
        self.rate.setGeometry(QRect(270, 20, 113, 20))
        self.sport = QLineEdit(self.groupBox2)
        self.sport.setObjectName(u"sport")
        self.sport.setGeometry(QRect(60, 80, 113, 20))
        self.data_dst = QLineEdit(self.groupBox2)
        self.data_dst.setObjectName(u"data_dst")
        self.data_dst.setGeometry(QRect(60, 50, 113, 20))
        self.label_dst = QLabel(self.groupBox2)
        self.label_dst.setObjectName(u"label_dst")
        self.label_dst.setGeometry(QRect(10, 50, 41, 16))
        self.send_udp = QPushButton(self.groupBox2)
        self.send_udp.setObjectName(u"send_udp")
        self.send_udp.setGeometry(QRect(230, 90, 75, 23))
        self.dport = QLineEdit(self.groupBox2)
        self.dport.setObjectName(u"dport")
        self.dport.setGeometry(QRect(60, 110, 113, 20))
        self.label_dport = QLabel(self.groupBox2)
        self.label_dport.setObjectName(u"label_dport")
        self.label_dport.setGeometry(QRect(10, 110, 51, 16))
        self.label_src = QLabel(self.groupBox2)
        self.label_src.setObjectName(u"label_src")
        self.label_src.setGeometry(QRect(10, 20, 31, 16))
        self.data_src = QLineEdit(self.groupBox2)
        self.data_src.setObjectName(u"data_src")
        self.data_src.setGeometry(QRect(60, 20, 113, 20))
        self.label_sport = QLabel(self.groupBox2)
        self.label_sport.setObjectName(u"label_sport")
        self.label_sport.setGeometry(QRect(10, 80, 41, 16))
        IgmpSerV2.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(IgmpSerV2)
        self.statusbar.setObjectName(u"statusbar")
        IgmpSerV2.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(IgmpSerV2)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 412, 22))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        IgmpSerV2.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.action)

        self.retranslateUi(IgmpSerV2)

        QMetaObject.connectSlotsByName(IgmpSerV2)
    # setupUi

    def retranslateUi(self, IgmpSerV2):
        IgmpSerV2.setWindowTitle(QCoreApplication.translate("IgmpSerV2", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("IgmpSerV2", u"\u5e2e\u52a9\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("IgmpSerV2", u"\u9009\u62e9\u7f51\u5361:", None))
        self.save_conf.setText(QCoreApplication.translate("IgmpSerV2", u"\u4fdd\u5b58\u914d\u7f6e", None))
        self.groupBox1.setTitle(QCoreApplication.translate("IgmpSerV2", u"IGMP\u62a5\u6587", None))
        self.label_inter.setText(QCoreApplication.translate("IgmpSerV2", u"\u53d1\u5305\u95f4\u9694", None))
        self.label_multicast.setText(QCoreApplication.translate("IgmpSerV2", u"\u7ec4\u64adIP", None))
        self.send_pro.setText(QCoreApplication.translate("IgmpSerV2", u"\u53d1\u9001", None))
        self.label_srcip.setText(QCoreApplication.translate("IgmpSerV2", u"\u6e90IP", None))
        self.label_dstip.setText(QCoreApplication.translate("IgmpSerV2", u"\u76ee\u7684IP", None))
        self.interval.setText("")
        self.label_resp.setText(QCoreApplication.translate("IgmpSerV2", u"Resp", None))
        self.groupBox2.setTitle(QCoreApplication.translate("IgmpSerV2", u"\u6570\u636e\u62a5\u6587", None))
        self.label_rate.setText(QCoreApplication.translate("IgmpSerV2", u"\u901f\u7387Mbps", None))
        self.label_dst.setText(QCoreApplication.translate("IgmpSerV2", u"\u76ee\u7684IP", None))
        self.send_udp.setText(QCoreApplication.translate("IgmpSerV2", u"\u53d1\u9001", None))
        self.label_dport.setText(QCoreApplication.translate("IgmpSerV2", u"\u76ee\u7684\u7aef\u53e3", None))
        self.label_src.setText(QCoreApplication.translate("IgmpSerV2", u"\u6e90IP", None))
        self.label_sport.setText(QCoreApplication.translate("IgmpSerV2", u"\u6e90\u7aef\u53e3", None))
        self.menuHelp.setTitle(QCoreApplication.translate("IgmpSerV2", u"help", None))
    # retranslateUi

