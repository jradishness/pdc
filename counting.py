""" Simple script for counting the tokens in the unprocessed corpus,
    as an assignment for Corpus Linguistics.
"""
fnamelist = ['pres_1960_chic.txt',
             'pres_1960_nyci.txt',
             'pres_1960_nyla.txt',
             'pres_1960_wash.txt',
             'pres_1976_phil.txt',
             'pres_1976_sanf.txt',
             'pres_1976_virg.txt',
             'pres_1980_clev.txt',
             'pres_1984_kcmo.txt',
             'pres_1984_kent.txt',
             'veep_1988_nebr.txt',
             'pres_1988_ucla.txt',
             'pres_1988_wsnc.txt',
             'pres_1992_mich.txt',
             'pres_1992_stlo.txt',
             'pres_1992_virg.txt',
             'pres_1996_hart.txt',
             'pres_1996_sdca.txt',
             'pres_2000_bost.txt',
             'pres_2000_stlo.txt',
             'pres_2000_wsnc.txt',
             'pres_2004_ariz.txt',
             'pres_2004_flor.txt',
             'pres_2004_stmo.txt',
             'pres_2008_hemp.txt',
             'pres_2008_nash.txt',
             'pres_2008_oxms.txt',
             'pres_2012_denv.txt',
             'pres_2012_flor.txt',
             'pres_2012_hemp.txt',
             'pres_2016_hemp.txt',
             'pres_2016_stmo.txt',
             'pres_2016_unlv.txt',
             'veep_1976_hous.txt',
             'veep_1984_phil.txt',
             'veep_1992_atla.txt',
             'veep_1996_stpe.txt',
             'veep_2000_kent.txt',
             'veep_2004_clev.txt',
             'veep_2008_stmo.txt',
             'veep_2012_kent.txt',
             'veep_2016_virg.txt']

# print('Total Files:\t' + str(len(fnamelist)))   # give a total file count
num_words = 0                               # initialize counter for overall words
for fname in fnamelist:                     # iterate through file list
    with open('data/'+fname, 'r') as f:     # iterate through the file
        textsize = 0                        # initialize document token counter
        for line in f:                      # iterate through lines in document
            words = line.split()            # split lines into tokens
            textsize += len(words)          # add line count to document count
            num_words += len(words)         # add line count to overall count
       # print('Filename: ' + str(fname) + '\tFile word count: ' + str(textsize))   # fancy printing
        print(str(fname) + '\t' + str(textsize))    # .tsv printing format


print('Word Count:\t' + str(num_words))     # total word count
