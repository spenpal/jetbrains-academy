# IMPORTS #
from bs4 import BeautifulSoup
import string
import re
import requests
import os


# # STAGE 2 CODE
# url = input('Input the URL:\n')
# print()
# if 'imdb' not in url:
#     print('Invalid movie page!')
#     sys.exit()
#
# response = requests.get(url)
# if not response.status_code == 200:
#     print('Invalid movie page!')
#     sys.exit()
#
# soup = BeautifulSoup(response.content, 'html.parser')
#
# movie_desc = soup.find('span', {'data-testid': 'plot-l'})
# movie_title = soup.find('h1')
# if not (movie_desc and movie_title):
#     print('Invalid movie page!')
#     sys.exit()
#
# print(dict(title=movie_title.text, description=movie_desc.text))


# # STAGE 3 CODE
# url = input('Input the URL:\n')
# print()
#
# response = requests.get(url)
# if not response.status_code == 200:
#     print(f'The URL returned {response.status_code}!')
#     sys.exit()
#
# with open('source.html', 'wb') as f:
#     f.write(response.content)
#     print('Content saved.')


# # STAGE 4 CODE
# url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
#
# articles = soup.find_all('article')
#
# for article in articles:
#     article_type = article.find('div', {'class': "c-card__section c-meta"}).span.span.text
#     if article_type != 'News': continue
#
#     path = article.find('a').get('href')
#     article_response = requests.get(f'https://www.nature.com{path}')
#     article_soup = BeautifulSoup(article_response.content, 'html.parser')
#
#     title = article_soup.find('h1').text
#     body = article_soup.find('div', {'class': re.compile('body')})
#     body = [p.text.strip() for p in body.find_all(['p', 'h2'])]
#     body = list(dict.fromkeys(body))  # remove duplicate sentences
#
#     filename = re.sub(fr'[{string.punctuation}]', '', title)
#     filename = '_'.join(word.strip() for word in filename.split())
#     filename += '.txt'
#     with open(filename, 'wb') as f:
#         text = '\n\n'.join(body)
#         f.write(text.encode())

# STAGE 5 CODE

def save_article(page_num, title, body):
    filename = re.sub(fr'[{string.punctuation}]', '', title)
    filename = '_'.join(word.strip() for word in filename.split())
    filename += '.txt'

    file_path = os.path.join(f'Page_{page_num}', filename)
    with open(file_path, 'wb') as f:
        text = '\n\n'.join(body)
        f.write(text.encode())


def scraper(page_num, url, requested_article_type):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('article')

    for article in articles:
        article_type = article.find('div', {'class': "c-card__section c-meta"}).span.span.text
        if article_type != requested_article_type: continue

        path = article.find('a').get('href')
        article_response = requests.get(f'https://www.nature.com{path}')
        article_soup = BeautifulSoup(article_response.content, 'html.parser')

        title = article_soup.find('h1').text
        body = article_soup.find('div', {'class': re.compile('body')})
        body = [p.text.strip() for p in body.find_all(['p', 'h2'])]
        body = list(dict.fromkeys(body))  # remove duplicate sentences

        save_article(page_num, title, body)


num_of_pages, requested_article_type = int(input()), input()
url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020'

for page_num in range(1, num_of_pages + 1):
    page_url = f'{url}&page={page_num}'
    dir_path = os.path.join(os.getcwd(), f'Page_{page_num}')
    os.mkdir(dir_path)
    scraper(page_num, page_url, requested_article_type)
