# -*- coding:utf-8 -*-

import json


def get_person_name():
    name_set = set()

    movie_person_file_path = '../../../data/bigdata/movie_person_info.txt'
    movie_person_str_list = open(movie_person_file_path, 'r').readlines()
    movie_person_json_list = [json.loads(movie_person) for movie_person in movie_person_str_list]

    for movie_person in movie_person_json_list:
        movie_person_name = movie_person['name']
        name_set.add(movie_person_name)

    book_person_file_path = '../../../data/bigdata/book_person_info.txt'
    book_person_str_list = open(book_person_file_path, 'r').readlines()
    book_person_json_list = [json.loads(book_person) for book_person in book_person_str_list]
    for book_person in book_person_json_list:
        book_person_name = book_person['name']
        name_set.add(book_person_name)

    name_list = list(name_set)
    person_name_file_path = 'person_name.txt'
    with open(person_name_file_path, 'w') as f:
        for name in name_list:
            f.write(name + ' nr\n')


def get_book_and_movie_name():
    name_set = set()

    movie_info_file_path = '../../../data/bigdata/movie_info.txt'
    movie_info_str_list = open(movie_info_file_path, 'r').readlines()
    movie_info_json_list = [json.loads(movie) for movie in movie_info_str_list]

    for movie in movie_info_json_list:
        movie_person_name = movie['name']
        name_set.add(movie_person_name)

    book_info_file_path = '../../../data/bigdata/book_info.txt'
    book_str_list = open(book_info_file_path, 'r').readlines()
    book_json_list = [json.loads(book) for book in book_str_list]
    for book in book_json_list:
        book_name = book['name']
        name_set.add(book_name)

    name_list = list(name_set)
    book_and_movie_name_file_path = 'book_and_movie_name.txt'
    with open(book_and_movie_name_file_path, 'w') as f:
        for name in name_list:
            f.write(name + ' nz\n')


if __name__ == '__main__':
    get_person_name()
    get_book_and_movie_name()
