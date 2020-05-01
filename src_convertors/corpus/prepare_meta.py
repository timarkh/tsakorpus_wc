import re


def prepare_meta(fnameIn, fnameOut):
    """
    Generate titles in the metadata table.
    """
    with open(fnameIn, 'r', encoding='utf-8-sig') as fIn:
        lines = fIn.readlines()
    with open(fnameOut, 'w', encoding='utf-8-sig') as fOut:
        for line in lines:
            line = line.strip('\r\n')
            fields = list(line.split('\t'))
            title = fields[4] + ' (' + fields[6] + ', ' + fields[5] + ')'
            fields[0] = re.sub('\\.[^.]*$', '', fields[0])
            fields = [fields[0]] + [title] + fields[1:]
            fOut.write('\t'.join(fields) + '\n')


if __name__ == '__main__':
    prepare_meta('meta.csv', 'meta_enhanced.csv')
