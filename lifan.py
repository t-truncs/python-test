from bs4 import BeautifulSoup

import urllib3
import encodings


url0 = 'm.lifanacg.com'
url = 'm.lifanacg.com/shaonv'
header = {'Referer': 'http://m.lifanacg.com',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    comment_list = soup.select('.comment > p')
    next_page = soup.select('#paginator > a')[2].get('href')
    date_nodes = soup.select('..comment-time')
    return comment_list, next_page, date_nodes


if __name__ == '__main__':
    cookies = {}
    # f_cookies = open('cookie.txt', 'r')
    # for line in f_cookies.read().split(';'):
    #     name, value = line.strip().split('=', 1)
    #     cookies[name] = value

    # html = requests.get(url, cookies=cookies, headers=header).content

    http=urllib3.PoolManager()
    r=http.request('get',url, headers=header)

    print (str(r.data.decode('gbk')))

    # comment_list = []
    # # 获取评论
    # comment_list, next_page, date_nodes = get_data(html,)
    # soup = BeautifulSoup(html, 'lxml')
    # comment_list = []
    # while (next_page != []):  # 查看“下一页”的A标签链接
    #     print(absolute + next_page)
    #     html = requests.get(absolute + next_page,
    #                         cookies=cookies, headers=header).content
    #     soup = BeautifulSoup(html, 'lxml')
    #     comment_list, next_page, date_nodes = get_data(html)
    #     with open("comments.txt", 'a', encoding='utf-8')as f:
    #         for node in comment_list:
    #             comment = node.get_text().strip().replace("\n", "")
    #             for date in date_nodes:
    #                 date = node.get_text().strip()
    #                 f.writelines((comment, date) + u'\n')
    #     time.sleep(1 + float(random.randint(1, 100)) / 20)
