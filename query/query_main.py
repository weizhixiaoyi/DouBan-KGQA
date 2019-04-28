# -*- coding:utf-8 -*-

"""
处理整个流程
"""
from ner.query_ner import QueryNER
from inference.query2sparql import Query2Sparql
from fuseki.sparql_query import SparqlQuery
from optimize.result import OptimizeResult


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

        # 优化返回答案
        self.optimize_result = OptimizeResult()
        print("Query初始化完成...")

    def parse(self, question):
        """
        解析主流程
        :return:
        """
        if "问答" in question:
            result ="你好啊, 你可以问我关于电影、书籍领域的问题哟.\n" \
                    "比如: 流浪地球的详细信息是什么呢？\n" \
                    "流浪地球的主演/导演/编剧/海报/上映地区/上映时间/时长/其他名字/简介/评分/评价人数是什么？\n" \
                    "吴京的详细信息是什么呢?\n" \
                    "吴京的图片/性别/星座/生日/出生地/职业/其他名称/介绍/是什么?\n" \
                    "吴京主演/导演/的电影有哪些？\n" \
                    "围城的详细信息是什么呢?\n" \
                    "围城的图片/出版社/出版日期/页数/简介/目录/评分/评价人数是什么?\n" \
                    "杨绛的详细信息是什么呢?\n" \
                    "杨绛的图片/性别/生日/出生地/其他名称/介绍/是什么?\n" \
                    "杨绛写作/翻译的书籍有哪些?\n" \
                    "...等等其他类型书籍、电影问题."
            return result
        # 命名实体识别
        # print('question: ' + str(question))
        question_label = self.query_ner.get_ner_objects(question)
        # for value in question_label:
        #     print(value.token, value.pos)

        # Sparql推理
        sparql_list = self.query2sparql.parse(question_label)
        # for sparql in sparql_list:
        #     print(sparql[0], sparql[1])
        #     print('=' * 20)

        # sparql查询
        candidate_list = []
        for sparql_q in sparql_list:
            sparql_result = self.sparql_query.get_sparql_result(sparql_q[1])
            sparql_result_value = self.sparql_query.get_sparql_result_value(sparql_result)
            candidate_list.append((sparql_q[0], sparql_result_value))
        # print(candidate_list)
        # print("candidate_list: " + str(candidate_list))
        # 寻找最相似的问题, 生成答案返回
        result = self.optimize_result.parse(candidate_list)
        return result


if __name__ == '__main__':
    query = Query()
    question = '流浪地球详细信息'
    while True:
        question = input('问题: ')
        ans = query.parse(question)
        print(ans)
