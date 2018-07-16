import os
import csv


def main():
    print_header()
    filename = get_data_file()
    print('Load from: {}'.format(filename))
    load_file(filename)


def print_header():
    print('--------------------------')
    print('       REAL ESTATE')
    print('--------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        # header = fin.readline().strip()
        # reader = csv.reader(fin)

        reader = csv.DictReader(fin)
        for row in reader:
            print(row)


if __name__ == '__main__':
    main()
