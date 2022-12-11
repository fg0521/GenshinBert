import re
import pandas as pd

def clear(x):
    x = re.sub('」「','」、「',x)
    x = re.sub('\n|\t|\r| |​|※|〓|﻿|●|\d{8}|={1,}|…+|▌|」|『|』|「|>>(.*?)<<|”|“|• ','',str(x))
    x = re.sub('！+','！',x)
    x = re.sub('!+','!',x)
    url_pattern = r'((?:(?<=[^a-zA-Z0-9]){0,}(?:(?:https?\:\/\/){0,1}(?:[a-zA-Z0-9\%]{1,}\:[a-zA-Z0-9\%]{1,}[@]){,1})(?:(?:\w{1,}\.{1}){1,5}(?:(?:[a-zA-Z]){1,})|(?:[a-zA-Z]{1,}\/[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\:[0-9]{1,4}){1})){1}(?:(?:(?:\/{0,1}(?:[a-zA-Z0-9\-\_\=\-]){1,})*)(?:[?][a-zA-Z0-9\=\%\&\_\-]{1,}){0,1})(?:\.(?:[a-zA-Z0-9]){0,}){0,1})'
    x = re.sub(url_pattern,'',x)
    x = re.sub('（|\(|【(.*?)】|\)|）','',x)
    x = re.sub(' {2,}',' ',x)
    x = re.sub('【|_|活动时间(.*?)59|','',x)
    if 'CV' in x:
        x = x[:x.index('CV')]
    if '>>>' in x:
        x = x[:x.index('>>>')]
    return x
    # print(x)



def clear_notice():
    df = pd.read_csv('../data/notice.csv')
    df['s_content'] = df['s_content'].apply(lambda x:clear(''.join(eval(x))))
    df.drop_duplicates(subset='s_content',inplace=True)
    content = df['s_content'].tolist()
    df['len'] = df['s_content'].apply(lambda x:len(x))
    with open('../data/hmy-notice.txt','w') as f:
        for i in content:

            i = i.replace('!','。').replace('！','。').replace('；','。').replace(';','。').replace('?','？')
            res = [k for k in i.split('。') if len(k)>1]
            if 0<len(res)<2:
                if len(res[0])>30:
                    f.write(res[0]+'\n')
            else:
                for j in range(len(res)-1):
                    s1 = res[j] if res[j].endswith('？') else res[j]+'。'
                    s2 = res[j+1] if res[j+1].endswith('？') else res[j+1]+'。'
                    s = (s1+s2).replace(' ','')
                    if 256>len(s) >30:
                        f.write(s+'\n')
        f.close()
    # print(df['len'].value_counts())

def clear_info():
    max_len = 0
    with open('../data/mhy-info.txt','r') as f:
        for line in f.readlines():
            line = line.replace('\n','')
            if len(line)>=256:
                print(line)
            # print(len(line))
            max_len = max(max_len,len(line))
    print(max_len)
if __name__ == '__main__':
    # clear_notice()
    clear_info()