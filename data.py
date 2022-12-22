import csv
from collections import defaultdict

import pubchempy as pcp
import json
import pandas as pd
cid_synonym_map = dict()



def get_all_synonyms(write=False):
    for cid in sorted(UNIQUE_CIDS):
        chem = pcp.Compound.from_cid(cid)
        synonyms = sorted(chem.synonyms)
        print(cid,synonyms)
        cid_synonym_map[cid] = synonyms
    if write:
        with open('cid_synonym_map.json', 'w') as out:
            out.write(json.dumps(cid_synonym_map, indent=2))
        print(cid_synonym_map)

def read_all_synonyms():
    with open('cid_synonym_map.json','r') as f:
        asdff = json.load(f)
    print(asdff)

def output_excel_for_scrubs():
    with open('cid_synonym_map.json','r') as f:
        asdff = json.load(f)
    dumb = dict()
    for k,v in asdff.items():
        dumb[k] = '\t'.join(v)
    df = pd.DataFrame(asdff.items(), columns=['cid','synonyms'])
    df.to_excel('./excel_sucks.xlsx')

def database_stats():
    all_cids = set()
    all_pmids = set()
    all_names = set()
    all_endpoints = set()
    all_systems = set()

    cid_to_pmids = defaultdict(set)
    cid_to_name = dict()
    cid_to_endpoints = defaultdict(set)

    with open('database.csv','r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cid = row['Primary identifier']
            name = row['Name']
            pmid = row['Literature identifier']
            endpoint = row['Endocrine-mediated endpoints']
            system = row['Endocrine mediated systems']
            all_cids.add(cid)
            all_pmids.add(pmid)
            all_names.add(name)
            all_endpoints.add(endpoint)
            all_systems.add(system)
            cid_to_pmids[cid].add(pmid)
            cid_to_endpoints[cid].add(endpoint)
            cid_to_name[cid] = name

    print("num chems",len(all_cids))
    print("num studies",len(all_pmids))
    print("num endpoints",len(all_endpoints))
    print("num systems",len(all_systems))
    #chems with the most unique studies
    asdf = reversed(sorted(cid_to_pmids.items(), key= lambda x: len(x[1]))) #print(row)
    print("\nmost studied ECDs\n")
    for k,v in asdf:
        print(cid_to_name[k], len(v))

    print("\nEDCs that affect the most things\n")
    asdf = reversed(sorted(cid_to_endpoints.items(), key=lambda x: len(x[1])))  # print(row)
    for k, v in asdf:
        print(cid_to_name[k], len(v))



#get_all_synonyms()
#read_all_synonyms()
#output_excel_for_scrubs()
database_stats()