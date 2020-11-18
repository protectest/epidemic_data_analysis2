import re
import os
import json
import requests
import pandas as pd
import multiprocessing
from bs4 import BeautifulSoup


def save_0():
    with open(r'D:\test\疫情数据分析2.0\data\u0\update.txt', 'w+', encoding='utf-8') as fb:
        fb.write(str(data['component'][0][keys[0]]))

    for element0 in data['component'][0][keys[1]]:
        method = os.path.join('D:/', 'test', '疫情数据分析2.0', 'data', 'u0', element0['area'])
        tmp_data0 = list()
        for element1 in element0['subList']:
            del element1['relativeTime']
            tmp_data0.append(element1)
        tmp_data1 = pd.DataFrame(tmp_data0)
        tmp_data1.to_csv(method)

    method = os.path.join('D:/', 'test', '疫情数据分析2.0', 'data', 'u0', keys[2])
    column = data['component'][0][keys[2]]['updateDate']
    index = list()
    tmp_data0 = list()
    for element in data['component'][0][keys[2]]['list']:
        index.append(element['name'])
        tmp_data0.append(element['data'])
    tmp_data1 = pd.DataFrame(tmp_data0, columns=column, index=index)
    tmp_data1.to_csv(method)


def save_1_2():
    for element0 in data['data']:
        method = os.path.join('D:/', 'test', '疫情数据分析2.0', 'data', name_list[i], element0['name'])
        index = list()
        tmp_data0 = list()
        for element1 in element0['trend']['list']:
            index.append(element1['name'])
            tmp_data0.append(element1['data'])
            tmp_data1 = pd.DataFrame(tmp_data0, columns=element0['trend']['updateDate'], index=index)
            tmp_data1.to_csv(method)


u0 = 'https://voice.baidu.com/act/newpneumonia/newpneumonia'
u1 = 'https://voice.baidu.com/newpneumonia/get?target=trend&isCaseIn=0&stage=publish&callback=jsonp_1591191502151_17075'
u2 = 'https://voice.baidu.com/newpneumonia/get?target=trend&isCaseIn=1&stage=publish&callback=jsonp_1591191502150_39236'
url = [u0, u1, u2]
name_list = ['u0', 'u1', 'u2']
keys = ['foreignLastUpdatedTime', 'globalList', 'allForeignTrend']


for _ in range(5):
    try:
        r = requests.get(url[0], timeout=1)
        r.encoding = 'utf-8'
        r = r.text
        r = BeautifulSoup(r, 'html.parser')
        r = str(r.find_all('script')[11])
        r = re.sub('<.*?>', '', r)
        data = json.loads(r)
        save_0()
    except:
        continue
    print('success 0')
    break
else:
    print('fail_0')

for i in range(1, 3):
    for _ in range(5):
        try:
            r = requests.get(url[i], timeout=1)
            r.encoding = 'utf-8'
            r = r.text
            r = re.findall(r"[(](.*?)[)]", r)
            r = list(r)
            data = json.loads(r[0])
            save_1_2()
        except:
            continue
        print('success {}'.format(i))
        break
    else:
        print('fail {}'.format(i))
