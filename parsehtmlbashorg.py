from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

for i in range(1, 240):
    soup = BeautifulSoup(open('rawhtml/' + str(i) + '.html'), "html.parser")

    quotes = soup.find_all('p', attrs={'class' : 'qt'})

    for quote in quotes:
        text = quote.get_text()
        lines = text.split('\r\n')
        printed_line = 0
        for line in lines:
            if len(line) > i and line[0] == '<':
                i = 1
                while len(line) > i and line[i] != '>': i+=1
                #from here, i = index of end of tag
                print line[i+2:]
                printed_line += 1

        if printed_line != 0 : print '==='
