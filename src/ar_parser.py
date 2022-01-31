class Parser:
  def __init__(self):
    self.curr_root = ''
  def parse_line(self, line):
    line = line[0:-1]
    delims = {' ', ',', '(', ')', '+', '=', ';'}
    words = []
    curr_word = ''
    for index in range(0, len(line)):
      if line[index] in delims:
        if curr_word != '':
          words.append(curr_word)
          curr_word = ''
        words.append(line[index])
      else:
        curr_word += line[index]
    if curr_word != '':
      words.append(curr_word)
    #print(words)
    out_str = ''
    for word in words:
      from src import translit_to_ar
      if word[0] == '@':
        self.curr_root = word[1:]
        out_str = 'qwerty<b>«'+translit_to_ar.translit_to_ar(self.curr_root)+'»</b>'
      elif word[0] in { 'I', 'V', 'X' }:
        if word[-1] == 'x':
          out_str += word[:-1]
        else:
          out_str += word
        do_conj = word[-1] != 'x' and word != 'I'
        if do_conj:
          from src import conj
          form = word
          enverb = conj.conj(self.curr_root, form, 'a', 'a')
          arverb = translit_to_ar.translit_to_ar(enverb)
          from src import hamzater
          out_str += ' ' + hamzater.hamzate(arverb)
      elif len(word) == 1 and word in {'A', '!', 'O', 'U' }:
        #out_str += get_pret(word, self.curr_root)
        from src import conj
        form = 'I'
        vowel = word
        if vowel == 'O':
          vowel = 'U'
        elif vowel == '!':
          vowel = 'I'
        enverb = conj.conj(self.curr_root, form, vowel.lower(), "pret")
        arverb = translit_to_ar.translit_to_ar(enverb)
        from src import hamzater
        out_str += hamzater.hamzate(arverb)
      elif len(word) == 1 and word in {'a', 'i', 'o', 'u' }:
        from src import conj
        form = 'I'
        vowel = word
        if vowel == 'o':
          vowel = 'u'
        enverb = conj.conj(self.curr_root, form, vowel, "ao")
        arverb = translit_to_ar.translit_to_ar(enverb)
        #import hamzater
        #out_str += hamzater.hamzate(arverb)
        out_str += arverb
      elif len(word) == 1 and word in delims:
        if word == ',':
          out_str += '،'
        elif word == '(':
          out_str += '('
        elif word == ')':
          out_str += ')'
        elif word == ';':
          out_str += '؛'
        else:
          out_str += word
      elif word == '\\n':
        out_str += '<br><br>'
      elif word == '--':
        out_str += '—'
      elif word == '=':
        out_str += chr(int('0x25a1', 16))
      elif word == '+':
        out_str += chr(int('0x2727', 16))
      elif ord(word[0]) >= ord('1') and ord(word[0]) <= ord('9'):
        from src import num2word
        temp = translit_to_ar.translit_to_ar(num2word.num2word(word, self.curr_root))
        from src import hamzater
        out_str += hamzater.hamzate(temp)
      elif word[0] in translit_to_ar.translit_map:
        out_str += translit_to_ar.translit_to_ar(word)
      else:
        out_str += word

    return out_str
  
  def parse_file(self, letter_index, ar_text_filename, en_text_filename, htmlout_filename):
    lines = ''
    
    with open(htmlout_filename, 'w') as fout, open(ar_text_filename) as fin_ar, open(en_text_filename) as fin_en:
      from src import write_html_pre
      write_html_pre.write_html_pre(fout)
      outstr = '<div class="row justify-content-center"><div class="col-auto" dir="ltr" lang="en">'
      outstr += 'Go to: <a href="index.html">Index page</a>\n'
      outstr += '</div></div>\n'
      from src import index2letter
      outstr = '<div class="row pt-4 justify-content-center"><div class="col-auto" dir="ltr" lang="en">'
      outstr +='<h4>Roots beginning with ' + index2letter.index2letter(letter_index) + ':</h4>\n'
      outstr += '</div></div>\n'
      fout.write(outstr)
      while True:
        ar_line = fin_ar.readline()
        ar_out_str = self.parse_line(ar_line)
        en_line = ''
        if ar_out_str[:6] == 'qwerty':
          ar_out_str = ar_out_str[6:]
        else:
          en_line = fin_en.readline()
        if not ar_line and not en_line:
          break
        if not ar_line:
          ar_line = ''
        if not en_line:
          en_line = ''
        outstr = '<div class="row py-2 justify-content-around"><div class="col-auto">'+ar_out_str+'</div>'
        outstr += '<div class="col" lang="en" dir="ltr">'+en_line+'</div></div>\n'
        fout.write(outstr)
      fout.write("</div></body></html>")
