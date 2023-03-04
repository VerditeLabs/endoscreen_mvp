import csv
import sys
#import cv2
import flet as ft
#import pytesseract
#import numpy as np

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


'''
# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation
def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)


# skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return rotated


# template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
'''






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
                if chem['cid'] == '16211214':
                    print()
                synonyms = chem['synonyms'].split(',') #TODO: redump database with json compliant double quotes
                synonyms = [s.replace(' ','') for s in synonyms]
                synonyms = [s.replace("'",'') for s in synonyms]
                synonyms = [s.replace('"','') for s in synonyms]
                synonyms = [s.replace('[','') for s in synonyms]
                synonyms = [s.replace(']','') for s in synonyms]
                if chem['cid'] == term:
                    ret.append(chem)
                if chem['name'] == term:
                    ret.append(chem)
                if term in synonyms:
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

#edcdb = NowIKnowMyEDCs()
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

    #resulttext = ft.Column(scroll="always")

    def scanocrnow(e):
        page.snack_bar = ft.SnackBar(
            ft.Column([
                ft.Row([
                    ft.Text("please wait...", size=30, weight="bold"),
                    ft.ProgressRing()
                ], alignment="center")
            ], alignment="center"),
            bgcolor="green"
        )
        page.snack_bar.open = True
        page.update()

        # AND GET YOU FILE
        for x in e.files:
            print(x.path)
            #image = cv2.imread(x.path)
            #gray = get_grayscale(image)

            #text = pytesseract.image_to_string(thresholding(gray), lang='eng', config="--psm 12 --oem 3 -c tessedit_char_whitelist=',ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz()/-0123456789 '")
            #pytesseract.image_to_string()
            #pytesseract.
            #text = text.replace('\n',' ')
            text = "asdf qwer sdfg"
            for word in text.split():

                term = 'cid:' + word.lower()
                ret = edcdb.fetch(term)
                if ret and word.lower() == 'borax':

                    print(term,ret[0]['name'])
                    resulttext.controls.append(ft.Text(term + ':' + ret[0]['name'], weight="bold"))

            #resulttext.controls.append(ft.Text(text, weight="bold"))
            page.update()

    def copytext(e):
        # AND COPY TO CLIPBOARD YOU TEXT RESULT
        with open("output.txt", "r") as file:
            text = file.read()
            print(text)
            page.set_clipboard(text)
            page.update()

    # CREATE UPLOAD PICK FILE
    #file_picker = ft.FilePicker(on_result=scanocrnow)

    #page.overlay.append(file_picker)
    '''
    page.add(
        ft.Column([
            ft.Text("Ocr image text to text", size=30, weight="bold"),
            ft.ElevatedButton("Scan Image upload",
                           bgcolor="blue", color="white",
                           on_click=lambda e: file_picker.pick_files()
                           ),

            # AND CREATE COPY ICON FOR COPY TEXT RESULT
            #ft.IconButton(icon="copy", on_click=copytext),
            resulttext

        ])
    )'''


ft.app(target=main)
