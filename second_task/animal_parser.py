import requests
from bs4 import BeautifulSoup
import re


class AnimalParser:
    def __init__(self):
        self.names = {}
        self.url = "https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту"

    def find_names(self):
        self.names.clear()
        page = requests.get(self.url).text
        print('Searching...')
        self.recursive_search(page)

    def recursive_search(self, page):
        soup = BeautifulSoup(page, 'lxml')
        category_groups = soup.find('div', class_='mw-category').findAll('div', class_='mw-category-group')
        for category_group in category_groups:
            char = category_group.find('h3').text
            is_cyrillic = bool(re.match('[А-Я]', char))
            if not is_cyrillic:
                return
            names = [name.text for name in category_group.find_all('a')]
            self.names[char] = self.names[char] + names if self.names.get(char) else names

        links = soup.find('div', id='mw-pages').find_all('a')
        for a in links:
            if a.text == 'Следующая страница':
                url = 'https://ru.wikipedia.org/' + a.get('href')
                page = requests.get(url).text
        self.recursive_search(page)

    def print_result(self):
        for key in sorted(self.names):
            count = len(self.names[key])
            print(f'{key}: {count}')
