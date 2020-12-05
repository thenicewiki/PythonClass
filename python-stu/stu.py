import pandas as pd
import numpy as np
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Scrollbar, Checkbutton, Label, Button, Treeview
import os
from style import ICONS, INFOS, ADRS



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
        wm_val = '1200x450+%d+%d' % ((scn_width - 800) / 2, (scn_height - 450) / 2)
        self.geometry(wm_val)
        # self.iconbitmap("img/editor.ico")


    def _create_menu_bar_(self):
        menu_bar = Menu(self)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='add', accelerator='Ctrl+N', command=self.add)
        file_menu.add_command(label='save_to_file', command=self.save_to_file)
        file_menu.add_command(label='Exit', command=self.edit)
        file_menu.add_command(label='Search', command=self.search)
        file_menu.add_command(label='Total', command=self.total)
        file_menu.add_command(label='save_to_DATAS', command=self.save_to_DATAS)
        file_menu.add_command(label='Average', command=self.average)
        file_menu.add_command(label='open_file', command=self.open_file)
        file_menu.add_command(label='add', command=self.add)
        file_menu.add_command(label='delete_selected_item', command=self.delete_item)
        file_menu.add_command(label='clear_all', command=self.clear_all)
        file_menu.add_command(label='delete_item', command=self.delete_item)
        file_menu.add_command(label='init_demo', command=self.init_demo)
        file_menu.add_command(label='sort_as_total', command=self.sort_as_total)
        file_menu.add_command(label='average_stu', command=self.average_stu)







        menu_bar.add_cascade(label='程序中所有函数(测试)', menu=file_menu)
        
        self["menu"] = menu_bar


    def _create_shortcut_bar_(self):
        shortcut_bar = Frame(self, height=25, background='#00CED1')
        shortcut_bar.pack(fill=X)

        right_bar = Frame(self, width=25, background='#FF8C00')
        right_bar.pack(side=RIGHT, fill=Y)

        for i, icon in enumerate(ICONS):
            icon_img = PhotoImage(file='img/%s.gif' % icon)
            btn = Button(shortcut_bar, image=icon_img, command= lambda x = icon : self._shortcut_action_(x))
            btn.pack(side=LEFT)
            self.icon_res.append(icon_img)


    def _create_body_(self):

        scrollBar = Scrollbar(self)
        scrollBar.pack(side=RIGHT, fill=Y)

        self.tree = Treeview(self, show='headings', yscrollcommand=scrollBar.set) # 表格
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
        self.tree.bind('<Double-Button-1>', self.edit) 
    
    
    # 响应快捷菜单
    def _shortcut_action_(self, type):

        if type == "open_file":
            self.open_file()
        elif type == "add":
            self.add()
        elif type == "edit":
            self.edit()
        elif type == "save_file":
            self.save_to_file()
        elif type == "save_DATAS":
            self.save_to_DATAS()
        elif type == "delete":
            self.delete_item()
        elif type == "clear_all":
            self.clear_all()
        elif type == "search":
            self.search()
        elif type == "total":
            try:
                self.total()
            except:
                messagebox.showinfo(title='警告', message='请检查输入信息')
        elif type == "average":
            try:
                self.average()
            except:
                messagebox.showinfo(title='警告', message='请检查输入信息')
        elif type == "sort":
            try:
                self.sort_as_total()
            except:
                messagebox.showinfo(title='警告', message='请检查输入信息')
        elif type == "sort_no":
            try:
                self.sort_as_no()
            except:
                messagebox.showinfo(title='警告', message='请检查输入信息')
        elif type == "exit":
            self.exit()
        elif type == "average_stu":
            try:
                self.average_stu()
            except:
                messagebox.showinfo(title='警告', message='请检查输入信息')
        elif type == "about":
            self.about()


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
    
    def init_demo(self):
        self.clear_all()
        self.DATAS = pd.DataFrame(columns=INFOS)
        print('---------------demo inited----------------')


    def delete_item(self, event=None):
        print('-------------Your selection:BEG-------------')
        print(self.tree.selection())
        for item in self.tree.selection():
            self.tree.delete(item)
        print('-------------Your selection cleared:END-------------')
        

    def add(self, event=None):
        add_windows = Toplevel(self)
        scn_width, scn_height = self.maxsize()
        wm_val = '320x400+%d+%d' % ((scn_width - 320) / 2, (scn_height - 400) / 2)
        add_windows.geometry(wm_val)
        add_windows.resizable(0, 0)
        add_windows.title('添加新的学生')
        
        frame = Frame(add_windows)
        frame.pack(fill=Y)

        self.entryList=locals()

        for i, info in enumerate(INFOS[:-2]): # -2 不添加总分 和 平均分
            Label(frame, text=info+' : ').grid(row=i, column=0, pady = 5)
            self.entryList[info] = Entry(frame)
            self.entryList[info].grid(row=i, column=1, pady=5)

        frame_btn = Frame(add_windows)
        frame_btn.pack(fill=Y)
        Button(frame_btn, text='添加', command=lambda : update()).grid(row=0, column=0, pady=5)
        Button(frame_btn, text='清空', command=lambda : clear()).grid(row=0, column=1, pady=5)
        Button(frame_btn, text='取消', command=lambda : exit()).grid(row=0, column=2, pady=5)
        

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
        

        def clear():
            for info in INFOS:
                self.entryList[info].delete(0, END)
        

        def exit():
            add_windows.destroy()

    def open_file(self, options=None):
        if options:
            input_file = options
        else:
            input_file = filedialog.askopenfilename(
                filetypes=[("所有文件", "*.*"), ("Excel文档", "*.xlsx")])
            
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

            # 测试用 把 平均分 和 总分 置空
            data[-1] = ''
            data[-2] = ''
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
        outputfile = filedialog.asksaveasfilename(filetypes=[("所有文件", "*.*"), ("Excel文档", "*.xlsx")])
        self.save_to_DATAS()
        # outputfile = 'new.xlsx'
        self.DATAS.to_excel(outputfile, index=FALSE)
        print('---------------------------save to file done!---------------------------------')

    def edit(self, event=None):

        item = self.tree.selection()
        
        # Layout
        edit_windows = Toplevel(self)
        scn_width, scn_height = self.maxsize()
        wm_val = '320x450+%d+%d' % ((scn_width - 320) / 2, (scn_height - 450) / 2)
        edit_windows.geometry(wm_val)
        edit_windows.resizable(0, 0)
        edit_windows.title('编辑学生信息')
        
        
        # 创建标签和输入框
        frame = Frame(edit_windows)
        frame.pack(fill=Y)
        self.entryList=locals()
        for i, info in enumerate(INFOS):
            Label(frame, text=info+' : ').grid(row=i, column=0, pady=5)
            self.entryList[info] = Entry(frame)
            self.entryList[info].grid(row=i, column=1, pady=5)


        # 创建按钮布局
        frame_btn = Frame(edit_windows)
        frame_btn.pack(fill=Y)
        Button(frame_btn, text='确定', command=lambda : update()).grid(row=0, column=0, pady=5)
        Button(frame_btn, text='清空', command=lambda : clear()).grid(row=0, column=1, pady=5)
        Button(frame_btn, text='取消', command=lambda : exit()).grid(row=0, column=2, pady=5)
    


        # 将待修改的数据导入输入框(方便修改,不用全部重新输入)
        values = self.tree.item(item, 'values')
        for value, info in zip(values, INFOS):
            self.entryList[info].insert(END, value)
            print(values)
            print('--------------input to entry done!------------')


        def update():
            temp = []
            for i, info in enumerate(INFOS):
                data = self.entryList[info].get()
                temp.append(data)
                self.tree.set(item, i, value=data)

            print('----------------editing data!-----------------')
            print(temp)
            print('---------------edit data done!-----------------')
            exit()


        def clear():
            for info in INFOS:
                self.entryList[info].delete(0, END)

        def exit():
            edit_windows.destroy()
        
        # item = self.tree.selection()
        # self.tree.set(item, 0, value='helloworld')


    def search(self):
        search_windows = Toplevel(self)
        search_windows.title('搜索全部')
        search_windows.transient(self)
        search_windows.resizable(0, 0)
        scn_width, scn_height = self.maxsize()
        wm_val = '380x70+%d+%d' % ((scn_width - 380) / 2, (scn_height - 70) / 2)
        search_windows.geometry(wm_val)
        Label(search_windows, text='查找全部:').grid(row=0, column=0, sticky=E)
        search_entry = Entry(search_windows, width=25)
        search_entry.grid(row=0, column=1, padx=2, pady=20, sticky='we')
        search_entry.focus_set()

        Button(search_windows, text='查找', command=lambda: search_result()).grid(row=0, column=2, sticky=E+W, padx=2, pady=2)



        def search_result():
            result = []
            indexs = self.tree.get_children()
            search_data = search_entry.get()
            print(search_data, type(search_data))

            for i, index in enumerate(indexs):
                values = self.tree.item(index, 'values')
                print(values, end=' ')
                for value in list(values)[:2]:
                    if search_data in value:
                        result.append(search_data)
                        print(result)
                        self.tree.selection_set(index)
                        self.tree.yview_moveto(i/len(indexs))
                        break
                    else:
                        print('No Found')

            if result:
                return
            else:
                messagebox.showinfo(title='提示', message='未找到匹配项')
        # 选择
        # self.tree.selection_set('I001')
        # self.tree.yview_moveto(1)

        # 取消选择
        # self.tree.selection_remove('I001')

    def update_to_tree(self):
        # 删除Treeview中所有元素
        for index in self.tree.get_children():
            self.tree.delete(index)
        # 插入DATAS中的元素到TreeView中
        for i in self.DATAS.iloc:
            data = i.tolist()
            self.tree.insert("", END, values=data)


    def total(self):
        self.save_to_DATAS()
        temp = self.DATAS[['成绩A', '成绩B', '成绩C']].astype('int')
        self.DATAS['总分'] = temp.sum(axis=1) 
        print('---------------------------Total calculate done!-----------------------------')
        print(self.DATAS)
        print('---------------------------Total calculate done!-----------------------------')

        # # 删除Treeview中所有元素
        # for index in self.tree.get_children():
        #     self.tree.delete(index)
        # # 插入DATAS中的元素到TreeView中
        # for i in self.DATAS.iloc:
        #     data = i.tolist()
        #     self.tree.insert("", END, values=data)

        self.update_to_tree()
    
    
    def average_stu(self):
        self.save_to_DATAS()
        temp = self.DATAS[['成绩A', '成绩B', '成绩C']].astype('int')
        
        # round 计算并保留两位小数 round( *, 2 )
        self.DATAS['平均分'] = round(temp.mean(axis=1), 2)
        print('---------------------------per average calculate done!-----------------------------')
        print(self.DATAS)
        print('---------------------------per average done!-----------------------------')

        self.update_to_tree()



    def average(self):
        self.total()
        temp = self.DATAS[['总分']].astype('float64')
        av = temp.mean(axis=0)
        print('---------------------------AV-----------------------------')
        print('平均分：', float(av))
        print('---------------------------AV-----------------------------')

        class_grade = '\t总平均分: %.2f' % float(av)

        messagebox.showinfo(title='平均分', message=class_grade)

    def sort_as_total(self):
        self.total()
        self.DATAS.sort_values(by='总分', ascending=False, inplace=True)
        print('--------------------sorting values!----------------')
        print(self.DATAS)
        print('--------------------sort values done!--------------')
        
        # drop 清洗列表 去掉NaN的行 
        self.DATAS.reset_index(drop=True, inplace=True)
        print('--------------------cleaning datas!----------------')
        print(self.DATAS)
        print('--------------------clean datas done!--------------')
        self.update_to_tree()
        print('--------------------update to tree done!--------------')

        # Text
        self.DATAS.to_excel('text.xlsx', index=False)

    
    def sort_as_no(self):
        self.save_to_DATAS()
        self.DATAS['学号'] = self.DATAS[['学号']].astype('int')
        self.DATAS.sort_values(by='学号', inplace=True)
        print(self.DATAS)
        print('-------------------sort as no done!-----------------')

        self.DATAS.reset_index(drop=True, inplace=True)
        print(self.DATAS)
        print('--------------------clean data done!-----------------')
        self.update_to_tree()
        print('--------------------update to tree done!--------------')

        # Text
        self.DATAS.to_excel('text_sort_no.xlsx', index=False)



    def about(self):
        # info = 'Github Page: %s \nWeb: %s\n' % (ADRS[0], ADRS[1])
        # messagebox.showinfo(title='About', message=info)

        about_windows = Toplevel(self)
        about_windows.title('about')
        for i, icon in enumerate(ICONS):
            icon_img = PhotoImage(file='img/%s.gif' % icon)
            Label(about_windows, image=icon_img).pack(fill=BOTH)
            # btn.pack(fill=Y)
            self.icon_res.append(icon_img) # 必须有这句话 保存图片


    def exit(self):
        if messagebox.askokcancel("退出?", "确定退出吗?"):
            self.quit()


if "__main__" == __name__:
    app = Demo()
    app.mainloop()
