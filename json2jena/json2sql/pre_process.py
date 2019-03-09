# -*- coding:utf-8 -*-

import json


def movie_info():
    """
    检查movie_info中是否有空的id和name, 规范化Json值
    :return:
    """
    movie_file_path = '../../data/bigdata/movie_info.txt'
    movie_str_list = open(movie_file_path, 'r').readlines()
    movie_json_list = [json.loads(movie) for movie in movie_str_list]

    new_movie_json_list = []
    for movie in movie_json_list:
        movie_actor = movie['actors']
        for actor in movie_actor:
            actor['href'] = actor['href'].replace('celebrity', '').replace('/', '')
            actor['id'] = actor['href']
            actor.pop('href')
        movie_director = movie['directors']
        for director in movie_director:
            director['href'] = director['href'].replace('celebrity', '').replace('/', '')
            director['id'] = director['href']
            director.pop('href')
        movie_writer = movie['writers']
        for writer in movie_writer:
            writer['href'] = writer['href'].replace('celebrity', '').replace('/', '')
            writer['id'] = writer['href']
            writer.pop('href')

        if len(movie['id']) == 0 or len(movie['name']) == 0:
            continue
        else:
            new_movie_json_list.append(movie)

    new_movie_file_path = '../../data/bigdata/movie_info.txt'
    with open(new_movie_file_path, 'w') as f:
        for movie in new_movie_json_list:
            f.write(json.dumps(movie, ensure_ascii=False) + '\n')


def movie_person():
    """
    检查movie_person中是否有空的id和name
    :return:
    """
    movie_person_file_path = '../../data/bigdata/movie_person_info.txt'
    movie_person_str_list = open(movie_person_file_path, 'r').readlines()
    movie_person_json_list = [json.loads(movie_person) for movie_person in movie_person_str_list]

    movie_id_set = set()
    new_movie_person_json_list = []
    for movie_person in movie_person_json_list:
        movie_person['id'] = movie_person['id'].replace('celebrity', '').replace('/', '')
        if movie_person['id'] in movie_id_set:
            # print(movie_person['id'])
            continue
        movie_id_set.add(movie_person['id'])
        if len(movie_person['id']) == 0 or len(movie_person['id']) == 0:
            continue
        else:
            new_movie_person_json_list.append(movie_person)

    new_movie_person_file_path = '../../data/bigdata/movie_person_info.txt'
    with open(new_movie_person_file_path, 'w') as f:
        for movie_person in new_movie_person_json_list:
            f.write(json.dumps(movie_person, ensure_ascii=False) + '\n')

    print(len(movie_person_json_list))
    print(len(new_movie_person_json_list))


def book_info():
    """
    检查是否有空的id,name,重复id。
    :return:
    """
    book_file_path = '../../data/bigdata/book_info.txt'
    book_str_list = open(book_file_path, 'r').readlines()
    book_json_list = [json.loads(book) for book in book_str_list]

    new_book_json_list = []
    book_id_set = set()
    for book in book_json_list:
        book_info_id = book['id']
        book_info_name = book['name']
        if len(book_info_id) == 0 or len(book_info_name) == 0:
            continue
        if book_info_id in book_id_set:
            continue
        book_id_set.add(book_info_id)

        book_author = book['author']
        for author in book_author:
            author['href'] = author['href'].replace('author', '').replace('/', '')
            author['id'] = author['href']
            author.pop('href')
        book_translator = book['translator']
        for translator in book_translator:
            translator['href'] = translator['href'].replace('author', '').replace('/', '')
            translator['id'] = translator['href']
            translator.pop('href')
        new_book_json_list.append(book)

    new_book_info_file_path = '../../data/bigdata/book_info.txt'
    with open(new_book_info_file_path, 'w') as f:
        for book in new_book_json_list:
            f.write(json.dumps(book, ensure_ascii=False) + '\n')


def book_person():
    """
    检查是否有空id,name,重复id
    :return:
    """
    book_person_file_path = '../../data/bigdata/book_person_info.txt'
    book_person_str_list = open(book_person_file_path, 'r').readlines()
    book_person_json_list = [json.loads(book_person) for book_person in book_person_str_list]

    new_book_person_list = []
    book_person_id_set = set()
    for book_person in book_person_json_list:
        book_person_id = book_person['id']
        book_person_name = book_person['name']
        if len(book_person_id) == 0 or len(book_person_name) == 0:
            continue
        if book_person_id in book_person_id_set:
            continue
        book_person_id_set.add(book_person_id)

        book_person['id'] = book_person['id'].replace('author', '').replace('/', '')
        new_book_person_list.append(book_person)

    new_book_person_file_path = '../../data/bigdata/book_person_info.txt'
    with open(new_book_person_file_path, 'w') as f:
        for book_person in new_book_person_list:
            f.write(json.dumps(book_person, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    # movie_info()
    # movie_person()
    # book_info()
    book_person()
