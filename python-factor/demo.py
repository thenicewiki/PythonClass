'''
*******************************************************************
Author:                PegausWiki
Date:                  2020-11-18
FileName：             demo.py
Copyright (C):         2020 All rights reserved
*******************************************************************
'''

from tkinter import *
import tkinter.messagebox as messagebox
import _thread
import re

class Demo(Tk):
    def __init__(self):
        super().__init__()
        self._set_window_()
        self._create_menu_bar_()
        self._create_layout_()

    def _set_window_(self):
        self.title("Demo")
        self.geometry("350x390")
        # self.resizable(0, 0)

    def _create_menu_bar_(self):
        # 创建菜单栏
        menubar = Menu(self)
        self["menu"] = menubar
        helpmenu = Menu(menubar,tearoff=0)
        menubar.add_cascade(label='帮助', menu=helpmenu)
        helpmenu.add_command(label='操作说明', command=self.description)
        helpmenu.add_command(label='关于', command=self.about)
        menubar.add_cascade(label='<---请先阅读帮助栏中的说明!!!', menu=helpmenu)
    
    def _create_layout_(self):
        frame = Frame(self)
        frame.pack(fill = Y, padx = 10, pady = 10)
        label = Label(frame, text='请输入一个整数：')
        label.grid(row=1, column=0)
        self._get_num_ = StringVar()

        self.entrynum = Entry(frame, textvariable=self._get_num_)
        self.entrynum.grid(row=1, column=1)
        # getname = Button(frame, text='确定', command= lambda: self.thread_calculate_factor())
        getname = Button(frame, text='确定', command= lambda: self.calculate_factor())

        getname.grid(row=1, column=2)

        self.listbox = Listbox(self)
        self.listbox.pack(fill = BOTH)

        getname = Button(self, text='Clear', command = lambda listbox = self.listbox : listbox.delete(0, END))
        getname.pack(fill = Y, padx =10, pady = 10)

        # 容器框 （LabelFrame）
        label_frame = Frame(self)
        label_frame.pack(fill = Y)
        group = LabelFrame(label_frame, text="Ps.", padx=5, pady=5)
        group.grid(pady=10)
        w = Label(group, text='本学习项目由  http://pegasu.cn  出品 \n\nGithub: https://github.com/thenicewiki')
        w.pack()

    def thread_calculate_factor(self):
        _thread.start_new_thread(self.calculate_factor, ())

    def calculate_factor(self):
        lst = []
        read = re.findall('\d+', self._get_num_.get())
        if read == []:
            messagebox.showwarning('警告','无效的输入！') 
            return
        num = int(read[0])
        if num == 0:
            messagebox.showinfo('提示','0 不是质数') 
            return
        elif num == 1:
            messagebox.showinfo('提示','1 不是质数') 
            return
        self.entrynum.delete(0, END) # 输入后删除输入框内的内容

        # while num > 1:
        #     if num % i == 0:
        #         lst.append(i)
        #         num /= i
        #     else:
        #         i+=
        while num > 1:
            for i in range(2, num + 1):
                if num % i == 0:
                    num //= i
                    lst.append(str(i))
                    break

        if len(lst) == 1:
            print('您输入的数字是质数！')
            self.listbox.insert(END, read[0] + ' 是质数')
            self.listbox.yview_moveto(1)
            return
        
        factor_nums = " × ".join([ str(i) for i in lst]) # 字符串拼接

        self.listbox.insert(END, read[0] + ' = ' +factor_nums)
        self.listbox.yview_moveto(1)

        print(read[0] + ' = ' + factor_nums)

    def description(self):
        messagebox.showinfo('帮助', '使用方法:\n1.在Entry中数字\n2.确定\n3.Clear Button清空输出\n\n特性:\n\t①使用正则表达式获取Entry中的数字\n\t自动屏蔽空白或其他特殊字符\n\t②运算结果输出保存控制台\n\t③输入0 1提示\n\t④计算后自动清空Entry方便再次计算\n\t')
    def about(self):
        messagebox.showinfo('帮助', '本学习项目由  http://pegasu.cn  出品 \n\nGithub: https://github.com/thenicewiki')


if "__main__" == __name__:
    app = Demo()
    app.mainloop()

