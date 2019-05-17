# 背景图片
# ======================================================================================================================================
# import tkinter as tk
# from PIL import ImageTk, Image
#
# root = tk.Tk()
# # 背景
# canvas = tk.Canvas(root, width=1200, height=699, bd=0, highlightthickness=0)
# imgpath = r".\images\element_4.png"
# img = Image.open(imgpath)
# photo = ImageTk.PhotoImage(img)
#
# canvas.create_image(80, 120, image=photo)
# canvas.pack()
# entry = tk.Entry(root, insertbackground='blue', highlightthickness=2)
# entry.pack()
# button = tk.Button(root, text="Begin")
# button.pack()
#
# canvas.create_window(100, 50, width=100, height=20,
#                      window=entry)
# canvas.create_window(400, 500, height=100, width=100, window=button)
#
# root.mainloop()
#
#
# # from tkinter import *
# #
# # root = Tk()  # 创建窗口
# #
# # photo = PhotoImage(file=r'F:\exploitation\codes\python\Pygame\game_system\images\element_0.png')  # pic.png就在工程目录里（和.py在同一个文件夹）
# # img_label = Label(root, imag=photo).pack()
# #
# # root.mainloop()
# from tkinter import *
#
# root = Tk()
# photo = PhotoImage(file=r".\images\pk_bg.png")
# Label(root, image=photo, width=400, height=400).pack()
#
#
# def callback():
#     print('点到我了')
#
#
# Button(root, text='点我', command=callback).place(relx=0.5, rely=0.5, anchor=CENTER)  # relx和rely是相对父组件的位置,范围是 00~1.0。0是最左边，0.5是正中间，1是最右边
# mainloop()
# ======================================================================================================================================


# 图片的压缩
# ======================================================================================================================================
# import os
# from PIL import Image
#
# for i in range(1, 14):
#     img_2 = Image.open(r".\images\element_" + str(i) + ".png")
#     print(img_2.width, img_2.height)
#     size = (39, 39)
#     img_2.resize(size, Image.ANTIALIAS).save(r".\images\element_" + str(i) + "_shrink.png")
# dir_img = "../img/"
# dir_save = "../img/"
# size = (39)
#
# list_img = os.listdir(dir_img)  # 获取目录下所有图片名
#
# # 遍历
# for img_name in list_img:
#     pri_image = Image.open(dir_img + img_name)
#     tmppath = dir_save + img_name
#
#     # 保存缩小的图片
#     pri_image.resize(size, Image.ANTIALIAS).save(tmppath)
# ======================================================================================================================================


# 动画的添加
# ======================================================================================================================================


# ======================================================================================================================================
