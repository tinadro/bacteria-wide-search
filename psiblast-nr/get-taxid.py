import pandas as pd
from Bio import Entrez
import sys
Entrez.email = 'td1515@ic.ac.uk'
Entrez.api_key = '41267f8592172caaa22ab00ec006c4330208'

pfl = sys.argv[1] # PflA or PflB
in_table = pd.read_csv('psiblast-nr-'+pfl+'.tsv', sep='\t') #open psiblast results table
taxid = [i.split(';')[0] for i in in_table['taxid']] # get the taxid numbers (sometimes there are several sperated by a ';', for slightly differnet strains fo the same bacterium)

def ent_search(query):
	handle = Entrez.esearch(db='taxonomy', term=query)
	record = Entrez.read(handle)
	handle.close()
	uid = record['IdList']
	return uid

def ent_summary(query):
	handle = Entrez.esummary(db='taxonomy', id=query, report='full')
	record = Entrez.read(handle)
	handle.close
	return record[0]


a = 0
for ele in taxid:
	try:
		info = ent_summary(ele)
		div = info['Division']
		genus = info['Genus']
		species = info['Species']
		df = pd.Series({'taxid': ele, 'division': div, 'genus': genus, 'species': species})
		df = df.to_frame().transpose()
		with open('psiblast-nr-'+pfl+'-taxonomy.tsv', 'a+') as f:
			df.to_csv(f, header=False, sep='\t', index=False)
		print(a)
		a += 1
	except RuntimeError:
		tx = 'txid'+ele+'[Name Tokens]'
		uid = ent_search(tx)
		info = ent_summary(uid)
		div = info['Division']
		genus = info['Genus']
		species = info['Species']
		df = pd.Series({'taxid': ele, 'division': div, 'genus': genus, 'species': species})
		df = df.to_frame().transpose()
		with open('psiblast-nr-'+pfl+'-taxonomy.tsv', 'a+') as f:
			df.to_csv(f, header=False, sep='\t', index=False)
		print(a)
		a += 1

	

