from tkinter import *

class stu():
    def __init__(self):
        self.name = ""
        self.num = 0
        self.grade = 0

    def _show_stu_(self):
        print(self.name, self.num, self.grade)


class Demo(Tk):
    def __init__(self):
        super().__init__()
        self._set_windows_()
        self._create_menu_bar_()
        self._create_layout_()

    def _set_windows_(self):
        self.title('StuMes')
        self.geometry('350x390')

    def _create_menu_bar_(self):
        print('hello')


    def _create_layout_(self):
        print('hello')

if "__main__" == __name__:
    a = stu()
    a._show_stu_()
    app = Demo()
    app.mainloop()