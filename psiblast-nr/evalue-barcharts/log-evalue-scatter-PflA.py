import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
from os.path import dirname, abspath

#~~~~~~~~~~~~~~~~~~~
# GET DATA FOR PLOT
#~~~~~~~~~~~~~~~~~~~

parentdir = dirname(dirname(abspath(__file__)))
fpath = parentdir+'/psiblast-nr-PflA-taxonomy.tsv'
f = pd.read_csv(fpath, sep='\t')

#print(list(f))
#kingdoms = f.b.unique() # Bacteria, Archaea, Eukaryota
print(f.b.unique())


x_bac = []
y_bac = []

x_eu = []
y_eu = []

x_ar = []
y_ar = []


for ind, row in f.iterrows():
	if row['b'] == 'Bacteria':
		x_bac.append(row['slen'])
		y_bac.append(row['eval'])
	elif row['b'] == 'Archaea':
		x_ar.append(row['slen'])
		y_ar.append(row['eval'])
	elif row['b'] == 'Eukaryota':
		x_eu.append(row['slen'])
		y_eu.append(row['eval'])

x_bac = [x/788 for x in x_bac]
x_ar = [x/788 for x in x_ar]
x_eu = [x/788 for x in x_eu]

print(len(x_eu))
print(len(y_eu))

y_bac = np.log10(y_bac)
y_ar = np.log10(y_ar)
y_eu = np.log10(y_eu)
print(len(y_eu))

#x = f['slen'].apply(lambda x: x/788)
#~~~~~~~~~~~~~~~~~~~~~~~
# MAKE THE SCATTER PLOT:
#~~~~~~~~~~~~~~~~~~~~~~~

#make the plot
fig, ax = plt.subplots()

ax.scatter(x_bac, y_bac, color='#f70027', marker='.', edgecolor='k', linewidth=0.4, label='Bacteria')
ax.scatter(x_ar, y_ar, color='#7cfc00', marker='.', edgecolor='k', linewidth=0.4, label='Archaea')
ax.scatter(x_eu, y_eu, color='#00bfff', marker='.', edgecolor='k', linewidth=0.4, label='Eukaryotes')

# axis labels
plt.xlabel('hit length/ query length ratio')
plt.ylabel('evalue')

#add xticks, label every second xtick
#plt.xticks(np.arange(0.5, 1.1, 0.1))
#for label in ax.xaxis.get_ticklabels()[-1:]:
#	label.set_visible(False)
#plt.yticks(range(50, 110, 10))
ax.xaxis.set_minor_locator(AutoMinorLocator(n=2))
ax.yaxis.set_minor_locator(AutoMinorLocator(n=2)) # turn on minor ticks to be for every 1 bin

#turn on y-axis gridlines
ax.yaxis.grid(b=True, which='major', linestyle='--', color='0.9')
ax.yaxis.grid(b=True, which='minor', linestyle='--', color='0.9')
plt.tick_params(axis='y', which='minor', length=0)
ax.set_axisbelow(True)

#figure size
fig.set_size_inches(6, 4)

#position legend, show plot
plt.legend()
plt.tight_layout()
plt.savefig('PflA-len-logevalue-tax', dpi=300)
plt.show()
