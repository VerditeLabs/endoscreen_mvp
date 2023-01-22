import csv
import os
import json
import sys

import flet as ft

# Endocrine Disrupting Chemicals DataBase / 0xEDCDB
# or
# Now I Know My EDCs
#
# EDCDB is
#   - a database of Endocrine Disrupting Chemicals, their health effects, and supporting scientific literature.
#   - compiled from multiple published EDC lists as well as systematic (re)search.
#   - a text-based API that supports plaintext or json formatted queries
#   - fast, small, usable, relevant
#
# EDCDB keys are strings
#   [
#     "cid:2519",
#     "endocrine disruptor",
#     'rat",
#     "bpa",
#     "bisphenol a",
#     'cas:58-08-2',
#     'doi:10.1016',
#     'pmid:29126512',
#     'cid:2519',
#     'edc',
#     'caffeine',
#     'rat',
#     ...
#   ]
#
# UPPERCASE keys for special keys
#   [
#     "DEDUCT2DB",
#     "TEDXDB",
#     ...
#   ]
#
# EDCDB entries are field,value pairs
#   {
#     'key': 'pmid:29126512',
#     'title':'What is an endocrine disruptor?',
#     'journal':'Comptes Rendus Biologies',
#     'date':'21-09-2017',
#     'related':[...],
#     ...
#   }
#
# EDCDB maps keys to entries
#   EDCDB['cid:2519'] -> {'key':'cid:2519', 'related':[], 'formula':'C8H10N4O2', 'name':'caffeine'}
#
# Entries have different sets of fields depending on the Entry type
#
# CHEMINFO
#   {'chem':str, 'related':[str], 'formula':str, 'name':str, ...}
#
# PAPERINFO
#   {'paper':str, 'related':[str], 'title':str, 'journal':str, 'date':str, 'pubtype':str, 'abstract':str, ...}
#
#
# EDCDB has 1 main API call and various wrappers
# fetch(key, field='*')
#   - returns INFO[field]
#     fetch("pmid:29126512") ->
#       {
#         'key': 'pmid:29126512',
#         'title':'What is an endocrine disruptor?',
#         'journal':'Comptes Rendus Biologies',
#         'date':'21-09-2017',
#         ...
#       }
#    fetch("pmid:29126512",field='date') ->
#      {
#        'date':'21-09-2017'
#      }
#
# query(key) -> fetch(key, field='related')
# chems(keys, field='*) -> fetch(key, field) for key in keys if key in query('ALLCHEMS')
# papers(keys, field='*) -> fetch(key, field) for key in keys if key in query('ALLPAPERS')
#
# How Do I...?
#   - get all deduct 2 chems?
#       query('DEDUCT2DB')
#   - get all entries for all deduct 2 chems?
#       fetch(t) for t in query('DEDUCT2DB')
#   - follow a workflow?
#
# def do_search(ingredients:[str]):
#   edcs = chems(ingredients)
#   if len(edcs) == 0:
#     return [] # no edcs
#   for edc in edcs:
#     name = edc['name']
#     ends = endpoints(edc['related'], field='desc')
#     lit = papers(edc['related'],field=['key','title'])
#
#     print(f"EDCDB detected {name} ")
#     print(f"{name} is associated with:")
#     [print(f"  {end}" for end in ends]
#     print("You can learn more in these papers")
#     [print(f"  {paper}") for paper in lit]
#
#

def get_size(obj, seen=None):
    """Recursively finds size of objects"""

    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()

    obj_id = id(obj)
    if obj_id in seen:
        return 0

    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)

    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, ( str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])

    return size

class NowIKnowMyEDCs:
    def __init__(self):
        with open('./edcdb_papers.csv', 'r') as f:
            reader = csv.DictReader(f)
            self.papers = []
            for line in reader:
                self.papers.append(line)
        with open('./edcdb_chems.csv', 'r') as f:
            reader = csv.DictReader(f)
            self.chems = []
            for line in reader:
                self.chems.append(line)
            print(get_size(self.papers))
            print(get_size(self.chems))

    def _dbget(self, key, field, fmt):
        #todo: support fmt
        try:
            prefix, term = key.split(':')
        except:
            return []
        ret = []
        if prefix == 'cid': #todo: support other chem identifiers
            for chem in self.chems:
                if chem['cid'] == term:
                    ret.append(chem)
        elif prefix == 'pubmed':
            for paper in self.papers:
                if key in paper['ids']:
                    ret.append(paper)
        elif prefix == 'term':
            for paper in self.papers:
                for k,v in paper.items():
                    if term in v:
                        ret.append(paper['ids'])
            for chem in self.chems:
                for k, v in chem.items():
                    if v is None:
                        continue
                    if term in v:
                        ret.append(chem['cid'])
        else:
            raise #todo: support more stuff
        if field == '*':
            if ret:
                return ret
            return []
        else:
            raise #todo: support this

    def fetch(self, key, field='*', fmt='json'):
        return self._dbget(key, field, fmt)

edcdb = NowIKnowMyEDCs()
def main(page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your search"
            page.update()
        else:
            search = txt_name.value
            ret = edcdb.fetch(search)
            lv = ft.ListView(expand=True, spacing=20)
            page.add(lv)
            for i, thing in enumerate(ret):
                lv.controls.append(ft.Text(f"{thing}"))
                if i % 50 == 0:
                    page.update()
            page.update()

    txt_name = ft.TextField(label="Your search")
    page.add(txt_name, ft.ElevatedButton(f"search!", on_click=btn_click))


ft.app(target=main)
