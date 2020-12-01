import pandas as pd
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Scrollbar, Checkbutton, Label, Button, Treeview
import os
from style import ICONS, INFOS


class stu():
    def __init__(self):
        self.name = ""
        self.num = 0
        self.grade = 0

    def _show_stu_(self):
        print(self.name, self.num, self.grade)


class Demo(Tk):
    icon_res = []
    file_name = None

    def __init__(self):
        super().__init__()
        self._set_windows_()
        self._create_menu_bar_()
        self._create_shortcut_bar_()
        self._create_body_()

    def _set_windows_(self):
        self.title('学生成绩管理系统')
        scn_width, scn_height = self.maxsize()
        wm_val = '750x450+%d+%d' % ((scn_width - 750) / 2, (scn_height - 450) / 2)
        self.geometry(wm_val)
        # self.iconbitmap("img/editor.ico")


    def _create_menu_bar_(self):
        menu_bar = Menu(self)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='New', accelerator='Ctrl+N', command=lambda: 1)
        file_menu.add_command(label='Open', accelerator='Ctrl+O', command=lambda: 1)
        #file_menu.add_separator()
        file_menu.add_command(label='Exit', accelerator='Ctrl+Q')

        menu_bar.add_cascade(label='File', menu=file_menu)
        
        self["menu"] = menu_bar


    def _create_shortcut_bar_(self):
        shortcut_bar = Frame(self, height=25, background='#20b2aa')
        shortcut_bar.pack(fill=X)

        right_bar = Frame(self, width=25, background='#E1B14C')
        right_bar.pack(side=RIGHT, fill=Y)
        for i, icon in enumerate(ICONS):
            icon = PhotoImage(file='img/%s.gif' % icon)
            btn = Button(shortcut_bar, image=icon, command=self.open_file)
            btn.pack(side=LEFT)
            self.icon_res.append(icon)


    def _create_body_(self):

        scrollBar = Scrollbar(self)
        scrollBar.pack(side=RIGHT, fill=Y)

        self.tree = Treeview(self, show='headings', yscrollcommand=scrollBar.set)#表格
        index = tuple([str(i) for i in range(len(INFOS))])
        self.tree["columns"]=index

        # a = tuple([str(i) for i in range(5)])
        # print(a, type(a))
        for i, info in zip(index, INFOS):
            self.tree.column(i, width=len(i)*10, anchor = 'center')
            self.tree.heading(i,text=info)  #显示表头

        # self.tree.column("c1",width=50, anchor = 'center')   #表示列,不显示
        # self.tree.column("c2",width=100, anchor = 'center')
        # self.tree.column("c3",width=100, anchor = 'center')
        
        # self.tree.heading("c1",text="姓名-name")  #显示表头
        # self.tree.heading("c2",text="年龄-age")
        # self.tree.heading("c3",text="身高-tall")
        self.tree.pack(fill=BOTH, ipady = 500)

        scrollBar.config(command=self.tree.yview)
        # for i in range(100):
        #     self.tree.insert("", i, values=[str(i)]*6)

        #self.tree.bind('<ButtonRelease-1>', self.showline)
        self.tree.bind('<Double-Button-1>', self.showline) 


    def showline(self, event=None):
        print(self.tree.selection())
        for item in self.tree.selection():

            item_text = self.tree.item(item, 'values')
            print(item_text)
        
        # x = self.tree.get_children()
        # for i in x:
        #     self.tree.delete(i)

    def delete_item(self, event=None):
        print(self.tree.selection())
        for item in self.tree.selection():
            self.tree.delete(item)

    def add(self, event=None):
        add_windows = Toplevel(self)
        add_windows.geometry("320x400")
        add_windows.resizable(0, 0)
        add_windows.title('添加新的学生')
        
        frame = Frame(add_windows)
        frame.pack(fill=Y)

        self.entryList=locals()

        for i, info in enumerate(INFOS):
            name = info
            Label(frame, text=info+' : ').grid(row=i, column=0, pady = 5)
            self.entryList[name] = Entry(frame)
            self.entryList[name].grid(row=i, column=1, pady=5)
        
        # self.entryList['学号'].insert(0, 'helloworld')
        # print(self.entryList['学号'].get())

        frame_btn = Frame(add_windows)
        frame_btn.pack(fill=Y)
        Button(frame_btn, text='添加', command=lambda : update()).grid(row=0, column=0, pady=5)
        Button(frame_btn, text='清空', command=lambda : clear()).grid(row=0, column=1, pady=5)
        Button(frame_btn, text='取消', command=lambda : exit()).grid(row=0, column=2, pady=5)
        
        def exit():
            add_windows.destroy()
        
        def clear():
            for info in INFOS:
                self.entryList[info].delete(0, END)
        
        def update():
            DATAS = []
            for info in INFOS:
                data = self.entryList[info].get()
                DATAS.append(data)
            
            for i in DATAS:
                if i == '':
                    messagebox.showwarning(title='警告', message='输入空白')
                    clear()
                    return
            
            self.tree.insert("", END, values=DATAS)
            print(DATAS)



    def open_file(self):
        input_file = filedialog.askopenfilename(
            filetypes=[("所有文件", "*.*"), ("文本文档", "*.xlsx")])
        
        if input_file:
            print(input_file, type(input_file))

        def read_excel(*file):
            df = pd.DataFrame(columns=pd.read_excel(file[0]).columns) # 读取Excel表表头 File[0]：其中一个文件 
            print(df)
            
            for i in file:
                df = df.append(pd.read_excel(i), ignore_index=True)
            df.to_excel('my.xlsx')
            print(df)
            return df
    
        df = read_excel(input_file)

        for i in df.iloc:
            data = i.tolist()
            print(data)
            self.tree.insert("", END, values=data)



if "__main__" == __name__:
    app = Demo()
    app.mainloop()
