import csv
import gzip
import json
import time
import os
import orjson

import untangle

from collections import defaultdict
#import easy_entrez
#from easy_entrez.parsing import xml_to_string
import xmltodict
#from xml.etree import ElementTree

exclusion_list = [
    'fish',
    'fishes',
    'zebrafish',
    'zebrafishes',
    'flies',
    'fly',
    'c elegens',
    'c. elegens',
    'mollusk',
    'worm',
    'worms',
    'fruit fly',
    'fruit flies',
    'editorial',
    'biography',
    'clam',
    'silica',
    'flatworm',
    'mixture',
    'nonmammalian',
    'trout',
    'cod',
    'molluscs',
    'yolk',
    'bird',
    'invertebrate',
    'invertebrates',
    'birds',
    'carp',
    'chlorophyll',
    'wastewater',
    'bass',
    'jetlag',
    'catfish',
    'minnow',
    'songbird',
    'mummichog',
    'medaka',
    'quail',
    'dolphin',
    'tilapia',
    'mussel',
    'amphibian',
    'Daphnia',
    'toads',
    'frogs',
    'frog',
    'toad',
    'swordfish',
    'elliptio',
    'mussels',
    'turtles',
    'crustacean',
]

def search_offline_csvs():
    path = '/Users/forrest/pubmed/ftp.ncbi.nlm.nih.gov/pubmed/baseline'
    with open('offline_pubmed_searched.csv','w') as out_f:
        writer = csv.DictWriter(out_f,
                                ['pmid', 'title', 'journal', 'date', 'pubtype', 'abstract', 'chemicals', 'meshterms',
                                 'keywords'])
        writer.writeheader()
        num = 0
        for file in reversed(sorted(os.listdir(path))):
            if not file.endswith('.csv'):
                continue
            with open(os.path.join(path,file),'r') as in_f:
                reader = csv.DictReader(in_f)

                for line in reader:
                    pmid = line['pmid']
                    title = line['title']
                    journal = line['journal']
                    date = line['date']
                    pubtype = line['pubtype']
                    abstract = line['abstract']
                    chemicals = line['chemicals']
                    meshterms = line['meshterms']
                    keywords = line['keywords']

                    searchable = title + abstract + chemicals + keywords + meshterms
                    if 'endocrine' in searchable and 'disrupt' in searchable:
                        for thing in exclusion_list:
                            if thing in searchable:
                                break
                        else:
                            print(pmid)
                            num+=1
                            print(num)
                            writer.writerow(line)


def convert_pubmed_to_json():
    indir='/Users/forrest/pubmed/ftp.ncbi.nlm.nih.gov/pubmed/baseline'
    outdir ='/Users/forrest/pubmed/ftp.ncbi.nlm.nih.gov/pubmed/asjson'
    for file in reversed(sorted(os.listdir(indir))):
        infilepath = os.path.join(indir,file)
        outfilepath = os.path.join(outdir,file).replace('.xml.gz','.json.gz')
        if not file.endswith('.xml.gz'):
            continue
        if os.path.exists(outfilepath):
            continue
        print("converting",infilepath,'to json',outfilepath)
        with gzip.open(infilepath, 'r') as in_f, gzip.open(outfilepath, 'w') as out_f:
            json.dump(xmltodict.parse(in_f),out_f)

def offline_json_search():
    indir = '/Users/forrest/pubmed/ftp.ncbi.nlm.nih.gov/pubmed/asjson'
    for file in reversed(sorted(os.listdir(indir))):
        infilepath = os.path.join(indir, file)
        if not infilepath.endswith('.json.gz'):
            continue
        print('scanning',file)
        with gzip.open(infilepath,'rb') as in_f:
            parsed = orjson.loads(in_f.read())
            for article in parsed['PubmedArticleSet']['PubmedArticle']:

                title = article['MedlineCitation']['Article']['ArticleTitle']
                if isinstance(title,dict):
                    try:
                        title = title['#text']
                    except:
                        title = 'Im too stupid to title my paper correctly'
                if title is None:
                    title = 'Im too stupid to title my paper'
                pmid = article['MedlineCitation']['PMID']['#text']
                journal = article['MedlineCitation']['Article']['Journal']['Title']
                if not isinstance(journal,str):
                    #print()
                    pass
                try:
                    abstract = article['MedlineCitation']['Article']['Abstract']['AbstractText']
                except:
                    abstract = ''
                if isinstance(abstract,list):
                    try:
                        abstract = [thing['#text'] for thing in abstract]
                    except:
                        #if your paper gets then you suck
                        abstract = ''
                    abstract = ','.join(abstract)
                elif isinstance(abstract,dict):
                    try:
                        abstract = abstract['#text']
                    except:
                        abstract = 'I suck at formatting my pubmed entries'
                if abstract is None:
                    abstract = '?????????????'

                try:
                    chemicals = article['MedlineCitation']['ChemicalList']['Chemical']
                except:
                    chemicals = []
                if not isinstance(chemicals, list):
                    chemicals = [chemicals]
                if len(chemicals) > 0 and isinstance(chemicals[0],dict):
                    chemicals = [thing['NameOfSubstance']['#text'] for thing in chemicals]

                try:
                    date = article['MedlineCitation']['DateCompleted']
                except:
                    date = article['MedlineCitation']['DateRevised']
                date = date['Day'] + '-' + date['Month'] + '-' + date['Year']

                try:
                    topics = article['MedlineCitation']['MeshHeadingList']['MeshHeading']
                except:
                    topics = []
                if not isinstance(topics,list):
                    topics = [topics]
                try:
                    topics = [thing['#text'] for thing in topics]
                except:
                    topics = [thing['DescriptorName']['#text'] for thing in topics]

                try:
                    keywords = article['MedlineCitation']['KeywordList']['Keyword']
                except:
                    keywords = []
                if not isinstance(keywords,list):
                    keywords = [keywords]
                try:
                    keywords = [thing['#text'] for thing in keywords]
                except:
                    keywords =[]

                try:
                    pubtype = article['MedlineCitation']['Article']['PublicationTypeList']['PublicationType']
                    if not isinstance(pubtype, list):
                        pubtype = [pubtype]
                    pubtype = [thing['#text'] for thing in pubtype]
                except:
                    pubtype = []


                pubtype = ','.join(pubtype)
                keywords = ','.join(keywords)
                chemicals = ','.join(chemicals)
                topics = ','.join(topics)

                pmid = pmid.encode('ascii','ignore')
                title = title.encode('ascii','ignore')
                journal = journal.encode('ascii','ignore')
                date = date.encode('ascii','ignore')
                pubtype = pubtype.encode('ascii','ignore')
                abstract = abstract.encode('ascii','ignore')
                chemicals = chemicals.encode('ascii','ignore')
                topics = topics.encode('ascii','ignore')
                keywords = keywords.encode('ascii','ignore')

                cited_pmids = set()
                if 'ReferenceList' in article['PubmedData']:
                    if 'Reference' in article['PubmedData']['ReferenceList']:
                        refs = article['PubmedData']['ReferenceList']['Reference']
                        if not isinstance(refs, list):
                            refs = [refs]
                        for ref in refs:
                            if 'ArticleIdList' in ref:
                                if 'ArticleId' in ref['ArticleIdList']:
                                    ids = ref['ArticleIdList']['ArticleId']
                                    if not isinstance(ids,list):
                                        ids = [ids]
                                    for id in ids:
                                        if id['@IdType'] == 'pubmed':
                                            cited_pmids.add(id['#text'])


                searchable = title + abstract + chemicals + keywords + topics
                searchable = searchable.decode('ascii')
                for thing in exclusion_list:
                    if thing in searchable:
                        break
                else:
                    if 'endocrine' in searchable and 'disrupt' in searchable:
                        print(pmid)
                        print(cited_pmids)



def offline_search():
    path='/Users/forrest/pubmed/ftp.ncbi.nlm.nih.gov/pubmed/baseline'
    print(sorted(os.listdir(path)))
    for file in reversed(sorted(os.listdir(path))):
        inpath = os.path.join(path,file)
        outpath = inpath.replace('.xml.gz','.csv')
        if not file.endswith('.xml.gz'):
            continue
        if os.path.exists(outpath):
            continue
        with gzip.open(inpath,'r') as in_f, open(outpath, 'w') as out_f:
            out = []
            print("parsing",file)
            parsed = xmltodict.parse(in_f)

            for article in parsed['PubmedArticleSet']['PubmedArticle']:
                title = article['MedlineCitation']['Article']['ArticleTitle']
                journal = article['MedlineCitation']['Article']['Journal']['Title']
                try:
                    abstract = article['MedlineCitation']['Article']['Abstract']['AbstractText']
                    if not isinstance(abstract,str):
                        print()
                    if abstract is None:
                        abstract = ''
                except:
                    abstract = ''

                try:
                    chemicals = article['MedlineCitation']['ChemicalList']['Chemical']
                    if isinstance(chemicals, dict):
                        chemicals = [chemicals]
                    chemicals = ','.join(chem['NameOfSubstance']['#text'].strip() for chem in chemicals)
                except:
                    chemicals = ''
                pmid = article['MedlineCitation']['PMID']['#text']
                try:
                    date = article['MedlineCitation']['DateCompleted']
                except:
                    try:
                        date = article['MedlineCitation']['DateRevised']
                    except:
                        pass
                date = date['Day'] + '-' + date['Month'] + '-' + date['Year']
                try:
                    topics = article['MedlineCitation']['MeshHeadingList']['MeshHeading']
                    if isinstance(topics,dict):
                        topics = [topics]
                    topics = ','.join(topic['DescriptorName']['#text'].strip() for topic in topics)
                except:
                    topics = ''
                try:
                    keywords = article['MedlineCitation']['KeywordList']['Keyword']
                    keywords = ','.join(word['#text'].strip() for word in keywords)
                except:
                    keywords = ''
                try:
                    publication_type = article['MedlineCitation']['Article']['PublicationTypeList']['PublicationType']
                    if isinstance(publication_type,dict):
                        publication_type = [publication_type]
                    pubtype = ','.join([t['#text'] for t in publication_type])
                except:
                    pubtype = ''
                #print(chemicals,topics,keywords)
                pmid = pmid.encode('ascii','ignore')
                try:
                    title = title.encode('ascii','ignore')
                except:
                    title = ''
                journal = journal.encode('ascii','ignore')
                date = date.encode('ascii','ignore')
                pubtype = pubtype.encode('ascii','ignore')
                try:
                    #todo: looks like some abstracts eist
                    abstract = abstract.encode('ascii','ignore')
                except:
                    abstract = ''
                chemicals = chemicals.encode('ascii','ignore')
                topics = topics.encode('ascii','ignore')
                keywords = keywords.encode('ascii','ignore')
                out.append({'pmid': pmid, 'title': title, 'journal': journal, 'date': date, 'pubtype': pubtype,
                            'abstract': abstract, 'chemicals': chemicals, 'meshterms': topics,
                            'keywords': keywords})
                if 'endocrine' in abstract and 'disrupt' in abstract:
                    print(pmid)
            writer = csv.DictWriter(out_f,['pmid', 'title', 'journal', 'date', 'pubtype', 'abstract', 'chemicals', 'meshterms','keywords'])
            writer.writeheader()
            writer.writerows(out)


def cas_to_cid():
    import easy_entrez

    from easy_entrez.parsing import xml_to_string
    all_cids = set()
    leftover_cas = set()
    entrez_api = easy_entrez.EntrezAPI(
        'endoscreen',
        'verditelabs@gmail.com',
        # optional
        return_type='json'
    )
    import time
    for cas in all_cas:
        time.sleep(.1)
        chem = entrez_api.search(cas, max_results = 10, database='pccompound')
        cid = chem.data['esearchresult']['idlist']
        if len(cid) == 0:
            leftover_cas.add(cas)
        else:
            all_cids.update(cid)
        print(cas,cid)
    print("all cids", all_cids)
    print("leftover cids", leftover_cas)

def find_lit2():
    import easy_entrez
    from easy_entrez.parsing import xml_to_string
    import xmltodict
    entrez_api = easy_entrez.EntrezAPI('endoscreen','verditelabs@gmail.com',return_type='json')
    search_term = ''
    res = entrez_api.search(search_term, max_results=99999, database='pubmed')
    print("found this many articles",len(res.data['esearchresult']['idlist']))
    fetched = entrez_api.fetch(res.data['esearchresult']['idlist'], max_results=1000, database='pubmed')
    parsed = xmltodict.parse(xml_to_string(fetched.data))

    print(res)


def find_literature():
    import easy_entrez
    from easy_entrez.parsing import xml_to_string
    import xmltodict
    entrez_api = easy_entrez.EntrezAPI(
        'endoscreen',
        'verditelabs@gmail.com',
        # optional
        return_type='json'
    )
    from collections import defaultdict
    out = defaultdict(list)
    fetched_out = defaultdict(list)
    with open('all_common_names.txt', 'r') as f:
        for line in f:
            name = line.strip()
            #names are crazy, let's keep to more common stuff
            if '(' in name or ',' in name:
                continue
            time.sleep(1)
            res = entrez_api.search(name + ' AND endocrine', max_results=100, database='pubmed')
            if res.data['esearchresult']['count'] == '0':
                continue
            #summary = entrez_api.summarize(res.data['esearchresult']['idlist'], max_results = 100)
            fetched = entrez_api.fetch(res.data['esearchresult']['idlist'], max_results = 100, database='pubmed')
            parsed = xmltodict.parse(xml_to_string(fetched.data))
            print(name,"got",len(parsed['PubmedArticleSet']['PubmedArticle']),'hits')
            fetched_out[name] = parsed['PubmedArticleSet']['PubmedArticle']
    import json
    with open('name_to_pmids_summary.json', 'w') as f:
        f.write(json.dumps(out))
    with open('name_to_fetched_data.json','w') as f:
        json.dump(fetched_out,f)

def contains_lowercase(s):
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            return True
    return False

def get_common_names():
    import pubchempy as pcp
    all_names = set()
    with open('all_cids2.txt','r') as f:
        for line in f:
            line = line.strip().replace('CID:','')
            cid = int(line)
            chem = pcp.Compound.from_cid(cid)
            print(chem.iupac_name)
            all_names.add(chem.iupac_name)
    print("all names",all_names)

def process_manual_search():
    import csv
    all_pmids = set()
    out = list()

    journals = defaultdict(lambda: 0)
    with open('manual_pubmed_search.csv','r') as f:
        for line in csv.DictReader(f):
            if line['PMID'] in all_pmids:
                continue
            all_pmids.add(line['PMID'])
            print(line)
            pmid, title, journal, date = line['PMID'],line['Title'],line['Journal/Book'],line['Create Date']
            journals[journal] += 1
            out.append([pmid,title,journal,date])

    print("num pmids",len(all_pmids))
    with open('manual_processed_summary.csv','w') as f:
        fieldnames = ['pmid', 'title','journal','date']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for line in out:
            writer.writerow({'pmid':line[0],'title':line[1],'journal':line[2],'date':line[3]})
    for k,v in reversed(sorted(journals.items(),key= lambda item: item[1])):
        print(k,v)
    print("wrote rows")
    print("num journals",len(journals))


def sanitize_synonyms():
    # synonyms be crazy, let's process them some
    banned_terms = [
        '[', ']', '%','>','=','<',';','{','}' #filter out weird punctuation stuff
        'CAS','CCRIS','CHEBI','CHEMBL','DSSTox','NCGC','NSC','NCI', # other identifiers?
        'Caswell','MLS','MFCD','STL','Tox','bmse','EINECS','ENT','ZINC',
        'UNII','VS-','WLN','BDBM','CCG','CS','_',
        'British','European','antibiotic','KBio','BPBio','Spectrum',
        'Prestwick','component','reference','ampule','injectable',
        'reagent','powder','tested','mg/mL','FEMA','BSPBio','United States','mixture',
        '(VAN)','(1:1)','/mL','byproduct','EPA','Standard','(TN)','german','indicator',
        'biological','Commission','Pesticide','RCRA','(R)','TraceCERT','(alpha)','(INN)',
        '.beta.','.alpha.','diameter','length','elemental','metallic','g/g','/','GRADE',
        'Nanopowder','Dispersion','Powder','dia','unpurified','#','ACon','Lopac','MEGxp',
        'Biomo','KBio','(TBB)','Reference','Handbook','Epitope','Rcra'
    ]

    names = None
    processed_names = dict()
    with open('cid_synonym_map.json','r') as f:
        names = json.load(f)
    for k,v in names.items():
        keep = set()
        for synonym in v:
            asdf = [term in synonym for term in banned_terms]
            if any(term in synonym for term in banned_terms):
                continue
            if not contains_lowercase(synonym):
                continue
            keep.add(synonym)
        processed_names[k] = sorted(list(keep))
    with open('processed_synonyms.json','w') as f:
        json.dump(processed_names,f)


my_list = ['geeks', 'for', 'geeks', 'like',
           'geeky', 'nerdy', 'geek', 'love',
           'questions', 'words', 'life']


def chunkify(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]



def parse_pubmed():
    entrez_api = easy_entrez.EntrezAPI(
        'endoscreen',
        'verditelabs@gmail.com',
        # optional
        return_type='json'
    )
    chem_occurrances = defaultdict(lambda: 0)
    mesh_occurrances = defaultdict(lambda: 0)
    keyword_occurrances = defaultdict(lambda: 0)
    out = list()
    with open('manual_processed_summary.csv','r') as f:
        reader = csv.DictReader(f)
        iter = 0
        for batch in chunkify(list(reader),100):
            print("num processed",iter)
            iter+=1
            if iter>10:
                pass
            time.sleep(.3)
            pmids = [i['pmid'] for i in batch]
            fetched = entrez_api.fetch(pmids, max_results=100, database='pubmed')
            parsed = xmltodict.parse(xml_to_string(fetched.data))
            for article in parsed['PubmedArticleSet']['PubmedArticle']:
                try:
                    title = article['MedlineCitation']['Article']['ArticleTitle']
                    journal = article['MedlineCitation']['Article']['Journal']['Title']
                    abstract = article['MedlineCitation']['Article']['Abstract']['AbstractText']
                    chemicals = article['MedlineCitation']['ChemicalList']['Chemical']
                    pmid = article['MedlineCitation']['PMID']['#text']

                    date = article['MedlineCitation']['DateCompleted']
                    date = date['Day'] + '-' + date['Month'] + '-' + date['Year']
                    if isinstance(chemicals,dict):
                        chemicals = [chemicals]
                    chemicals = ','.join(chem['NameOfSubstance']['#text'].strip() for chem in chemicals)
                    topics = article['MedlineCitation']['MeshHeadingList']['MeshHeading']
                    topics = ','.join(topic['DescriptorName']['#text'].strip() for topic in topics)
                    keywords = article['MedlineCitation']['KeywordList']['Keyword']
                    keywords = ','.join(word['#text'].strip() for word in keywords)
                    publication_type = article['MedlineCitation']['Article']['PublicationTypeList']['PublicationType']
                    pubtype = ','.join([t['#text'] for t in publication_type])
                    #print(chemicals,topics,keywords)
                    out.append({'pmid':pmid,'title':title,'journal':journal,'date':date,'pubtype':pubtype,'abstract':abstract,'chemicals':chemicals,'meshterms':topics,'keywords':keywords})
                    #print(out)
                except:
                    pass
    with open('out_summary.csv','w') as f:
        writer = csv.DictWriter(f,['pmid','title','journal','date','pubtype','abstract','chemicals','meshterms','keywords'])
        writer.writeheader()
        writer.writerows(out)


#cas_to_cid()
#get_common_names()
#find_literature()
#sanitize_synonyms()
#find_lit2()
#process_manual_search()
#parse_pubmed()
#offline_search()
search_offline_csvs()
#convert_pubmed_to_json()
#offline_json_search()