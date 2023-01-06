import flet as ft
import pandas as pd

# Data Base of Endocrine Disrupting Chemicals / 0xDBEDC
# or
# Now I Know My EDCs
#
# DBEDC is
#   - a database of Endocrine Disrupting Chemicals, their health effects, and supporting scientific literature.
#   - compiled from multiple published EDC lists as well as systematic (re)search.
#   - a text-based API that supports plaintext or json formatted queries
#   - fast, small, usable, relevant
#
# DBEDC keys are strings
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
# DBEDC entries are field,value pairs
#   {
#     'key': 'pmid:29126512',
#     'title':'What is an endocrine disruptor?',
#     'journal':'Comptes Rendus Biologies',
#     'date':'21-09-2017',
#     'related':[...],
#     ...
#   }
#
# DBEDC maps keys to entries
#   DBEDC['cid:2519'] -> {'key':'cid:2519', 'related':[], 'formula':'C8H10N4O2', 'name':'caffeine'}
#
# Entries have different sets of fields depending on the Entry type
#
# CHEMINFO
#   {'chem':str, 'related':[str], 'formula':str, 'name':str, ...}
#
# PAPERINFO
#   {'paper':str, 'related':[str], 'title':str, 'journal':str, 'date':str, 'pubtype':str, 'abstract':str, ...}
#
# ENDPOINTINFO
#   {'endpoint':str, 'related':[str], 'desc':str}
#
# DBEDC has 1 main API call and various wrappers
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
# endpoints(keys, field='*) -> fetch(key, field) for key in keys if key in query('ALLENDPOINTS')
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
#     print(f"DBEDC detected {name} ")
#     print(f"{name} is associated with:")
#     [print(f"  {end}" for end in ends]
#     print("You can learn more in these papers")
#     [print(f"  {paper}") for paper in lit]
#
# DB
#
#
#
class NowIKnowMyEDCs:
    def __init__(self):
        self.db = {
            'term': dict(),
        }
    def _dbget(self, key, fmt):
        if fmt == 'str':
            prefix, term = key.split(':')
            prefix = prefix if prefix else 'term'
            return self.db[prefix][term]

    def fetch(self, key, fmt='str'):
        return self._dbget(key, fmt)
    def search(self, key, fmt='str'):
        return self._dbget(key, fmt)




def main(page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your search"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}!"))

    txt_name = ft.TextField(label="Your name")

    page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))


ft.app(target=main)