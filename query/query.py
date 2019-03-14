# -*- coding:utf-8 -*-

"""
处理整个流程
"""

import yaml
from sparal.jena_sparql_endpoint import JenaFuseki
from ner.question_ner import QuestionNER
from inference import movie_info_template


class Query:
    def __init__(self):
        """
        初始化
        """

        # 初始化Jena Fuseki服务器
        self.fuseki = JenaFuseki()

        # NER初始化加载词
        self.question_ner = QuestionNER(['ner/book_and_movie_name.txt', 'ner/person_name.txt'])

        # 初始化加载movie_info template
        self.movie_info_rules = movie_info_template.rules

    def parse(self, question):
        """
        解析主流程
        :return:
        """
        # 命名实体识别
        ner_object = self.question_ner.get_ner_objects(question)
        # for value in ner_object:
        #     print(value.token, value.pos)

        # 推理模型
        query_list = []
        for movie_info_rule in self.movie_info_rules:
            query, num = movie_info_rule.apply(ner_object)
            # print(query, num)
            # print(type(query), type(num))
            if isinstance(query, list) and query:
                for temp_query in query:
                    query_list.append((num, temp_query))
                continue
            if query:
                query_list.append((num, query))
                continue
        print(query_list)

        # 进行sparql查询
        question_ans = []
        for sparql_q in query_list:
            sparql_result = self.fuseki.get_sparql_result(sparql_q[1])
            sparql_result_value = self.fuseki.get_sparql_result_value(sparql_result)
            question_ans.append(sparql_result_value)


        # 寻找最相似的问题

        print(question_ans)


if __name__ == '__main__':
    query = Query()
    question = '流浪地球的演员是谁啊'
    while True:
        question = input('问题: ')
        ans = query.parse(question)
        print(ans)
