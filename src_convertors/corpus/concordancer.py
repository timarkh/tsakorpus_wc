import re
import os
rxWords = re.compile('\\b\\w[\\w-]*\\w\\b|\\b\\w\\b')


def process_file(fpath, fname, dictConc):
    """
    Collect all words from a CSV file with transcriptions
    of images.
    Modify the frequency dictionaries passed as dictConc.
    dictConc: {lang: {word: freq}}
    Return total number of words.
    """
    with open(os.path.join(fpath, fname), 'r', encoding='utf-8-sig') as fIn:
        lines = fIn.readlines()
    nWords = 0
    for line in lines:
        line = line.strip(' \r\n')
        if '\t' not in line:
            continue
        line = line.split('\t')
        lang = line[-1].lower()
        if lang not in dictConc:
            dictConc[lang] = {}
        lineText = line[2].replace('\\n', ' ').lower()
        words = rxWords.findall(lineText)
        for word in words:
            nWords += 1
            try:
                dictConc[lang][word] += 1
            except KeyError:
                dictConc[lang][word] = 1
            if '-' in word:
                parts = word.split('-')
                for iPart in range(len(parts)):
                    part = parts[iPart]
                    if iPart != len(parts) - 1:
                        part += '-'
                    else:
                        part = '-' + part
                    try:
                        dictConc[lang][part] += 1
                    except KeyError:
                        dictConc[lang][part] = 1
    return nWords


def write_conc(dictConc, fname):
    for lang in dictConc:
        f = open(lang + '_' + fname, 'w', encoding='utf-8')
        for word in sorted(dictConc[lang], key=lambda w: (-dictConc[lang][w], w)):
            f.write(word + '\t' + str(dictConc[lang][word]) + '\n')
        f.close()


conc = {}
nWords = 0
for root, dirs, files in os.walk('csv'):
    print(root)
    for fname in files:
        if not fname.endswith('.csv') or re.search('\\bmeta\\b|parsed|concord|_uncleaned', fname) is not None:
            continue
        nWords += process_file(root, fname, conc)
write_conc(conc, 'wordlist.csv')
print('Corpus size: ' + str(nWords) + ' words.')
