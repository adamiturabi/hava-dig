class Parser:
  def __init__(self):
    self.curr_root = ''
  def parse_line(self, line):
    line = line[0:-1]
    delims = {' ', ',', '(', ')', '+', '='}
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
      import translit_to_ar
      if word[0] == '#':
        self.curr_root = word[1:]
        out_str = 'qwerty('+self.curr_root+')'
      elif word[0] in { 'I', 'V', 'X' }:
        #out_str += get_pret(word, self.curr_root)
        import conj
        form = word
        vowel = 'a'
        if word[-1] in {'a', 'i', 'o', 'u' }:
          form = word[:-1]
          vowel = word[-1]
          if vowel == 'o':
            vowel = 'u'
        enverb = conj.conj(self.curr_root, form, vowel, 'a')
        arverb = translit_to_ar.translit_to_ar(enverb)
        out_str += arverb
      elif len(word) == 1 and word in {'a', 'i', 'o', 'u' }:
        if word == 'o':
          out_str += 'u'
        else:
          out_str += word
      elif len(word) == 1 and word in delims:
        if word == ',':
          out_str += '،'
        elif word == '(':
          out_str += '('
        elif word == ')':
          out_str += ')'
        else:
          out_str += word
      elif ord(word[0]) >= ord('1') and ord(word[0]) <= ord('9'):
        import num2word
        out_str += translit_to_ar.translit_to_ar(num2word.num2word(word, self.curr_root))
      elif word[0] in translit_to_ar.translit_map:
        out_str += translit_to_ar.translit_to_ar(word)
      else:
        out_str += word

    return out_str
  
  def parse_file(self, ar_text_filename, en_text_filename, htmlout_filename):
    lines = ''
    
    with open(htmlout_filename, 'w') as fout, open(ar_text_filename) as fin_ar, open(en_text_filename) as fin_en:
      import write_html_pre
      write_html_pre.write_html_pre(fout)
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
        outstr = '<div class="row"><div class="col-sm-auto">'+ar_out_str+'</div>'
        outstr += '<div class="col-sm-auto"><span class="text-start" lang="en" dir="ltr">'+en_line+'</span></div></div>\n'
        fout.write(outstr)
      fout.write("</div></body></html>")
