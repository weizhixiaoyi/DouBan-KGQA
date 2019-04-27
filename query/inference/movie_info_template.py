# -*- coding:utf-8 -*-

"""
基于规则的推理
------------
电影信息
"""
from refo import Star, Any
from inference.basic_inference import W, Rule, KeywordRule
from inference.basic_inference import SPARQL_PREFIX, SPARQL_ASK_TEM, SPARQL_COUNT_TEM, SPARQL_SELECT_TEM
from inference.basic_inference import pos_person, pos_book_or_movie, pos_number, person_entity, book_or_movie_entity, number_entity
from inference.basic_inference import MoviePropertyValueSet

"""
电影信息
"""
# 电影类型
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
genre = (plot | disaster | music | absurd | motion | west | opera | science
         | history | martial_arts | adventure | biography | musical | fantasy
         | crime | action | costume | horror | love | short | ghosts | suspense
         | child | mystery | war | thriller | comedy | erotic | gay | family
         | animation | reality_show | documentary | talk_show | stagecraft | film_noir)

movie = (W("电影") | W("影片") | W("片子") | W("片") | W("剧") | W('电视剧') | W('动漫'))  # 电影
category = (W("类型") | W("种类"))  # 类型
actor = (W("演员") | W("艺人") | W("表演者") | W('主演'))  # 演员
writer = (W('编剧'))  # 编剧
director = (W('导演') | W('指导'))  # 导演
image_url = (W('海报') | W('图片'))
country = (W('上映地区') | W('上映国家'))  # 上映国家
language = (W('语言') | W('上映语言'))  # 语言
pubdate = (W("时间") | W('上映时间'))  # 上映时间
duration = (W('多长时间') | W('时长'))  # 时长
other_name = (W('其他名字') | W('其他名称') | W('别名') | W('中文名') | W('英文名'))  # 电影其他名称
summary = (W('介绍') | W('简介'))  # 简介
rating = (W('评分') | W('分') | W('分数'))  # 评分
review_count = (W('评分人数'))  # 评分人数
detail_information = (W('详细信息') | W('详细介绍'))

rating_basic = (rating | review_count)
movie_info = (image_url | country | language | pubdate | duration | other_name | summary | rating | review_count)

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
    def has_movie_info(word_objects):
        """
        某电影的基本信息
        :param word_objects:
        :return:
        """

        keyword = None
        for r in basic_movie_info:
            keyword = r.apply(word_objects)
            if keyword is not None:
                break

        select = u"?x"
        sparql = None
        for w in word_objects:
            if w.pos == pos_book_or_movie:
                e = u"?s :movie_info_name '{movie}'." \
                    u"?s {keyword} ?x.".format(movie=w.token, keyword=keyword)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX, select=select, expression=e)

                break

        return sparql

    @staticmethod
    def has_movie_genre(word_objects):
        """
        某电影的类别
        :return:
        """
        select = u"?x"
        sparql = None
        for w in word_objects:
            if w.pos == pos_book_or_movie:
                e = u"?m :movie_info_name '{movie}'.\n" \
                    u"?m :has_movie_genre ?g.\n" \
                    u"?g :movie_genre_name ?x".format(movie=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def has_actor(word_objects):
        """
        某电影有哪些演员
        :param word_objects:
        :return:
        """
        select = u"?x"
        sparql = None
        for w in word_objects:
            if w.pos == pos_book_or_movie:
                e = u"?m :movie_info_name '{movie}'." \
                    u"?m :has_actor ?a." \
                    u"?a :movie_person_name ?x".format(movie=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def has_writer(word_objects):
        """
        某电影有哪些编剧
        :param word_objects:
        :return:
        """
        select = u"?x"
        sparql = None
        for w in word_objects:
            if w.pos == pos_book_or_movie:
                e = u"?m :movie_info_name '{movie}'." \
                    u"?m :has_writer ?a." \
                    u"?a :movie_person_name ?x".format(movie=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def has_director(word_objects):
        """
        某电影有哪些导演
        :param word_objects:
        :return:
        """
        select = u"?x"
        sparql = None
        for w in word_objects:
            if w.pos == pos_book_or_movie:
                e = u"?m :movie_info_name '{movie}'.\n" \
                    u"?m :has_director ?a.\n" \
                    u"?a :movie_person_name ?x".format(movie=w.token)

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
            MoviePropertyValueSet.return_movie_info_image_url_value(),
            MoviePropertyValueSet.return_movie_info_country_value(),
            MoviePropertyValueSet.return_movie_info_language_value(),
            MoviePropertyValueSet.return_movie_info_pubdate_value(),
            MoviePropertyValueSet.return_movie_info_duration_value(),
            MoviePropertyValueSet.return_movie_info_other_name_value(),
            MoviePropertyValueSet.return_movie_info_summary_value(),
            MoviePropertyValueSet.return_movie_info_rating_value(),
            MoviePropertyValueSet.return_movie_info_review_count_value()
        ]
        sparql_list = []
        for w in word_objects:
            if w.pos == pos_book_or_movie:
                for key_word in information_list:
                    e = u"?m :movie_info_name '{movie}'." \
                        u"?m {key_word} ?x".format(movie=w.token, key_word=key_word)

                    sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX,
                                                      select=select,
                                                      expression=e)
                    sparql_list.append(sparql)

                break
        return sparql_list


# 问题模版, 匹配规则
"""
# 某电影的图片/上映地区/语言/上映时间/时长/其他名称/介绍/评分/ 评价人数
# 某电影的类型
# 某电影有哪些演员
# 某电影有哪些编剧
# 某电影有哪些导演
# 某电影的详细信息
"""

movie_info_rules = [
    Rule(condition_num=1, condition=book_or_movie_entity + Star(Any(), greedy=False) + movie_info + Star(Any(), greedy=False), action=QuestionSet.has_movie_info),
    Rule(condition_num=1, condition=book_or_movie_entity + Star(Any(), greedy=False) + category + Star(Any(), greedy=False), action=QuestionSet.has_movie_genre),
    Rule(condition_num=1,condition=(book_or_movie_entity + Star(Any(), greedy=False) + actor + Star(Any(), greedy=False)) | (actor + Star(Any(), greedy=False) + book_or_movie_entity + Star(Any(), greedy=False)), action=QuestionSet.has_actor),
    Rule(condition_num=1,condition=(book_or_movie_entity + Star(Any(), greedy=False) + writer + Star(Any(), greedy=False)) | (writer + Star(Any(), greedy=False) + book_or_movie_entity + Star(Any(), greedy=False)), action=QuestionSet.has_writer),
    Rule(condition_num=1,condition=(book_or_movie_entity + Star(Any(), greedy=False) + director + Star(Any(), greedy=False)) | (writer + Star(Any(), greedy=False) + book_or_movie_entity) + Star(Any(), greedy=False), action=QuestionSet.has_director),
    Rule(condition_num=1, condition=(book_or_movie_entity + Star(Any(), greedy=False) + detail_information + Star(Any(), greedy=False)) | (detail_information + Star(Any(), greedy=False) + book_or_movie_entity + Star(Any(), greedy=False)), action=QuestionSet.has_detail_information)
]

basic_movie_info = [
    KeywordRule(condition=book_or_movie_entity + Star(Any(), greedy=False) + image_url + Star(Any(), greedy=False), action=MoviePropertyValueSet.return_movie_info_image_url_value),
    KeywordRule(condition=book_or_movie_entity + Star(Any(), greedy=False) + country + Star(Any(), greedy=False), action=MoviePropertyValueSet.return_movie_info_country_value),
    KeywordRule(condition=book_or_movie_entity + Star(Any(), greedy=False) + language + Star(Any(), greedy=False), action=MoviePropertyValueSet.return_movie_info_language_value),
    KeywordRule(condition=book_or_movie_entity + Star(Any(), greedy=False) + pubdate + Star(Any(), greedy=False), action=MoviePropertyValueSet.return_movie_info_pubdate_value),
    KeywordRule(condition=book_or_movie_entity + Star(Any(), greedy=False) + duration + Star(Any(), greedy=False), action=MoviePropertyValueSet.return_movie_info_duration_value),
    KeywordRule(condition=book_or_movie_entity + Star(Any(), greedy=False) + other_name + Star(Any(), greedy=False), action=MoviePropertyValueSet.return_movie_info_other_name_value),
    KeywordRule(condition=book_or_movie_entity + Star(Any(), greedy=False) + summary + Star(Any(), greedy=False), action=MoviePropertyValueSet.return_movie_info_summary_value),
    KeywordRule(condition=book_or_movie_entity + Star(Any(), greedy=False) + rating + Star(Any(), greedy=False), action=MoviePropertyValueSet.return_movie_info_rating_value),
    KeywordRule(condition=book_or_movie_entity + Star(Any(), greedy=False) + review_count + Star(Any(), greedy=False), action=MoviePropertyValueSet.return_movie_info_review_count_value)
]
