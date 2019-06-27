""" A script for counting POS tag usage by each candidate.
    """

# Imports and initiations
import spacy, os, collections
nlp = spacy.load('en_core_web_lg')

for filename in os.listdir('results'):
    if filename.endswith(".txt"):
        tag_dict = collections.defaultdict(int)
        pos_dict = collections.defaultdict(int)

        # Load files
        fileText = open("results/" + str(filename)).read()
        doc = nlp(fileText)

        # Count POS tags, both granularities
        for token in doc:
            tag_dict[token.tag_] += 1
            pos_dict[token.pos_] += 1

        with open('results/pos/' + str(filename), 'w') as f:
            print("Coarse-Grained Tags", file=f)
            print("Tag\tCount\n", file=f)
            for key, value in pos_dict.items():
                print(str(key) + "\t" + str(value), file=f)

            print("\n\n\nFine-Grained Tags", file=f)
            print("Tag\tCount\n", file=f)
            for key, value in tag_dict.items():
                print(str(key) + "\t" + str(value), file=f)
        f.close()
    else:
        pass
