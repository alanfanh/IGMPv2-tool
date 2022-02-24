#encoding=utf-8
import sys,os,time
import configparser

def cur_file_dir():
    #获取当前路径
    path=sys.path[0]
    if os.path.isdir(path):
        print(path)
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

mainpath=cur_file_dir()
print(mainpath)
configfile=os.path.join(mainpath,'config.ini')
print(configfile)


def read_config():
    #读取config.ini
    kargs={}
    cfg=configparser.ConfigParser()
    cfg.read(configfile.replace("\\","/"))
    for opt in cfg.sections():
        if opt:
            kargs[opt]={}
    for opt in kargs.keys():
        for k,v in cfg.items(opt):
            kargs[opt][k]=v
    return kargs