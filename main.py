import csv
from dialog_ui import *
import requests
from bs4 import BeautifulSoup


tags, rating, votes, anime_type, fin = dialog()
dict_cur = {}
dict_csv = {}

with open('anime.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader: #алгоритм рекомендации конкретного аниме
        cur_tags = list(row[tag_search('Tags', headers)].split(", "))
        rate_csv = row[tag_search('Rating Score', headers)]
        if rate_csv == 'Unknown' or rate_csv == 'Rating Score':
            rate_csv = 0
        else:
             rate_csv = float(row[tag_search('Rating Score', headers)])            
        if rate_csv >= rating:
            rate_cur = 1
        else:
            rate_cur = 0
        votes_csv = row[tag_search('Number Votes', headers)]
        if votes_csv == 'Unknown' or votes_csv == 'Rating Score':
            votes_csv = 0
        else:
            votes_csv = int(row[tag_search('Number Votes', headers)])
        if votes_csv >= votes:
            votes_rs = 1
        else:
            votes_rs = 0
        if row[tag_search('Type', headers)] == anime_type:
            type_rs = 1
        else:
            type_rs = 0
        if fin == 'True':
            fin_rs = 1
        else:
            fin_rs = 0
        res = results(cur_tags, tags, rate_cur, votes_rs, type_rs, fin_rs)
        cur_id = row[tag_search('Anime-PlanetID', headers)]
        dict_cur[cur_id] = res
        name_cur = row[tag_search('Name', headers)]
        url_cur = row[tag_search('Url', headers)]
        dict_csv[cur_id] = name_cur + ':    ' + url_cur
sorted_dict = {}
sorted_keys = sorted(dict_cur, key=dict_cur.get, reverse=True)
for w in sorted_keys:
    sorted_dict[w] = dict_cur[w]
i = 0
f = open('answer.txt', 'w', encoding='utf-8')
for key, value in sorted_dict.items():
    i += 1
    for key_2, value_2 in dict_csv.items():
        if key == key_2:
            ans = str(value_2)
            index_url = ans.index('https:')
            if i <= min(5, len(dict_csv)):
                response = requests.get(ans[index_url:len(ans)])
                soup = BeautifulSoup(response.text,'html.parser')
                img = requests.get("https://www.anime-planet.com/" + soup.find('img', class_='screenshots')['src'])
                img_file = open(str(i) + '.jpg', 'wb')
                img_file.write(img.content)
                img_file.close()
            f.write(ans + '\n')
            break
    if i == 100: #изменять значние, для размера подборки
        break