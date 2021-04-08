import requests
from bs4 import BeautifulSoup
from string import ascii_letters


class AnimalParser:
    def __init__(self):
        self.names = {}
        self.url = "https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту"

    def get_soups(self):
        url = self.url
        with requests.Session() as session:
            while url:
                page = session.get(url).text
                soup = BeautifulSoup(page, 'lxml')
                next_page = soup.find('div', id='mw-pages').find('a', text='Следующая страница')
                url = 'https://ru.wikipedia.org/' + next_page.get('href') if next_page else None
                yield soup

    def find_names(self):
        self.names.clear()
        print('Searching...')

        soups = self.get_soups()
        for soup in soups:
            categories = soup.find('div', class_='mw-category')
            category_groups = categories.findAll('div', class_='mw-category-group')
            for category_group in category_groups:
                char = category_group.find('h3').text
                if char in ascii_letters:
                    print('Done!')
                    return
                names = [name.text for name in category_group.find_all('a')]
                self.names[char] = self.names[char] + names if char in self.names else names

    def print_result(self):
        for key in sorted(self.names):
            count = len(self.names[key])
            print(f'{key}: {count}')
