# -*- coding:utf-8 -*-

"""
jena fuseki查询
"""

from collections import OrderedDict
from SPARQLWrapper import SPARQLWrapper, JSON


class SparqlQuery:
    """
    SPARQL 查询
    """

    def __init__(self, endpoint_url='http://localhost:3030/douban_kgqa/query'):
        """
        初始化链接
        :param endpoint_url:
        """
        self.sparql_conn = SPARQLWrapper(endpoint_url)

    def get_sparql_result(self, query):
        """
        根据查询条件,得到查询结果
        :param query:
        :return:
        """
        self.sparql_conn.setQuery(query)
        self.sparql_conn.setReturnFormat(JSON)
        return self.sparql_conn.query().convert()

    @staticmethod
    def parse_result(query_result):
        """
        解析返回的结果
        :param query_result:
        :return:
        """
        try:
            query_head = query_result['head']['vars']
            query_results = []
            for r in query_result['results']['bindings']:
                temp_dict = OrderedDict()
                for h in query_head:
                    temp_dict[h] = r[h]['value']
                query_results.append(temp_dict)
            return query_head, query_results
        except Exception as err:
            print('解析结果错误' + str(err))

    def get_sparql_result_value(self, query_result):
        """
        列表存储结果值
        :param query_result:
        :return:
        """
        query_head, query_result = self.parse_result(query_result)
        if query_head is None:
            return query_result
        else:
            values = []
            for qr in query_result:
                for _, value in qr.items():
                    values.append(value)
            return values


if __name__ == '__main__':
    # 测试
    fuseki = SparqlQuery()
    query_test = """
PREFIX : <http://www.douban_kgqa.com#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX vocab: <http://localhost:2020/resource/vocab/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX map: <http://localhost:2020/resource/#>
PREFIX db: <http://localhost:2020/resource/>
SELECT * WHERE {
  ?s :movie_info_name '霸王别姬'.
  ?s ?p ?o.
}
LIMIT 3
    """
    result = fuseki.get_sparql_result(query_test)
    print(str(result))
    query_head, query_result = fuseki.parse_result(result)
    print(str(query_head), str(query_result))
    result_value = fuseki.get_sparql_result_value(result)
    print(result_value)
