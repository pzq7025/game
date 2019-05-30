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
#     img_2.resize(size, Image.ANTIALIAS).save(r".\images\element_have_" + str(i) + "_shrink.png")
# dir_img = "../img/"
# dir_save = "../img/"
# size = (39)
#
# list_img = os.listdir(dir_img)  # 获取目录下所有图片名
#
# --------------------------------------------*******************************--------------------------
# 单个图片处理
# image = Image.open(r".\images_new\pk_18~1.png")
# size = (1052, 766)
# image.resize(size, Image.ANTIALIAS).save(r".\images_new\pk_18_11.png")

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
# import tkinter as tk
# from PIL import ImageTk, Image
# import time
#
# root = tk.Tk()
# # 背景
# time_s = 200
# canvas = tk.Canvas(root, width=200, height=200, background="white")
# canvas.place(x=10, y=20)
# root.geometry("700x475+250+100")
# fill_line = canvas.create_rectangle(0, 0, 50, time_s, fill='blue')
#
#
# def decline(time_n):
#     time_n -= 10
#     canvas.coords(fill_line, (0, 0, 50, time_n))
#     root.update()
#
#
# button = tk.Button(root, text="Begin", command=decline(time_s))
# button.pack()
#
# # while time_s >= 0:
# #     canvas.create_rectangle(0, 0, 50, time_s, fill='blue')
# #     time_s -= 10
# #     canvas.configure(time_s)
# #     time.sleep(2)
# root.mainloop()

# ========================================== 进度条 ==================================================================================
# import tkinter as tk
# import time
#
# # 创建主窗口
# window = tk.Tk()
# window.title('进度条')
# window.geometry('500x430')
#
# # 设置下载进度条
# canvas = tk.Canvas(window, width=22, height=180, bg="green")
# canvas.place(x=110, y=60)


# # 显示下载进度
# def progress():
#     # 填充进度条
#     fill_line = canvas.create_rectangle(1.5, 1.5, 23, 0, width=0, fill="white")
#     x = 360  # 未知变量，可更改
#     n = 180 / x  # 465是矩形填充满的次数
#     for i in range(x):
#         n += 180 / x
#         canvas.coords(fill_line, (0, 0, 60, n))
#         window.update()
#         time.sleep(0.02)  # 控制进度条流动的速度
#         if n == 180:
#             exit()
#
#     # # 清空进度条
#     # fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="white")
#     # x = 500  # 未知变量，可更改
#     # n = 465 / x  # 465是矩形填充满的次数
#
#     # for t in range(x):
#     #     n = n + 465 / x
#     #     # 以矩形的长度作为变量值更新
#     #     canvas.coords(fill_line, (0, 0, n, 60))
#     #     window.update()
#     #     time.sleep(0)  # 时间为0，即飞速清空进度条
#
#
# def add():
#     a = 1
#     b = 2
#     c = a + b
#     if c == a:
#         pass
#
#
# btn_download = tk.Button(window, text='启动进度条', command=progress)
# btn_download.place(x=400, y=105)
#
# window.mainloop()
# ======================================================================================================================================
# from tkinter import *
#
# if __name__ == '__main__':
#     root = Tk()
#     root.geometry("500x400+200+200")
#     canvas = Canvas(root, width=300, height=300, bg='green')
#
#     canvas.pack(expand=YES, fill=BOTH)
#
#     x0 = 150  # 圆心横坐标
#
#     y0 = 100  # 圆心纵坐标
#
#     # canvas.create_oval(x0 - 10, y0 - 10, x0 + 10, y0 + 10)  # 圆外矩形左上角与右下角坐标
#     #
#     # canvas.create_oval(x0 - 20, y0 - 20, x0 + 20, y0 + 20)  # 圆外矩形左上角与右下角坐标
#     #
#     # canvas.create_oval(x0 - 50, y0 - 50, x0 + 50, y0 + 50)  # 圆外矩形左上角与右下角坐标
#     # points = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
#     points = [100, 140, 120, 160, 140, 140, 140, 40, 120, 20, 100, 40]
#     canvas.create_polygon(points, outline='red', fill='yellow', width=3)
#
#     root.mainloop()

# ======================================================================================================================================
# from tkinter import *
#
# canvas_width = 500
# canvas_height = 150
#
#
# def paint(event):
#     python_green = "#476042"
#     x1, y1 = (event.x - 1), (event.y - 1)
#     x2, y2 = (event.x + 1), (event.y + 1)
#     w.create_oval(x1, y1, x2, y2, fill=python_green)
#
#
# master = Tk()
# master.title("Painting using Ovals")
# w = Canvas(master,
#            width=canvas_width,
#            height=canvas_height)
# w.pack(expand=YES, fill=BOTH)
# w.bind("<B1-Motion>", paint)
#
# message = Label(master, text="Press and Drag the mouse to draw")
# message.pack(side=BOTTOM)
#
# mainloop()

# =========================================================================================================================================


# ========================================================================================================================================
# 去掉图片背景
# import PIL.Image as Image
#
#
# # 以第一个像素为准，相同色改为透明
# def transparent_back(img):
#     img = img.convert('RGBA')
#     L, H = img.size
#     color_0 = img.getpixel((0, 0))
#     for h in range(H):
#         for l in range(L):
#             dot = (l, h)
#             color_1 = img.getpixel(dot)
#             if color_1 == color_0:
#                 color_1 = color_1[:-1] + (0,)
#                 img.putpixel(dot, color_1)
#     return img
#
#
# if __name__ == '__main__':
#     for i in range(1, 14):
#         img = Image.open(r'.\images\element_' + str(i) + '_shrink.png')
#         img = transparent_back(img)
#         img.save(r'.\images\element_' + str(i) + '_shrink.png')


# from PIL import Image
#
# import os
#
# # for filename in os.listdir(r'c:/image/png'):
# img = Image.open(r".\images\element_2.png")
# img = img.convert("RGBA")
# pixdata = img.load()
#
# for y in range(img.size[1]):
#     for x in range(img.size[0]):
#         if pixdata[x, y][0] > 220 and pixdata[x, y][1] > 220 and pixdata[x, y][2] > 220 and pixdata[x, y][3] > 220:
#             pixdata[x, y] = (255, 255, 255, 0)
# img.save(r".\images\element__2__new.png")


# ============================================================= 视频处理 ==========================================================
# import cv2
#
# cap = cv2.VideoCapture('C2.mp4')
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == True:
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         cv2.imshow('frame', gray)
#         # & 0xFF is required for a 64-bit system
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
# cap.release()
# cv2.destroyAllWindows()
# ======================================================================================================================================


# =========================================================== 网址驱动 ==================================================================
# from tkinter import *
# import webbrowser
#
# root = Tk()
#
# text = Text(root, width=30, height=5)
# text.pack()
#
# text.insert(INSERT, "百度一下，你就知道")
#
# text.tag_add("link", "1.0", "1.4")
# text.tag_config("link", foreground="blue", underline=True)
#
#
# def click(event):
#     webbrowser.open("http://www.baidu.com")
#
#
# text.tag_bind("link", "<Button-1>", click)
#
# mainloop()
# =============================================================================================================================
