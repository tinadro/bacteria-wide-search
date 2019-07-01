import os
import pandas as pd  
from Bio import Entrez, SeqIO
from os.path import dirname, abspath
Entrez.email = 'td1515@ic.ac.uk'
Entrez.api_key = '41267f8592172caaa22ab00ec006c4330208'

parentdir = dirname(dirname(abspath(__file__)))

# OPEN RESULTS TABLE:
def open_results(query):
	filepath = parentdir + '/1_bidirectional-best-hits/results-Cj' + query + '-names.xlsx'
	bbh = pd.read_excel(filepath, sheet_name='BBH-eval-filter')
	psi = pd.read_excel(filepath, sheet_name='psiblast-eval-filter') #open the bbh and psiblast results tables
	combined = bbh.append(psi, ignore_index=True) #combine them together 
	nr = combined.drop_duplicates(subset=['saccver']) #drop duplicate acc.vers 
	return nr

#fetch fasta sequence given an acc.ver
def get_sequence(hit):
	handle = Entrez.efetch(db="protein", id=hit, rettype="fasta", retmode="text") # fetch the full sequence of that acc.ver
	record = SeqIO.read(handle, "fasta") # read it out
	handle.close()
	return record

#make the multi-fasta of all acc.vers in the 'nr' dataframe
def make_mfa(nr_df, query):
	i = 0
	hits = [i for i in nr_df['saccver']]

	with open(query+'-hits.mfa', 'a+') as f:
		for hit in hits:
			seq = get_sequence(hit)
			i += 1
			print(i)
			SeqIO.write(seq, f, 'fasta')
	print('made ', query)

nr_a = open_results('PflA')
make_mfa(nr_a, 'PflA')

nr_b = open_results('PflB')
make_mfa(nr_b, 'PflB')

