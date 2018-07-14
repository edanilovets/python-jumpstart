#
# File Searcher app without generator methods (yield keyword)
#
import os
import collections

SearchResult = collections.namedtuple('SearchResult', 'file, line, text')


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print('Invalid folder...')
    text = get_search_text_from_user()
    if not text:
        print('Invalid text...')

    matches = search_files_in_folder(folder, text)
    matches_count = 0
    for m in matches:
        matches_count += 1
        # print('------MATCH------')
        # print('file: ' + m.file)
        # print('line #{}: {}'.format(m.line, m.text))
    print('Found {} matches'.format(matches_count))

def print_header():
    print('--------------------------')
    print('       FILE SEARCHER')
    print('--------------------------')
    print()


def get_folder_from_user():
    folder = input('What folder do you want to search?')
    if not folder or not folder.strip() or not os.path.isdir(folder):
        return None
    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What are you searching for? [single phrases only]: ')
    return text.lower()


def search_files_in_folder(folder, text):
    print('Would search {} for "{}"'.format(folder, text))
    all_matches = []
    items = os.listdir(folder)
    for item in items:
        full_item = os.path.join(folder, item)
        if not os.path.isdir(full_item):
            matches = search_text_in_file(full_item, text)
            all_matches.extend(matches)
        else:
            # recursion to look for files in sub folders
            matches = search_files_in_folder(full_item, text)
            all_matches.extend(matches)

    return all_matches


def search_text_in_file(filename, text):
    matches = []
    with open(filename, 'r', encoding='utf-8') as fin:
        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(text) >= 0:
                m = SearchResult(line=line_num, file=filename, text=line)
                matches.append(m)
    return matches


if __name__ == '__main__':
    main()
