# -*- coding:utf-8 -*-

"""
基于规则的推理
------------
公共模块
"""
from refo import finditer, Predicate
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
        # 流浪地球 nz
        # 详细信息 n
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
pos_book_or_movie = "nz"
pos_number = "m"


person_entity = (W(pos=pos_person))
book_or_movie_entity = (W(pos=pos_book_or_movie))
number_entity = (W(pos=pos_number))


# 电影属性集合
class MoviePropertyValueSet:
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
    def return_movie_info_image_url_value():
        return u':movie_info_image_url'

    @staticmethod
    def return_movie_info_country_value():
        return u':movie_info_country'

    @staticmethod
    def return_movie_info_language_value():
        return u':movie_info_language'

    @staticmethod
    def return_movie_info_pubdate_value():
        return u':movie_info_pubdate'

    @staticmethod
    def return_movie_info_duration_value():
        return u':movie_info_duration'

    @staticmethod
    def return_movie_info_other_name_value():
        return u':movie_info_other_name'

    @staticmethod
    def return_movie_info_summary_value():
        return u':movie_info_summary'

    @staticmethod
    def return_movie_info_rating_value():
        return u':movie_info_rating'

    @staticmethod
    def return_movie_info_review_count_value():
        return u':movie_info_review_count'

    @staticmethod
    def return_movie_person_image_url_value():
        return u':movie_person_image_url'

    @staticmethod
    def return_movie_person_gender_value():
        return u":movie_person_gender"

    @staticmethod
    def return_movie_person_constellation_value():
        return u":movie_person_constellation"

    @staticmethod
    def return_movie_person_birthday_value():
        return u":movie_person_birthday"

    @staticmethod
    def return_movie_person_birthplace_value():
        return u":movie_person_birthplace"

    @staticmethod
    def return_movie_person_profession_value():
        return u":movie_person_profession"

    @staticmethod
    def return_movie_person_other_name_value():
        return u":movie_person_other_name"

    @staticmethod
    def return_movie_person_introduction_value():
        return u":movie_person_introduction"

    @staticmethod
    def return_higher_value():
        return u'>'

    @staticmethod
    def return_lower_value():
        return u'<'

class BookPropertyValueSet:
    def __init__(self):
        pass

    @staticmethod
    def return_book_info_image_url_value():
        return u":book_info_image_url"

    @staticmethod
    def return_book_info_press_value():
        return u":book_info_press"

    @staticmethod
    def return_book_info_publish_year_value():
        return u":book_info_publish_year"

    @staticmethod
    def return_book_info_page_num_value():
        return u":book_info_page_num"

    @staticmethod
    def return_book_info_price_value():
        return u":book_info_price"

    @staticmethod
    def return_book_info_content_abstract_value():
        return u":book_info_content_abstract"

    @staticmethod
    def return_book_info_catalog_value():
        return u":book_info_catalog"

    @staticmethod
    def return_book_info_rating_value():
        return u":book_info_rating"

    @staticmethod
    def return_book_info_review_count_value():
        return u":book_info_review_count"

    @staticmethod
    def return_book_person_image_url_value():
        return u":book_person_image_url"

    @staticmethod
    def return_book_person_gender_value():
        return u":book_person_gender"

    @staticmethod
    def return_book_person_birthday_value():
        return u":book_person_birthday"

    @staticmethod
    def return_book_person_birthplace_value():
        return u":book_person_birthplace"

    @staticmethod
    def return_book_person_other_name_value():
        return u":book_person_other_name"

    @staticmethod
    def return_book_person_introduction_value():
        return u":book_person_introduction"

    @staticmethod
    def return_higher_value():
        return u'>'

    @staticmethod
    def return_lower_value():
        return u'<'



