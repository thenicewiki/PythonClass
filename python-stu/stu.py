import pandas as pd
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Scrollbar, Checkbutton, Label, Button, Treeview
import os
from style import ICONS, INFOS


class Demo(Tk):
    icon_res = []
    file_name = None

    def __init__(self):
        super().__init__()
        self._set_windows_()
        self._create_menu_bar_()
        self._create_shortcut_bar_()
        self._create_body_()
        self.DATAS = pd.DataFrame(columns=INFOS)



    def _set_windows_(self):
        self.title('学生成绩管理系统')
        scn_width, scn_height = self.maxsize()
        wm_val = '750x450+%d+%d' % ((scn_width - 750) / 2, (scn_height - 450) / 2)
        self.geometry(wm_val)
        # self.iconbitmap("img/editor.ico")


    def _create_menu_bar_(self):
        menu_bar = Menu(self)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='add', accelerator='Ctrl+N', command=self.add)
        file_menu.add_command(label='Osave_to_file', accelerator='Ctrl+O', command=self.save_to_file)
        #file_menu.add_separator()
        file_menu.add_command(label='Exit', accelerator='Ctrl+Q', command=self.edit)
        file_menu.add_command(label='Search', accelerator='Ctrl+Q', command=self.search)
        file_menu.add_command(label='Total', accelerator='Ctrl+Q', command=self.total)
        file_menu.add_command(label='save_to_DATAS', accelerator='Ctrl+Q', command=self.save_to_DATAS)
        file_menu.add_command(label='Average', accelerator='Ctrl+Q', command=self.average)
        file_menu.add_command(label='open_file', accelerator='Ctrl+Q', command=self.open_file)
        file_menu.add_command(label='add', accelerator='Ctrl+Q', command=self.add)
        file_menu.add_command(label='delete_selected_item', accelerator='Ctrl+Q', command=self.delete_item)
        file_menu.add_command(label='clear_all', accelerator='Ctrl+Q', command=self.clear_all)
        file_menu.add_command(label='delete_item', accelerator='Ctrl+Q', command=self.delete_item)






        menu_bar.add_cascade(label='File', menu=file_menu)
        
        self["menu"] = menu_bar


    def _create_shortcut_bar_(self):
        shortcut_bar = Frame(self, height=25, background='#20b2aa')
        shortcut_bar.pack(fill=X)

        right_bar = Frame(self, width=25, background='#E1B14C')
        right_bar.pack(side=RIGHT, fill=Y)
        for i, icon in enumerate(ICONS):
            icon = PhotoImage(file='img/%s.gif' % icon)
            btn = Button(shortcut_bar, image=icon, command= lambda : self.open_file('new.xlsx'))
            btn.pack(side=LEFT)
            self.icon_res.append(icon)


    def _create_body_(self):

        scrollBar = Scrollbar(self)
        scrollBar.pack(side=RIGHT, fill=Y)

        self.tree = Treeview(self, show='headings', yscrollcommand=scrollBar.set)#表格
        index = tuple([str(i) for i in range(len(INFOS))])
        self.tree["columns"]=index

        for i, info in zip(index, INFOS):
            self.tree.column(i, width=len(i)*10, anchor = 'center')
            self.tree.heading(i,text=info)  #显示表头

        self.tree.pack(fill=BOTH, ipady = 500)

        # 将滚动条绑定至Treeview
        scrollBar.config(command=self.tree.yview)

        # 快捷键相关设置
        # 函数参数需要有event=None
        self.tree.bind('<Double-Button-1>', self.showline) 


    def showline(self, event=None):
        print(self.tree.selection())
        for item in self.tree.selection():
            item_text = self.tree.item(item, 'values')
            print(item_text)
        

    def clear_all(self):
        print('-------------follow item will be cleared:BEG-------------')
        print(self.tree.get_children())
        print('\n')
        for item in self.tree.get_children():
            self.tree.delete(item)
            print(item + ' : ', end = ' ')
            print('deleted', end=' ')
        print('\n-------------items had been cleared:END-------------')
        


    def delete_item(self, event=None):
        print('-------------Your selection:BEG-------------')
        print(self.tree.selection())
        for item in self.tree.selection():
            self.tree.delete(item)
        print('-------------Your selection cleared:END-------------')
        

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
            
            for i in DATAS[:-1]:
                if i == '':
                    messagebox.showwarning(title='警告', message='输入空白')
                    clear()
                    return
            
            self.tree.insert("", END, values=DATAS)



    def open_file(self, options=None):
        if options:
            input_file = options
        else:
            input_file = filedialog.askopenfilename(
                filetypes=[("所有文件", "*.*"), ("文本文档", "*.xlsx")])
            
            if input_file:
                print('-----------------成功导入文件:', input_file, type(input_file), '---------------')

        def read_excel(file):
            df = pd.read_excel(file)
            print('---------------reading excel!-----------------')
            print(df)
            print('---------------read excel done!-----------------')
            return df

        df = read_excel(input_file)

        # input data to Treeview
        print('---------------inputing to TreeView!-----------------')
        for i in df.iloc:
            data = i.tolist()
            # 若导入的文件中缺少数据，则缺少的数据用空补上
            for i in range(len(INFOS)-len(data)):
                data.append('')
            # 打印测试
            print(data)
            self.tree.insert("", END, values=data)
        print('---------------input to TreeView done!-----------------')
        

        
    
    def save_to_DATAS(self):
        print('---------------saving to DATAS!-----------------')
        self.DATAS = pd.DataFrame(columns=INFOS)
        indexs = self.tree.get_children()
        for i in indexs:
            value = self.tree.item(i, 'values')
            print(value)
            self.DATAS.loc[len(self.DATAS)] = list(value)
        print('---------------save to DATAS done!-----------------')


    def save_to_file(self):
        self.save_to_DATAS()
        outputfile = 'new.xlsx'
        self.DATAS.to_excel(outputfile, index=FALSE)
        print('---------------------------save to file done!---------------------------------')

    def edit(self):
        item = self.tree.selection()

        self.tree.set(item, 0, value='helloworld')


    def search(self):
        search_windows = Toplevel(self)
        search_windows.title('查找文本')
        search_windows.transient(self)
        search_windows.resizable(0, 0)

        Label(search_windows, text='查找全部:').grid(row=0, column=0, sticky=E)
        search_entry = Entry(search_windows, width=25)
        search_entry.grid(row=0, column=1, padx=2, pady=20, sticky='we')
        search_entry.focus_set()

        Button(search_windows, text='查找', command=lambda: search_result()).grid(row=0, column=2, sticky=E+W, padx=2, pady=2)



        def search_result():
            indexs = self.tree.get_children()
            search_data = search_entry.get()
            print(search_data, type(search_data))

            for i, index in enumerate(indexs):
                values = self.tree.item(index, 'values')
                print(values, end=' ')
                for value in list(values)[:2]:
                    if search_data in value:
                        print('Found')
                        self.tree.selection_set(index)
                        self.tree.yview_moveto(i/len(indexs))
                        return
                    else:
                        print('No Found')

        # 选择
        # self.tree.selection_set('I001')
        # self.tree.yview_moveto(1)

        # 取消选择
        # self.tree.selection_remove('I001')


    def total(self):
        self.save_to_DATAS()
        temp = self.DATAS[['成绩A', '成绩B', '成绩C']].astype('int')
        self.DATAS['总分'] = temp.sum(axis=1)
        print('---------------------------Total calculate done!-----------------------------')
        print(self.DATAS)
        print('---------------------------Total calculate done!-----------------------------')

        # 删除Treeview中所有元素
        for index in self.tree.get_children():
            self.tree.delete(index)
        # 插入DATAS中的元素到TreeView中
        for i in self.DATAS.iloc:
            data = i.tolist()
            data = data if len(data) == len(INFOS) else data.append('')
            self.tree.insert("", END, values=data)



    def average(self):
        self.total()
        temp = self.DATAS[['总分']].astype('float64')
        av = temp.mean(axis=0)
        print('---------------------------AV-----------------------------')
        print('平均分：', float(av))
        print('---------------------------AV-----------------------------')


if "__main__" == __name__:
    app = Demo()
    app.mainloop()
