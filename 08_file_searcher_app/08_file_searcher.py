def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print('Invalid folder...')
    text = get_search_text_from_user()
    if not text:
        print('Invalid text...')

    search_folders(folder, text)


def print_header():
    print('--------------------------')
    print('       FILE SEARCHER')
    print('--------------------------')
    print()


def get_folder_from_user():
    pass


def get_search_text_from_user():
    pass


def search_folders(folder, text):
    pass


if __name__ == '__main__':
    main()
