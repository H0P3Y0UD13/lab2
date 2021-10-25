import csv

print("Что?")
s = input()
print(s)
with open("anime.csv", "r", encoding='utf-8') as file:
    reader = csv.reader(file)
    for line in reader:
        print(line[1])