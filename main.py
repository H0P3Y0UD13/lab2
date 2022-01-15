import csv
from dialog_ui import dialog
from dialog_ui import tag_search
from dialog_ui import tags_coincidence
import requests
from bs4 import BeautifulSoup


def csv_assign(asg_csv, dep_csv, dialog_var):
    if asg_csv == 'Unknown' or asg_csv == dep_csv:
        asg_csv = 0
    else:
        asg_csv = float(row[tag_search(dep_csv, headers)])            
    if asg_csv >= dialog_var:
        return 1
    else:
        return 0
    

tags, rating, votes, anime_type, fin = dialog()
dict_cur = {}
dict_csv = {}


with open('anime.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader: #Алгоритм рекомендации конкретного аниме.
        res = 0
        cur_tags = list(row[tag_search('Tags', headers)].split(", "))
        rate_csv = row[tag_search('Rating Score', headers)]
        res += int(csv_assign(rate_csv, 'Rating Score', rating))
        votes_csv = row[tag_search('Number Votes', headers)]
        res += int(csv_assign(votes_csv, 'Number Votes', votes))
        if row[tag_search('Type', headers)] == anime_type:
            res += 1
        if fin == 'True' and row[tag_search('Finished', headers)] == 'True':
            res += 1
        res += tags_coincidence(cur_tags, tags)
        print(res)
        cur_id = row[tag_search('Anime-PlanetID', headers)]
        dict_cur[cur_id] = res
        name_cur = row[tag_search('Name', headers)]
        url_cur = row[tag_search('Url', headers)]
        dict_csv[cur_id] = name_cur + ':    ' + url_cur
sorted_dict = {}
sorted_keys = sorted(dict_cur, key=dict_cur.get, reverse=True)
for w in sorted_keys:
    sorted_dict[w] = dict_cur[w]
POINT = 0
f = open('answer.txt', 'w', encoding='utf-8')
for key, value in sorted_dict.items():
    POINT += 1
    for key_2, value_2 in dict_csv.items():
        if key == key_2:
            ans = str(value_2)
            index_url = ans.index('https:')
            if POINT <= min(5, len(dict_csv)):
                response = requests.get(ans[index_url:len(ans)])
                soup = BeautifulSoup(response.text,'html.parser')
                img = requests.get("https://www.anime-planet.com/" + soup.find('img', class_='screenshots')['src'])
                img_file = open(str(POINT) + '.jpg', 'wb')
                img_file.write(img.content)
                img_file.close()
            f.write(ans + '\n')
            break
    if POINT == 100: #Изменять значение, для размера подборки.
        break
print('Всё готово. Ответ находится в answer.txt. Все изображения так же находятся в корневой папке программы(lab2).')