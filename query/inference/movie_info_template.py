# -*- coding:utf-8 -*-

"""
基于规则的推理
------------
慢慢更新之中
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
        return u':movie_info_image_url'

    @staticmethod
    def return_country_value():
        return u':movie_info_country'

    @staticmethod
    def return_language_value():
        return u':movie_info_language'

    @staticmethod
    def return_pubdate_value():
        return u':movie_info_pubdate'

    @staticmethod
    def return_duration_value():
        return u':movie_info_duration'

    @staticmethod
    def return_other_name_value():
        return u':movie_info_other_name'

    @staticmethod
    def return_summary_value():
        return u':movie_info_summary'

    @staticmethod
    def return_rating_value():
        return u':movie_info_rating'

    @staticmethod
    def return_review_count_value():
        return u':movie_info_review_count'

    @staticmethod
    def return_higher_value():
        return u'>'

    @staticmethod
    def return_lower_value():
        return u'<'


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
问题SPARQL模版
"""
class QuestionSet:
    def __init__(self):
        pass

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
            if w.pos == pos_movie:
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
            if w.pos == pos_movie:
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
            if w.pos == pos_movie:
                e = u"?m :movie_info_name '{movie}'.\n" \
                    u"?m :has_director ?a.\n" \
                    u"?a :movie_person_name ?x".format(movie=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

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
            if w.pos == pos_movie:
                e = u"?s :movie_info_name '{movie}'." \
                    u"?s {keyword} ?x.".format(movie=w.token, keyword=keyword)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX, select=select, expression=e)

                break

        return sparql


"""
定义关键词
"""
pos_person = "nr"
pos_movie = "nz"
pos_number = "m"

# person_entity = (W(pos=pos_person))
movie_entity = (W(pos=pos_movie))
number_entity = (W(pos=pos_number))

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
actor = (W("演员") | W("艺人") | W("表演者"))  # 演员
writer = (W('编剧'))  # 编剧
director = (W('导演') | W('指导'))  # 导演
image_url = (W('海报') | W('图片'))
country = (W('上映地区') | W('上映国家'))  # 上映国家
language = (W('语言') | W('上映语言'))  # 语言
pubdate = (W('上映') | W("时间") | W('上映时间'))  # 上映时间
duration = (W('多长时间') | W('时长'))  # 时长
other_name = (W('其他名字') | W('其他名称') | W('别名') | W('中文名') | W('英文名'))  # 电影其他名称
summary = (W('介绍') | W('简介'))  # 简介
rating = (W('评分') | W('分') | W('分数'))  # 评分
review_count = (W('评分人数'))  # 评分人数

rating_basic = (rating | review_count)
movie_info = (image_url | country | language | pubdate | duration | other_name | summary | rating | review_count)

# 比较类
higher = (W("大于") | W("高于"))
lower = (W("小于") | W("低于"))
compare = (higher | lower)

# 类型
when = (W("何时") | W("时候"))
where = (W("哪里") | W("哪儿") | W("何地") | W("何处") | W("在") + W("哪"))


# 问题模版, 匹配规则
"""
# 某电影的图片/上映地区/语言/上映时间/时长/其他名称/介绍/评分/ 评价人数 ||| 整体简介
# 某电影的类型
# 某电影有哪些演员
# 某电影有哪些编剧
# 某电影有哪些导演
"""

rules = [
    Rule(condition_num=1, condition=(movie_entity + Star(Any(), greedy=False) + actor + Star(Any(), greedy=False)) | (actor + Star(Any(), greedy=False) + movie_entity + Star(Any(), greedy=False)), action=QuestionSet.has_actor),
    Rule(condition_num=1, condition=(movie_entity + Star(Any(), greedy=False) + writer + Star(Any(), greedy=False)) | (writer + Star(Any(), greedy=False) + movie_entity + Star(Any(), greedy=False)), action=QuestionSet.has_writer),
    Rule(condition_num=1, condition=(movie_entity + Star(Any(), greedy=False) + director + Star(Any(), greedy=False)) | (writer + Star(Any(), greedy=False) + movie_entity) + Star(Any(), greedy=False), action=QuestionSet.has_director),
    Rule(condition_num=1, condition=movie_entity + Star(Any(), greedy=False) + movie_info + Star(Any(), greedy=False), action=QuestionSet.has_movie_info)
]

basic_movie_info = [
    KeywordRule(condition=movie_entity + Star(Any(), greedy=False) + image_url + Star(Any(), greedy=False), action=PropertyValueSet.return_image_url_value),
    KeywordRule(condition=movie_entity + Star(Any(), greedy=False) + country + Star(Any(), greedy=False), action=PropertyValueSet.return_country_value),
    KeywordRule(condition=movie_entity + Star(Any(), greedy=False) + language + Star(Any(), greedy=False), action=PropertyValueSet.return_language_value),
    KeywordRule(condition=movie_entity + Star(Any(), greedy=False) + pubdate + Star(Any(), greedy=False), action=PropertyValueSet.return_pubdate_value),
    KeywordRule(condition=movie_entity + Star(Any(), greedy=False) + duration + Star(Any(), greedy=False), action=PropertyValueSet.return_duration_value),
    KeywordRule(condition=movie_entity + Star(Any(), greedy=False) + other_name + Star(Any(), greedy=False), action=PropertyValueSet.return_other_name_value),
    KeywordRule(condition=movie_entity + Star(Any(), greedy=False) + summary + Star(Any(), greedy=False), action=PropertyValueSet.return_summary_value),
    KeywordRule(condition=movie_entity + Star(Any(), greedy=False) + rating + Star(Any(), greedy=False), action=PropertyValueSet.return_rating_value),
    KeywordRule(condition=movie_entity + Star(Any(), greedy=False) + rating + Star(Any(), greedy=False), action=PropertyValueSet.return_review_count_value)
]
