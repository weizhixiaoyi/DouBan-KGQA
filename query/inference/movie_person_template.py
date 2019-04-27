# -*- coding:utf-8 -*-

"""
基于规则的推理
------------
电影用户
"""

from refo import Star, Any
from inference.basic_inference import W, Rule, KeywordRule
from inference.basic_inference import SPARQL_PREFIX, SPARQL_ASK_TEM, SPARQL_COUNT_TEM, SPARQL_SELECT_TEM
from inference.basic_inference import pos_person, pos_book_or_movie, pos_number, person_entity, book_or_movie_entity, number_entity
from inference.basic_inference import MoviePropertyValueSet

"""
电影类型信息
"""
plot = (W('剧情') | W('剧情片'))
disaster = (W('灾难') | W('灾难片'))
music = (W('音乐') | W('音乐片'))
absurd = (W('荒诞') | W('荒诞片'))
motion = (W('运动') | W('运动片'))
west = (W('西部') | W('西部片'))
opera = (W('戏曲') | W('戏曲片'))
science = (W('科幻') | W('科幻片'))
history = (W('历史') | W('历史片'))
martial_arts = (W('武侠') | W('武侠片'))
adventure = (W('冒险') | W('冒险片'))
biography = (W('传记') | W('传记片'))
musical = (W('歌舞') | W('歌舞片'))
fantasy = (W('奇幻') | W('奇幻片'))
crime = (W('犯罪') | W('犯罪片'))
action = (W('动作') | W('动作片'))
costume = (W('古装') | W('古装片'))
horror = (W('恐怖') | W('恐怖片'))
love = (W('爱情') | W('爱情片'))
short = (W('短片'))
ghosts = (W('鬼怪') | W('鬼怪片') | W('鬼神') | W('鬼神片'))
suspense = (W('悬念') | W('悬念片'))
child = (W('儿童') | W('儿童片'))
mystery = (W("悬疑") | W("悬疑片"))
war = (W('战争') | W('战争片'))
thriller = (W('惊悚') | W('惊悚片'))
comedy = (W('喜剧') | W('喜剧片'))
erotic = (W('情色') | W('情色片'))
gay = (W('同性') | W('同性片'))
family = (W('家庭') | W('家庭片'))
animation = (W('动画') | W('动画片'))
reality_show = (W('真人秀'))
documentary = (W('纪录') | W('纪录片'))
talk_show = (W('脱口秀'))
stagecraft = (W('舞台艺术'))
film_noir = (W('黑色电影'))

"""
电影用户信息
"""
movie = (W("电影") | W("影片") | W("片子") | W("片") | W("剧"))  # 电影
director = (W('导演') | W('指导'))  # 导演
writer = (W('编剧') | W('写作') | W('写了'))  # 编剧
actor = (W("演了") | W("出演") | W('主演'))  # 演员
image_url = (W('图片') | W('照片') | W('写真'))  # 图片
gender = (W('性别'))  # 性别
constellation = (W('星座'))  # 星座
birthday = (W('出生日期') | W("出生时间") | W('生日') | W('时间') + W('出生'))  # 生日
birthplace = (W('出生地') | W('地点') + W('出生'))  # 出身地
profession = (W('职业') | W('工作'))  # 职业
other_name = (W('其他名字') | W('其他名称') | W('别名') | W('中文名') | W('英文名'))  # 其他名称
introduction = (W('简介') | W('个人简介') | W('自我介绍'))  # 简介
movie_person_info = (image_url | gender | constellation | birthday | birthplace |
                profession | other_name | introduction)
detail_information = (W('详细信息') | W('详细介绍'))

category = (W("类型") | W("种类"))
several = (W("多少") | W("几部"))

higher = (W("大于") | W("高于"))
lower = (W("小于") | W("低于"))
compare = (higher | lower)

when = (W("何时") | W("时候"))
where = (W("哪里") | W("哪儿") | W("何地") | W("何处") | W("在") + W("哪"))

class QuestionSet:
    def __init__(self):
        pass

    @staticmethod
    def has_movie_person_info(word_objects):
        """
        某人的基本信息
        :param word_objects:
        :return:
        """
        keyword = None
        for r in basic_movie_person:
            keyword = r.apply(word_objects)
            if keyword is not None:
                break

        select = u"?x"
        sparql = None
        for w in word_objects:
            if w.pos == pos_person:
                e = u"?p :movie_person_name '{person}'.\n" \
                    u"?p {keyword} ?x.".format(person=w.token, keyword=keyword)
                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def has_acted_in(word_objects):
        """
        某人演了哪些电影
        :param word_objects:
        :return:
        """
        select = u"?x"
        sparql = None
        for w in word_objects:
            if w.pos == pos_person:
                e = u"?p :movie_person_name '{person}'.\n" \
                    u"?p :has_acted_in ?m.\n" \
                    u"?m :movie_info_name ?x".format(person=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def has_writed_in(word_objects):
        """
        某人写了哪些电影
        :param word_objects:
        :return:
        """
        select = u"?x"
        sparql = None
        for w in word_objects:
            if w.pos == pos_person:
                e = u"?p :movie_person_name '{person}'.\n" \
                    u"?p :has_writed_in ?m.\n" \
                    u"?m :movie_info_name ?x".format(person=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def has_directed_in(word_objects):
        """
        某人导演了哪些电影
        :param word_objects:
        :return:
        """
        select = u"?x"
        sparql = None
        for w in word_objects:
            if w.pos == pos_person:
                e = u"?p :movie_person_name '{person}'.\n" \
                    u"?p :has_directed_in ?m.\n" \
                    u"?m :movie_info_name ?x".format(person=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def has_detail_information(word_objects):
        """
        某电影的详细信息
        :param word_objects:
        :return:
        """
        select = u"?x"
        information_list = [
            MoviePropertyValueSet.return_movie_person_image_url_value(),
            MoviePropertyValueSet.return_movie_person_gender_value(),
            MoviePropertyValueSet.return_movie_person_constellation_value(),
            MoviePropertyValueSet.return_movie_person_birthday_value(),
            MoviePropertyValueSet.return_movie_person_birthplace_value(),
            MoviePropertyValueSet.return_movie_person_profession_value(),
            MoviePropertyValueSet.return_movie_person_other_name_value(),
            MoviePropertyValueSet.return_movie_person_introduction_value()
        ]
        sparql_list = []
        for w in word_objects:
            if w.pos == pos_person:
                for keyword in information_list:
                    e = u"?p :movie_person_name '{person}'.\n" \
                        u"?p {keyword} ?x".format(person=w.token, keyword=keyword)

                    sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX,
                                                      select=select,
                                                      expression=e)
                    sparql_list.append(sparql)

                break
        return sparql_list

    @staticmethod
    def has_quantity_movie(word_objects):
        """
        某演员演了多少部电影
        :param word_objects:
        :return:
        """
        select = u"?x"
        sparql = None
        for w in word_objects:
            if w.pos == pos_person:
                e = u"?p :movie_person_name '{person}'.\n" \
                    u"?p :has_acted_in ?x.".format(person=w.token)

                sparql = SPARQL_COUNT_TEM.format(prefix=SPARQL_PREFIX,
                                                 select=select,
                                                 expression=e)
                break

        return sparql

    # @staticmethod
    # def has_quantity_movie(word_objects):
    #     """
    #     某演员演了多少部电影
    #     :param word_objects:
    #     :return:
    #     """
    #     select = u"?x"
    #
    #     sparql = None
    #     for w in word_objects:
    #         if w.pos == pos_person:
    #             e = u"?s :personName '{person}'." \
    #                 u"?s :hasActedIn ?x.".format(person=w.token.decode('utf-8'))
    #
    #             sparql = SPARQL_COUNT_TEM.format(prefix=SPARQL_PREXIX, select=select, expression=e)
    #             break
    #
    #     return sparql

# 问题模版, 匹配规则
"""
# 某人的图片/性别/星座/生日/出生地/职业/其他名称/介绍/
# 某人演了哪些电影
# 某人写了哪些电影
# 某人指导了哪些电影
# 某人的详细信息

# 未完成
# 某人出演了多少部电影
# 某人写了多少部电影
# 某人导演了多少部电影
# 某演员参演的评分大于X的电影有哪些
# 某演员出演过哪些类型的电影
# 演员A和演员B合作出演了哪些电影
"""
movie_person_rules = [
    Rule(condition_num=2, condition=person_entity + Star(Any(), greedy=False) + movie_person_info + Star(Any(), greedy=False), action=QuestionSet.has_movie_person_info),
    Rule(condition_num=2, condition=person_entity + Star(Any(), greedy=False) + director + Star(Any(), greedy=False), action=QuestionSet.has_directed_in),
    Rule(condition_num=2, condition=person_entity + Star(Any(), greedy=False) + writer + Star(Any(), greedy=False), action=QuestionSet.has_writed_in),
    Rule(condition_num=2, condition=person_entity + Star(Any(), greedy=False) + actor + Star(Any(), greedy=False), action=QuestionSet.has_acted_in),
    Rule(condition_num=2, condition=person_entity + Star(Any(), greedy=False) + detail_information + Star(Any(), greedy=False), action=QuestionSet.has_detail_information),
]

basic_movie_person = [
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + image_url + Star(Any(), greedy=False), action=MoviePropertyValueSet.return_movie_person_image_url_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + gender + Star(Any(), greedy=False), action=MoviePropertyValueSet.return_movie_person_gender_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + constellation + Star(Any(), greedy=False), action=MoviePropertyValueSet.return_movie_person_constellation_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + birthday + Star(Any(), greedy=False), action=MoviePropertyValueSet.return_movie_person_birthday_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + birthplace + Star(Any(), greedy=False), action=MoviePropertyValueSet.return_movie_person_birthplace_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + profession + Star(Any(), greedy=False), action=MoviePropertyValueSet.return_movie_person_profession_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + other_name + Star(Any(), greedy=False), action=MoviePropertyValueSet.return_movie_person_other_name_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + introduction + Star(Any(), greedy=False), action=MoviePropertyValueSet.return_movie_person_introduction_value)
]