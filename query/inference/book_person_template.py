# -*- coding:utf-8 -*-

"""
基于规则的推理
------------
书籍用户
"""

from refo import Star, Any
from inference.basic_inference import W, Rule, KeywordRule
from inference.basic_inference import SPARQL_PREFIX, SPARQL_ASK_TEM, SPARQL_COUNT_TEM, SPARQL_SELECT_TEM
from inference.basic_inference import pos_person, pos_book_or_movie, pos_number, person_entity, book_or_movie_entity, number_entity
from inference.basic_inference import BookPropertyValueSet

"""
书籍用户信息
"""
book = (W('书籍') | W('书') | W('图书')) # 图书
author = (W('写作') | W('写了') | W('写过'))  #作者
translator = (W('翻译'))  #译者
image_url = (W('海报') | W('图片') | W('封面'))  # 封面
gender = (W('性别'))  # 性别
birthday = (W('出生日期') | W("出生时间") | W('生日') | W('时间') + W('出生'))  # 生日
birthplace = (W('出生地') | W('地点') + W('出生'))  # 出身地
other_name = (W('其他名字') | W('其他名称') | W('别名') | W('中文名') | W('英文名'))  # 其他名称
introduction = (W('简介') | W('自我介绍') | W('介绍') | W("是") + W("谁"))  # 简介
detail_information = (W('详细信息') | W('详细介绍'))

book_person_info = (image_url | gender | birthday | birthplace | other_name | introduction)

# 数量类
category = (W("类型") | W("种类"))
several = (W("多少") | W("几部"))

# 比较类
higher = (W("大于") | W("高于"))
lower = (W("小于") | W("低于"))
compare = (higher | lower)

# 类型
when = (W("何时") | W("时候"))
where = (W("哪里") | W("哪儿") | W("何地") | W("何处") | W("在") + W("哪"))

"""
问题SPARQL模版
"""
class QuestionSet:
    def __init__(self):
        pass

    @staticmethod
    def has_book_person_info(word_objects):
        """
        某人的基本信息
        :return:
        """
        keyword = None
        for r in basic_book_person:
            keyword = r.apply(word_objects)
            if keyword is not None:
                break

        select = u"?x"
        sparql = None
        for w in word_objects:
            if w.pos == pos_person:
                e = u"?p :book_person_name '{person}'." \
                    u"?p {keyword} ?x.".format(person=w.token, keyword=keyword)
                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def has_authored_in(word_objects):
        """
        某人写了哪些书籍
        :param word_objects:
        :return:
        """
        select = u"?x"
        sparql = None
        for w in word_objects:
            if w.pos == pos_person:
                e = u"?p :book_person_name '{person}'." \
                    u"?p :has_authored_in ?b." \
                    u"?b :book_info_name ?x".format(person=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def has_translated_in(word_objects):
        """
        某人写了哪些书籍
        :param word_objects:
        :return:
        """
        select = u"?x"
        sparql = None
        for w in word_objects:
            if w.pos == pos_person:
                e = u"?p :book_person_name '{person}'." \
                    u"?p :has_translated_in ?b." \
                    u"?b :book_info_name ?x".format(person=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def has_detail_information(word_objects):
        """
        某书籍的详细信息
        :param word_objects:
        :return:
        """
        select = u"?x"
        information_list = [
            BookPropertyValueSet.return_book_person_image_url_value(),
            BookPropertyValueSet.return_book_person_gender_value(),
            BookPropertyValueSet.return_book_person_birthday_value(),
            BookPropertyValueSet.return_book_person_birthplace_value(),
            BookPropertyValueSet.return_book_person_other_name_value(),
            BookPropertyValueSet.return_book_person_introduction_value()
        ]
        sparql_list = []
        for w in word_objects:
            if w.pos == pos_person:
                for keyword in information_list:
                    e = u"?p :book_person_name '{person}'." \
                        u"?p {keyword} ?x".format(person=w.token, keyword=keyword)
                    sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX,
                                                      select=select,
                                                      expression=e)
                    sparql_list.append(sparql)
                break
        return sparql_list

# 问题模版, 匹配规则
"""
# 某人的图片/性别/生日/出生地/其他名称/介绍/
# 某人写了哪些书籍
# 某人翻译了哪些书籍
# 某人的详细信息
"""

book_person_rules = [
    Rule(condition_num=4, condition=person_entity + Star(Any(), greedy=False) + book_person_info +  Star(Any(), greedy=False), action=QuestionSet.has_book_person_info),
    Rule(condition_num=4, condition=person_entity + Star(Any(), greedy=False) + author + Star(Any(), greedy=False), action=QuestionSet.has_authored_in),
    Rule(condition_num=4, condition=person_entity + Star(Any(), greedy=False) + translator + Star(Any(), greedy=False), action=QuestionSet.has_translated_in),
    Rule(condition_num=4, condition=person_entity + Star(Any(), greedy=False) + detail_information + Star(Any(), greedy=False), action=QuestionSet.has_detail_information)
]

basic_book_person = [
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + image_url + Star(Any(), greedy=False), action=BookPropertyValueSet.return_book_person_image_url_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + gender + Star(Any(), greedy=False), action=BookPropertyValueSet.return_book_person_gender_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + birthday + Star(Any(), greedy=False), action=BookPropertyValueSet.return_book_person_birthday_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + birthplace + Star(Any(), greedy=False), action=BookPropertyValueSet.return_book_person_birthplace_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + other_name + Star(Any(), greedy=False), action=BookPropertyValueSet.return_book_person_other_name_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + introduction + Star(Any(), greedy=False), action=BookPropertyValueSet.return_book_person_introduction_value)
]