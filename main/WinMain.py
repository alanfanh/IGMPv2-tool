# -*- coding: utf-8 -*-
import sys, wmi
from scapy.contrib.igmp import *
from scapy.all import *
from Global import *
from PySide6 import QtCore,QtWidgets
from PySide6.QtCore import SIGNAL
from gui import Ui_IgmpSerV2

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui=Ui_IgmpSerV2()
        self.ui.setupUi(self)
        self.setWindowTitle(u"模拟IGMPv2-Ser发包工具")
        self.init_iface()
        self.init_config()
        self.select_iface()
        self.connect(self.ui.save_conf,SIGNAL("clicked()"),self.save_config)
        self.connect(self.ui.send_pro,SIGNAL("clicked()"),self.send_igmp)
        self.connect(self.ui.send_udp,SIGNAL("clicked()"),self.send_udp)
        self.connect(self.ui.action,QtCore.SIGNAL('triggered()'),self.about)
        self.runthread=RunThread(self)
        self.send_data=RunSendData(self)
        # self.runthread.send_singal.connect(self.show_state)
        
    def send_igmp(self):
        cur_text=self.ui.send_pro.text()
        print(cur_text)
        if cur_text == u"发送":
            self.select_iface()
            self.save_config(False)
            self.ui.send_pro.setText(u"停止")
            self.showstate(msg=u'已发送IGMP报文')
            self.runthread.start_test()
        else:
            self.runthread.stop_test()
            self.showstate(msg=u'已停止发送IGMP')
            self.ui.send_pro.setText(u"发送")
    def send_udp(self):
        text=self.ui.send_udp.text()
        print(text)
        if text == u"发送":
            self.select_iface()
            self.save_config(False)
            self.ui.send_udp.setText(u"停止")
            self.showstate(msg=u'正在发送UDP数据报文')
            self.send_data.start_test()
        else:
            self.send_data.stop_test()
            self.showstate(msg=u'已停止发送UDP数据报文')
            self.ui.send_udp.setText(u"发送")
    def init_config(self):
        #初始化GUI时，加载默认配置
        self.config=read_config()
        self.ui.data_dst.setText(self.config['igmp']['data_dst'])
        self.ui.data_src.setText(self.config['igmp']['data_src'])
        self.ui.dst_ip.setText(self.config['igmp']['dstip'])
        self.ui.src_ip.setText(self.config['igmp']['srcip'])
        self.ui.resp.setText(self.config['igmp']['resp'])
        self.ui.dport.setText(self.config['igmp']['dport'])
        self.ui.sport.setText(self.config['igmp']['sport'])
        self.ui.multicast.setText(self.config['igmp']['multicast'])
        self.ui.interval.setText(self.config['igmp']['interval'])
        self.ui.rate.setText(self.config['igmp']['rate'])
    def save_config(self,flag=True):
        #保存配置，将GUI界面上的参数保存至config.ini文件中
        guid_cfg={}
        guid_cfg['igmp']={}
        guid_cfg['igmp']['srcip']=self.ui.src_ip.text()
        guid_cfg['igmp']['dstip']=self.ui.dst_ip.text()
        guid_cfg['igmp']['multicast']=self.ui.multicast.text()
        guid_cfg['igmp']['resp']=self.ui.resp.text()
        guid_cfg['igmp']['data_src']=self.ui.data_src.text()
        guid_cfg['igmp']['data_dst']=self.ui.data_dst.text()
        guid_cfg['igmp']['sport']=self.ui.sport.text()
        guid_cfg['igmp']['dport']=self.ui.dport.text()
        guid_cfg['igmp']['interval']=self.ui.interval.text()
        guid_cfg['igmp']['rate']=self.ui.rate.text()

        init_dict=read_config()
        cfg=configparser.ConfigParser()
        for key,value in init_dict.items():
             cfg.add_section(key)
             for k,v in value.items():
                if key in guid_cfg:
                    if k in guid_cfg[key]:
                        cfg.set(key,k,guid_cfg[key][k])
                        continue
                cfg.set(key,k,v)
        with open(configfile.replace("\\","/"),"w+") as f:
            cfg.write(f)
        self.config=read_config()
        if flag:
                QtWidgets.QMessageBox.information(self,"提示",u"保存配置成功",QtWidgets.QMessageBox.Yes)
    def init_iface(self):
        #初始化网卡接口，显示至下拉列表中
        print("*****init iface*****")
        # iface_mac=self.get_ifaceMapMac()
        iface_list=self.get_iface()
        for iface in iface_list:
            self.ui.iface.addItem(iface.strip())

    def select_iface(self):
        #选择选中的网卡发包
        cur_iface=self.ui.iface.currentText()
        self.iface=cur_iface
        print(cur_iface)
    def get_iface(self):
        #获取网卡列表，返回list
        iface_list=[]
        wm=wmi.WMI()
        ifaces=wm.Win32_NetworkAdapterConfiguration (IPEnabled=1)
        for iface in ifaces:
            iface_desc=iface.Description
            iface_list.append(iface_desc)
        print(iface_list)
        return iface_list
    def get_ifaceMapMac(self,desc):
        #获取网卡接口描述与mac地址映射字典
        desc_mac={}
        mac_ip={}
        w=wmi.WMI()
        ifaces=w.Win32_NetworkAdapterConfiguration (IPEnabled=1)
        for iface in ifaces:
            desc_mac[iface.Description]=iface.MACAddress
            mac_ip[iface.MACAddress]=iface.IPADDRESS[0]
            # iface_list.append(iface_desc)
        print(desc_mac[desc])
        return desc_mac[desc]
    def get_multicast_mac(self,ip):
        mac_s='01:00:5e:'
        ip_list=ip.split('.')[1:]
        num_list=list(map(int,ip_list))
        i=0
        if num_list[0] >= 128:
            num_list[0]=num_list[0]-128
        for v in num_list:
            str=hex(v)
            if len(str)==3:
                str=str.replace("0x","0")
                num_list[i]=str
            elif len(str)==4:
                str=str.replace("0x","")
                num_list[i]=str
            i=i+1
        mac_end=':'.join(num_list)
        mac_addr=mac_s+mac_end
        return mac_addr
    def about(self):
        QtWidgets.QMessageBox.about(self,u"帮助信息",u"Auther:FanHao\n1、本工具仅支持IGMPv2，可以模拟IGMP Server发送IGMP协议报文和组播数据报文。\n2、本工具不支持解包功能。\n3、组播IP选项置空时，点击第一个发送按钮，将发送IGMP通用组查询报文。\n4、组播IP不置空时，点击第一个发送按钮，将发送特定组查询报文。\n5、点击发送按钮，线程将一直发包。直到点击停止按钮，此时发包停止。\n6、如果数据报文目的IP填写为空，程序将控制线程往地址0.0.0.0发送UDP数据报文。\n7、如果发包间隔设置为空，则后台将以默认间隔2s发送报文。")

    def showstate(self,msg):
        #状态栏显示状态信息
        self.ui.statusbar.showMessage(msg)

    def close_event(self,event):
        reply = QtWidgets.QMessageBox.question(self,'Message','Are you sure to quit?',QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class RunThread(QtCore.QThread):
    send_singal=QtCore.Signal(str)
    def __init__(self,parent):
        super(RunThread,self).__init__(parent)
        self.parent=parent
    def init_data(self):
        self.iface=self.parent.iface
        self.src_mac=self.parent.get_ifaceMapMac(self.iface)
        self.srcip=self.parent.config['igmp']['srcip']
        self.dstip=self.parent.config['igmp']['dstip']
        self.mulicast=self.parent.config['igmp']['multicast']
        self.resp=self.parent.config['igmp']['resp']
        self.interval=int(self.parent.config['igmp']['interval'])
        print(self.interval,type(self.interval))
    def start_test(self):
        self.init_data()
        self.start()
    def stop_test(self):
        self.terminate()
        self.wait()
    def run(self):
        str='000000000000000000'
        c=IGMP(type=0x11,gaddr=self.mulicast)
        if self.interval=="":
            self.interval=2
        if self.dstip=="":
            dst_mac=self.parent.get_multicast_mac(ip='224.0.0.1')
            a=Ether(src=self.src_mac,dst=dst_mac)
            b=IP(src=self.srcip,dst='224.0.0.1')
        else:
            dst_mac=self.parent.get_multicast_mac(self.dstip)
            a=Ether(src=self.src_mac,dst=dst_mac)
            b=IP(src=self.srcip,dst=self.dstip)
        pkt=a/b/c/Padding(str)
        sendp(pkt,iface=self.iface,inter=self.interval,loop=1)

class RunSendData(QtCore.QThread):
    data_singal=QtCore.Signal(str)
    def __init__(self,parent):
        super(RunSendData,self).__init__(parent)
        self.parent=parent
    def init_data(self):
        self.iface=self.parent.iface
        self.s_mac=self.parent.get_ifaceMapMac(self.iface)
        self.data_src=self.parent.config['igmp']['data_src']
        self.data_dst=self.parent.config['igmp']['data_dst']
        self.sport=int(self.parent.config['igmp']['sport'])
        print(type(self.sport))
        self.dport=int(self.parent.config['igmp']['dport'])
        self.rate=int(self.parent.config['igmp']['rate'])
    def start_test(self):
        self.init_data()
        self.start()
    def stop_test(self):
        self.terminate()
        self.wait()
    def run(self):
        str="AAAAAAAAAAAAAA0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        c=UDP(sport=self.sport,dport=self.dport)
        #构造UDP数据包，进行填充
        #第二种，抓包保存pcap文件，循环读取，发包（待确认）
        if self.rate == "":
            self.rate=2
        if self.data_dst == "":
            self.parent.showstate(msg=u'请填写目的IP')
            d_mac=self.parent.get_multicast_mac(ip='0.0.0.0')
            a=Ether(src=self.s_mac,dst=d_mac)
            b=IP(src=self.data_src,dst=self.data_dst)
            pkt=a/b/c/Raw(str)
            sendp(pkt,iface=self.iface,inter=self.rate,loop=1)
        else:
            d_mac=self.parent.get_multicast_mac(ip=self.data_dst)
            a=Ether(src=self.s_mac,dst=d_mac)
            b=IP(src=self.data_src,dst=self.data_dst)
            pkt=a/b/c/Raw(str)
            # sendpfast(pkt,iface=self.iface,mbps=self.rate,loop=1)
            sendp(pkt,iface=self.iface,inter=self.rate,loop=1)
            print('data send ok')


if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    wm=MainWindow()
    wm.show()
    sys.exit(app.exec())