
import tkinter
from tkinter import ttk  #导入内部包
 
win=tkinter.Tk()


scrollBar = tkinter.Scrollbar(win)
scrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

tree=ttk.Treeview(win, show='headings', yscrollcommand=scrollBar.set)#表格
tree["columns"]=("c1","c2","c3")


tree.column("c1",width=100, anchor = 'center')   #表示列,不显示
tree.column("c2",width=100, anchor = 'center')
tree.column("c3",width=100, anchor = 'center')
 
tree.heading("c1",text="姓名-name")  #显示表头
tree.heading("c2",text="年龄-age")
tree.heading("c3",text="身高-tall")
tree.pack(fill=tkinter.Y, ipady = 100)


scrollBar.config(command=tree.yview)
# tree.insert(", 0,values=("1","2","3")) #插入数据，
# tree.insert(", 1,values=("1","2","3"))
# tree.insert(", 2,values=("1","2","3"))
# tree.insert(", 3,values=("1","2","3"))
 
for i in range(100):
    tree.insert("", i, values=[str(i)]*6)
win.mainloop()