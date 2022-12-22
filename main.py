import csv

from collections import defaultdict

# CSV header
# ~~~~~~~~~
# Primary identifier # unique chemical name e.g. CID:6623
# Name # common name e.g. Bisphenol A
# Literature identifier # link to specific study PMID:20813173
# Study type # ?
# Endocrine-mediated endpoints # bad thing it does
# Endocrine mediated systems # ? high level category for what system is disrupted
#
# Primary Identifier <> Name

def main():
    id_name_map = dict()
    ids = set()
    names = set()
    name_lit_map = defaultdict(set)
    with open('database.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            print(row)
            name, id, lit = row['Name'],row['Primary identifier'],row['Literature identifier']
            ids.add(id)
            names.add(name)
            id_name_map[id] = name
            name_lit_map[name].add(lit)
        print('\n'.join(sorted(names)))
        print("preprocessed names")

def scrape():
    import pandas as pd
    from bs4 import BeautifulSoup
    import requests
    import time
    import random
    for ingr in sanitized_ingredients:
        time.sleep(random.randrange(1, 10) / 10 + 1)
        #print("trying",ingr)
        f = requests.get("https://incidecoder.com/ingredients/" + ingr)
        soup = BeautifulSoup(f.text)
        import re
        txt = soup.get_text()
        txt = re.sub(r"\s+", ' ', txt)
        if 'this page does not seem' in txt:
            #print(ingr," not found")
            continue
        else:
            print(ingr)
            #print(soup.get_text())




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    #scrape()