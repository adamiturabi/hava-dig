#!/usr/bin/python3
from src.ar_parser import *
parser = Parser()
roots_set = set()
num_letters = 2
for i in range(1, num_letters+1):
#parser.parse_file('ar_text.txt', 'en_text.txt', 'out.html')
  parser.parse_file(i, 'txt/'+str(i)+'_ar.txt', 'txt/'+str(i)+'_en.txt', 'docs/'+str(i)+'.html', roots_set)

from src import get_roots_divs
roots_divs = get_roots_divs.get_roots_divs(roots_set)

from src import gen_title_page
gen_title_page.gen_title_page(num_letters, roots_divs)

for i in range(1, num_letters+1):
  with open('docs/'+str(i)+'.html', 'a') as fout:
    fout.write(roots_divs)
    fout.write('</div></body></html>\n')


