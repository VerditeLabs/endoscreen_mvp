import flet as ft
import json
import io

from google.cloud import vision

client = vision.ImageAnnotatorClient()



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

class NowIKnowMyEDCs:
    def __init__(self):
        with open('./edcdb.json', 'r') as f:
            with open('edcdb.json', 'r') as f:
                self.papers, self.chems = json.load(f)

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
                if chem['name'] == term:
                    ret.append(chem)
                if term in chem['synonyms']:
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

    resulttext = ft.Column(scroll="always")

    def scanocrnow(e):
        page.snack_bar = ft.SnackBar(
            ft.Column([
                ft.Row([
                    ft.Text("please wait..."),
                    ft.ProgressRing()
                ])
            ]),
            bgcolor="green"
        )
        page.snack_bar.open = True
        page.update()

        # AND GET YOU FILE
        for x in e.files:
            print(x.path)

            with io.open(x.path, 'rb') as f:
                content = f.read()
            image = vision.Image(content=content)
            response = client.text_detection(image=image)
            texts = response.text_annotations

            text = ' '.join(t.description for t in texts)
            text = text.replace('\n',' ')
            resulttext.controls.append(ft.Text("detected text: " + text))

            #for word in text.split():
            #    term = 'cid:' + word.lower()
            #    ret = edcdb.fetch(term)
            #    if ret and word.lower() == 'borax':

            #        print(term,ret[0]['name'])
            #        resulttext.controls.append(ft.Text(term + ':' + ret[0]['name']))

            page.update()

    file_picker = ft.FilePicker(on_result=scanocrnow)

    page.overlay.append(file_picker)

    page.add(
        ft.Column([
            ft.Text("Detect EDC from image"),
            ft.ElevatedButton("Image upload", on_click=lambda e: file_picker.pick_files()),
            resulttext
        ])
    )

if __name__ == '__main__':
    ft.app(target=main, host='0.0.0.0', port=8080)
