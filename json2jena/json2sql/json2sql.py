# -*- coding:utf-8 -*-

import json
import pymysql


# change json data to sql

def movie_genre():
    """
    提取电影类别, 并存入到mysql之中
    :return: None
    """
    # 读取文件
    movie_file_path = '../../data/bigdata/movie_info.txt'
    movie_str_list = open(movie_file_path, 'r').readlines()
    movie_json_list = [json.loads(movie) for movie in movie_str_list]

    # 电影类型
    movie_genres = set()
    for movie in movie_json_list:
        for genre in movie['genres']:
            movie_genres.add(genre)
    movie_genres = list(movie_genres)
    movie_genres.sort(key=lambda i: len(i))
    print(movie_genres)

    # 连接mysql数据库
    kgqa_connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root123456',
        db='douban_kgqa',
        cursorclass=pymysql.cursors.DictCursor
    )
    # 存储信息到数据库之中
    try:
        genre_id = 1
        with kgqa_connection.cursor() as cursor:
            # Insert Data
            for genre in movie_genres:
                sql = "INSERT INTO `movie_genre` (`movie_genre_id`, `movie_genre_name`) VALUES (%s, %s)"
                cursor.execute(sql, (genre_id, genre))
                genre_id += 1
            kgqa_connection.commit()
    except Exception as err:
        print('movie_genres数据插入错误' + str(err))


def movie_info():
    """
    提取电影信息,存储到mysql之中
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
                movie_info_image_url = movie['image_url']
                movie_info_name = movie['name']
                movie_info_country = ','.join(movie['countries'])
                movie_info_language = ','.join(movie['languages'])
                movie_info_pubdate = ','.join(movie['pubdates'])
                movie_info_duration = ','.join(movie['durations'])
                movie_info_other_name = ','.join(movie['other_names'])
                movie_info_summary = movie['summary']
                movie_info_rating = movie['rating']['average']
                movie_info_review_count = movie['rating']['reviews_count']

                sql = "INSERT INTO `movie_info` (`movie_info_id`, `movie_info_image_url`, `movie_info_name`, `movie_info_country`," \
                      "`movie_info_language`, `movie_info_pubdate`, `movie_info_duration`, `movie_info_other_name`," \
                      "`movie_info_summary`, `movie_info_rating`, `movie_info_review_count`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                cursor.execute(sql, (
                    movie_info_id, movie_info_image_url, movie_info_name, movie_info_country, movie_info_language,
                    movie_info_pubdate, movie_info_duration, movie_info_other_name,
                    movie_info_summary,
                    movie_info_rating, movie_info_review_count))
            kgqa_connection.commit()
    except Exception as err:
        print('movie_info插入数据错误' + str(err))


def movie_person():
    """
    提取电影演员(演员、编剧、导演)信息到数据库之中
    :return:
    """
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
                movie_person_name = movie_person['name']
                movie_person_image_url = movie_person['image_url']
                movie_person_gender = movie_person['gender']
                movie_person_constellation = movie_person['constellation']
                movie_person_birthday = movie_person['birthday']
                movie_person_birthplace = movie_person['birthplace']
                movie_person_profession = movie_person['profession']
                movie_person_other_name = movie_person['other_english_name'] + movie_person['other_chinese_name']
                movie_person_introduction = movie_person['introduction']

                sql = "INSERT INTO `movie_person` (`movie_person_id`, `movie_person_name`, `movie_person_image_url`," \
                      "`movie_person_gender`, `movie_person_constellation`, `movie_person_birthday`, `movie_person_birthplace`," \
                      "`movie_person_profession`, `movie_person_other_name`, " \
                      "`movie_person_introduction`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (movie_person_id, movie_person_name, movie_person_image_url, movie_person_gender,
                                     movie_person_constellation,
                                     movie_person_birthday, movie_person_birthplace, movie_person_profession,
                                     movie_person_other_name, movie_person_introduction))
            kgqa_connection.commit()
    except Exception as err:
        print('movie_person数据插入错误' + str(err))


def movie_to_genre():
    """
    电影和电影类别之间进行关联
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
    try:
        with kgqa_connection.cursor() as cursor:
            for movie in movie_json_list:
                movie_info_id = movie['id']
                movie_genres = movie['genres']
                for genre in movie_genres:
                    movie_genre_id_sql = "SELECT `movie_genre_id` FROM `movie_genre` where `movie_genre_name`=" + '\'' + str(
                        genre) + '\''
                    cursor.execute(movie_genre_id_sql)
                    movie_genre_info = cursor.fetchone()
                    movie_genre_id = movie_genre_info['movie_genre_id']

                    # 插入到movie_to_genre之中
                    # print(str(movie_info_id) + ':' + str(movie_genre_id))
                    movie_to_genre_sql = 'INSERT INTO `movie_to_genre` (`movie_info_id`, `movie_genre_id`) VALUES (%s, %s)'
                    cursor.execute(movie_to_genre_sql, (movie_info_id, movie_genre_id))
            kgqa_connection.commit()


    except Exception as err:
        print('movie_to_genre数据插入错误' + str(err))


def actor_to_movie():
    """
    电影和演员之间进行关联
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

    try:
        with kgqa_connection.cursor() as cursor:
            for movie in movie_json_list:
                movie_info_id = movie['id']
                movie_actor = movie['actors']
                movie_actor_id = [actor['id'] for actor in movie_actor]
                movie_actor_id = list(set(movie_actor_id))
                if '' in movie_actor_id:
                    movie_actor_id.remove('')
                for actor_id in movie_actor_id:
                    # 判断movie_person中是否存在该ID
                    is_existed_sql = 'select 1 from `movie_person` where `movie_person_id` = ' + '\'' + actor_id + '\'' + 'limit 1'
                    cursor.execute(is_existed_sql)
                    is_existed = cursor.fetchone()
                    if is_existed is None:
                        continue
                    actor_to_movie_sql = "INSERT INTO `actor_to_movie` (`movie_info_id`, `movie_actor_id`) VALUES (%s, %s)"
                    cursor.execute(actor_to_movie_sql, (movie_info_id, actor_id))
            kgqa_connection.commit()
    except Exception as err:
        print('actor_to_movie数据插入错误' + str(err))


def writer_to_movie():
    """
    电影和编剧之间进行关联
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

    try:
        with kgqa_connection.cursor() as cursor:
            for movie in movie_json_list:
                movie_info_id = movie['id']
                movie_writer = movie['writers']
                movie_writer_id = [writer['id'] for writer in movie_writer]
                movie_writer_id = list(set(movie_writer_id))
                if '' in movie_writer_id:
                    movie_writer_id.remove('')
                for writer_id in movie_writer_id:
                    # 判断movie_person中是否存在该ID
                    is_existed_sql = 'select 1 from `movie_person` where `movie_person_id` = ' + '\'' + writer_id + '\'' + 'limit 1'
                    cursor.execute(is_existed_sql)
                    is_existed = cursor.fetchone()
                    if is_existed is None:
                        continue
                    writer_to_movie_sql = "INSERT INTO `writer_to_movie` (`movie_info_id`, `movie_writer_id`) VALUES (%s, %s)"
                    cursor.execute(writer_to_movie_sql, (movie_info_id, writer_id))
            kgqa_connection.commit()
    except Exception as err:
        print('actor_to_movie数据插入错误' + str(err))


def director_to_movie():
    """
    电影和导演之间进行关联
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

    try:
        with kgqa_connection.cursor() as cursor:
            for movie in movie_json_list:
                movie_info_id = movie['id']
                movie_director = movie['directors']
                movie_director_id = [director['id'] for director in movie_director]
                movie_director_id = list(set(movie_director_id))
                if '' in movie_director_id:
                    movie_director_id.remove('')
                for director_id in movie_director_id:
                    # 判断movie_person中是否存在该ID
                    is_existed_sql = 'select 1 from `movie_person` where `movie_person_id` = ' + '\'' + director_id + '\'' + 'limit 1'
                    cursor.execute(is_existed_sql)
                    is_existed = cursor.fetchone()
                    if is_existed is None:
                        continue
                    director_to_movie_sql = "INSERT INTO `director_to_movie` (`movie_info_id`, `movie_director_id`) VALUES (%s, %s)"
                    cursor.execute(director_to_movie_sql, (movie_info_id, director_id))
            kgqa_connection.commit()
    except Exception as err:
        print('actor_to_movie数据插入错误' + str(err))


#############solve book information ####################
def book_genre():
    """
    提取书籍类别，并保存到mysql之中
    :return:
    """
    # 读取文件
    book_file_path = '../../data/bigdata/book_info.txt'
    book_str_list = open(book_file_path, 'r').readlines()
    book_json_list = [json.loads(book) for book in book_str_list]

    # 提取书籍类别
    book_genre = set()
    for book in book_json_list:
        book_genre.add(book['tag'].strip())
    book_genre = list(book_genre)
    book_genre.sort(key=lambda i: len(i))

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
            genre_id = 1
            for genre in book_genre:
                sql = "INSERT INTO `book_genre` (`book_genre_id`, `book_genre_name`) VALUES (%s, %s)"
                cursor.execute(sql, (genre_id, genre))
                genre_id += 1
            kgqa_connection.commit()
    except Exception as err:
        print('book_genre数据插入错误' + str(err))


def book_info():
    """
    将图书信息加入到数据库之中
    :return:
    """
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
                book_info_image_url = book['image_url']
                book_info_name = book['name']
                book_info_press = book['press']
                book_info_publish_year = book['publish_year']
                book_info_page_num = book['page_num']
                book_info_price = book['price']
                book_info_content_abstract = book['content_abstract']
                book_info_catalog = book['catalog']
                book_info_rating = book['rating']['average']
                book_info_review_count = book['rating']['reviews_count']
                movie_info_sql = "INSERT INTO `book_info` (`book_info_id`, `book_info_image_url`, `book_info_name`, " \
                                 "`book_info_press`, `book_info_publish_year`, `book_info_page_num`," \
                                 "`book_info_price`, `book_info_content_abstract`, `book_info_catalog`, `book_info_rating`," \
                                 "`book_info_review_count`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                cursor.execute(movie_info_sql, (book_info_id, book_info_image_url, book_info_name, book_info_press,
                                                book_info_publish_year, book_info_page_num, book_info_price,
                                                book_info_content_abstract,
                                                book_info_catalog, book_info_rating, book_info_review_count))
            kgqa_connection.commit()
    except Exception as err:
        print('book_info数据插入错误' + str(err))


def book_person():
    """
    将图书作者信息插入到mysql数据库之中
    :return:
    """
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
                book_person_image_url = book_person['image_url']
                book_person_gender = book_person['gender']
                book_person_birthday = book_person['birthday']
                book_person_birthplace = book_person['country']
                book_person_other_name = ''
                book_person_other_chinese_name = book_person['other_chinese_name']
                book_person_other_english_name = book_person['other_english_name']
                if book_person_other_chinese_name and not book_person_other_english_name:
                    book_person_other_name = book_person_other_chinese_name
                if not book_person_other_chinese_name and book_person_other_english_name:
                    book_person_other_name = book_person_other_english_name
                if not book_person_other_chinese_name and not book_person_other_english_name:
                    book_person_other_name = ''
                if book_person_other_chinese_name and book_person_other_english_name:
                    book_person_other_name = book_person_other_chinese_name + '/' + book_person_other_english_name
                book_person_introduction = book_person['introduction']
                book_person_info_sql = "INSERT INTO `book_person` (`book_person_id`, `book_person_name`, `book_person_image_url`," \
                                       "`book_person_gender`, `book_person_birthday`, `book_person_birthplace`, `book_person_other_name`," \
                                       "`book_person_introduction`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

                cursor.execute(book_person_info_sql,
                               (book_person_id, book_person_name, book_person_image_url, book_person_gender,
                                book_person_birthday, book_person_birthplace, book_person_other_name,
                                book_person_introduction))
            kgqa_connection.commit()
    except Exception as err:
        print('book_info数据插入错误' + str(err))


def book_to_genre():
    """
    书籍和书籍类别之间进行关联
    :return:
    """
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
    try:
        with kgqa_connection.cursor() as cursor:
            for book in book_json_list:
                book_info_id = book['id']
                book_genre = book['tag']
                book_genre_id_sql = "SELECT `book_genre_id` FROM `book_genre` WHERE `book_genre_name`=" + '\'' + str(
                    book_genre) + '\''
                cursor.execute(book_genre_id_sql)
                book_genre_info = cursor.fetchone()
                book_genre_id = book_genre_info['book_genre_id']

                book_to_genre_sql = "INSERT INTO `book_to_genre` (`book_info_id`, `book_genre_id`) VALUES (%s, %s)"
                cursor.execute(book_to_genre_sql, (book_info_id, book_genre_id))
            kgqa_connection.commit()
    except Exception as err:
        print('book_to_genre数据插入错误' + str(err))

def author_to_book():
    """
    作者和书籍之间进行关联
    :return:
    """
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
    try:
        with kgqa_connection.cursor() as cursor:
            for book in book_json_list:
                book_info_id = book['id']
                book_author = book['author']
                book_author_id = [author['id'] for author in book_author]
                book_author_id = list(set(book_author_id))
                if '' in book_author_id:
                    book_author_id.remove('')
                for author_id in book_author_id:
                    # 判断book_person是否存在该ID
                    is_existed_sql = 'select 1 from `book_person` where `book_person_id`=' + '\'' + author_id + '\'' + 'limit 1'
                    cursor.execute(is_existed_sql)
                    is_existed = cursor.fetchone()
                    if not is_existed:
                        continue
                    author_to_book_sql = 'INSERT INTO `author_to_book` (`book_info_id`, `book_author_id`) VALUES (%s, %s)'
                    cursor.execute(author_to_book_sql, (book_info_id, author_id))
            kgqa_connection.commit()
    except Exception as err:
        print('author_to_book数据插入错误' + str(err))

def translator_to_book():
    """
    译者和书籍之间进行关联
    :return:
    """
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
    try:
        with kgqa_connection.cursor() as cursor:
            for book in book_json_list:
                book_info_id = book['id']
                book_translator = book['translator']
                book_translator_id = [translator['id'] for translator in book_translator]
                book_translator_id = list(set(book_translator_id))
                if '' in book_translator_id:
                    book_translator_id.remove('')
                for translator_id in book_translator_id:
                    # 判断book_person是否存在该ID
                    is_existed_sql = 'select 1 from `book_person` where `book_person_id`=' + '\'' + translator_id + '\'' + 'limit 1'
                    cursor.execute(is_existed_sql)
                    is_existed = cursor.fetchone()
                    if not is_existed:
                        continue
                    translator_to_book_sql = 'INSERT INTO `translator_to_book` (`book_info_id`, `book_translator_id`) VALUES (%s, %s)'
                    cursor.execute(translator_to_book_sql, (book_info_id, translator_id))
            kgqa_connection.commit()
    except Exception as err:
        print('author_to_book数据插入错误' + str(err))

if __name__ == '__main__':
    # movie_genre()
    # movie_info()
    # movie_person()
    # movie_to_genre()
    # actor_to_movie()
    # writer_to_movie()
    # director_to_movie()
    # book_genre()
    # book_info()
    # book_to_genre()
    # book_person()
    # author_to_book()
    translator_to_book()
