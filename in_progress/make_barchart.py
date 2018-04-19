import random
import matplotlib.pyplot as plt

# Right now, this is just a hard-coded, test barchart.


# counts = [random.random() for i in range(25)]
num_cols = range(26)
y_vals = [random.randint(1, 100) for i in range(26)]
names = [
    'General function - R', 'Translation - J', 'Amino Acids - E', 'DNA - L',
    'Unknown - S', 'Envelope - M', 'Carbohydrates - G', 'Energy - C',
    'Transcription - K', 'Coenzymes - H', 'Nucleotides - F', 'Inorganic - P',
    'Protein turnover - O', 'Lipids - I', 'Signal transduction - T',
    'Secretion - U', 'Cell cycle - D', 'Defense - V', '2nd metabolites - Q',
    'Cell motility - N', 'RNA - A', 'Chromatin - B', 'Extracellular - W',
    'Mobilome - X', 'Nuclear structure - Y', 'Cytoskeleton - Z']
my_colors = ['r','g','b','k','y','m','c']  #red, green, blue, black, etc.
plt.barh(num_cols, y_vals, align='center', tick_label=names, color=my_colors)
# fig = plt.gcf()
# fig.set_size_inches(18.5, 10.5)
plt.tight_layout()
plt.show()
