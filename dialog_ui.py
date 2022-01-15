def dialog():
    print("Какие жанрsы вас интересуют? Пишите, пожалуйста, жанры через запятую на английском языке. Нажмите ENTER, если хотите пропустить.")
    tags = list(input().split(', '))
    print("Какая минимальная оценка аниме вас устроит по пятибальной шкале? Нажмите ENTER, если хотите пропустить.")
    rating = input()
    rating = float(rating) if rating else 0
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

def tags_coincidence(cur_tags, tags):
    return len(list(set(cur_tags) & set(tags)))