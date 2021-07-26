# Parce ывааааda as
import requests


# Подпрограмма получает урл и возвращает страницу
def get_html(url):
    html = requests.get(url)
    return html.text


def main():
    print(get_html('http://google.ru'))


if __name__ == '__main__':
    main()
