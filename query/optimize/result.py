# -*- coding:utf-8 -*-


class OptimizeResult:
    def parse(self, candidate_list):
        result_set = set()
        for i in range(0, len(candidate_list)):
            for j in range(0, len(candidate_list[i])):
                result_set.add(candidate_list[i][j])

        result_list = list(result_set)
        result_str = ','.join(result_list)
        return result_str
