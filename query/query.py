# -*- coding:utf-8 -*-

"""
处理整个流程
"""

import yaml
from ner.query_ner import QueryNER
from inference.query2sparql import Query2Sparql
from fuseki.sparql_query import SparqlQuery


class Query:
    def __init__(self):
        """
        初始化
        """

        # 初始化Jena Fuseki服务器
        self.sparql_query = SparqlQuery()

        # NER初始化加载词
        self.query_ner = QueryNER(['ner/book_and_movie_name.txt', 'ner/person_name.txt'])

        # 初始化加载推理模型
        self.query2sparql = Query2Sparql()

    def parse(self, question):
        """
        解析主流程
        :return:
        """
        # 命名实体识别
        question_label = self.query_ner.get_ner_objects(question)
        for value in question_label:
            print(value.token, value.pos)

        # 语义推断

        # Sparql推理
        sparql_list = self.query2sparql.parse(question_label)
        print(sparql_list)
        for sparql in sparql_list:
            print(sparql[0], sparql[1])

        # sparql查询
        candidate_set = []
        for sparql_q in sparql_list:
            sparql_result = self.sparql_query.get_sparql_result(sparql_q[1])
            sparql_result_value = self.sparql_query.get_sparql_result_value(sparql_result)
            candidate_set.append(sparql_result_value)
        print(candidate_set)

        # 寻找最相似的问题, 生成答案返回


if __name__ == '__main__':
    query = Query()
    question = '流浪地球的演员是谁啊'
    while True:
        question = input('问题: ')
        ans = query.parse(question)
        print(ans)
