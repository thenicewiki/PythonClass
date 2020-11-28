'''
*******************************************************************
Author:                PegausWiki
Date:                  2020-11-25
FileName：             cal.py
Copyright (C):         2020 All rights reserved
*******************************************************************
'''

from tkinter import *
import tkinter.font as tf
import tkinter.messagebox as tm

class Demo(Tk):
    def __init__(self):
        super().__init__()
        self._set_windows_()
        self._create_menu_bar_()
        self._create_layout_()

    def _set_windows_(self):
        self.title('计算器')
        self.geometry('320x360')

    def _create_menu_bar_(self):
        menu_bar = Menu(self)
        self['menu'] = menu_bar

        filemenu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label='文件', menu = filemenu)
        filemenu.add_command(label='关闭', command = self.quit)

        helpmenu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label='帮助', menu = helpmenu)
        helpmenu.add_command(label = '操作说明', command = lambda : 1)
        helpmenu.add_command(label = '关于', command = self.about)

        displaymenu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label='显示', menu = displaymenu)
        displaymenu.add_command(label = '✓基础型', command = lambda : 1)
        displaymenu.add_command(label = '❏科学型（待开发）', command = lambda : 1)
        displaymenu.add_command(label = '❏编程型（待开发）', command = lambda : 1)
        menu_bar.add_cascade(label='<---请先阅读帮助栏中的说明!!!', menu=helpmenu)

    def _create_layout_(self):
        self.display = Entry(self, width = 40, bg = "white", font = tf.Font(size = 30))
        self.display.pack(ipadx = 10, ipady = 10)

        buttons = [
        ['AC',  '+/-',  '%',  '÷'],
        ['7',  '8',  '9',  '×'],
        ['4',  '5',  '6',  '-'],
        ['1',  '2',  '3',  '+'],
        ['0',  '.',  '=', '←']
        ]
        
        frame = Frame(self)
        frame.pack()
        for i, rows in zip(buttons, range(5)):
            for key, cols in zip(i, range(4)):
                # lambda 一定是 lambda x = key : self.fun(x) 而不是 lambda : self.fun(key)
                Button(frame, text = key, font = tf.Font(size = 30), command = lambda x = key: self.fun(x)).\
                    grid(row = rows, column = cols, ipadx = 5, ipady = 10)
        


    def fun(self, key):
        if key == '=':
            # print(self.display.get())
            try:
                result = eval(self.display.get())
                print(result, type(result))
                self.display.delete(0, END)
                self.display.insert(END, '%s' %result)
            except:
                self.display.delete(0, END)
                # self.display.insert(END, 'Err.')
                tm.showwarning('Warning', '无法计算，请重新输入运算符！')
        
        elif key == '←':
            self.display.delete(len(self.display.get())-1, END)

        elif key == 'AC':
            self.display.delete(0, END)

        elif key == '+/-':
            if(self.display.get()[0] == '-'):
                self.display.delete(0, 1)
            else:
                self.display.insert(0, '-')

        elif key == '÷':
            self.display.insert(END, '/')

        elif key == '×':
            self.display.insert(END, '*')

        else:
            self.display.insert(END, key)
        
    def about(self):
        tm.showinfo('帮助', '本学习项目由  http://pegasu.cn  出品 \n\nGithub: https://github.com/thenicewiki')
if "__main__" == __name__:
    app = Demo()
    app.mainloop()

