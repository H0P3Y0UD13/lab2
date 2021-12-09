def dialog():
    print("Какие жанрsы вас интересуют? Пишите, пожалуйста, жанры через запятую на английском языке. Нажмите ENTER, если хотите пропустить.")
    tags = list(input().split(', '))
    print("Какая минимальная оценка аниме вас устроит по десятибальной шкале? Нажмите ENTER, если хотите пропустить.")
    rating = input()
    if rating == '':
        rating = 0
    else:
        rating = float(rating)
    print("Какое количество отзывов вас устроит? Нажмите ENTER, если хотите пропустить.")
    votes = input()
    if votes == '':
        votes = 0
    else:
        votes = int(votes)
    print("Какой тип аниме вас интересует? Нажмите ENTER, если хотите пропустить.")
    anime_type = input()
    print("Вас интересует законченное аниме? (True/False) Нажмите ENTER, если хотите пропустить.")
    fin = input()
    return tags, rating, votes, anime_type, fin

def tag_search(cur, headers):
    head_s = headers.index(cur)
    return head_s

def results(cur_tags,tags, cur_rs, votes, anime_type, fin):
    x1 = len(list(set(cur_tags) & set(tags)))
    x2 = cur_rs + votes + anime_type + fin
    return x1+x2