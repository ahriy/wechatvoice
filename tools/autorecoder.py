import pyautogui
import time
import os
from tkinter import *
from pygame import mixer
from tkinter.filedialog import *
from mutagen.mp3 import MP3
pyautogui.PAUSE = 1.5
pyautogui.size()

class AutoSender:

    voice_path = ""

    def __init__(self):
        self.top = Tk()
        self.voice_path_v = StringVar()
        self.coord_v = StringVar()
        self.send_coord_x = 0
        self.send_coord_y = 0

        mixer.init()
        Label(self.top, text="目标路径:").grid(row=0, column=0)
        Entry(self.top, textvariable=self.voice_path_v).grid(row=0, column=1)
        Button(self.top, text="路径选择", command=self.select_voice_path).grid(row=0, column=2)
        Button(self.top, text="发送", command=self.send_voices).grid(row=0, column=3)

        Label(self.top, text="按钮坐标:").grid(row=1, column=0)
        Entry(self.top, textvariable=self.coord_v).grid(row=1, column=1)
        Button(self.top, text="设定坐标", command=self.set_coord).grid(row=1, column=2)

    def start(self):
        self.top.mainloop()

    @staticmethod
    def exit(self):
        exit(0)
    @staticmethod
    def center(pos):
        return pos[0] + pos[2] / 2, pos[1] + pos[3] / 2

    def set_coord(self):
        time.sleep(3)
        self.send_coord_x, self.send_coord_y = pyautogui.position()
        self.coord_v.set("x: {}, y: {}".format(self.send_coord_x, self.send_coord_y))

    def send_voices(self):
        # print(self.voice_path_v.get().strip('(').strip()lstrip().rstrip())
        voice_path = self.voice_path_v.get() \
            .strip('()').replace("'", "").split(",")
        for v in voice_path:
            self.send_voice(v.strip())

    def send_voice(self, path):
        print(path)
        audio = MP3(path)
        mixer.music.load(path)
        # pyautogui.moveTo(x=self.send_coord_x, y=self.send_coord_y)
        mixer.music.play()
        pyautogui.mouseDown(x=self.send_coord_x, y=self.send_coord_y)
        # os.system(voice_path)
        time.sleep(audio.info.length + 0.5)
        pyautogui.mouseUp(x=self.send_coord_x, y=self.send_coord_y)

    def select_voice_path(self):
        self.voice_path_v.set(askopenfilenames())

v = AutoSender()
v.start()

# send_voice("016.Tutorial2.PVPnet.Skins.mp3")