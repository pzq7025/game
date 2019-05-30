#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2019-5-11 15:46
# @Author: pzq    (*********@qq.com)
from ppx import *
import pygame as py
import webbrowser


class MainInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.start_button = tk.Button()
        self.comfortable = tk.Button()
        self.difficult = tk.Button()
        self.exit_b = tk.Button()
        self.help_button = tk.Button()
        self.setting_button = tk.Button()
        self.rank_button = tk.Button()

    def start(self):
        """
        启动按钮
        :return:
        """
        self.root.title("皮卡连连看")
        bg = PhotoImage(file=r".\images\pk_bg_main.png")
        tk.Label(self.root, text="皮卡连连看\n\n\n\n\n\n\n", compound=tk.CENTER, font=("华文行楷", 40), fg="purple", image=bg).pack()
        self.root.iconbitmap(r".\images\login.ico")
        self.root.resizable(False, False)
        py.mixer.init()
        py.mixer.music.load(r'.\videos\forget.mp3')
        py.mixer.music.play(-1, 10)
        self.root.geometry("700x475+250+100")
        self.components()
        self.root.mainloop()

    def components(self):
        """
        组件设置
        :return:
        """
        # 开始按钮
        self.start_button = tk.Button(self.root, bg="lightgrey", fg="black", command=self.base_game_window, font="华文行楷", text="基本模式")
        self.start_button.place(x=30, y=180)
        # 休闲模式
        self.comfortable = tk.Button(self.root, bg="lightgrey", fg="black", command=self.comfortable_game, font="华文行楷", text="休闲模式")
        self.comfortable.place(x=30, y=240)
        # 困难模式
        self.difficult = tk.Button(self.root, bg="lightgrey", fg="black", command=self.level_game, font="华文行楷", text="关卡模式")
        self.difficult.place(x=30, y=300)
        # 退出
        self.exit_b = tk.Button(self.root, bg="lightgrey", fg="black", command=self.exit_game, font="华文行楷", text="退出游戏")
        self.exit_b.place(x=30, y=360)
        # 排行榜
        self.rank_button = tk.Button(self.root, bg='lightgrey', fg='black', command=self.rank_content, font="华文行楷", text="排行榜", width=7)
        self.rank_button.place(x=495, y=420)
        # 帮助
        self.help_button = tk.Button(self.root, bg='lightgrey', fg='black', command=self.set_content, font="华文行楷", text="帮助", width=7)
        self.help_button.place(x=575, y=420)
        # 设置
        self.setting_button = tk.Button(self.root, bg='lightgrey', fg='black', command=self.set_web, font="华文行楷", text="设置", width=7)
        self.setting_button.place(x=415, y=420)

    @staticmethod
    def base_game_window():
        """
        基本模式
        :return:
        """
        InterfaceWindow(base_m=True).interface()

    @staticmethod
    def comfortable_game():
        """
        休闲模式
        :return:
        """
        InterfaceWindow(com_m=True).interface()

    @staticmethod
    def level_game():
        """
        闯关模式
        :return:
        """
        InterfaceWindow(level_m=True).interface()

    def exit_game(self):
        self.root.quit()
        exit()

    @staticmethod
    def set_content():
        new = tk.Toplevel()
        new.title("参考文档")
        new.resizable(False, False)
        bg = PhotoImage(file=r".\images_new\pk_11~1.png")
        with open(r".\text_content\content.txt", encoding='utf-8') as f:
            content = f.read()
        Label(new, image=bg, text=content, compound=tk.CENTER, font=("华文行楷", 20), fg="green", width=600, height=650).pack()
        new.geometry("500x375+350+150")
        new.mainloop()

    @staticmethod
    def rank_content():
        rank_tk = tk.Toplevel()
        rank_tk.title("排行榜")
        bg = PhotoImage(file=r".\images_new\pk_20~1.png")
        with open(r".\text_content\rank.txt", encoding='utf-8') as f:
            content = f.read()
        Label(rank_tk, image=bg, text=content, compound=tk.CENTER, font=("华文行楷", 20), fg="red", width=600, height=650).pack()
        rank_tk.geometry("500x375+350+150")
        rank_tk.mainloop()

    @staticmethod
    def set_web():
        webbrowser.open("https://vd1.bdstatic.com/mda-hinvggq8wzyixwd8/vs-29ca63f38d8cb5b5a2547bde59276e7b-watermark/hd/mda-hinvggq8wzyixwd8.mp4?auth_key=1559130732-0-0-798f3b6cc661644b55526ce9a9b39bc3&bcevod_channel=searchbox_feed&pd=bjh&abtest=all")


if __name__ == '__main__':
    main_interface = MainInterface()
    main_interface.start()
