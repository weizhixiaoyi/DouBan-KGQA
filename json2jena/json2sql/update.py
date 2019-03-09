# -*- coding:utf-8 -*-

import json
import re
import pymysql


def update_book_info():
    book_info_file_path = '../../data/bigdata/book_info.txt'
    book_str_list = open(book_info_file_path, 'r').readlines()
    book_json_list = [json.loads(book) for book in book_str_list]

    for book in book_json_list:
        book['rating']['reviews_count'] = book['rating']['reviews_count'].replace('人评价', '')
    new_book_info_file_path = '../../data/bigdata/book_info.txt'
    with open(new_book_info_file_path, 'w') as f:
        for book in book_json_list:
            f.write(json.dumps(book, ensure_ascii=False) + '\n')


def update_movie_person_info():
    # movie_info_file_path = '../../data/bigdata/movie_info.txt'
    # movie_str_list = open(movie_info_file_path, 'r').readlines()
    # movie_json_list = [json.loads(movie) for movie in movie_str_list]
    #
    # name_list = []
    # name_id_set = set()
    # for movie in movie_json_list:
    #     movie_actor = movie['actors']
    #     for actor in movie_actor:
    #         if actor['id'] in name_id_set:
    #             continue
    #         name_id_set.add(actor['id'])
    #         name_list.append(actor)
    #
    #     movie_writer = movie['writers']
    #     for writer in movie_writer:
    #         if writer['id'] in name_id_set:
    #             continue
    #         name_id_set.add(writer['id'])
    #         name_list.append(writer)
    #
    #     movie_director = movie['directors']
    #     for director in movie_director:
    #         if director['id'] in name_id_set:
    #             continue
    #         name_id_set.add(director['id'])
    #         name_list.append(director)
    #
    # movie_person_name_file_path = '../../data/bigdata/movie_person_name.txt'
    # with open(movie_person_name_file_path, 'w') as f:
    #     for name in name_list:
    #         f.write(json.dumps(name, ensure_ascii=False) + '\n')

    # movie_person_file_path = '../../data/bigdata/movie_person_info.txt'
    # movie_person_str_list = open(movie_person_file_path, 'r').readlines()
    # movie_person_json_list = [json.loads(movie_person) for movie_person in movie_person_str_list]
    #
    # movie_person_name_file_path = '../../data/bigdata/movie_person_name.txt'
    # movie_person_name_str_list = open(movie_person_name_file_path, 'r').readlines()
    # movie_person_name_json_list = [json.loads(movie_person_name) for movie_person_name in movie_person_name_str_list]
    # movie_json_dict = {}
    # for name in movie_person_name_json_list:
    #     movie_json_dict[name['id']] = name['name']
    #
    # # update movie_person_info name
    # for person in movie_person_json_list:
    #     person_id = person['id']
    #     person_name = person['name']
    #     new_person_name = movie_json_dict[person_id]
    #
    #     person['name'] = new_person_name
    #
    # new_movie_person_file_path = '../../data/bigdata/movie_person_info.txt'
    # with open(new_movie_person_file_path, 'w') as f:
    #     for movie_person in movie_person_json_list:
    #         f.write(json.dumps(movie_person, ensure_ascii=False) + '\n')
    pass


def update_book_person_info():
    # 先提取正常姓名， 并写入到文件之中
    # book_person_file_path = '../../data/bigdata/book_person_info.txt'
    # book_person_str_list = open(book_person_file_path, 'r').readlines()
    # book_person_json_list = [json.loads(book_person) for book_person in book_person_str_list]
    #
    # name_list = []
    # new_name_list = []
    # for book_person in book_person_json_list:
    #     book_id = book_person['id']
    #     book_name = book_person['name']
    #     if book_name.replace('·', '').replace(' ', '').encode('utf-8').isalpha():
    #         name_list.append({book_id: book_name})
    #         continue
    #     else:
    #         name_list.append({book_id: book_name.split(' ')[0]})
    #
    # new_book_person_name_file_path = '../../data/bigdata/new_book_person_name.txt'
    # with open(new_book_person_name_file_path, 'w') as f:
    #     for name in name_list:
    #         f.write(json.dumps(name, ensure_ascii=False) + '\n')

    # 更新到book_person_info之中
    # book_person_file_path = '../../data/bigdata/book_person_info.txt'
    # book_person_str_list = open(book_person_file_path, 'r').readlines()
    # book_person_json_list = [json.loads(book_person) for book_person in book_person_str_list]
    #
    # # 读取new_book_person_name
    # new_book_person_name_file_path = '../../data/bigdata/new_book_person_name.txt'
    # new_book_person_name_str_list = open(new_book_person_name_file_path, 'r').readlines()
    # new_book_person_name_json_list = [json.loads(name) for name in new_book_person_name_str_list]
    #
    # new_person_name = {}
    # for name in new_book_person_name_json_list:
    #     new_person_name[list(name.keys())[0]] = name[list(name.keys())[0]]
    #
    # for book_person in book_person_json_list:
    #     book_preson_id = book_person['id']
    #     book_person['name'] = new_person_name[book_preson_id]
    #
    # new_book_person_info_file_path = 'book_person_info.txt'
    # with open(new_book_person_info_file_path, 'w') as f:
    #     for book_person in book_person_json_list:
    #         f.write(json.dumps(book_person, ensure_ascii=False) + '\n')
    pass


def update_movie_info():
    # movie_info_file_path = '../../data/bigdata/movie_info.txt'
    # movie_str_list = open(movie_info_file_path, 'r').readlines()
    # movie_json_list = [json.loads(movie) for movie in movie_str_list]
    #
    # new_movie_name = []
    # for movie in movie_json_list:
    #     movie_id = movie['id']
    #     movie_name = movie['name']
    #     # movie_name = '\"Saturday Night Live\" Peyton Manning/Carrie Underwood'
    #
    #     temp_movie_name = movie_name.replace(' ', '').replace(':', '').replace('-', '').replace('&', '').replace('\'',
    #                                                                                                              '')
    #     temp_movie_name = temp_movie_name.replace('(', '').replace(')', '').replace('\\', '').replace('\"', '').replace(
    #         '.', '')
    #     temp_movie_name = temp_movie_name.replace('+', '').replace(',', '').replace('/', '').replace('?', '')
    #     for i in range(0, 10):
    #         temp_movie_name = temp_movie_name.replace(str(i), '')
    #     # print(temp_movie_name)
    #     if temp_movie_name.encode('utf-8').isalpha():
    #         # new_movie_name.append({movie_id: movie_name, movie_id + '#': movie_name})
    #         new_movie_name.append({movie_id: movie_name})
    #         continue
    #     else:
    #         # new_movie_name.append({movie_id: movie_name, movie_id + '#': movie_name.split(' ')[0]})
    #         # 处理第*季节问题
    #         season_flag = re.findall(r'第.*季', movie_name)
    #         if season_flag:
    #             new_movie_name.append({movie_id: movie_name.split('季')[0].replace(' ', '') + '季'})
    #             continue
    #         part_flag = re.findall(r'第.*部', movie_name)
    #         if part_flag:
    #             new_movie_name.append({movie_id: movie_name.split('部')[0].replace(' ', '') + '部'})
    #             continue
    #
    #         new_movie_name.append({movie_id: movie_name.split(' ')[0].replace(' ', '')})
    # new_movie_name_file_path = '../../data/bigdata/new_movie_name.txt'
    # with open(new_movie_name_file_path, 'w') as f:
    #     for movie_name in new_movie_name:
    #         f.write(json.dumps(movie_name, ensure_ascii=False) + '\n')

    # # 更新movie_info
    # movie_info_file_path = '../../data/bigdata/movie_info.txt'
    # movie_str_list = open(movie_info_file_path, 'r').readlines()
    # movie_json_list = [json.loads(movie) for movie in movie_str_list]
    #
    # # 读取new_movie_name
    # new_movie_name_file_path = '../../data/bigdata/new_movie_name.txt'
    # new_movie_name_str_list = open(new_movie_name_file_path, 'r').readlines()
    # new_movie_name_json_list = [json.loads(name) for name in new_movie_name_str_list]
    #
    # new_movie_name = {}
    # for name in new_movie_name_json_list:
    #     new_movie_name[list(name.keys())[0]] = name[list(name.keys())[0]]
    #
    # for movie in movie_json_list:
    #     movie_id = movie['id']
    #     movie['name'] = new_movie_name[movie_id]
    #
    # new_movie_info_file_path = '../../data/bigdata/movie_info.txt'
    # with open(new_movie_info_file_path, 'w') as f:
    #     for movie in movie_json_list:
    #         f.write(json.dumps(movie, ensure_ascii=False) + '\n')
    pass


def update_sql_movie_info():
    """
    更新电影信息
    :return:
    """
    # 读取文件
    movie_file_path = '../../data/bigdata/movie_info.txt'
    movie_str_list = open(movie_file_path, 'r').readlines()
    movie_json_list = [json.loads(movie) for movie in movie_str_list]

    # 连接mysql数据库
    kgqa_connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root123456',
        db='douban_kgqa',
        cursorclass=pymysql.cursors.DictCursor
    )

    # 存储信息到mysql数据库之中
    try:
        with kgqa_connection.cursor() as cursor:
            for movie in movie_json_list:
                movie_info_id = movie['id']
                movie_info_name = movie['name'].replace('\"', '')
                movie_info_other_name = '/'.join(movie['other_names']).replace('\"', '')

                movie_info_update_sql = "UPDATE `movie_info` SET `movie_info_other_name` =" + '\"' + str(
                    movie_info_other_name) + '\"' + "WHERE `movie_info_id`=" + str(movie_info_id)
                # print(movie_info_update_sql)
                cursor.execute(movie_info_update_sql)
            kgqa_connection.commit()
    except Exception as err:
        print('movie_info插入数据错误' + str(err))


def update_sql_movie_person_info():
    # 读取文件
    movie_person_file_path = '../../data/bigdata/movie_person_info.txt'
    movie_person_str_list = open(movie_person_file_path, 'r').readlines()
    movie_person_json_list = [json.loads(movie) for movie in movie_person_str_list]

    # 连接mysql数据库
    kgqa_connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root123456',
        db='douban_kgqa',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with kgqa_connection.cursor() as cursor:
            for movie_person in movie_person_json_list:
                movie_person_id = movie_person['id']
                movie_person_name = movie_person['name'].replace('\"', '')

                movie_person_update_sql = "UPDATE `movie_person` SET `movie_person_name` =" + '\"' + str(
                    movie_person_name) + '\"' "WHERE `movie_person_id`=" + str(movie_person_id)
                # print(movie_person_update_sql)
                cursor.execute(movie_person_update_sql)
            kgqa_connection.commit()
    except Exception as err:
        print('movie_person数据插入错误' + str(err))


def update_sql_book_info():
    # 读取文件
    book_file_path = '../../data/bigdata/book_info.txt'
    book_str_list = open(book_file_path, 'r').readlines()
    book_json_list = [json.loads(book) for book in book_str_list]

    # 连接mysql数据库
    kgqa_connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root123456',
        db='douban_kgqa',
        cursorclass=pymysql.cursors.DictCursor
    )

    # 存储信息到mysql数据库之中
    try:
        with kgqa_connection.cursor() as cursor:
            for book in book_json_list:
                book_info_id = book['id']
                book_info_review_count = book['rating']['reviews_count'].replace('人评价', '')
                update_book_info_sql = "UPDATE `book_info` SET `book_info_review_count` = " + '\'' + str(
                    book_info_review_count) + '\'' + "WHERE `book_info_id`=" + str(book_info_id)
                cursor.execute(update_book_info_sql)
            kgqa_connection.commit()
    except Exception as err:
        print('book_info数据插入错误' + str(err))


def update_sql_book_person_info():
    # 读取文件
    book_person_file_path = '../../data/bigdata/book_person_info.txt'
    book_person_str_list = open(book_person_file_path, 'r').readlines()
    book_person_json_list = [json.loads(book_person) for book_person in book_person_str_list]

    # 连接mysql数据库
    kgqa_connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root123456',
        db='douban_kgqa',
        cursorclass=pymysql.cursors.DictCursor
    )

    # 存储信息到mysql数据库之中
    try:
        with kgqa_connection.cursor() as cursor:
            for book_person in book_person_json_list:
                book_person_id = book_person['id']
                book_person_name = book_person['name']

                update_book_person_info_sql = "UPDATE `book_person` SET `book_person_name`=" + '\'' + str(
                    book_person_name) + '\'' + 'WHERE `book_person_id`=' + str(book_person_id)

                cursor.execute(update_book_person_info_sql)
            kgqa_connection.commit()
    except Exception as err:
        print('book_info数据插入错误' + str(err))


if __name__ == '__main__':
    # update_book_info()
    # update_movie_person_info()
    # update_book_person_info()
    # update_movie_info()

    # update_sql_movie_info()
    # update_sql_movie_person_info()
    # update_sql_book_info()
    update_sql_book_person_info()
