from translit import *

harakaat_and_sukoon = { a, u, i, ss, o, F, N, K }
letters = {A, b, p, t, v, j, H, x, d, dh, r, z, s, sh, S, D, T, Z, E, g, f, q, k, l, m, n, h, w, Y, y , hmz, A_wasl}

class ConsonantInfo:
  cons = ""
  doubled = False
  vowel_mark = ""
  vowel = ""
  hmz = ""
  post_cons_str = ""
  suff = False
  def __str__(self):
    return "cons="+self.cons+", doubled="+str(self.doubled)+", vowel_mark="+self.vowel_mark+", vowel="+self.vowel+", suff="+str(self.suff)

def build_cons_list(basestr, suff):
  instr = basestr + suff
  cons_list = []
  index = 0
  while index < len(instr):
    assert instr[index] in letters, "basestr="+str(basestr)+", index="+str(index)
    cons_info = ConsonantInfo()
    cons_info.cons = instr[index]
    if index >= len(basestr):
      cons_info.suff = True
    index += 1
    if index < len(instr) and instr[index] == o:
      if index >= len(basestr):
        cons_info.suff = True
      cons_info.vowel_mark = o
      cons_info.vowel = o
      cons_info.post_cons_str += o
      index += 1
      cons_list.append(cons_info)
      continue
    if index < len(instr) and instr[index] == ss:
      if index >= len(basestr):
        cons_info.suff = True
      cons_info.doubled = True
      cons_info.post_cons_str += ss
      index += 1
    if index < len(instr) and instr[index] == a:
      if index >= len(basestr):
        cons_info.suff = True
      cons_info.vowel_mark = a
      cons_info.vowel = a
      cons_info.post_cons_str += a
      index += 1
      if index < len(instr) and instr[index] == A:
        if index >= len(basestr):
          cons_info.suff = True
        cons_info.vowel += A
        cons_info.post_cons_str += A
        index += 1
      elif index < (len(instr)-1) and instr[index:(index+1)] == Y:
        if index >= len(basestr):
          cons_info.suff = True
        cons_info.vowel += A
        cons_info.post_cons_str += Y
        index+=2
      elif index < (len(instr)-1) and instr[index:(index+2)] == y+o:
        if index >= len(basestr):
          cons_info.suff = True
        cons_info.vowel += y+o
        cons_info.post_cons_str += y+o
        index += 2
      elif index < (len(instr)-1) and instr[index:(index+2)] == w+o:
        if index >= len(basestr):
          cons_info.suff = True
        cons_info.vowel += w+o
        cons_info.post_cons_str += w+o
        index += 2
      cons_list.append(cons_info)
      continue
    if index < len(instr) and instr[index] == i:
      if index >= len(basestr):
        cons_info.suff = True
      cons_info.vowel_mark = i
      cons_info.vowel = i
      cons_info.post_cons_str += i
      index += 1
      if (index == (len(instr)-1) and instr[index] == y) or (index < (len(instr)-1) and instr[index] == y and instr[index+1] in letters):
        if index >= len(basestr):
          cons_info.suff = True
        cons_info.vowel += y
        cons_info.post_cons_str += y
        index += 1
      cons_list.append(cons_info)
      continue
    if index < len(instr) and instr[index] == u:
      if index >= len(basestr):
        cons_info.suff = True
      cons_info.vowel_mark = u
      cons_info.vowel = u
      cons_info.post_cons_str += u
      index += 1
      if (index == (len(instr)-1) and instr[index] == w) or (index < (len(instr)-1) and instr[index] == w and instr[index+1] in letters):
        if index >= len(basestr):
          cons_info.suff = True
        cons_info.vowel += w
        cons_info.post_cons_str += w
        index += 1
      cons_list.append(cons_info)
      continue
    if index < len(instr) and instr[index] in { N, F, K}:
      if index >= len(basestr):
        cons_info.suff = True
      cons_info.vowel_mark = instr[index]
      cons_info.vowel = instr[index]
      cons_info.post_cons_str += instr[index]
      index += 1
    cons_list.append(cons_info)

  for index in range(1, len(cons_list)):
    this_cons = cons_list[index]
    prev_cons = cons_list[index-1]
    if this_cons.cons == hmz and this_cons.vowel_mark == F and A not in prev_cons.vowel:
      assert(A not in this_cons.vowel)
      this_cons.vowel_mark = a
      this_cons.vowel = this_cons.vowel.replace(F, a)
      this_cons.vowel += A
      this_cons.post_cons_str += A
      cons_list[index] = this_cons

  return cons_list

def print_cons_list(cons_list):
  print("------------")
  for this_cons in cons_list:
    print(this_cons)

def build_str(cons_list):
  retval = ""
  for this_cons in cons_list:
    add_post_str = True
    if this_cons.hmz != "":
      retval += this_cons.hmz
      if this_cons.hmz == A_md:
        add_post_str = False
    else:
      retval += this_cons.cons
    if add_post_str:
      retval += this_cons.post_cons_str
  retval = retval.replace(A+hmz_ab+a+A+hmz_ab+o, A_md)
  return retval

def normalize_hamza(instr):
  instr = instr.replace(A_md, hmz+a+A)
  instr = instr.replace(A+hmz_ab, hmz)
  instr = instr.replace(A+hmz_bl, hmz)
  instr = instr.replace(y+hmz_ab, hmz)
  instr = instr.replace(y+hmz_bl, hmz)
  instr = instr.replace(w+hmz_ab, hmz)
  instr = instr.replace(w+hmz_bl, hmz)
  instr = instr.replace(y_hmz, hmz)
  instr = instr.replace(w_hmz, hmz)
  # remove extra alef after hmz+F for now
  instr = instr.replace(hmz+F+A, hmz+F)
  instr = instr.replace(hmz+ss+F+A, hmz+ss+F)
  return instr

def reduce_hamza_comb_chars(instr):
  instr = instr.replace(A+hmz_ab, A_hmz_ab)
  instr = instr.replace(A+hmz_bl, A_hmz_bl)
  instr = instr.replace(y+hmz_ab, y_hmz)
  instr = instr.replace(y+hmz_bl, y_hmz)
  instr = instr.replace(w+hmz_ab, w_hmz)
  instr = instr.replace(w+hmz_bl, w_hmz)
  #instr = instr.replace(A_md, A+md_ab)
  return instr

def det_hamza_orth(cons_list, cons_list_base):
  for index in range(0, len(cons_list)):
    this_cons = cons_list[index]
    if this_cons.cons == hmz:
      if index == 0:
        # beginning
        if this_cons.vowel == a+A:
          this_cons.hmz = A_md
        elif this_cons.vowel_mark == i:
          this_cons.hmz = A+hmz_bl
        else:
          this_cons.hmz = A+hmz_ab
      elif index == (len(cons_list)-1):
        # end
        prev_cons = cons_list[index-1]
        if (not prev_cons.vowel in { a+A, i+y, u+w, a+y+o, a+w+o } and
          not prev_cons.vowel_mark == o and
          not (prev_cons.cons == w and prev_cons.doubled and prev_cons.vowel_mark == u)):
          if prev_cons.vowel_mark == i:
            this_cons.hmz = y+hmz_ab
          elif prev_cons.vowel_mark == u:
            this_cons.hmz = w+hmz_ab
          else:
            if this_cons.vowel == a+A:
              pass
            else:
              if this_cons.vowel_mark == i:
                this_cons.hmz = A+hmz_bl
              else:
                this_cons.hmz = A+hmz_ab
      else:
        # middle
        prev_cons = cons_list[index-1]
        #next_cons = cons_list[index+1]
        if prev_cons.vowel in { a+A, u+w, i+y, a+y+o, a+w+o }:
          if prev_cons.vowel in { i+y, a+y+o }:
            pass
          elif prev_cons.vowel in { u+w, a+w+o }:
            if this_cons.vowel_mark == i:
              this_cons.hmz = y+hmz_ab
            else:
              if this_cons.vowel == a+A and this_cons.post_cons_str[-1] == A and not this_cons.doubled and not this_cons.suff:
                this_cons.hmz = A_md
              else:
                pass
              #pass
          else:
            if this_cons.vowel_mark == i:
              this_cons.hmz = y+hmz_ab
            elif this_cons.vowel_mark == u:
              this_cons.hmz = w+hmz_ab
            else:
              pass
        elif prev_cons.vowel_mark == o:
          if this_cons.suff or index == (len(cons_list_base)-1):
            pass
          else:
            if this_cons.vowel_mark == i:
              this_cons.hmz = y+hmz_ab
            elif this_cons.vowel_mark == u:
              this_cons.hmz = w+hmz_ab
            else:
              if this_cons.vowel == a+A and this_cons.post_cons_str[-1] == A:
                if this_cons.doubled:
                  pass
                else:
                  this_cons.hmz = A_md
              else:
                this_cons.hmz = A+hmz_ab
        elif this_cons.vowel_mark == o:
          if prev_cons.vowel_mark == i:
            this_cons.hmz = y+hmz_ab
          elif prev_cons.vowel_mark == u:
            this_cons.hmz = w+hmz_ab
          else:
            this_cons.hmz = A+hmz_ab
        else:
          if this_cons.vowel_mark == i or prev_cons.vowel_mark == i:
            this_cons.hmz = y+hmz_ab
          elif this_cons.vowel_mark == u or prev_cons.vowel_mark == u:
            this_cons.hmz = w+hmz_ab
          else:
            if this_cons.vowel == a+A and this_cons.post_cons_str[-1] == A:
              if this_cons.doubled or this_cons.suff:
                pass
              else:
                this_cons.hmz = A_md
            else:
              this_cons.hmz = A+hmz_ab

  apply_tatweel = False
  if apply_tatweel:
    for index in range(1, len(cons_list)-1):
      this_cons = cons_list[index]
      prev_cons = cons_list[index-1]
      if (this_cons.cons == hmz and this_cons.hmz == "" and 
        A not in prev_cons.post_cons_str and
        d not in prev_cons.post_cons_str and
        dh not in prev_cons.post_cons_str and
        r not in prev_cons.post_cons_str and
        z not in prev_cons.post_cons_str and
        w not in prev_cons.post_cons_str):
        this_cons.hmz = tatw+hmz_ab

 
def str_replace_at_index(instr, index, repl_with):
  outstr = instr[:index] + repl_with + instr[(index+1):]
  return outstr

#def process_tanwin_fath(instr):
#  index_F = outstr.rfind(F)
#  if index_F != -1:
#    outstr = str_replace_at_index(outstr, index_F, a)
#    if outstr[-1] == A:
#      outstr = outstr

def hamzate(base_str, suff_str="", pref_str=""):
  base_str = normalize_hamza(base_str)
  suff_str = normalize_hamza(suff_str)
  cons_list = build_cons_list(base_str, suff_str)
  cons_list_base = build_cons_list(base_str, "")
  det_hamza_orth(cons_list, cons_list_base)
  outstr = build_str(cons_list)
  # For debugging:
  #if (base_str == "bada'"):
  #  print_cons_list(cons_list)
  #  print("outstr="+outstr)
  outstr = reduce_hamza_comb_chars(outstr)
  return pref_str + outstr

def test():
  pairs = [
    (("'aAmana", "", ""), "|mana"),
    (("'asolama", "", ""), "A^asolama"),
    (("'uriydu", "", ""), "A^uriydu"),
    (("'isolaAm", "", ""), "A/isolaAm"),
    (("'iymaAn", "", ""), "A/iymaAn"),
    (("'uwxiCa", "", ""), "A^uwxiCa"),
    (("'aAmana", "", "la"), "la|mana"),
    (("'asolama", "", "li"), "liA^asolama"),
    (("'uriydu", "", "fa"), "faA^uriydu"),
    (("'isolaAm", "", "bi"), "biA/isolaAm"),
    (("'iymaAn", "", "bi"), "biA/iymaAn"),
    (("'uwxiCa", "", "fa"), "faA^uwxiCa"),
    (("hayo'ap", "", ""), "hayo'ap"),
    (("xaTiy'ap", "", ""), "xaTiy'ap"),
    (("bariy'", "uwn", ""), "bariy'uwn"),
    (("bariy'", "aAni", ""), "bariy'aAni"),
    (("cayo'u", "hu", ""), "cayo'uhu"),
    (("cayo'a", "hu", ""), "cayo'ahu"),
    (("cayo'i", "hu", ""), "cayo'ihu"),
    (("majiy'u", "hu", ""), "majiy'uhu"),
    (("majiy'a", "hu", ""), "majiy'ahu"),
    (("majiy'i", "hu", ""), "majiy'ihu"),
    (("Aistayo'aAs", "", ""), "Aistayo'aAs"),
    (("Aistiy'aAr", "", ""), "Aistiy'aAr"),
    (("Aistiy'aAlN", "", ""), "Aistiy'aAlN"),
    (("suw'i", "hi", ""), "suwy^ihi"),
    (("Daw'i", "hi", ""), "Dawy^ihi"),
    (("suw'a", "hu", ""), "suw'ahu"),
    (("suw'", "aAn", ""), "suw'aAn"),
    (("tawo'am", "", ""), "tawo'am"),
    (("Dawo'a", "hu", ""), "Dawo'ahu"),
    (("Dawo'", "aAn", ""), "Dawo'aAn"),
    (("suw'u", "hu", ""), "suw'uhu"),
    (("yasuw'", "uwna", ""), "yasuw'uwna"),
    (("nuw'aAn", "", ""), "nuw|n"),
    (("saA'il", "", ""), "saAy^il"),
    (("tasaA'ul", "", ""), "tasaAw^ul"),
    (("tasaA'ala", "", ""), "tasaA'ala"),
    (("qiraA'aAt", "", ""), "qiraA'aAt"),
    (("juzo'", "aAn", ""), "juzo'aAn"),
    (("Eibo'", "aAni", ""), "Eibo'aAni"),
    (("Eibo'", "ayoni", ""), "Eibo'ayoni"),
    (("buTo'a", "hu", ""), "buTo'ahu"),
    (("buTo'", "uhu", ""), "buTo'uhu"),
    (("buTo'", "ihi", ""), "buTo'ihi"),
    (("maso'uwl", "", ""), "masow^uwl"),
    (("taro'iys", "", ""), "taroy^iys"),
    (("miro'aAp", "", ""), "miro|p"),
    (("Zamo'aAnu", "", ""), "Zamo|nu"),
    (("maso'alap", "", ""), "masoA^alap"),
    (("Alomaro'ap", "", ""), "AlomaroA^ap"),
    (("bi'osa", "", ""), "biy^osa"),
    (("mut~aki'", "iyna", ""), "mut~akiy^iyna"),
    (("ra'iys", "", ""), "ray^iys"),
    (("su'aAl", "", ""), "suw^aAl"),
    (("ru'uws", "", ""), "ruw^uws"),
    (("lu'ay~", "", ""), "luw^ay~"),
    (("cana'aAn", "", ""), "cana|n"),
    (("sa'ala", "", ""), "saA^ala"),
    (("ra'aY", "", ""), "raA^aY"),
    (("ra'~asa", "", ""), "raA^~asa"),
    (("ru'~isa", "", ""), "ruy^~isa"),
    (("tafa'~ul", "", ""), "tafaw^~ul"),
    (("yubar~i'", "uwn", ""), "yubar~iy^uwn"),
    (("yubar~a'", "uwn", ""), "yubar~aw^uwn"),
    (("sa'~aAl", "", ""), "sa'~aAl"),
    (("la'~aAl", "", ""), "la'~aAl"),
    (("duEaA'u", "", ""), "duEaA'u"),
    (("suw'u", "", ""), "suw'u"),
    (("jiy'a", "", ""), "jiy'a"),
    (("Dawo'a", "", ""), "Dawo'a"),
    (("cayo'a", "", ""), "cayo'a"),
    (("Eibo'u", "", ""), "Eibo'u"),
    (("caTo'u", "", ""), "caTo'u"),
    (("tabaw~u'", "", ""), "tabaw~u'"),
    (("yuhad~i'u", "", ""), "yuhad~iy^u"),
    (("say~i'u", "", ""), "say~iy^u"),
    (("baTu'a", "", ""), "baTuw^a"),
    (("yahoda'u", "", ""), "yahodaA^u"),
    (("mubotada'i", "", ""), "mubotadaA/i"),
    (("mubotada'F", "", ""), "mubotada'FA"),
    (("mubotada'FA", "", ""), "mubotada'FA"),
    (("mubotadi'F", "", ""), "mubotadiy^FA"),
    (("duEaA'F", "", ""), "duEaA'F"),
    (("duEaA'FA", "", ""), "duEaA'F"),
    (("saq~aA'F", "", ""), "saq~aA'F"),
    (("maloja'F", "", ""), "maloja'FA"),
    (("cayo'F", "", ""), "cayo'FA"),
    (("bado'ap", "", ""), "badoA^ap"),
    (("bada'", "aAt", ""), "bada'aAt"),
    #(("", ""), ""),
  ]

  for pair in pairs:
    base_str = pair[0][0]
    suff_str = pair[0][1]
    pref_str = pair[0][2]
    exp_str = reduce_hamza_comb_chars(pair[1])
    out_str = hamzate(base_str, suff_str, pref_str)
    assert out_str == exp_str, "in=("+base_str+","+suff_str+"), exp="+exp_str+", got="+out_str

test()
