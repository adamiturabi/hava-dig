class Parser:
  special_chars = {
    "indent": '&ldca;&nbsp;&nbsp;&nbsp;',
    "square": '&square;',
    "4star": chr(int('0x2727', 16))
  }
  def __init__(self):
    self.curr_root = ''
  def process_span(self, instr):
    outstr = ''
    classcode_beg_idx = instr.find('{')
    classcode = instr[(classcode_beg_idx+2):-1]
    text = instr[1:(classcode_beg_idx-1)]
    if classcode == 'latin':
      outstr = '<span lang="en" dir="ltr">'+text+'</span>'
    elif classcode == 'fbr':
      outstr = '<span class="foreignborrowing" lang="en" dir="ltr">'+text+'</span>'
    else:
      outstr = "NOT FOUND: " + classcode
    return outstr

  def parse_line(self, line):
    line = line[0:-1]
    delims = {' ', ',', '(', ')', '+', '=', ';'}
    words = []
    curr_word = ''
    index = 0
    #for index in range(0, len(line)):
    while index < len(line):
      if line[index] == '[': #[some text]{.classcode}
        if curr_word != '':
          words.append(curr_word)
        curr_word = ''
        for index2 in range(index, len(line)):
          if line[index2] == '}':
            curr_word += '}'
            words.append(curr_word)
            index = index2
            curr_word = ''
            break
          else:
            curr_word += line[index2]
      elif line[index] in delims:
        if curr_word != '':
          words.append(curr_word)
          curr_word = ''
        words.append(line[index])
      else:
        curr_word += line[index]
      index += 1
    if curr_word != '':
      words.append(curr_word)
    #print(words)
    out_str = ''
    for word in words:
      from src import translit_to_ar
      if word[0] == '@':
        self.curr_root = word[1:]
        out_str = 'qwerty'+translit_to_ar.translit_to_ar(self.curr_root)
      #elif word[0:2] == '##':
      #  out_str += '<span class="foreignborrowing">' + word[2:] + '</span>'
      elif word[0] == '[':
        out_str += self.process_span(word)
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
        elif word == '=':
          #out_str += chr(int('0x25a1', 16))
          out_str += self.special_chars["square"]
        elif word == '+':
          out_str += self.special_chars["4star"]
        else:
          out_str += word
      elif word == '\\n':
        out_str += '<br><br>' + self.special_chars["indent"]
      elif word == '--':
        out_str += '—'
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
  
  def process_en_line(self, en_line):
    out_str = ''
    for x in en_line:
      if x == '+':
        out_str += self.special_chars["4star"]
      elif x == '=':
        out_str += self.special_chars["square"]
      else:
        out_str += x
    return out_str

  def parse_file(self, letter_index, ar_text_filename, en_text_filename, htmlout_filename):
    lines = ''
    
    with open(htmlout_filename, 'w') as fout, open(ar_text_filename) as fin_ar, open(en_text_filename) as fin_en:
      from src import write_html_pre
      write_html_pre.write_html_pre(fout)
      outstr = '<div class="row py-2 justify-content-center"><div class="col-auto" dir="ltr" lang="en">'
      outstr += '<a href="index.html">Index page</a>\n'
      outstr += '</div></div>\n'
      from src import index2letter
      outstr += '<div class="row py-2 justify-content-center"><div class="col-auto" dir="ltr" lang="en">'
      outstr +='<h4>Roots beginning with ' + index2letter.index2letter(letter_index) + ':</h4>\n'
      outstr += '</div></div>\n'
      fout.write(outstr)
      while True:
        ar_line = fin_ar.readline()
        ar_out_str = self.parse_line(ar_line)
        en_line = ''
        if ar_out_str[:6] == 'qwerty':
          this_root = ar_out_str[6:]
          ar_out_str = '<span id="'+this_root+'"><b>«'+this_root+'»</b></span>'
        else:
          en_line = fin_en.readline()
          en_line = self.process_en_line(en_line)
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
