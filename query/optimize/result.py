# -*- coding:utf-8 -*-


class OptimizeResult:
    def parse(self, candidate_list):
        movie_info = []
        book_info = []
        for i in range(0, len(candidate_list)):
            if candidate_list[i][0] == 1 or candidate_list[i][0] == 2:
                movie_info.append((candidate_list[i][1]))
            if candidate_list[i][0] == 3 or candidate_list[i][0] == 4:
                book_info.append((candidate_list[i][1]))
        movie_and_book_info = {
            'movie_info': movie_info,
            'book_info': book_info
        }

        return movie_and_book_info