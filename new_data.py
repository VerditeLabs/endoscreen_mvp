import csv
import gzip
import json
import time
import os

from collections import defaultdict
import easy_entrez
from easy_entrez.parsing import xml_to_string
import xmltodict
import pubchempy as pcp

from raw_data import DEDUCT_FINAL_PAPERS


from easy_entrez.parsing import xml_to_string
from raw_data import ALL_PAPERS, ALL_CHEMS_CAS, HIGH_SCORE_TERMS, LOW_SCORE_TERMS
import sqlite3
import easy_entrez
import pprint
import json


def get_pubmed_data(article):
    title = article['MedlineCitation']['Article']['ArticleTitle']
    if isinstance(title, dict):
        try:
            title = title['#text']
        except:
            title = 'Im too stupid to title my paper correctly'
    if title is None:
        title = 'Im too stupid to title my paper'
    pmid = article['MedlineCitation']['PMID']['#text']
    journal = article['MedlineCitation']['Article']['Journal']['Title']
    if not isinstance(journal, str):
        # print()
        pass
    try:
        abstract = article['MedlineCitation']['Article']['Abstract']['AbstractText']
    except:
        abstract = ''
    if isinstance(abstract, list):
        try:
            abstract = [thing['#text'] for thing in abstract]
        except:
            # if your paper gets then you suck
            abstract = ''
        abstract = ','.join(abstract)
    elif isinstance(abstract, dict):
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
    if len(chemicals) > 0 and isinstance(chemicals[0], dict):
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
    if not isinstance(topics, list):
        topics = [topics]
    try:
        topics = [thing['#text'] for thing in topics]
    except:
        topics = [thing['DescriptorName']['#text'] for thing in topics]

    try:
        keywords = article['MedlineCitation']['KeywordList']['Keyword']
    except:
        keywords = []
    if not isinstance(keywords, list):
        keywords = [keywords]
    try:
        keywords = [thing['#text'] for thing in keywords]
    except:
        keywords = []

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

    # pmid = pmid.decode('ascii', 'ignore')
    # title = title.decode('ascii', 'ignore')
    # journal = journal.decode('ascii', 'ignore')
    # date = date.decode('ascii', 'ignore')
    # pubtype = pubtype.decode('ascii', 'ignore')
    # abstract = abstract.decode('ascii', 'ignore')
    # chemicals = chemicals.decode('ascii', 'ignore')
    # topics = topics.decode('ascii', 'ignore')
    # keywords = keywords.encode('ascii', 'ignore')

    return pmid, title, journal, date, pubtype, abstract, chemicals, topics, keywords


def get_offline_articles_from_csv():
    indir = '/Users/forrest/pubmed/ftp.ncbi.nlm.nih.gov/pubmed/baseline'
    for file in reversed(sorted(os.listdir(indir))):
        infilepath = os.path.join(indir, file)
        if not file.endswith('.csv'):
            continue
        with open(infilepath, 'r') as f:
            reader = csv.DictReader(f)
            for line in reader:
                yield line


def get_offline_articles():
    indir = '/Users/forrest/pubmed/ftp.ncbi.nlm.nih.gov/pubmed/asjson'
    for file in reversed(sorted(os.listdir(indir))):
        infilepath = os.path.join(indir, file)
        if not infilepath.endswith('.json.gz'):
            continue
        with gzip.open(infilepath, 'r') as in_f:
            parsed = json.load(in_f)
            for article in parsed['PubmedArticleSet']['PubmedArticle']:
                yield article


def search_offline_csvs():
    path = '/Users/forrest/pubmed/ftp.ncbi.nlm.nih.gov/pubmed/baseline'
    with open('offline_pubmed_searched.csv', 'w') as out_f:
        writer = csv.DictWriter(out_f,
                                ['pmid', 'title', 'journal', 'date', 'pubtype', 'abstract', 'chemicals', 'meshterms',
                                 'keywords'])
        writer.writeheader()
        num = 0
        for file in reversed(sorted(os.listdir(path))):
            if not file.endswith('.csv'):
                continue
            with open(os.path.join(path, file), 'r') as in_f:
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
                            num += 1
                            print(num)
                            writer.writerow(line)


def convert_pubmed_to_json():
    indir = '/Users/forrest/pubmed/ftp.ncbi.nlm.nih.gov/pubmed/baseline'
    outdir = '/Users/forrest/pubmed/ftp.ncbi.nlm.nih.gov/pubmed/asjson'
    for file in reversed(sorted(os.listdir(indir))):
        infilepath = os.path.join(indir, file)
        outfilepath = os.path.join(outdir, file).replace('.xml.gz', '.json.gz')
        if not file.endswith('.xml.gz'):
            continue
        if os.path.exists(outfilepath):
            continue
        print("converting", infilepath, 'to json', outfilepath)
        with gzip.open(infilepath, 'r') as in_f, gzip.open(outfilepath, 'w') as out_f:
            json.dump(xmltodict.parse(in_f), out_f)


def offline_json_search():
    indir = '/Users/forrest/pubmed/ftp.ncbi.nlm.nih.gov/pubmed/asjson'
    for file in reversed(sorted(os.listdir(indir))):
        infilepath = os.path.join(indir, file)
        if not infilepath.endswith('.json.gz'):
            continue
        print('scanning', file)
        with gzip.open(infilepath, 'rb') as in_f:
            parsed = json.loads(in_f.read())
            for article in parsed['PubmedArticleSet']['PubmedArticle']:

                pmid, title, journal, date, pubtype, abstract, chemicals, topics, keywords = get_pubmed_data(article)

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
                                    if not isinstance(ids, list):
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
    path = '/Users/forrest/pubmed/ftp.ncbi.nlm.nih.gov/pubmed/baseline'
    print(sorted(os.listdir(path)))
    for file in reversed(sorted(os.listdir(path))):
        inpath = os.path.join(path, file)
        outpath = inpath.replace('.xml.gz', '.csv')
        if not file.endswith('.xml.gz'):
            continue
        if os.path.exists(outpath):
            continue
        with gzip.open(inpath, 'r') as in_f, open(outpath, 'w') as out_f:
            out = []
            print("parsing", file)
            parsed = xmltodict.parse(in_f)

            for article in parsed['PubmedArticleSet']['PubmedArticle']:
                title = article['MedlineCitation']['Article']['ArticleTitle']
                journal = article['MedlineCitation']['Article']['Journal']['Title']
                try:
                    abstract = article['MedlineCitation']['Article']['Abstract']['AbstractText']
                    if not isinstance(abstract, str):
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
                    if isinstance(topics, dict):
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
                    if isinstance(publication_type, dict):
                        publication_type = [publication_type]
                    pubtype = ','.join([t['#text'] for t in publication_type])
                except:
                    pubtype = ''
                # print(chemicals,topics,keywords)
                pmid = pmid.encode('ascii', 'ignore')
                try:
                    title = title.encode('ascii', 'ignore')
                except:
                    title = ''
                journal = journal.encode('ascii', 'ignore')
                date = date.encode('ascii', 'ignore')
                pubtype = pubtype.encode('ascii', 'ignore')
                try:
                    # todo: looks like some abstracts eist
                    abstract = abstract.encode('ascii', 'ignore')
                except:
                    abstract = ''
                chemicals = chemicals.encode('ascii', 'ignore')
                topics = topics.encode('ascii', 'ignore')
                keywords = keywords.encode('ascii', 'ignore')
                out.append({'pmid': pmid, 'title': title, 'journal': journal, 'date': date, 'pubtype': pubtype,
                            'abstract': abstract, 'chemicals': chemicals, 'meshterms': topics,
                            'keywords': keywords})
                if 'endocrine' in abstract and 'disrupt' in abstract:
                    print(pmid)
            writer = csv.DictWriter(out_f, ['pmid', 'title', 'journal', 'date', 'pubtype', 'abstract', 'chemicals',
                                            'meshterms', 'keywords'])
            writer.writeheader()
            writer.writerows(out)


def cas_to_cid():
    import easy_entrez
    from raw_data import ALL_CHEMS_CAS
    from easy_entrez.parsing import xml_to_string
    all_cids = set()
    leftover_cas = set()
    entrez_api = easy_entrez.EntrezAPI(
        'endoscreen',
        'contact@endoscreen.org',
        # optional
        return_type='json'
    )
    import time
    for cas in ALL_CHEMS_CAS:
        try:
            time.sleep(.5)
            chem = entrez_api.search(cas.replace('CAS:', ''), max_results=10, database='pccompound')
            cid = chem.data['esearchresult']['idlist']
            if len(cid) == 0:
                leftover_cas.add(cas)
            else:
                all_cids.update(cid)
            print(all_cids)
        except:
            print("failed during", cas)
    print("all cids", all_cids)
    print("leftover cids", leftover_cas)


def find_lit2():
    import easy_entrez
    from easy_entrez.parsing import xml_to_string
    import xmltodict
    entrez_api = easy_entrez.EntrezAPI('endoscreen', 'verditelabs@gmail.com', return_type='json')
    search_term = ''
    res = entrez_api.search(search_term, max_results=99999, database='pubmed')
    print("found this many articles", len(res.data['esearchresult']['idlist']))
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
            # names are crazy, let's keep to more common stuff
            if '(' in name or ',' in name:
                continue
            time.sleep(1)
            res = entrez_api.search(name + ' AND endocrine', max_results=100, database='pubmed')
            if res.data['esearchresult']['count'] == '0':
                continue
            # summary = entrez_api.summarize(res.data['esearchresult']['idlist'], max_results = 100)
            fetched = entrez_api.fetch(res.data['esearchresult']['idlist'], max_results=100, database='pubmed')
            parsed = xmltodict.parse(xml_to_string(fetched.data))
            print(name, "got", len(parsed['PubmedArticleSet']['PubmedArticle']), 'hits')
            fetched_out[name] = parsed['PubmedArticleSet']['PubmedArticle']
    import json
    with open('name_to_pmids_summary.json', 'w') as f:
        f.write(json.dumps(out))
    with open('name_to_fetched_data.json', 'w') as f:
        json.dump(fetched_out, f)


def contains_lowercase(s):
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            return True
    return False


def get_common_names():
    import pubchempy as pcp
    all_names = set()
    with open('all_cids2.txt', 'r') as f:
        for line in f:
            line = line.strip().replace('CID:', '')
            cid = int(line)
            chem = pcp.Compound.from_cid(cid)
            print(chem.iupac_name)
            all_names.add(chem.iupac_name)
    print("all names", all_names)


def process_manual_search():
    import csv
    all_pmids = set()
    out = list()

    journals = defaultdict(lambda: 0)
    with open('manual_pubmed_search.csv', 'r') as f:
        for line in csv.DictReader(f):
            if line['PMID'] in all_pmids:
                continue
            all_pmids.add(line['PMID'])
            print(line)
            pmid, title, journal, date = line['PMID'], line['Title'], line['Journal/Book'], line['Create Date']
            journals[journal] += 1
            out.append([pmid, title, journal, date])

    print("num pmids", len(all_pmids))
    with open('manual_processed_summary.csv', 'w') as f:
        fieldnames = ['pmid', 'title', 'journal', 'date']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for line in out:
            writer.writerow({'pmid': line[0], 'title': line[1], 'journal': line[2], 'date': line[3]})
    for k, v in reversed(sorted(journals.items(), key=lambda item: item[1])):
        print(k, v)
    print("wrote rows")
    print("num journals", len(journals))


def sanitize_synonyms():
    # synonyms be crazy, let's process them some
    banned_terms = [
        '[', ']', '%', '>', '=', '<', ';', '{', '}'  # filter out weird punctuation stuff
                                                'CAS', 'CCRIS', 'CHEBI', 'CHEMBL', 'DSSTox', 'NCGC', 'NSC', 'NCI',
        # other identifiers?
        'Caswell', 'MLS', 'MFCD', 'STL', 'Tox', 'bmse', 'EINECS', 'ENT', 'ZINC',
        'UNII', 'VS-', 'WLN', 'BDBM', 'CCG', 'CS', '_',
        'British', 'European', 'antibiotic', 'KBio', 'BPBio', 'Spectrum',
        'Prestwick', 'component', 'reference', 'ampule', 'injectable',
        'reagent', 'powder', 'tested', 'mg/mL', 'FEMA', 'BSPBio', 'United States', 'mixture',
        '(VAN)', '(1:1)', '/mL', 'byproduct', 'EPA', 'Standard', '(TN)', 'german', 'indicator',
        'biological', 'Commission', 'Pesticide', 'RCRA', '(R)', 'TraceCERT', '(alpha)', '(INN)',
        '.beta.', '.alpha.', 'diameter', 'length', 'elemental', 'metallic', 'g/g', '/', 'GRADE',
        'Nanopowder', 'Dispersion', 'Powder', 'dia', 'unpurified', '#', 'ACon', 'Lopac', 'MEGxp',
        'Biomo', 'KBio', '(TBB)', 'Reference', 'Handbook', 'Epitope', 'Rcra'
    ]

    names = None
    processed_names = dict()
    with open('cid_synonym_map.json', 'r') as f:
        names = json.load(f)
    for k, v in names.items():
        keep = set()
        for synonym in v:
            asdf = [term in synonym for term in banned_terms]
            if any(term in synonym for term in banned_terms):
                continue
            if not contains_lowercase(synonym):
                continue
            keep.add(synonym)
        processed_names[k] = sorted(list(keep))
    with open('processed_synonyms.json', 'w') as f:
        json.dump(processed_names, f)


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
    with open('manual_processed_summary.csv', 'r') as f:
        reader = csv.DictReader(f)
        iter = 0
        for batch in chunkify(list(reader), 100):
            print("num processed", iter)
            iter += 1
            if iter > 10:
                pass
            time.sleep(.3)
            pmids = [i['pmid'] for i in batch]
            fetched = entrez_api.fetch(pmids, max_results=100, database='pubmed')
            parsed = xmltodict.parse(xml_to_string(fetched.data))
            for article in parsed['PubmedArticleSet']['PubmedArticle']:
                try:
                    citation = article['MedlineCitation']

                    title = citation['Article']['ArticleTitle']
                    journal = citation['Article']['Journal']['Title']
                    abstract = citation['Article']['Abstract']['AbstractText']
                    chemicals = citation['ChemicalList']['Chemical']
                    pmid = citation['PMID']['#text']
                    meshterms = citation['MeshHeadingList']['MeshHeading']
                    keywords = citation['KeywordList']['Keyword']
                    pubtype = citation['Article']['PublicationTypeList']['PublicationType']
                    date = citation['DateCompleted']

                    date = date['Day'] + '-' + date['Month'] + '-' + date['Year']
                    chemicals = ','.join(t['NameOfSubstance']['#text'] for t in chemicals)
                    meshterms = ','.join(t['DescriptorName']['#text'] for t in meshterms)
                    keywords = ','.join(t['#text'] for t in keywords)
                    pubtype = ','.join(t['#text'] for t in pubtype)

                    out.append({'pmid': pmid,
                                'title': title,
                                'journal': journal,
                                'date': date,
                                'pubtype': pubtype,
                                'abstract': abstract,
                                'chemicals': chemicals,
                                'meshterms': meshterms,
                                'keywords': keywords})

                except:
                    pass
    with open('out_summary.csv', 'w') as f:
        writer = csv.DictWriter(f, ['pmid', 'title', 'journal', 'date', 'pubtype', 'abstract', 'chemicals', 'meshterms',
                                    'keywords'])
        writer.writeheader()
        writer.writerows(out)

def analyze_frequency(s: str):
    import string
    from raw_data import MOST_COMMON_WORDS
    # returns a filtered word frequency for s

    # preprocess s
    s = s.lower()
    # TODO: collapse some punctuated terms, e.g. anti-estrogenic, in-vivo
    # into single words so that they aren't split into 2 words

    # remove punctuation
    s = s.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
    # s = s.split()
    s = filter(lambda x: x not in MOST_COMMON_WORDS, s.split())
    s = filter(lambda x: not x.isnumeric(), s)
    s = filter(lambda x: len(x) > 1, s)
    freq = defaultdict(lambda: 0)
    for word in s:
        # print(word)
        freq[word] += 1
    return freq


def do_pubmed_freq_analysis():
    with open('badwords.txt','r') as f:
        words = f.readlines()
        WORDS = {w.strip() for w in words}

    out = list()

    num = 0
    articles = 0
    for article in get_offline_articles_from_csv():
        num += 1
        # if num > 100000:
        #    break
        # for article in get_offline_articles():
        # pmid, title, journal, date, pubtype, abstract, chemicals, topics, keywords = get_pubmed_data(article)
        # searchable = ' '.join(get_pubmed_data(article))
        pmid = article['pmid']
        if len(article['abstract']) < 100:
            continue
        searchable = ' '.join(article.values())
        searchable = searchable.lower()

        score = 0
        if ('endocrine' in searchable and 'disrupt' in searchable):
            freq = analyze_frequency(searchable)
            for k, v in freq.items():
                if k in searchable:
                    score -= v

            articles += 1
            print(articles)
            freq = list(reversed(sorted(freq.items(),key=lambda x: x[1])))
            print(pmid, score, )
            #for f in freq:
            #    if f[1] > 1:
            #        print (f)
            article['score'] = score
            out.append(article)
    with open('pubmed_freq_scores.csv', 'w') as f:
        columns = ['pmid', 'score', 'title', 'date', 'journal', 'pubtype', 'abstract', 'chemicals', 'topics',
                   'keywords', 'meshterms']
        writer = csv.DictWriter(f, columns)
        writer.writeheader()
        out = reversed(sorted(out, key=lambda x: x['score']))
        writer.writerows(out)


def gen_deduct_freq_analysis():
    from raw_data import ALL_PAPERS, MOST_COMMON_WORDS, HIGH_SCORE_TERMS, LOW_SCORE_TERMS,EXCLUDE_TERMS
    from scratch_19 import DEDUCT_FINAL_PAPERS
    entrez_api = easy_entrez.EntrezAPI(
        'endoscreen',
        'contact@endoscreen.orgm',
        # optional
        return_type='json'
    )

    ALL_PAPERS = ALL_PAPERS.difference(DEDUCT_FINAL_PAPERS)

    #fetched = entrez_api.fetch([str(p) for p in list(DEDUCT_FINAL_PAPERS)], max_results=4000, database='pubmed')
    fetched = entrez_api.fetch([str(p) for p in list(ALL_PAPERS)[:9999]], max_results=9999, database='pubmed')
    fetched2 = entrez_api.fetch([str(p) for p in list(ALL_PAPERS)[9999:]], max_results=9999, database='pubmed')

    parsed = xmltodict.parse(xml_to_string(fetched.data))
    parsed2 = xmltodict.parse(xml_to_string(fetched2.data))
    parsed['PubmedArticleSet']['PubmedArticle'].extend(parsed2['PubmedArticleSet']['PubmedArticle'])
    # print(parsed)
    out = defaultdict(lambda: 0)
    num_words = 0
    for article in parsed['PubmedArticleSet']['PubmedArticle']:
        searchable = ' '.join(get_pubmed_data(article))
        num_words += len(searchable.split())
        freq = analyze_frequency(searchable)
        # print(freq)
        for k, v in freq.items():
            out[k] += v
    with open('deduct_word_scores.json', 'w') as f:
        json.dump(out, f)
    for k,w in reversed(sorted(out.items(), key=lambda x: x[1])):
        print(k)



def listify(l):
    if isinstance(l, list):
        return l
    return [l]


def genfreq2():
    pass


def get_related(fetched, info):
    pass
    s = ''
    score = 0
    related = set()

    print(fetched['MedlineCitation']['PMID']['#text'], "score", score, related)
    # print(fetched.__repr__())
    # print(fetched.__str__())
    # related


def gen_paperinfo():
    import os
    api = easy_entrez.EntrezAPI('endoscreen', 'contact@endoscreen.org', return_type='json', api_key=os.environ['NCBI_API_KEY'])

    papers = list()

    count = 0
    for chunk in chunkify(list(DEDUCT_FINAL_PAPERS), 50):
        time.sleep(1)
        print("count", count)
        lst = [p.replace('PMID:', '') for p in chunk]
        try:
            fetched = xmltodict.parse(xml_to_string(api.fetch(lst, max_results=100).data))
            while 'PubmedArticleSet' not in fetched:
                print("trying again...")
                fetched = xmltodict.parse(xml_to_string(api.fetch(lst, max_results=100).data))
        except:
            fetched = xmltodict.parse(xml_to_string(api.fetch(lst, max_results=100).data))
            while 'PubmedArticleSet' not in fetched:
                print("trying again...")
                fetched = xmltodict.parse(xml_to_string(api.fetch(lst, max_results=100).data))

        # todo: investigate why this can fail
        # assert len(chunk) == len(fetched['PubmedArticleSet']['PubmedArticle'])
        for paper in fetched['PubmedArticleSet']['PubmedArticle']:
            info = dict()

            info['ids'] = list()
            for aid in listify(paper['PubmedData']['ArticleIdList']['ArticleId']):
                info['ids'].append(':'.join([aid['@IdType'], aid['#text']]))

            info['pubdate'] = ''
            for date in listify(paper['PubmedData']['History']['PubMedPubDate']):
                if date['@PubStatus'] == 'pubmed':
                    info['pubdate'] = '{Day}-{Month}-{Year}'.format(**date)

            info['authors'] = list()
            if 'AuthorList' in paper['MedlineCitation']['Article']:
                for author in listify(paper['MedlineCitation']['Article']['AuthorList']['Author']):
                    a = author.get('LastName')
                    if a:
                        if f := author.get('ForeName'):
                            a += ', ' + f
                    else:
                        a = author.get('CollectiveName')
                    info['authors'].append(a)
            else:
                pass

            info['title'] = paper['MedlineCitation']['Article']['ArticleTitle']
            if isinstance(info['title'], dict):
                info['title'] = info['title']['#text']
            info['pubtypes'] = list()
            for pub in listify(paper['MedlineCitation']['Article']['PublicationTypeList']['PublicationType']):
                info['pubtypes'].append(pub['#text'])

            # todo: get citations and cited by

            info['journal'] = paper['MedlineCitation']['Article']['Journal']['Title']

            if 'Abstract' in paper['MedlineCitation']['Article']:
                info['abstract'] = paper['MedlineCitation']['Article']['Abstract']['AbstractText']
                if isinstance(info['abstract'], list):
                    abstract = ''
                    for section in info['abstract']:
                        abstract = abstract + section['@Label'] + " " + section['#text']
                    info['abstract'] = abstract
                elif isinstance(info['abstract'], dict):
                    info['abstract'] = info['abstract']['#text']
            else:
                info['abstract'] = ''

            terms = list()
            if 'ChemicalList' in paper['MedlineCitation']:
                for chem in listify(paper['MedlineCitation']['ChemicalList']['Chemical']):
                    terms.append(chem['NameOfSubstance']['#text'])
            if 'MeshHeadingList' in paper['MedlineCitation']:
                for mesh in listify(paper['MedlineCitation']['MeshHeadingList']['MeshHeading']):
                    terms.append(mesh['DescriptorName']['#text'])
            if 'KeywordList' in paper['MedlineCitation']:
                for keyword in listify(paper['MedlineCitation']['KeywordList']['Keyword']):
                    terms.append(keyword['#text'])

            terms = [s.lower() for s in terms]
            terms = [s.replace(',', '').replace('-', '') for s in terms]

            info['related'] = list(terms)

            papers.append(info)
        count += len(chunk)
    return papers


from raw_data import ALL_CHEMS_CID


def gen_cheminfo():
    chems = []
    for cid in ALL_CHEMS_CID:
        try:
            info = dict()
            chem = pcp.Compound.from_cid(cid)
            info['cid'] = str(chem.cid)
            info['name'] = chem.iupac_name
            info['synonyms'] = [s.lower() for s in chem.synonyms]
            info['formula'] = chem.molecular_formula
            info['related'] = [] #TODO
            chems.append(info)
            print(info)
        except:
            #???
            pass

    return chems


def gen_terms(papers, chems):
    import string
    related = set()

    for paper in papers:
        print(paper['ids'][0])
        s = paper['title'] + paper['abstract']
        freq = analyze_frequency(s)
        # todo: make this better
        score = 0
        terms = set(freq.keys()).intersection(HIGH_SCORE_TERMS)
        paper['related'].extend(terms)

        s = s.lower()
        s = s.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))

        for chem in chems:
            if (overlap := set(chem['synonyms']).intersection(set(s.split()))):
                print("got a paper <> chem match",overlap)
                chem['related'].extend(overlap)
                paper['related'].extend(set(paper['related']).intersection(overlap))
            #print(chem)

def gen_edcdb():
    if os.path.exists('termsdb.json'):
        with open('termsdb.json', 'r') as f:
            papers, chems = json.load(f)
    else:
        papers = gen_paperinfo()
        chems = gen_cheminfo()
        gen_terms(papers, chems)
        with open('termsdb.json', 'w') as f:
            json.dump([papers, chems], f)
    with open('edcdb_gcp/edcdb_papers.csv', 'w') as f:
        ps = []
        for p in papers:
            if p['ids'][0].replace('pubmed:','') in DEDUCT_FINAL_PAPERS:
                ps.append(p)
        writer = csv.DictWriter(f, ['ids','pubdate','authors','title','pubtypes','journal','abstract','related'])
        writer.writeheader()
        writer.writerows(ps)
        print()
    with open('edcdb_gcp/edcdb_chems.csv', 'w') as f:
        writer = csv.DictWriter(f, ['cid','name','synonyms','formula','related'])
        writer.writeheader()
        writer.writerows(chems)
        print()



def most_common_words():
    from raw_data import EXCLUDE_TERMS
    ALL_WORDS = defaultdict(lambda : 0)
    FILTERED_WORDS = defaultdict(lambda : 0)

    count = 0
    for article in get_offline_articles_from_csv():
        count += 1
        if count%10000==0:
            print(count)
        if count > 100000:
            break
        searchable = ' '.join(article.values())
        for w in searchable.split():
            ALL_WORDS[w] += 1
        filtered = analyze_frequency(searchable)
        for k,v in filtered.items():
            FILTERED_WORDS[k] += v
            #print(k,v)


    with open('all_word_freqs.csv', 'w') as f:
        columns = ['word', 'numoccur']
        writer = csv.DictWriter(f, columns)
        writer.writeheader()
        out = reversed(sorted(ALL_WORDS.items(), key=lambda x: x[1]))
        for thing in out:
            writer.writerow({'word': thing[0],'numoccur': thing[1]})


    with open('all_word_freqs_filtered.csv', 'w') as f:
        columns = ['word', 'numoccur']
        writer = csv.DictWriter(f, columns)
        writer.writeheader()
        out = reversed(sorted(FILTERED_WORDS.items(), key=lambda x: x[1]))
        for thing in out:
            writer.writerow({'word': thing[0],'numoccur': thing[1]})


# cas_to_cid()
# get_common_names()
# find_literature()
# sanitize_synonyms()
# sfind_lit2()
# process_manual_search()
# parse_pubmed()
# offline_search()
# search_offline_csvs()
# convert_pubmed_to_json()
# offline_json_search()
#gen_deduct_freq_analysis()
#do_pubmed_freq_analysis()
gen_edcdb()
#most_common_words()

#with open('deduct_word_scores.json','r') as f:
#    all_words = json.load(f)
#with open('deduct_word_scores_final.json','r') as f:
#    final_words = json.load(f)
#diffs = dict()
#for k,w in final_words.items():
#    try:
#        if w > 10:
#            del all_words[k]
#    except:
#        pass

#for k, v in reversed(sorted(all_words.items(), key=lambda item: item[1])):
#    print(k,v)


#print(all_words)

#with open('scratch_23.txt','r') as f:
#    gathered_papers = {w.strip() for w in f.readlines()}
#from raw_data import ALL_PAPERS
#from scratch_19 import DEDUCT_FINAL_PAPERS
#papers = {p.replace('PMID:','') for p in ALL_PAPERS}
#print(len(gathered_papers))
#print(len(papers.intersection(gathered_papers))/len(papers))
#print(len(DEDUCT_FINAL_PAPERS.intersection(gathered_papers))/len(DEDUCT_FINAL_PAPERS))

#count = 0

#with open('pubmed_freq_scores.csv','r') as in_f, open('emily_papers.csv','w') as out_f:
#    reader = csv.DictReader(in_f)
#    writer = csv.DictWriter(out_f,['pmid', 'score', 'title', 'date', 'journal', 'pubtype', 'abstract', 'chemicals', 'topics',
#                   'keywords', 'meshterms'])
#    for line in reader:
#        if line['pmid'] not in papers:
#            writer.writerow(line)
#            count += 1
#            print(line)

#print(count)