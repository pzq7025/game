#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2019-5-11 15:46
# @Author: pzq    (*********@qq.com)
import random
import time
import sys as s
import tkinter as tk
from tkinter import *
# import pygame as py
import tkinter.messagebox
from tkinter.messagebox import *

from PIL import ImageTk, Image

"""
图片大小是size(40, 40)
在测试py里面调试
"""


class InterfaceWindow:
    __n = 16  # 定义量用来决定图片的数量 必须是偶数个
    __title = "连连看"  # 游戏的标题
    __game_canvas_width = 700  # 界面宽度
    __game_canvas_height = 450  # 界面高度
    __score = 0  # 统计的分数
    __large_time = 180  # 上限时间
    __time = __large_time  # 实时游戏时间 开始等于最大时间
    __add_time = 5  # 每次消除增加的时间和时间柱开始的位置
    __cycle = __large_time  # 循环量
    __scalar = 180 / __cycle  # 矩形每次填充的量  速率  180是矩形高度
    __game_start = False  # 游戏的状态
    __icons = []  # 存小图片
    __map = []  # 游戏地图
    __game_size = 8  # 游戏尺寸 决定游戏界面的大小
    __icon_kind = __game_size * __game_size / __n  # 小图片种类 int 决定了游戏数量的多少  这样保证了和界面大小一样
    __icon_width = 40  # 图片长
    __icon_height = 40  # 图片宽
    __delta = 25  # 距离画布两边的距离
    __isFirst = True  # 第一次查看
    __isGameStart = False  # 游戏是否开始
    __formerPoint = None  # 点的形式
    __score_level = 2  # 分数的等级
    __score_base = 10  # 分数的基数
    EMPTY = -1  # 该位置为空
    NONE_LINK = 0  # 没有连接的
    STRAIGHT_LINK = 1  # 直接连接
    ONE_CORNER_LINK = 2  # 拐一次的
    TWO_CORNER_LINK = 3  # 拐两次的

    def __init__(self, base_m=False, com_m=False, level_m=False):
        """
        初始化界面信息
        """
        self.n = 0  # 每次画布的增加量  和图片数量冲突了
        self.root = tk.Toplevel()
        self.com_ = com_m  # 休闲模式
        self.base_ = base_m  # 基本模式
        self.level_ = level_m  # 闯关模式
        self.time_counter = tk.Canvas()
        self.show_time = tk.Label()
        self.start_button = tk.Button()

    def interface(self):
        # 背景的添加
        bg = PhotoImage(file=r".\images\pk_bg.png")
        Label(self.root, image=bg).pack()
        # 标题
        self.root.title(self.__title)
        self.root.iconbitmap(r".\images\login.ico")
        self.root.resizable(False, False)
        # # 添加背景音乐
        # py.mixer.init()
        # py.mixer.music.load(r'.\videos\forget.mp3')
        # py.mixer.music.play(-1, 10)
        # 设置大小和位置 这样可以保证先生成游戏界面再来生成操作界面
        self.__add_components()
        # 设置窗口大小
        self.root.geometry("700x475+250+100")
        self.root.mainloop()

    def __add_components(self):
        """
        添加界面的布局方式
        :return:
        """
        # 画布布局
        self.canvas = tk.Canvas(self.root, bg='lightgrey', width=450, height=450, bd=0, highlightthickness=0)
        self.canvas.bind('<Button-1>', self.click_canvas)
        self.canvas.place(x=130, y=12)

        # 开始按钮
        self.start_button = tk.Button(self.root, command=self.begin_game, bg="lightgrey", fg="black", font="叶根友毛笔行书2.0版 15 bold", text="开始")
        self.start_button.place(x=35, y=100)

        # 提示按钮
        self.tip_button = tk.Button(self.root, command=self.pause_sys, bg="lightgrey", fg="black", font="叶根友毛笔行书2.0版 15 bold", text="暂停")
        self.tip_button.place(x=35, y=160)

        # 结束按钮
        self.exit_button = tk.Button(self.root, command=self.tip, bg="lightgrey", fg="black", font="叶根友毛笔行书2.0版 15 bold", text="提示")
        self.exit_button.place(x=35, y=220)

        # 重新排列按钮
        self.resort_button = tk.Button(self.root, command=self.resort, bg="lightgrey", fg="black", font="叶根友毛笔行书2.0版 15 bold", text="重排")
        self.resort_button.place(x=35, y=280)

        # 分数显示
        self.show_score = tk.Label(self.root, bg="lightgrey", fg="red", font="叶根友毛笔行书2.0版 15 bold", text=f"分数\n{self.__score}")
        self.show_score.place(x=35, y=20)

    def begin_game(self):
        """
        对游戏进行初始化  包括分解图片 生成地图以及计时
        :return:
        """
        # 分解图片
        self.extract_small_icon_list()
        # 初始化地图
        self.init_map()
        # 将图片和地图联系起来
        self.draw_map()
        self.__game_start = True
        if self.level_ or self.base_ is True:
            self.counter()
        else:
            self.start_button.configure(state=tk.DISABLED)

    # =========================================================== 功能模块 ===============================================================
    def counter(self):
        """
        计时柱的构建
        :return:
        """
        self.start_button.configure(state=tk.DISABLED)
        self.time_counter = tk.Canvas(self.root, width=22, height=180, bg="yellow")
        self.time_counter.place(x=615, y=80)

        # 时间显示
        self.show_time = tk.Label(self.root, bg="lightgrey", fg="purple", font="叶根友毛笔行书2.0版 15 bold", text=f"剩余时间\n{self.__time}s")
        self.show_time.place(x=590, y=20)
        # try:
        fill_line = self.time_counter.create_rectangle(1.5, 1.5, 23, 0, width=0, fill="white")
        while self.__cycle > 0:  # self.time 做循环量处理
            if self.__game_start:
                self.n += self.__scalar
                # 移动开始减少
                self.time_counter.coords(fill_line, (0, 0, 80, self.n))
                self.root.update()
                self.__time -= 1
                self.show_time.configure(text=f"剩余时间\n{self.__time}s", fg="purple")
                time.sleep(1.0)  # 控制进度条流动的速度 1秒一次
                # 时间结束  游戏结束  退出
                if self.__time == 0:
                    tk.messagebox.showinfo("Tip", f"最后分数:{self.__score}")
                    self.__game_start = False
                self.__cycle = self.__time  # 保证了和时间的一致性
        # except Exception as e:
        # _ = e.__traceback__
        # print(e.__cause__, "counter")
        # self.root.quit()

    def continue_game(self):
        """
        继续游戏的游戏设定
        :return:
        """
        # try:
        continue_game_a = askokcancel('提示', '是否接续游戏')
        if continue_game_a:
            # 继续游戏
            self.__game_start = True
            self.__n = 8
            self.__game_size = 8
            self.__icon_kind = self.__game_size * self.__game_size / self.__n
            self.begin_game()
        else:
            # 游戏结束
            tk.messagebox.showinfo("Tip", f"最后分数:{self.__score}")
            self.__score = 0
            # self.root.quit()
        # except Exception as e:
        # _ = e.__traceback__
        # print(e.__cause__, "continue game")
        # self.root.quit()

    @staticmethod
    def pause_sys():
        # try:
        pause = askyesno("提示", "点击继续")
        while True:
            time.sleep(1)
            if pause:
                break
            else:
                break

    # except Exception as e:
    # _ = e.__traceback__
    # self.root.quit()
    # print(e.__cause__, "pause")

    def resort(self):
        """
        重新排列
        :return:
        """
        result = []  # 随机数产生的结果
        remain = []  # 剩余图片

        # 先获取剩余的图片的地图信息
        for i in range(0, self.__game_size):
            for j in range(0, self.__game_size):
                remain.append(self.__map[i][j])
        total = self.__game_size * self.__game_size

        # print(remain)
        # print()
        # 将图片打乱
        for x in range(0, total):
            index = random.randint(0, total - x - 1)
            result.append(remain[index])
            del remain[index]
            # del remain[index]
        # print(result)
        # 置空地图开始存值
        self.__map = []
        for y in range(0, self.__game_size):
            for x in range(0, self.__game_size):
                if x == 0:
                    self.__map.append([])
                self.__map[y].append(result[x + y * self.__game_size])

        # 画图
        self.draw_resort_map()

    def draw_resort_map(self):
        """
        重排列之后进行重新画图
        :return:
        """
        self.canvas.delete("all")
        for y in range(0, self.__game_size):
            for x in range(0, self.__game_size):
                point = self.get_outer_left_top_point(Point(x, y))
                if self.__map[y][x] != self.EMPTY:
                    _ = self.canvas.create_image((point.x, point.y),
                                                 image=self.__icons[self.__map[y][x]], anchor='nw', tags='im%d%d' % (x, y))

    def tip(self):
        """
        退出系统
        :return:
        """
        counter = 0
        for x in range(self.__game_size):
            for y in range(self.__game_size):
                point = Point(x, y)
                if point.is_useful() and not self.empty_map(point) and counter < 2:
                    # 是否是第一次遇到这个点
                    if self.__isFirst:
                        self.__isFirst = False
                        self.__formerPoint = point  # 把这个点保存下来
                        counter += 1
                    else:
                        # 两次点击消除
                        if self.__formerPoint.equal(point):
                            self.__isFirst = True
                            self.canvas.delete("rectRedOne")
                            continue
                        else:
                            # 判断是否可以链接
                            link_type = self.get_link_type(self.__formerPoint, point)
                            if link_type['type'] != self.NONE_LINK:
                                # count += 1
                                self.draw_selected_area(point)
                                self.draw_selected_area(self.__formerPoint)
                                self.__isFirst = True
                                counter += 1
                                break

    def detail(self):
        """
        消完之后做加分处理  加时处理
        :return:
        """
        # 加分处理
        if self.__game_start:
            self.__score += self.__score_level * self.__score_base
            self.show_score.configure(text=f"分数\n{self.__score}", fg="red")

            # 加时处理
            # 由于一秒一减少  所以self.n的值和self.__time的值一样
            self.__time += self.__add_time
            self.n -= self.__scalar * self.__add_time
            # 将溢出的全部删除
            if self.__time >= self.__large_time:
                self.show_time.configure(text=f"剩余时间\n{self.__large_time}s", fg="purple")
                self.__time = self.__large_time
                self.n = 0
            else:
                self.show_time.configure(text=f"剩余时间\n{self.__time}s", fg="purple")

    # =========================================================== 游戏模块 =============================================================
    def click_canvas(self, event):
        # try:
        # 如果游戏处于可以继续运行的状态
        if self.__game_start:
            point = self.get_inner_point(Point(event.x, event.y))
            # 有效点击坐标
            if point.is_useful() and not self.empty_map(point):
                # 判断是否是第一次点击
                if self.__isFirst:
                    self.draw_selected_area(point)
                    self.__isFirst = False
                    self.__formerPoint = point
                else:
                    # 如果点击两次相同的就消去
                    if self.__formerPoint.equal(point):
                        self.__isFirst = True
                        self.canvas.delete("rectRedOne")

                    else:
                        # 获取类型
                        link_type = self.get_link_type(self.__formerPoint, point)
                        if link_type['type'] != self.NONE_LINK:
                            self.clear_linked_blocks(self.__formerPoint, point)
                            self.canvas.delete("rectRedOne")
                            if self.level_ or self.base_ is True:
                                self.detail()
                            self.__isFirst = True
                            if self.game_over():
                                # 通过的游戏结束
                                self.__game_start = False
                                self.continue_game()
                        # 如果不满足条件重新
                        else:
                            self.__formerPoint = point
                            self.canvas.delete("rectRedOne")
                            self.draw_selected_area(point)

    # except Exception as e:
    #     print(e.__cause__)
    # _ = e.__traceback__
    # self.root.quit()

    def draw_map(self):
        """
        根据点绘制图像
        :return:
        """
        self.canvas.delete("all")
        for y in range(0, self.__game_size):
            for x in range(0, self.__game_size):
                point = self.get_outer_left_top_point(Point(x, y))
                _ = self.canvas.create_image((point.x, point.y),
                                             image=self.__icons[self.__map[y][x]], anchor='nw', tags='im%d%d' % (x, y))

    def init_map(self):
        """
        初始化存值  存值为0-24  将图片的信息存入游戏界面中
        :return:
        """
        self.__map = []  # 地图的存储
        tmp_records = []  # 将产生的所有图片存起来
        records = []  # 将产生的图片随机排列
        # 获取图片的数量 将产生的总数量存起来
        for i in range(0, int(self.__icon_kind)):
            for j in range(0, int(self.__n)):
                tmp_records.append(i)

        # 根据地图大小随机排列这些数 最后将结果存入records
        total = self.__game_size * self.__game_size
        for x in range(0, total):
            index = random.randint(0, total - x - 1)
            records.append(tmp_records[index])
            del tmp_records[index]

        # 一维数组转成二维 y为高维度 地图的存储
        for y in range(0, self.__game_size):
            for x in range(0, self.__game_size):
                if x == 0:
                    self.__map.append([])
                self.__map[y].append(records[x + y * self.__game_size])

    def game_over(self):
        """
        判断游戏是否结束
        :return:
        """
        for y in range(0, self.__game_size):
            for x in range(0, self.__game_size):
                if self.__map[y][x] != self.EMPTY:
                    return False
        return True

    def extract_small_icon_list(self):
        """
        加载图片的种类  分隔小图
        :return:
        """
        # 将图片清空 保证在继续游戏的时候不会因为数组问题而报错
        self.__icons = []
        # image_source = Image.open(r".\images\naruto.png")
        for index in range(0, int(self.__icon_kind)):
            # region = image_source.crop((self.__icon_width * index, 0, self.__icon_width * index + self.__icon_width - 1, self.__icon_height - 1))
            # 这个可以加载其他的图片
            region = Image.open(r".\images\element_have_" + str(index + 1) + "_shrink.png")
            self.__icons.append(ImageTk.PhotoImage(region))

    def draw_selected_area(self, point):
        """
        选中的区域变红
        :param point: 为内部坐标
        :return:
        """
        point_lt = self.get_outer_left_top_point(point)
        point_rb = self.get_outer_left_top_point(Point(point.x + 1, point.y + 1))
        self.canvas.create_rectangle(point_lt.x, point_lt.y, point_rb.x - 1, point_rb.y - 1, outline='red', tags="rectRedOne")

    def clear_linked_blocks(self, p1, p2):
        """
        消除两个连通块
        :param p1:
        :param p2:
        :return:
        """
        self.__map[p1.y][p1.x] = self.EMPTY
        self.__map[p2.y][p2.x] = self.EMPTY
        self.canvas.delete("im%d%d" % (p1.x, p1.y))
        self.canvas.delete("im%d%d" % (p2.x, p2.y))

    def empty_map(self, point):
        """
        判断地图上两点是否为空
        :param point:
        :return:
        """
        if self.__map[point.y][point.x] == self.EMPTY:
            return True
        else:
            return False

    # ====================================================== 获取坐标点 =============================================================
    def get_x(self, x):
        """
        获取x的量
        :param x:
        :return:
        """
        return x * self.__icon_width + self.__delta

    def get_y(self, y):
        """
        获取y的量
        :param y:
        :return:
        """
        return y * self.__icon_height + self.__delta

    def get_outer_left_top_point(self, point):
        """
        获取外部坐标对应矩形左上角顶点坐标  起始点坐标  这个用来建立图片的初始位置
        :param point:
        :return:
        """
        return Point(self.get_x(point.x), self.get_y(point.y))

    def get_outer_center_point(self, point):
        """
        获取外部点  也就是图片的位置点  这个可用像素来控制
        :param point:
        :return:
        """
        return Point(self.get_x(point.x) + int(self.__icon_width / 2), self.get_y(point.y) + int(self.__icon_height / 2))

    def get_inner_point(self, point):
        """
        获取内部的点击的点  点击范围为一个图片
        :param point:
        :return:
        """
        x = -1
        y = -1

        for i in range(0, self.__game_size):
            x1 = self.get_x(i)
            x2 = self.get_x(i + 1)
            if x1 <= point.x < x2:
                x = i

        for j in range(0, self.__game_size):
            j1 = self.get_y(j)
            j2 = self.get_y(j + 1)
            if j1 <= point.y < j2:
                y = j

        return Point(x, y)

    # ======================================================= 游戏规则模块 =====================================================

    def straight_line(self, p1, p2):
        """
        直连模式
        :param p1:
        :param p2:
        :return:
        """
        # 水平判断
        if p1.y == p2.y:
            # 大小判断 确定起始点
            if p2.x < p1.x:
                start = p2.x
                end = p1.x
            else:
                start = p1.x
                end = p2.x
            # 遍历点
            for x in range(start + 1, end):
                if self.__map[p1.y][x] != self.EMPTY:
                    return False
            return True
        # 竖直判断
        elif p1.x == p2.x:
            # 大小判断确定起始点
            if p1.y > p2.y:
                start = p2.y
                end = p1.y
            else:
                start = p1.y
                end = p2.y
            # 遍历点
            for y in range(start + 1, end):
                if self.__map[y][p1.x] != self.EMPTY:
                    return False
            return True
        return False

    def once_corner_line(self, p1, p2):
        """
        拐一次的规则
        :param p1:
        :param p2:
        :return:
        """
        # 第一个点的x和第二个点的y
        point_corner = Point(p1.x, p2.y)
        if self.straight_line(p1, point_corner) and self.straight_line(point_corner, p2) and self.empty_map(point_corner):
            return point_corner

        # 第二个点的x和第一个点的y
        point_corner = Point(p2.x, p1.y)
        if self.straight_line(p1, point_corner) and self.straight_line(point_corner, p2) and self.empty_map(point_corner):
            return point_corner

    def two_corner_line(self, p1, p2):
        """
        拐两次的规则
        :param p1:
        :param p2:
        :return:
        """
        # 竖向判断
        for y in range(-1, self.__game_size + 1):
            point_corner_1 = Point(p1.x, y)
            point_corner_2 = Point(p2.x, y)
            if y == p1.y or y == p2.y:
                continue
            if y == -1 or y == self.__game_size:
                if self.straight_line(p1, point_corner_1) and self.straight_line(point_corner_2, p2):
                    return {
                        'p1': point_corner_1,
                        'p2': point_corner_2
                    }
            else:
                if self.straight_line(p1, point_corner_1) and self.straight_line(point_corner_1, point_corner_2) and self.straight_line(point_corner_2, p2) and self.empty_map(point_corner_1) and self.empty_map(point_corner_2):
                    return {
                        'p1': point_corner_1,
                        'p2': point_corner_2,
                    }

        # 横向判断
        for x in range(-1, self.__game_size + 1):
            point_corner_1 = Point(x, p1.y)
            point_corner_2 = Point(x, p2.y)
            if x == p1.x or x == p2.x:
                continue
            if x == -1 or x == self.__game_size:
                if self.straight_line(p1, point_corner_1) and self.straight_line(point_corner_2, p2):
                    return {
                        'p1': point_corner_1,
                        'p2': point_corner_2,
                    }
            else:
                if self.straight_line(p1, point_corner_1) and self.straight_line(point_corner_1, point_corner_2) and self.straight_line(point_corner_2, p2) and self.empty_map(point_corner_1) and self.empty_map(point_corner_2):
                    return {
                        'p1': point_corner_1,
                        'p2': point_corner_2,
                    }

    def get_link_type(self, p1, p2):
        """
        通过返回的类型来确定 拐角类型
        :param p1:
        :param p2:
        :return:
        """
        # 判断两个方块中图片是否相同
        if self.__map[p1.y][p1.x] != self.__map[p2.y][p2.x]:
            return {
                'type': self.NONE_LINK
            }

        if self.straight_line(p1, p2):
            return {
                'type': self.STRAIGHT_LINK
            }

        res = self.once_corner_line(p1, p2)
        if res:
            return {
                'type': self.ONE_CORNER_LINK,
                'p1': res
            }
        res = self.two_corner_line(p1, p2)
        if res:
            return {
                'type': self.TWO_CORNER_LINK,
                'p1': res['p1'],
                'p2': res['p2'],
            }
        return {
            'type': self.NONE_LINK
        }


# =========================================================== 点对象 =================================================================
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_useful(self):
        """
        判断该点是否可用
        :return:
        """
        if self.x >= 0 and self.y >= 0:
            return True
        else:
            return False

    def equal(self, point):
        """
        判断两个点是否相同
        :param point:
        :return:
        """
        if self.x == point.x and self.y == point.y:
            return True
        else:
            return False

# if __name__ == '__main__':
#     interface = InterfaceWindow()
#     interface.interface()
