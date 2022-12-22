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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()