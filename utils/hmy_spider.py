import re
import time

from bs4 import BeautifulSoup
import requests


class HMYSpider():
    def __init__(self):
        self.url = 'https://www.jjwxc.net/onebook.php?novelid=6518121&chapterid='
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }

    def parse(self):
        for i in range(27,188):
            if i in [97,102,132]:
                continue
            url = self.url+str(i)
            res = requests.get(url=url,headers=self.headers)
            if res.status_code==200:
                s = res.content
                s.decode('ISO-8859-1')
                bs = BeautifulSoup(s, "html.parser")
                text = bs.prettify()
                text = text.replace('\n','')
                title = re.findall('<h2>(.*?)</h2>',text)
                title = title[0].strip().replace('/','-') if title else 'unknown'
                print(title)
                content = re.findall('<div style="clear:both;">      </div>(.*?)<div',text)
                content = content[0].split('<br/>') if content else ''
                with open(f'../dataset/{title}.txt','a+') as f:
                    [f.write(s.strip()+'\n') for s in content]
                time.sleep(2)



if __name__ == '__main__':
    spider = HMYSpider()
    spider.parse()