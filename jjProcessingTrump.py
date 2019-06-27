""" A script for counting adjectives used by Donald Trump
    for the purposes of comparison with other candidates.
    """
# Imports and initiations
import spacy, os, collections
nlp = spacy.load('en_core_web_lg')
adj_dict = collections.defaultdict(int)

# Load files
fileText = open("results/TRUMP.txt").read()
doc = nlp(fileText)

# Count POS tags, both granularities
for token in doc:
    if token.pos_ == "ADJ":
        adj_dict[token.text] += 1
    else:
        pass

with open('results/pos/TrumpAdj.txt', 'w') as f:
    print("Donald Trump", file=f)
    print("Counts of Adjectives", file=f)
    print("Word\tCount\n", file=f)
    for key, value in adj_dict.items():
        print(str(key) + "\t" + str(value), file=f)
f.close()
