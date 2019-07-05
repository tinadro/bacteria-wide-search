from Bio.Blast.Applications import NcbipsiblastCommandline
from Bio import SeqIO
import pandas as pd
import sys

#~~~~~~~~~~~~~~~~~~~~~~~~~~
# DEFINING SOME VARIABLES:
#~~~~~~~~~~~~~~~~~~~~~~~~~~

query = sys.argv[1]
pssm = query+'-pssm.asn1'
output = 'psiblast-'+query+'.tsv'
out_format = " '6 qaccver saccver bitscore evalue qlen slen length qcovs pident staxids sscinames' " # blastp output cols
out_columns = out_format[4:-2] # gets only the output format specifiers in out_format
database = '~/datalocal/nr_db/nr'
e_cut = 1e-3

#~~~~~~~~~~~~~~~~~~~~~
# RUN 1 BLASTP ROUND:
#~~~~~~~~~~~~~~~~~~~~~

print('about to run')
# Run BLASTP in command line, according to above settings \
psiblast_cline = NcbipsiblastCommandline(in_pssm=pssm, num_iterations='1', out=output, outfmt=out_format, db=database, evalue=e_cut)
print(psiblast_cline)
print('psiblast done')


