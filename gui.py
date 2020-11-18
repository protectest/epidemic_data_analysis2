import tkinter as tk
import data_analyze
import creeper
import os


def press0():
    v = list()
    file = None
    for j in range(len(data_analyze.u0_list)):
        if listbox0.select_includes(j):
            v.append(listbox0.get(j))
            file = 'u0'
    for j in range(len(data_analyze.u1_list)):
        if listbox1.select_includes(j):
            v.append(listbox1.get(j))
            file = 'u1'
    for j in range(len(data_analyze.u2_list)):
        if listbox2.select_includes(j):
            v.append(listbox2.get(j))
            file = 'u2'
    data_analyze.multi_draw0(v, file=file)


def press1():
    mode_list = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get()]
    path = list(entry1.get())
    path = ''.join(path)
    back = data_analyze.user_file(path)
    for j in range(len(back[0])):
        if listbox3.select_includes(j):
            path = os.path.join(path, listbox3.get(j))
            break
    else:
        return
    data_analyze.multi_draw1(path, var0.get(), ''.join(entry2.get()), ''.join(entry3.get()), mode_list)


def press2():
    listbox3.delete(0, 'end')
    path = list(entry1.get())
    path = ''.join(path)
    back = data_analyze.user_file(path)
    for j in back[0]:
        listbox3.insert('end', j)
    if back[1] == 0:
        window0 = tk.Tk()
        window0.geometry('500x120')
        show = tk.Label(window0, text='该路径不存在，或者输入格式错误，将显示默认路径。')
        show.place(x=100, y=40)


def press3():
    v = list(entry0.get())
    v = ''.join(v)
    data_list = [v]
    if v in data_analyze.u0_list:
        data_analyze.multi_draw0(place_list=data_list, file='u0')
    elif v in data_analyze.u1_list:
        data_analyze.multi_draw0(place_list=data_list, file='u1')
    elif v in data_analyze.u2_list:
        data_analyze.multi_draw0(place_list=data_list, file='u2')
    else:
        window0 = tk.Tk()
        window0.geometry('200x120')
        show = tk.Label(window0, text='该数据不存在。')
        show.pack()


status_list = list()


if __name__ == '__main__':
    window = tk.Tk()
    window.title('疫情实时数据分析')
    window.geometry('680x450+0+27')
    window.resizable(False, False)

    entry0 = tk.Entry(window, width=30)
    entry0.insert(0, '搜索')
    entry0.place(x=10, y=10)

    entry1 = tk.Entry(window, width=35)
    entry1.insert(0, r'D:\test\疫情数据分析2.0\data\user')
    entry1.place(x=330, y=10)

    entry2 = tk.Entry(window, width=20)
    entry2.insert(0, 'X轴标题：')
    entry2.place(x=520, y=300)

    entry3 = tk.Entry(window, width=20)
    entry3.insert(0, 'Y轴标题：')
    entry3.place(x=520, y=320)

    listbox0 = tk.Listbox(window)
    for i in data_analyze.u0_list:
        listbox0.insert('end', i)
    listbox0.place(x=10, y=50)

    listbox1 = tk.Listbox(window, selectmode='multiple')
    for i in data_analyze.u1_list:
        listbox1.insert('end', i)
    listbox1.place(x=10, y=250)

    listbox2 = tk.Listbox(window, selectmode='multiple')
    for i in data_analyze.u2_list:
        listbox2.insert('end', i)
    listbox2.place(x=170, y=50)

    listbox3 = tk.Listbox(window, width=25, height=21)
    listbox3.place(x=330, y=50)

    button0 = tk.Button(window, width=19, text='确定', command=press0)
    button0.place(x=170, y=400)

    button1 = tk.Button(window, width=19, text='确定', command=press1)
    button1.place(x=520, y=400)

    button2 = tk.Button(window, width=8, text='导入', command=press2)
    button2.place(x=600, y=10)

    button3 = tk.Button(window, width=8, text='搜索', command=press3)
    button3.place(x=250, y=10)

    var0 = tk.IntVar()
    checkbutton = tk.Checkbutton(window, text='转置', variable=var0, onvalue=1, offvalue=0)
    checkbutton.place(x=520, y=350)

    var1 = tk.IntVar()
    check0 = tk.Checkbutton(window, text=data_analyze.mode_list[0], variable=var1, onvalue=1, offvalue=0)
    check0.place(x=520, y=50)

    var2 = tk.IntVar()
    check1 = tk.Checkbutton(window, text=data_analyze.mode_list[1], variable=var2, onvalue=1, offvalue=0)
    check1.place(x=520, y=100)

    var3 = tk.IntVar()
    check2 = tk.Checkbutton(window, text=data_analyze.mode_list[2], variable=var3, onvalue=1, offvalue=0)
    check2.place(x=520, y=150)

    var4 = tk.IntVar()
    check3 = tk.Checkbutton(window, text=data_analyze.mode_list[3], variable=var4, onvalue=1, offvalue=0)
    check3.place(x=520, y=200)

    var5 = tk.IntVar()
    check4 = tk.Checkbutton(window, text=data_analyze.mode_list[4], variable=var5, onvalue=1, offvalue=0)
    check4.place(x=520, y=250)

    window.mainloop()
