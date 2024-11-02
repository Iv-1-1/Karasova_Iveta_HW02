import json
import pandas as pd

file = 'netflix_titles.tsv'

netflix_read = pd.read_csv(file, sep="\t", usecols=["PRIMARYTITLE", "DIRECTOR", "CAST", "GENRES", "STARTYEAR" ])
data_list = []

for x in range(len(netflix_read)):
    primarytitle = {
        "title": netflix_read["PRIMARYTITLE"][x],
        "directors": [netflix_read["DIRECTOR"].fillna("")[x]],
        "cast": [netflix_read["CAST"][x]],
        "genres": [netflix_read["GENRES"][x]],
        "decade": str(netflix_read["STARTYEAR"][x]//10*10)
    }
    data_list.append(primarytitle)

with open('hw02_output.json.', mode='w', encoding='utf-8') as text_write:
    json.dump(data_list, text_write, ensure_ascii=False, indent=4)
