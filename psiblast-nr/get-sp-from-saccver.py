import pandas as pd
from Bio import Entrez
import sys
Entrez.email = 'td1515@ic.ac.uk'
Entrez.api_key = '41267f8592172caaa22ab00ec006c4330208'

pfl = sys.argv[1] # PflA or PflB
in_table = pd.read_csv('psiblast-nr-'+pfl+'.tsv', sep='\t') #open psiblast results table
saccver = [i for i in in_table['saccver']] # get the taxid numbers (sometimes there are several sperated by a ';', for slightly differnet strains fo the same bacterium)

def prot_search(query):
	handle = Entrez.esearch(db='protein', term=query)
	record = Entrez.read(handle)
	handle.close()
	uid = record['IdList']
	return uid

def prot_summary(uid):
	handle = Entrez.esummary(db='protein', id=uid, report='full')
	record = Entrez.read(handle)
	handle.close
	return record[0]

def tax_search(query):
	handle = Entrez.esearch(db='taxonomy', term=query)
	record = Entrez.read(handle)
	handle.close()
	uid = record['IdList']
	return uid

def tax_efetch(uid):
	handle = Entrez.efetch(db='taxonomy', id=uid)
	record = Entrez.read(handle)
	handle.close()
	return record[0]
a = 0
for ele in saccver:
	d = []
	uid = prot_search(ele)
	info = prot_summary(uid)
	d.append(info['TaxId']) # add taxid 
	d.append(info['Title']) # add name of protein 
	uid2 = tax_efetch(info['TaxId'])
	d.append(uid2['ScientificName']) # add species
	for i in range(len(uid2['LineageEx'])):
		d.append(uid2['LineageEx'][i]['ScientificName']) # add taxonomy levels, one by one 
	s = pd.Series(d)
	s = s.to_frame().transpose() # make the series a DF, so it will get written as a row
	with open('psiblast-nr-'+pfl+'-saccver-tax.tsv', 'a+') as f:
		s.to_csv(f, header=False, sep='\t', index=False) #write row in results table 
	print(a)
	a += 1

	

