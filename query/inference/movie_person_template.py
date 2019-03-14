# -*- coding:utf-8 -*-

# 问题模版, 匹配规则
"""
# 某演员的图片/性别/星座/生日/出生地/职业/其他名称/介绍/ ||| 整体简介
# 某演员演了哪些电影
# 某演员出演了多少部电影
# 某演员参演的评分大于X的电影有哪些
# 某演员出演过哪些类型的电影
# 某演员出演的XX类型电影有哪些
# 某演员是**类型演员吗
# 演员A和演员B合作出演了哪些电影
"""


several = (W("多少") | W("几部"))  # 数量


"""
演员信息
"""
# 出生日期
birthday = (W("生日") | W("出生") + W("日期") | W("出生"))
# 出生地
birthplace = (W("出生地") | W("出生"))


# 某人主演了哪些类型的电影
genre_keyword_rules = [
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + adventure + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_adventure_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + fantasy + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_fantasy_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + animation + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_animation_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + drama + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_drama_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + thriller + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_thriller_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + action + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_action_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + comedy + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_comedy_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + history + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_history_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + western + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_western_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + horror + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_horror_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + crime + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_crime_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + documentary + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_documentary_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + science_fiction + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_fiction_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + mystery + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_mystery_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + music + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_music_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + romance + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_romance_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + family + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_family_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + war + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_war_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + TV + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=PropertyValueSet.return_tv_value)
]

person_basic_keyword_rules = [
    KeywordRule(condition=(person_entity + Star(Any(), greedy=False) + where + birth_place + Star(Any(), greedy=False)) | (person_entity + Star(Any(), greedy=False) + birth_place + Star(Any(), greedy=False)), action=PropertyValueSet.return_birth_place_value),
    KeywordRule(condition=person_entity + Star(Disjunction(Any(), where), greedy=False) + birth + Star(Any(), greedy=False), action=PropertyValueSet.return_birth_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + english_name + Star(Any(), greedy=False), action=PropertyValueSet.return_english_name_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + introduction + Star(Any(), greedy=False), action=PropertyValueSet.return_person_introduction_value)
]

compare_keyword_rules = [
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + higher + number_entity + Star(Any(), greedy=False) + movie + Star(Any(), greedy=False), action=PropertyValueSet.return_higher_value),
    KeywordRule(condition=person_entity + Star(Any(), greedy=False) + lower + number_entity + Star(Any(), greedy=False) + movie + Star(Any(), greedy=False), action=PropertyValueSet.return_lower_value)
]
