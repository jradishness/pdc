""" A script for counting adjectives used by all candidates not named
    Trump for the purposes of comparison with Donald Trump.
"""
# Imports and initiations
import spacy, os, collections
nlp = spacy.load('en_core_web_lg')

tag_dict = collections.defaultdict(int)
pos_dict = collections.defaultdict(int)
adj_dict = collections.defaultdict(int)
counter = 0

for filename in os.listdir('results'):
    if filename.endswith("D.txt"):
        # Load files
        fileText = open("results/" + str(filename)).read()
        doc = nlp(fileText)

        # Count POS tags, both granularities
        for token in doc:
            if token.pos_ == "ADJ":
                adj_dict[token.text] += 1
                counter += 1
            else:
                pass
    else:
        pass

    with open('results/DemocratAdj.txt', 'w') as f:
        print("Everyone but Trump", file=f)
        print("Counts of Adjectives:   " + str(counter), file=f)
        print("Word\tCount\n", file=f)
        for key, value in adj_dict.items():
            print(str(key) + "\t" + str(value), file=f)
    f.close()
