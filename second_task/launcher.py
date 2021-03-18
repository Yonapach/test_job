#!./venv/bin/python3

from animal_parser import AnimalParser

if __name__ == '__main__':
    parser = AnimalParser()
    parser.find_names()
    parser.print_result()
