import requests
import urllib.parse
from bs4 import BeautifulSoup


INDEX = 'https://www.ptt.cc/bbs/movie/index.html'
NOT_EXIST = BeautifulSoup('<a>本文已被刪除</a>', 'lxml').a


#f = open('post_list.txt', 'w', encoding = 'utf-8')


def append_post(meta):
    if "好雷" in meta.getText().strip():
        #print(meta)
        posts.append({
            'title': meta.getText().strip(),
            'link': meta.get('href') or 'nolink',
            'push': article.find('div', 'nrec').getText(),
            'date': article.find('div', 'date').getText(),
            'author': article.find('div', 'author').getText(),
        })

def get_posts_on_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    posts = list()
    for article in soup.find_all('div', 'r-ent'):
        meta = article.find('div', 'title').find('a') or NOT_EXIST
        if "好雷" in meta.getText().strip():
            posts.append({
                'title': meta.getText().strip(),
                'link': meta.get('href') or 'nolink',
                'push': article.find('div', 'nrec').getText(),
                'date': article.find('div', 'date').getText(),
                'author': article.find('div', 'author').getText(),
            })
        elif "負雷" in meta.getText().strip():
            posts.append({
                'title': meta.getText().strip(),
                'link': meta.get('href') or 'nolink',
                'push': article.find('div', 'nrec').getText(),
                'date': article.find('div', 'date').getText(),
                'author': article.find('div', 'author').getText(),
            })
        """
        posts.append({
            'title': meta.getText().strip(),
            'link': meta.get('href') or 'nolink',
            'push': article.find('div', 'nrec').getText(),
            'date': article.find('div', 'date').getText(),
            'author': article.find('div', 'author').getText(),
        })
        """

    next_link = soup.find('div', 'btn-group-paging').find_all('a', 'btn')[1].get('href')

    return posts, next_link


def get_pages(num):
    page_url = INDEX
    all_posts = list()
    for i in range(num):
        posts, link = get_posts_on_page(page_url)
        all_posts += posts
        page_url = urllib.parse.urljoin(INDEX, link)
    return all_posts

def write_file(post):
    f.write(post['push'])
    f.write('\t')
    f.write(post['date'])
    f.write('\t')
    f.write(post['title'])
    f.write('\t')
    f.write(post['link'])
    f.write('\n')

if __name__ == '__main__':
    pages = 70
    f = open('post_list.txt', 'w', encoding = 'utf-8')

    for post in get_pages(pages):
        f.write(post['push'])
        f.write('\t')
        f.write(post['date'])
        f.write('\t')
        f.write(post['title'])
        f.write('\t')
        f.write(post['link'])
        f.write('\n')


    f.close()