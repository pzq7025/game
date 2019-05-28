#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2019-5-11 15:46
# @Author: pzq    (*********@qq.com)
from ppx import *
import pygame as py


class MainInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.start_button = tk.Button()
        self.comfortable = tk.Button()
        self.difficult = tk.Button()
        self.exit_b = tk.Button()

    def start(self):
        """
        启动按钮
        :return:
        """
        self.root.title("PK")
        bg = PhotoImage(file=r".\images\pk_bg_main.png")
        Label(self.root, image=bg).pack()
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
        self.start_button = tk.Button(self.root, bg="lightgrey", fg="black", command=self.base_game_window, font="叶根友毛笔行书2.0版 15 bold", text="基本模式")
        self.start_button.place(x=30, y=180)
        # 休闲模式
        self.comfortable = tk.Button(self.root, bg="lightgrey", fg="black", command=self.comfortable_game, font="叶根友毛笔行书2.0版 15 bold", text="休闲模式")
        self.comfortable.place(x=30, y=240)
        # 困难模式
        self.difficult = tk.Button(self.root, bg="lightgrey", fg="black", command=self.level_game, font="叶根友毛笔行书2.0版 15 bold", text="关卡模式")
        self.difficult.place(x=30, y=300)
        # 退出
        self.exit_b = tk.Button(self.root, bg="lightgrey", fg="black", command=self.exit_game, font="叶根友毛笔行书2.0版 15 bold", text="退出游戏")
        self.exit_b.place(x=30, y=360)

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


if __name__ == '__main__':
    main_interface = MainInterface()
    main_interface.start()
