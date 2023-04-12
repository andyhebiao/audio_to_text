# -*- utf-8 -*-
# @Time:  2023/4/12 9:41
# @Autor: Andy Ye
# @File:  utility.py
# @IDE: PyCharm
import configparser
import threading as td
import socket

def load_config(self, file_path="./Config/config.cfg"):
    cfg = configparser.ConfigParser()
    try:
        cfg.read(file_path, encoding='gbk')
    except UnicodeError:
        cfg.read(file_path, encoding='utf-8')
    for (key, value) in cfg.items("config"):
        if "sb_" + key in dir(self.ui):
            exec("self.ui.sb_" + key + ".setValue(" + value + ")")
            # exec("self." + key + "=" + value)
            print("self." + key + "=" + value)
        elif "ds_" + key in dir(self.ui):
            exec("self.ui.ds_" + key + ".setValue(" + value + ")")
            # exec("self." + key + "=" + value)
            print("self." + key + "=" + value)
        elif "le_" + key in dir(self.ui):
            # print("le_" + key)
            exec("self.ui.le_" + key + ".setText(\"" + value + "\")")
            # exec("self." + key + "=\"" + value + "\"")
            print("self." + key + "=" + value)
        elif key in dir(self):
            exec("self." + key + "=" + value)
            print("self." + key + "=" + value)
        else:
            print("redundant parameters:", key, "=", value)


class UdpServer(td.Thread):
    def __init__(self, port, callback_start_record, callback_stop_record, ip="", buffer=1024, daemon=True):
        super(UdpServer, self).__init__(daemon=daemon)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((ip, port))
        self.buffer = buffer
        self.record = False
        self.callback_start_record = callback_start_record
        self.callback_stop_record = callback_stop_record

    def run(self):
        lock = td.Lock()
        print("start udp server")
        while True:
            data, addr = self.sock.recvfrom(self.buffer)
            print(data.decode("utf-8"))
            cmd = data.decode("utf-8")
            if cmd == "Start recording":
                with lock:
                    self.record = True
                self.callback_start_record()
                print("udp server Start recording")
            elif cmd == "Stop recording":
                with lock:
                    self.record = False
                self.callback_stop_record()
                print("udp server Stop recording")
            else:
                print("unknown command:", cmd)




