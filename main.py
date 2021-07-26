# Парсим согластно fl заказу: https://www.fl.ru/projects/4801912/parsing-kataloga.html
# Выбранна странчка для парсинга https://www.game29.ru/products?page=1&category=926
# План
# 1. Получить html страничку
# 2. Получить кол-во страниц
# 3. Генерировать адреса страничек
# 4. Получить данные с странички 1(название, цена)


import requests
from bs4 import BeautifulSoup


# Кол-во страниц
def get_total_page(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('ul', class_='pagination-new').find_all('a')[-2].get('href')
    total_pages = pages.split('=')[-1]
    # print(total_pages)
    return total_pages


# Подпрограмма получает урл и возвращает страницу
def get_html(url):
    r = requests.get(url)
    print(r.text)
    # return r.text


def main():
    # get_total_page(get_html('https://www.game29.ru/products?page=1&category=926'))
    # print(get_html('http://sportoriginal.by/items/filter/b_14/page_1'))
    url = 'https://www.game29.ru/products?page=1&category=926'
    base_url = 'https://www.game29.ru/products?'
    page_part = 'page='
    query_part = '&category=926'

    total_page = get_total_page(get_html(url))
    print(total_page)

    if __name__ == '__main__':
        main()
