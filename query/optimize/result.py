# -*- coding:utf-8 -*-


class OptimizeResult:
    def parse(self, candidate_list):
        movie_info = []
        book_info = []
        for i in range(0, len(candidate_list)):
            if candidate_list[i][0] == 1 or candidate_list[i][0] == 2:
                if len(candidate_list[i][1]) != 0:
                    movie_info.append((candidate_list[i][1]))
            if candidate_list[i][0] == 3 or candidate_list[i][0] == 4:
                if len(candidate_list[i][1]) != 0:
                    book_info.append((candidate_list[i][1]))

        result = '对不起, 我不知道这个问题答案.\n' \
                 '你可以回复\"问答\", 来了解我可以回答的问题类型.'
        if movie_info and not book_info:
            movie_str_list = []
            for movie in movie_info:
                movie_str = ', '.join(movie)
                movie_str_list.append(movie_str)
            result = ' | '.join(movie_str_list)
        if not movie_info and book_info:
            book_str_list = []
            for book in book_info:
                book_str = ', '.join(book)
                book_str_list.append(book_str)
            result = ' | '.join(book_str_list)
        if movie_info and book_info:
            movie_str_list = []
            for movie in movie_info:
                movie_str = ', '.join(movie)
                movie_str_list.append(movie_str)
            book_str_list = []
            for book in book_info:
                book_str = ', '.join(book)
                book_str_list.append(book_str)

            result = "电影类别信息\n" + ' | '.join(movie_str_list) + '\n' + \
                     '书籍类别信息\n' + ' | '.join(book_str_list) + '\n'

        return result