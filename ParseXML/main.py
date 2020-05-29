import lxml.etree as et
from random import randrange


def search(to_search):
    files = ['10-19-30s_705posts.xml', '10-19-20s_706posts.xml']
    index = randrange(2)
    path = files[index]
    return parse_selected_file(path, to_search), path


def parse_selected_file(file_path, to_search):
    tree = et.parse(file_path)
    root = tree.getroot()
    posts = list(root[0])
    count = 0
    for post in posts:
        if to_search in post.text.lower():
            count += 1
    return count


def main():
    print('Enter the string to search...')
    to_search = input()
    count, file = search(to_search)
    print(f'Number of matches in {file}: {count}')


if __name__ == '__main__':
    main()