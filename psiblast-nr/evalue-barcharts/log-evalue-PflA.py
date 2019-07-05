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
ls = f['eval']

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CONVERT DATA TO LOG VALUES:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

zero = [i for i in ls if i == 0] # list of all the zeroes 
data = [i for i in ls if i != 0] # list of all non-zero evalues
print(len(zero))

logs = np.floor(np.log10(data)) # convert all the numbers to log values
logs = [int(z) for z in logs]

max_point = max(logs)
min_point = min(logs)
print(max_point)
print(min_point)

bins = list(range(min_point, 1, 1))

def bar_data(data, x_bins=bins): #put in data[], bins, data[1] bins, etc 
	ls = []
	for ele in x_bins:
		nr = data.count(ele)
		ls.append(nr)
	return ls

#~~~~~~~~~~~~~~~~~~~~~~
# MAKE THE BAR CHART:
#~~~~~~~~~~~~~~~~~~~~~~

#set width of bars
width = .9

#set position of bar on x axis
r1 = np.arange(len(bins)) # how many bins there are 
r1_ticks = list(range(3, len(bins), 10)) # the bins that i want to have as major ticks

major_bins = bins[3::10] # the labels for the major ticks

#make the plot
fig, ax = plt.subplots()
plt.bar(r1, bar_data(logs), width=width) # input the data. number of bins and the corresponding height of bar for each bin

#add xticks, label every second xtick
plt.xticks(r1_ticks, major_bins)
plt.minorticks_on()
ax.xaxis.set_minor_locator(AutoMinorLocator(n=10)) # turn on minor ticks to be for every 1 bin
plt.tick_params(axis='y', which='minor', length=0)
plt.tick_params(axis='x', which='minor', length=3)
plt.tick_params(axis='x', which='major', length=6)

#turn on y-axis gridlines
ax.yaxis.grid(b=True, which='major')
ax.yaxis.grid(b=True, which='minor', linestyle='--', color='0.9')
ax.set_axisbelow(True) # place the gridlines behind the bars 

#figure size
fig.set_size_inches(8, 4)

#position legend, show plot
plt.margins(x=.005)
plt.tight_layout()
plt.savefig('PflA-logevalue', dpi=300)
plt.show()


