# -*- coding:utf-8 -*-

"""
基于规则的推理
------------
电影用户
"""

from refo import finditer, Predicate, Star, Any, Disjunction
import re


class W(Predicate):
    def __init__(self, token=".*", pos=".*"):
        self.token = re.compile(token + "$")
        self.pos = re.compile(pos + "$")
        super(W, self).__init__(self.match)

    def match(self, word):
        m1 = self.token.match(word.token)
        m2 = self.pos.match(word.pos)
        return m1 and m2


class Rule(object):
    def __init__(self, condition_num, condition=None, action=None):
        assert condition and action
        self.condition_num = condition_num
        self.condition = condition
        self.action = action

    def apply(self, sentence):
        matches = []
        for m in finditer(self.condition, sentence):
            i, j = m.span()
            matches.extend(sentence[i:j])
        return self.action(matches), self.condition_num


class KeywordRule(object):
    def __init__(self, condition=None, action=None):
        assert condition and action
        self.condition = condition
        self.action = action

    def apply(self, sentence):
        matches = []
        for m in finditer(self.condition, sentence):
            i, j = m.span()
            matches.extend(sentence[i:j])
        if len(matches) == 0:
            return None
        else:
            return self.action()


class PropertyValueSet:
    def __init__(self):
        pass

    # 电影类型
    @staticmethod
    def return_plot_value():
        return u'剧情'

    @staticmethod
    def return_disaster_value():
        return u'灾难'

    @staticmethod
    def return_music_value():
        return u'音乐'

    @staticmethod
    def return_absurd_value():
        return u'荒诞'

    @staticmethod
    def return_motion_value():
        return u'运动'

    @staticmethod
    def return_west_value():
        return u'西部'

    @staticmethod
    def return_opera_value():
        return u'戏曲'

    @staticmethod
    def return_science_value():
        return u'科幻'

    @staticmethod
    def return_history_value():
        return u'历史'

    @staticmethod
    def return_martial_arts_value():
        return u'武侠'

    @staticmethod
    def return_adventure_value():
        return u'冒险'

    @staticmethod
    def return_biography_value():
        return u'传记'

    @staticmethod
    def return_musical_value():
        return u'歌舞'

    @staticmethod
    def return_fantasy_value():
        return u'奇幻'

    @staticmethod
    def return_crime_value():
        return u'犯罪'

    @staticmethod
    def return_action_value():
        return u'动作'

    @staticmethod
    def return_costume_value():
        return u'古装'

    @staticmethod
    def return_horror_value():
        return u'恐怖'

    @staticmethod
    def return_love_value():
        return u'爱情'

    @staticmethod
    def return_short_value():
        return u'短片'

    @staticmethod
    def return_ghosts_value():
        return u'鬼怪'

    @staticmethod
    def return_suspense_value():
        return u'悬念'

    @staticmethod
    def return_child_value():
        return u'儿童'

    @staticmethod
    def return_mystery_value():
        return u'悬疑'

    @staticmethod
    def return_war_value():
        return u'战争'

    @staticmethod
    def return_thriller_value():
        return u'惊悚'

    @staticmethod
    def return_comedy_value():
        return u'喜剧'

    @staticmethod
    def return_erotic_value():
        return u'情色'

    @staticmethod
    def return_gay_value():
        return u'同性'

    @staticmethod
    def return_family_value():
        return u'家庭'

    @staticmethod
    def return_animation_value():
        return u'动画'

    @staticmethod
    def return_reality_show_value():
        return u'真人秀'

    @staticmethod
    def return_documentary_value():
        return u'纪录'

    @staticmethod
    def return_talk_show_value():
        return u'脱口秀'

    @staticmethod
    def return_stagecraft_value():
        return u'舞台艺术'

    @staticmethod
    def return_film_noir_value():
        return u'黑色电影'

    @staticmethod
    def return_image_url_value():
        return u':movie_person_image_url'

    @staticmethod
    def return_gender_value():
        return u":movie_person_gender"

    @staticmethod
    def return_constellation_value():
        return u":movie_person_constellation"

    @staticmethod
    def return_birthday_value():
        return u":movie_person_birthday"

    @staticmethod
    def return_birthplace_value():
        return u":movie_person_birthplace"

    @staticmethod
    def return_profession_value():
        return u":movie_person_profession"

    @staticmethod
    def return_other_name_value():
        return u":movie_person_profession"

    @staticmethod
    def return_introduction_value():
        return u":movie_person_introduction"

    @staticmethod
    def return_higher_value():
        return u'>'

    @staticmethod
    def return_lower_value():
        return u'<'

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
            PropertyValueSet.return_image_url_value(),
            PropertyValueSet.return_gender_value(),
            PropertyValueSet.return_constellation_value(),
            PropertyValueSet.return_birthday_value(),
            PropertyValueSet.return_birthplace_value(),
            PropertyValueSet.return_profession_value(),
            PropertyValueSet.return_other_name_value(),
            PropertyValueSet.return_introduction_value()
        ]
        sparql_list = []
        for w in word_objects:
            if w.pos == pos_movie:
                for keyword in information_list:
                    e = u"?p :movie_person_name '{person}'.\n" \
                        u"?p {keyword} ?x".format(person=w.token, keyword=keyword)

                    sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX,
                                                      select=select,
                                                      expression=3)
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

"""
前缀和模版
"""
SPARQL_PREFIX = u"""PREFIX : <http://www.douban_kgqa.com#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
"""
SPARQL_SELECT_TEM = u"{prefix}\n" + \
                    u"SELECT DISTINCT {select} WHERE {{\n" + \
                    u"{expression}\n" + \
                    u"}}\n"

SPARQL_COUNT_TEM = u"{prefix}\n" + \
                   u"SELECT COUNT({select}) WHERE {{\n" + \
                   u"{expression}\n" + \
                   u"}}\n"

SPARQL_ASK_TEM = u"{prefix}\n" + \
                 u"ASK {{\n" + \
                 u"{expression}\n" + \
                 u"}}\n"

"""
定义关键词
"""
pos_person = "nr"
pos_movie = "nz"
pos_number = "m"

person_entity = (W(pos=pos_person))
# movie_entity = (W(pos=pos_movie))
number_entity = (W(pos=pos_number))

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
actor = (W("演了") | W("出演"))  # 演员
writer = (W('编剧') | W('写作') | W('写了'))  # 编剧
director = (W('导演') | W('指导'))  # 导演
image_url = (W('图片') | W('照片') | W('写真'))  # 图片
gender = (W('性别'))  # 性别
constellation = (W('星座'))  # 星座
birthday = (W('出生日期') | W("出生时间") | W('生日') | W('时间') + W('出生'))  # 生日
birthplace = (W('出生地') | W('地点') + W('出生'))  # 出身地
profession = (W('职业') | W('工作'))  # 职业
other_name = (W('其他名字') | W('其他名称') | W('别名') | W('中文名') | W('英文名'))  # 其他名称
introduction = (W('简介') | W('自我介绍') | W('介绍') | W("是") + W("谁"))  # 简介
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

# 问题模版, 匹配规则
"""
# 某人的图片/性别/星座/生日/出生地/职业/其他名称/介绍/
# 某人演了哪些电影
# 某人写了哪些电影
# 某人指导了哪些电影
# 某人的详细信息


# 某人出演了多少部电影
# 某人写了多少部电影
# 某人导演了多少部电影
# 某演员参演的评分大于X的电影有哪些
# 某演员出演过哪些类型的电影
# 演员A和演员B合作出演了哪些电影
"""
movie_person_rules = [
    Rule(condition_num=2, condition=person_entity + Star(Any(), greedy=False) + movie_person_info + Star(Any(), greedy=False), action=QuestionSet.has_movie_person_info),
    Rule(condition_num=2, condition=person_entity + Star(Any(), greedy=False) + movie + Star(Any(), greedy=False), action=QuestionSet.has_acted_in),
    Rule(condition_num=2, condition=person_entity + Star(Any(), greedy=False) + movie + Star(Any(), greedy=False), action=QuestionSet.has_writed_in),
    Rule(condition_num=2, condition=person_entity + Star(Any(), greedy=False) + movie + Star(Any(), greedy=False), action=QuestionSet.has_directed_in),
    Rule(condition_num=2, condition=person_entity + Star(Any(), greedy=False) + detail_information + Star(Any(), greedy=False), action=QuestionSet.has_detail_information),
]

basic_movie_person = [
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + image_url + Star(Any(), greedy=False), action=PropertyValueSet.return_image_url_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + gender + Star(Any(), greedy=False), action=PropertyValueSet.return_gender_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + constellation + Star(Any(), greedy=False), action=PropertyValueSet.return_constellation_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + birthday + Star(Any(), greedy=False), action=PropertyValueSet.return_birthday_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + birthplace + Star(Any(), greedy=False), action=PropertyValueSet.return_birthplace_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + profession + Star(Any(), greedy=False), action=PropertyValueSet.return_profession_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + other_name + Star(Any(), greedy=False), action=PropertyValueSet.return_other_name_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + introduction + Star(Any(), greedy=False), action=PropertyValueSet.return_introduction_value)
]

# 某人主演了哪些类型的电影
genre_keyword_rules = [
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + plot + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_plot_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + disaster + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_disaster_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + music + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_music_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + absurd + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_absurd_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + motion + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_motion_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + west + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_west_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + opera + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_opera_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + science + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_science_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + history + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_history_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + martial_arts + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_martial_arts_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + adventure + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_adventure_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + biography + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_biography_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + musical + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_musical_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + fantasy + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_fantasy_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + crime + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_crime_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + action + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_action_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + costume + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_costume_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + horror + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_horror_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + love + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_love_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + short + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_short_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + ghosts + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_ghosts_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + suspense + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_suspense_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + child + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_child_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + mystery + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_mystery_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + war + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_war_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + thriller + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_thriller_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + comedy + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_comedy_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + erotic + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_erotic_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + gay + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_gay_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + family + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_family_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + animation + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_animation_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + reality_show + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_reality_show_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + documentary + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_documentary_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + talk_show + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_talk_show_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + stagecraft + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_stagecraft_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + film_noir + Star(Any(), greedy=False) + (
            movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_film_noir_value)
]

# 评分大于多少分的电影
compare_keyword_rules = [
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + higher + number_entity + Star(Any(), greedy=False) + movie + Star(Any(), greedy=False), action=PropertyValueSet.return_higher_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + lower + number_entity + Star(Any(), greedy=False) + movie + Star(Any(), greedy=False), action=PropertyValueSet.return_lower_value)
]