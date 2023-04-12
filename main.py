# -*- utf-8 -*-
# @Time:  2023/4/12 9:26
# @Autor: Andy Ye
# @File:  main.py
# @IDE: PyCharm

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui
from gui_audio_to_text import Ui_MainWindow
import sys
from utility import *
from audio import *
from ost_fast import *
import socket


class AudioToText(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        load_config(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # self.sock.bind(("", self.ui.sb_python_port.value()))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(12)
        # self.ui.pte_text.setFont(font)


        self.ui.pb_ask.pressed.connect(self.ask_pressed)
        self.ui.pb_ask.released.connect(self.ask_released)
        self.ui.pb_ask.setStyleSheet("background-color: rgba(255, 0, 0, 150); color: rgb(255, 255, 255);"
                                     "border-radius: 50px; border:2px solid white; border-style: outset;")
        # self.ui.pb_ask.setStyleSheet("background-color: rgba(0, 180, 0, 150);border-radius: 15px; "
        #                              "border: 5px groove gray;border-style: outset;")
        self.udp_server = UdpServer(self.ui.sb_python_port.value(), self.ask_pressed, self.ask_released)
        self.udp_server.start()
        self.recorder = None
        # self.ui_timer = QtCore.QTimer()
        # self.ui_timer.timeout.connect(self.get_udp_cmd)
        # self.ui_timer.start(30)

    # def get_udp_cmd(self):
    #     if self.udp_server.record

    def ask_pressed(self):
        if self.recorder is None:
            print("Start recording")
            self.recorder = Recorder()
            self.recorder.start()
            self.ui.pb_ask.setStyleSheet("background-color: rgba(255, 0, 0, 255); color: rgb(255, 255, 255);"
                                         "border-radius: 50px; border:2px solid white; border-style: outset;")
            self.ui.pb_ask.setText("记录中....")
        else:
            # self.ui.pte_text.appendPlainText("Audio Recoder is already running")
            print("Audio Recoder is already running")

    def ask_released(self):
        print("===self.recorder", self.recorder)
        if self.recorder is not None:
            print("Stop recording")
            ui = self.ui
            self.recorder.stop()
            self.ui.pb_ask.setStyleSheet("background-color: rgba(255, 0, 0, 150); color: rgb(255, 255, 255);"
                                         "border-radius: 50px; border:2px solid white; border-style: outset;")
            self.ui.pb_ask.setText("按住说话")
            time.sleep(0.5)
            # t1 = time.time()
            text = FastAudioToText(ui.le_appid.text(), ui.le_apikey.text(), ui.le_apisecret.text()).get_result()
            self.sock.sendto(text.encode('utf-8'), (ui.le_ue_ip.text(), ui.sb_ue_port.value()))
            # self.ui.pte_text.appendPlainText(text)
            self.recorder = None
        else:
            print("Audio Recoder is not running")
            # self.ui.pte_text.appendPlainText("Audio Recorder is not running")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AudioToText()
    window.show()
    sys.exit(app.exec_())




