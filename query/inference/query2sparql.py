# -*- coding:utf-8 -*-

from inference.movie_info_template import movie_info_rules
from inference.movie_person_template import movie_person_rules
from inference.book_info_template import book_info_rules
from inference.book_person_template import book_person_rules


class Query2Sparql:
    def __init__(self):
        self.movie_info_rules = movie_info_rules
        self.movie_person_rules = movie_person_rules
        self.book_info_rules = book_info_rules
        self.book_person_rules = book_person_rules

    def parse(self, question_label):
        """
        解析问题模型
        :return:
        """
        sparql_list = []

        # 尝试电影信息解析
        for rule in self.movie_info_rules:
            sparql, num = rule.apply(question_label)
            if isinstance(sparql, list) and sparql:
                for temp_sparql in sparql:
                    sparql_list.append((num, temp_sparql))
                continue
            if sparql:
                sparql_list.append((num, sparql))
                continue

        # 尝试电影人物解析
        for rule in self.movie_person_rules:
            sparql, num = rule.apply(question_label)
            if isinstance(sparql, list) and sparql:
                for temp_sparql in sparql:
                    sparql_list.append((num, temp_sparql))
                continue
            if sparql:
                sparql_list.append((num, sparql))
                continue

        # 尝试书籍信息解析
        for rule in self.book_info_rules:
            sparql, num = rule.apply(question_label)
            if isinstance(sparql, list) and sparql:
                for temp_sparql in sparql:
                    sparql_list.append((num, temp_sparql))
                continue
            if sparql:
                sparql_list.append((num, sparql))

        # 尝试书籍人物解析
        for rule in self.book_person_rules:
            sparql, num = rule.apply(question_label)
            if isinstance(sparql, list) and sparql:
                for temp_sparql in sparql:
                    sparql_list.append((num, temp_sparql))
                continue
            if sparql:
                sparql_list.append((num, sparql))

        return sparql_list
