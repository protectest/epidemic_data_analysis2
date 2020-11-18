import os
import math
import pandas as pd
import multiprocessing
from matplotlib import pyplot as plt


class MyProcess(multiprocessing.Process):

    def __init__(self, i, path, x_name, y_name, trans):
        super().__init__()
        self.i = i
        self.path = path
        self.x_name = x_name
        self.y_name = y_name
        self.trans = trans

    def run(self):
        try:
            mode_function_list[self.i](self.path, self.x_name, self.y_name, self.trans)
        except:
            print('文件类型或格式不支持。')


def multi_draw0(place_list, file, x_name='日期', y_name='人数'):
    if file == 'u0':
        for i in place_list:
            draw0(i)
    else:
        if len(place_list) > 1:
            process = multiprocessing.Process(target=cmp_draw, args=(place_list, file))
            process.start()
        for i in place_list:
            process = multiprocessing.Process(target=draw1, args=(i, file, x_name, y_name))
            process.start()


def multi_draw1(path, trans, x_name, y_name, mode):
    draw_list = list()
    for i in range(5):
        if mode[i]:
            draw_list.append(MyProcess(i, path, x_name, y_name, trans))
    for i in draw_list:
        i.start()


def cmp_draw(place_list, file):
    tmp_data = list()
    for i in place_list:
        path = os.path.join('D:/', 'test', '疫情数据分析2.0', 'data', file, i)
        tmp_data.append(pd.read_csv(path, index_col=0))
    index = tmp_data[0].index
    plt.figure()
    for i in range(len(index)):
        plt.subplot(2, 2, 1 + i)
        plt.subplots_adjust(wspace=0.1, hspace=0.3, left=0.035, right=0.99, top=0.95, bottom=0.1)
        data = list()
        for j in tmp_data:
            data.append(j.iloc[i, :])
        data = pd.concat(data, axis=1, sort=True)
        data.columns = place_list
        index_list = list(map(str, list(data.index)))
        index_list.sort(key=lambda a: (int(a[0]), int(a[2:])))
        data = data.reindex(index_list)
        plt.title(index[i])
        plt.plot(data)
        plt.xticks(rotation=90)
        plt.grid()
        plt.legend(place_list)
    plt.show()


def draw0(place):
    path = os.path.join('D:/', 'test', '疫情数据分析2.0', 'data', 'u0', place)
    data = pd.read_csv(path, index_col=0)
    if place == 'allForeignTrend':
        data = data.T
        data.plot()
    else:
        data.index = data.loc[:, 'country']
        data.plot(kind='bar')
    plt.show()


# place只能传入字符串（即该函数一次只能画一张图）x_name和y_name参数是数轴名
def draw1(place, file, x_name='日期', y_name='人数'):
    path = os.path.join('D:/', 'test', '疫情数据分析2.0', 'data', file, place)
    data = pd.read_csv(path, index_col=0)
    x = list(data.columns)
    index = list(data.index)
    plt.figure(figsize=(20, 10), dpi=80)
    plt.title(place)
    for i in range(len(index)):
        plt.subplot(math.ceil(len(index) / 2), 2, 1 + i)
        plt.subplots_adjust(wspace=0.1, hspace=0.3, left=0.035, right=0.99, top=0.95, bottom=0.1)
        data1 = pd.Series(data.loc[index[i], :])
        plt.plot(x, data1.values)
        plt.grid(alpha=0.4)
        plt.xticks(rotation=90)
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.title(place + index[i])
    plt.show()


# trans参数控制数据转置 place只能传入字符串（即该函数一次只能画一张图）
def plot_draw(path, x, y, trans=False):
    data = pd.read_csv(path, index_col=0)
    if trans:
        data = data.T
    data.plot()
    plt.xlabel(x)
    plt.ylabel(y)
    plt.legend(list(data.columns))
    plt.show()


def bar_draw(path, x, y, trans=False):
    data = pd.read_csv(path, index_col=0)
    if trans:
        data = data.T
    data.plot(kind='bar')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.legend(list(data.columns))
    plt.show()


def hist_draw(path, x, y, trans=False):
    data = pd.read_csv(path, index_col=0)
    if trans:
        data = data.T
    data.plot(kind='hist')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.legend(list(data.columns))
    plt.show()


def scatter_draw(path, x, y, trans=False):
    data = pd.read_csv(path, index_col=0)
    if trans:
        data = data.T
    plt.figure()
    for i in range(len(data.index)):
        plt.scatter(data.columns, y=data.iloc[i])
    plt.xticks(rotation=90)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.legend(list(data.index))
    plt.show()


def box_draw(path, x, y, trans=False):
    data = pd.read_csv(path, index_col=0)
    if trans:
        data = data.T
    data.plot(kind='box')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.legend(list(data.columns))
    plt.show()


def user_file(path):
    try:
        return list(os.listdir(path=path)), 1
    except:
        return list(os.listdir(path=r'D:\test\疫情数据分析2.0\data\user')), 0


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

file_name = ['u0', 'u1', 'u2', 'user']
u0_list = set(os.listdir(path=r'D:\test\疫情数据分析2.0\data\u0')) - {'热门', '其他', 'update', 'update.txt'}
u1_list = set(os.listdir(path=r'D:\test\疫情数据分析2.0\data\u1'))
u2_list = set(os.listdir(path=r'D:\test\疫情数据分析2.0\data\u2')) - {'钻石公主号邮轮'}
u3_list = 'allForeignTrend'
main_list = u0_list | u1_list | u2_list
mode_list = ['折线图', '条形图', '直方图', '散点图', '箱式图']
mode_function_list = [plot_draw, bar_draw, hist_draw, scatter_draw, box_draw]

if __name__ == '__main__':
    pass
