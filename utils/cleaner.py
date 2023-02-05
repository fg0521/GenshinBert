import json
import re
import pandas as pd
from openpyxl import Workbook,load_workbook
# from openpyxl.reader.excel import load_workbook
import os

def clear(x):
    x = re.sub('」「', '」、「', x)
    x = re.sub('\n|\t|\r| |​|※|〓|﻿|●|\d{8}|={1,}|…+|▌|」|『|』|「|>>(.*?)<<|”|“|• ', '', str(x))
    x = re.sub('！+', '！', x)
    x = re.sub('!+', '!', x)
    url_pattern = r'((?:(?<=[^a-zA-Z0-9]){0,}(?:(?:https?\:\/\/){0,1}(?:[a-zA-Z0-9\%]{1,}\:[a-zA-Z0-9\%]{1,}[@]){,1})(?:(?:\w{1,}\.{1}){1,5}(?:(?:[a-zA-Z]){1,})|(?:[a-zA-Z]{1,}\/[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\:[0-9]{1,4}){1})){1}(?:(?:(?:\/{0,1}(?:[a-zA-Z0-9\-\_\=\-]){1,})*)(?:[?][a-zA-Z0-9\=\%\&\_\-]{1,}){0,1})(?:\.(?:[a-zA-Z0-9]){0,}){0,1})'
    x = re.sub(url_pattern, '', x)
    x = re.sub('（|\(|【(.*?)】|\)|）', '', x)
    x = re.sub(' {2,}', ' ', x)
    x = re.sub('【|_|活动时间(.*?)59|', '', x)
    if 'CV' in x:
        x = x[:x.index('CV')]
    if '>>>' in x:
        x = x[:x.index('>>>')]
    return x
    # print(x)


def clear_notice():
    df = pd.read_csv('../dataset/notice.csv')
    df['s_content'] = df['s_content'].apply(lambda x: clear(''.join(eval(x))))
    df.drop_duplicates(subset='s_content', inplace=True)
    content = df['s_content'].tolist()
    df['len'] = df['s_content'].apply(lambda x: len(x))
    with open('../data/hmy-notice.txt', 'w') as f:
        for i in content:

            i = i.replace('!', '。').replace('！', '。').replace('；', '。').replace(';', '。').replace('?', '？')
            res = [k for k in i.split('。') if len(k) > 1]
            if 0 < len(res) < 2:
                if len(res[0]) > 30:
                    f.write(res[0] + '\n')
            else:
                for j in range(len(res) - 1):
                    s1 = res[j] if res[j].endswith('？') else res[j] + '。'
                    s2 = res[j + 1] if res[j + 1].endswith('？') else res[j + 1] + '。'
                    s = (s1 + s2).replace(' ', '')
                    if 256 > len(s) > 30:
                        f.write(s + '\n')
        f.close()
    # print(df['len'].value_counts())


def clear_info():
    res = []
    with open('../data/mhy-info.txt', 'r') as f:
        for line in f.readlines():
            while '」「' in line:
                idx = line.find('」「')
                if re.findall('[\u4e00-\u9fa5\da-zA-Z]+', line[idx - 1]) and re.findall('[\u4e00-\u9fa5\da-zA-Z]+',
                                                                                        line[idx + 2]):
                    line = line.replace('」「', '，')
                else:
                    line = line.replace('」「', '')
            line = re.sub('」|「|『|』', '', line)
            print(line)
            if len(line) > 15:
                res.append(line)
    with open('../data/mhy-info-clear.txt', 'w') as f1:
        [f1.write(i) for i in res]


def clear_audio():
    res = []
    symbol = set()
    rep_dict ={'~！':'~','···？':'？','….':'...','~~':'~','&nbsp;':'','…':'...',' ':'',',':'，',' ':'','██':'',
               '···':'...','？！':'？','！。':'！'}
    with open('../dataset/mhy-audio.txt') as f:
        for line in f.readlines():
            while '」「' in line:
                idx = line.find('」「')
                if re.findall('[\u4e00-\u9fa5\da-zA-Z]+', line[idx - 1]) and re.findall('[\u4e00-\u9fa5\da-zA-Z]+',
                                                                                        line[idx + 2]):
                    line = line.replace('」「', '，')
                else:
                    line = line.replace('」「', '')
            line = re.sub('」|「|『|』', '', line)
            if len(re.findall('[\u4e00-\u9fa5]', line)) >= 20 and '特殊料理' not in line:
                for k,v in rep_dict.items():
                    line = line.replace(k,v)
                [symbol.add(j) for j in re.findall('[^\u4e00-\u9fa5\da-zA-Z]+',line)]
                res.append(line)
    with open('../data/mhy-audio-clear.txt', 'w') as f1:
        [f1.write(i) for i in res]
    print(symbol)


def clear_xlsx():
    wb = load_workbook('../dataset/原神语音文本.xlsx')
    sheets = wb.worksheets  # 获取当前所有的sheet
    print(sheets)

    with open('../data/mhy-paimeng-clear.txt','w') as f:
        for sheet in sheets:
            print(sheet)
            try:
                for col in sheet['B']:
                    if len(str(col.value))>10:
                        f.write(col.value+'\n')
            except Exception as e:
                print(e)
                continue

def clear_story():
    content = []
    texts = os.listdir('../dataset/story')
    for t in texts:
        with open(os.path.join('../dataset/story',t),'r') as f:
            res = f.read().split('\n')
        each_content = ''
        for i in res:
            each_content = each_content+i
            if len(each_content)>80 and len(each_content)<256:
                each_content = re.sub('『|』|—{4,}|（.*?）','',each_content)
                each_content = each_content.replace('……','...').replace('“...”','')
                print(len(each_content))
                if len(each_content) >30:
                    content.append(each_content)
                each_content = ''
        # print(content)
        # break
    with open('../data/hmy-story-clear.txt','w') as f1:
        [f1.write(i+'\n') for i in content]


def get_audio_text():
    with open('/Users/maoyufeng/Downloads/GenshinVoice-main/result.json') as f:
        text = json.load(f)
    # print(type(text))
    with open('../data/hmy-audio2-clear.txt','w') as f:
        for k,v in text.items():
            if v['language'] == 'CHS' and v.get('text'):
                f.write(v['text']+'\n')

def clear_audio2():
    with open('../data/hmy-audio2-clear.txt','r') as f:
        text = [i for i in f.readlines() if len(re.findall('[\u4e00-\u9fa5]',i)) > 6]
    text = list(set(text))
    [print(i) for i in text if len(i)>255]
    with open('../data/hmy-audio2-clear2.txt','w') as f:
        [f.write(i) for i in text]



def clear_hot_strategy():
    rep_dict = {
        '①':'1.','②':'2.','③':'3.','④':'4.','⑤':'5.','⑥':'6.','⑦':'7.','⑧':'8.','⑨':'9.','⑩':'10.',
        '…':'...','➕':'+','＞':'>','＋':'+','≈':'=',
    }
    symbol = ['～', 'ω', '❶', 'Ⅱ', '｀',  '▲', '❸', '▋',  '②', '️', '◆',  '🔹', '④', '\ufeff',
     '③', 'Ⅰ', '▼','×',  '●',  '▌',  'ェ', '」', '❷',
         '。', '→', '\u200b', '•', '★',  '✪', '※',  '☆', 'Ⅲ', '´', '↓', '\xa0', '°', '⭐', '①',  '\t', '⑤', '√','>>']

    df = pd.read_csv('../dataset/hot_strategy.csv')
    df = df[['s_content']]
    df['s_content'] = df['s_content'].apply(lambda x:''.join(eval(x)).split('\n'))
    df['s_content'] = df['s_content'].apply(lambda x:[re.sub(' |_\(.*?\)','',s) for s in x if re.findall('[\u4e00-\u9fa5]+',s)])
    data = []
    for _,row in df.iterrows():
        data.extend(row['s_content'])
    new_data = []
    for s in data:
        for k,v in rep_dict.items():
            s = s.replace(k,v)
        for i in symbol:
            s = s.replace(i,'')
        if len(re.findall('[\u4e00-\u9fa5]',s))>10:
            new_data.append(s)
    # new_data = list(set(new_data))
    with open('../data/mhy-strategy-clear.txt','w') as f:
        [f.write(s+'\n') for s in new_data]
    [print(s) for s in new_data if len(s)>256]
    # symbol = set(list(''.join(re.findall('[^\da-zA-Z\u4e00-\u9fa5]',''.join(data)))))
    # print(list(symbol))


if __name__ == '__main__':
    clear_hot_strategy()
    # with open('../data/mhy-strategy-clear.txt', 'r') as f:
    #     res = [i.replace('\n','') for i in f.readlines()]
    # new_data = list(set(res))
    # with open('../data/mhy-strategy-clear.txt','w') as f:
    #     [f.write(s+'\n') for s in new_data]