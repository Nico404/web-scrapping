from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

for i in range(1, 723):
    soup = BeautifulSoup(open('rawdatasetsbashfr/' + str(i) + '.html'), "html.parser")

    quotes = soup.find_all('p', attrs={'class' : 'item-content'})

    for quote in quotes:
        text = quote.get_text()
        text = text.replace('<', '\n <')
        lines = text.split('\n')
        printed_line = 0
        for line in lines:
            if len(line) > 1 and line[1] == '<':
                i = 1
                while len(line) > i and line[i] != '>': i+=1
                print line[i+2:]
                printed_line += 1

        if printed_line != 0 : print '==='
