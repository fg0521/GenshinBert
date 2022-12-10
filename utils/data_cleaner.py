import re
import numpy as np
import pandas as pd




def clear(x):
    x = re.sub('\n|\t|\r| |​| |﻿','',str(x))
    myre = re.compile(u'[\U0001F300-\U0001F64F-\U0001F680-\U0001F6FF-\u2600-\u26FF\u2700-\u27BF]+',re.UNICODE)
    x = myre.sub('',x)
    x = re.sub('_\((.*?)\)','',x)
    x = re.sub('\((.*?)\)|（(.*?)）','',x)
    x = re.sub('UID:\d+|UID：\d+|uid:\d+|uid：\d+|uid\d+|UID\d+','',x)
    x = re.sub('—{4,}','；',x)
    # x = re.sub('\((.*?)\)','',x)
    # x = re.sub('[。]+','。',x)
    # x = re.sub('^a-zA-Z\d\u4e00-\u9fa5+=-）（\)\(\*&\^%\$#@!！?？、」「\{}\[]【】：:_<>《》/"\'“”\.。，,','',x)
    # x = x.replace('①','1.').replace('②','2.').replace('③','3.').replace('④','4.').replace('⑤','5.')\
    # .replace('⑥', '6.').replace('⑦','7.').replace('⑧','8.').replace('⑨','9.').replace('⑩','10.')
    return x

def split_sentence(x):
    split_list = ['。','!','！','?','？']
    index_list = [-1]
    res = []
    for i in range(len(x)):
        if x[i] in split_list and i>0:
            index_list.append(i)
    # index_list.append(len(x))
    for j in range(len(index_list)-1):
        res.append(x[index_list[j]+1:index_list[j+1]+1])
    return res





if __name__ == '__main__':


    # subject,content,post_id,uid,s_content,auther,my_last_id,last_id,topic1,topic2,topic3
    df = pd.read_csv('../dataset/最新发帖.csv',lineterminator="\n")
    # df = df[['subject','content','s_content']]
    # df['subject'] = df['subject'].apply(lambda x:clear(x))
    # df['content'] = df['content'].apply(lambda x:clear(x))
    df = df[['s_content']]
    df['s_content'] = df['s_content'].apply(lambda x:clear(''.join(eval(x))))
    df['s_content'] = df['s_content'].apply(lambda x:split_sentence(x))
    s = df['s_content'].tolist()
    # for i in s:
    #     for j in i:
    #         print(j)
    with open('../dataset/sentences.txt', 'a+') as f:
        for i in s:
            [f.write(j+'\n') for j in i if len(j)>8]


    # df.to_csv('../dataset/content.csv',encoding='utf-8',index=False)
    # with open('../dataset/train_data.txt', 'a+') as f:
    #     for _,row in df.iterrows():
            # subject = row['subject']
            # content = row['content']
            # s = ''
            # if re.findall('[\u4e00-\u9fa5]+]',subject):
            #     s = s+subject+'。' if not subject.endswith('。') else s+subject
            # if re.findall('[\u4e00-\u9fa5]+]',content):
            #     s = s+content+'。' if not content.endswith('。') else s+content
            # if s:
            #     print(s)
            #     f.write(s+'\n')
            # s_content = row['s_content']
            # symbol1 = ['。','!','！','?','？']
            # symbol2 = ['①','②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩',
            #            '⑴','⑵','⑶','⑷','⑸','⑹','⑺','⑻','⑼','⑽','1.','2.',
            #            '3.','4.','5.','6.','7.','8.','9.','10.','一、','二、'
            #            ,'三、','四、','五、','六、','七、','八、','九、','十、',
            #            '1、', '2、',
            #            '3、', '4、', '5、', '6、', '7、', '8、', '9、', '10、',
            #            '一.', '二.'
            #     , '三.', '四.', '五.', '六.', '七.', '八.', '九.', '十.',
            #            ]
            # for i in symbol1:
            #     s_content = s_content.replace(i,i+'\n')
            # for i in symbol2:
            #     s_content = s_content.replace(i,'\n'+i)
            #
            # content_len = 0
            # ss = ''
            # for i in s_content.split('\n'):
            #     if i:
            #         content_len+=len(i)
            #         ss = ss+i
            #         if content_len<25:
            #             continue
            #         elif content_len>128:
            #             with open('../dataset/long_text.txt','a+') as f1:
            #                 f1.write(ss+'\n')
            #             content_len = 0
            #             ss = ''
            #         else:
            #             f.write(ss+'\n')
            #             content_len = 0
            #             ss = ''
