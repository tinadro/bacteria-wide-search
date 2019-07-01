import os, sys, glob, subprocess, shutil
from os.path import dirname, abspath, isdir
import pandas as pd
from Bio.Blast.Applications import NcbipsiblastCommandline
from Bio import SeqIO


#~~~~~~~~~~~~~~~~~~~~~~~~~~
# DEFINE NAMES OF FILES :
#~~~~~~~~~~~~~~~~~~~~~~~~~~

query = sys.argv[1] # what the query sequence was ('PflA' or  'PflB')

parentdir = dirname(dirname(abspath(__file__)))
query_fa = parentdir + '/1_bidirectional-best-hits/Cj'+query+'.faa'
blastdb = query+'-db/'+query+'-hits'

pssm = query + '-pssm.asn1'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CONVERT TO PSSM BY A SINGLE PSI-BLAST ITERATION:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

psiblast_cline = NcbipsiblastCommandline(query=query_fa, db=blastdb, num_iterations='2', out_pssm=pssm) # do one iteration of psiblast, take the original query (CjPflA or CjPflB) as the 'subject', and save the pssm it creates
stdout, stderr = psiblast_cline() # make the PSSM with the original query and dummy database 


