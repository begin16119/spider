import json
import re
from multiprocessing.pool import Pool

import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


def get_one_page(url):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.text
    except RequestException:
        return None


def parser_one_page(html):
    # soup = BeautifulSoup(html,'html.parser')
    # items = soup.find_all("dd")

    # todo 正则匹配 学习
    pattern = re.compile(
        r'<dd>.*?board-index.*?">(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',
        re.S)

    items = re.findall(pattern, html)
    # 这一步生成的其实是由元组组成的列表，列表的每一个元素是元组，元组则有前面正则表达式提取的电影名称，地址，演员名，上映时间，排序，评分等，这个列表怎么用，是一个很重要的问题
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }
    # todo 生成器学习

def main(offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    for item in parser_one_page(html):
        print(item)
        write_to_file(item)


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


if __name__ == '__main__':
    # for i in range(10):
    #     main(i*10)
    pool = Pool()
    pool.map(main, [i * 10 for i in range(10)])
