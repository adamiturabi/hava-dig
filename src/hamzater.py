from src import translit

harakaat_and_sukoon = { a, u, i, ss, o, F, N, K }
letters = {A, b, p, t, v, j, H, x, d, dh, r, z, s, sh, S, D, T, Z, E, g, f, q, k, l, m, n, h, w, Y, y , hmz, Awasl}

class ConsonantInfo:
  cons = ""
  doubled = False
  vowel_mark = ""
  vowel = ""
  hmz = ""
  post_cons_str = ""
  def __str__(self):
    return "cons="+self.cons+", doubled="+str(self.doubled)+", vowel_mark="+self.vowel_mark+", vowel="+self.vowel

def build_cons_list(instr):
  cons_list = []
  index = 0
  while index < len(instr):
    if instr[index] not in letters:
      print(index)
      assert(False)
    cons_info = ConsonantInfo()
    cons_info.cons = instr[index]
    index += 1
    if index < len(instr) and instr[index] == o:
      cons_info.vowel_mark = o
      cons_info.vowel = o
      cons_info.post_cons_str += o
      index += 1
      cons_list.append(cons_info)
      continue
    if index < len(instr) and instr[index] == ss:
      cons_info.doubled = True
      cons_info.post_cons_str += ss
      index += 1
    if index < len(instr) and instr[index] == a:
      cons_info.vowel_mark = a
      cons_info.vowel = a
      cons_info.post_cons_str += a
      index += 1
      if index < len(instr) and instr[index] == A:
        cons_info.vowel += A
        cons_info.post_cons_str += A
        index += 1
      elif index < (len(instr)-1) and instr[index:(index+2)] == Y:
        cons_info.vowel += A
        cons_info.post_cons_str += Y:
        index+=2
      elif index < (len(instr)-1) and instr[index:(index+2)] == y+o:
        cons_info.vowel += y+o
        cons_info.post_cons_str += y+o
        index += 2
      elif index < (len(instr)-1) and instr[index:(index+2)] == w+o:
        cons_info.vowel += w+o
        cons_info.post_cons_str += w+o
        index += 2
      cons_list.append(cons_info)
      continue
    if index < len(instr) and instr[index] == i:
      cons_info.vowel_mark = i
      cons_info.vowel = i
      cons_info.post_cons_str += i
      index += 1
      if (index == (len(instr)-1) and instr[index] == y) or (index < (len(instr)-1) and instr[index] == y and instr[index+1] in letters):
        cons_info.vowel += y
        cons_info.post_cons_str += y
        index += 1
      cons_list.append(cons_info)
      continue
    if index < len(instr) and instr[index] == u:
      cons_info.vowel_mark = u
      cons_info.vowel = u
      cons_info.post_cons_str += u
      index += 1
      if (index == (len(instr)-1) and instr[index] == w) or (index < (len(instr)-1) and instr[index] == w and instr[index+1] in letters):
        cons_info.vowel += w
        cons_info.post_cons_str += w
        index += 1
      cons_list.append(cons_info)
      continue
    if index < len(instr) and instr[index] in { N, F, K}:
      cons_info.vowel_mark = instr[index]
      cons_info.vowel = instr[index]
      cons_info.post_cons_str += instr[index]
      index += 1
    cons_list.append(cons_info)
  return cons_list

def print_cons_list(cons_list):
  print("------------")
  for x in cons_list:
    print(x)

def build_str(cons_list):
  retval = ""
  for x in cons_list:
    add_post_str = True
    if x.hmz != "":
      retval += x.hmz
      if x.hmz == A_md:
        add_post_str = False
    else:
      retval += x.cons
    if add_post_str:
      retval += x.post_cons_str
  retval = retval.replace(A+hmz_ab+a+A+hmz_ab+o, A_md)
  return retval

def hamzate(instr):
  cons_list = build_cons_list(instr)
  for index in range(0, len(cons_list)):
    x = cons_list[index]
    if x.cons == hmz:
      if index == 0:
        # beginning
        if x.vowel == a+A:
          x.hmz = A_md
        elif x.vowel_mark == i:
          x.hmz = A+hmz_bl
        else:
          x.hmz = A+hmz_ab
      elif index == (len(cons_list)-1):
        # end
        prev_cons = cons_list[index-1]
        if (not prev_cons.vowel in { a+A, i+y, u+w, a+y+o, a+w+o } and
          not prev_cons.vowel_mark == o and
          not (prev_cons.cons == w and prev_cons.doubled and prev_cons.vowel_mark == u)):
          if prev_cons.vowel_mark == i:
            x.hmz = y+hmz_ab
          elif prev_cons.vowel_mark == u:
            x.hmz = w+hmz_ab
          else:
            if x.vowel_mark == i:
              x.hmz = A+hmz_bl
            else:
              x.hmz = A+hmz_ab
      else:
        # middle
        prev_cons = cons_list[index-1]
        #next_cons = cons_list[index+1]
        if prev_cons.vowel in { a+A, u+w, i+y, a+y+o, a+w+o }:
          if prev_cons.vowel in { i+y, a+y+o }:
            pass
          elif prev_cons.vowel in { u+w, a+w+o }:
            if x.vowel_mark == i:
              x.hmz = y+hmz_ab
            else:
              if x.vowel == a+A and x.post_cons_str[-1] == A:
                x.hmz = A_md
              else:
                pass
              #pass
          else:
            if x.vowel_mark == i:
              x.hmz = y+hmz_ab
            elif x.vowel_mark == u:
              x.hmz = w+hmz_ab
            else:
              pass
        elif prev_cons.vowel_mark == o:
          if x.vowel_mark == i:
            x.hmz = y+hmz_ab
          elif x.vowel_mark == u:
            x.hmz = w+hmz_ab
          else:
            if x.vowel == a+A and x.post_cons_str[-1] == A:
              if x.doubled:
                pass
              else:
                x.hmz = A_md
            else:
              x.hmz = A+hmz_ab
        elif x.vowel_mark == o:
          if prev_cons.vowel_mark == i:
            x.hmz = y+hmz_ab
          elif prev_cons.vowel_mark == u:
            x.hmz = w+hmz_ab
          else:
            x.hmz = A+hmz_ab
        else:
          if x.vowel_mark == i or prev_cons.vowel_mark == i:
            x.hmz = y+hmz_ab
          elif x.vowel_mark == u or prev_cons.vowel_mark == u:
            x.hmz = w+hmz_ab
          else:
            if x.vowel == a+A and x.post_cons_str[-1] == A:
              if x.doubled:
                pass
              else:
                x.hmz = A_md
            else:
              x.hmz = A+hmz_ab

  apply_tatweel = False
  if apply_tatweel:
    for index in range(1, len(cons_list)-1):
      x = cons_list[index]
      prev_cons = cons_list[index-1]
      if (x.cons == hmz and x.hmz == "" and 
        A not in prev_cons.post_cons_str and
        d not in prev_cons.post_cons_str and
        dh not in prev_cons.post_cons_str and
        r not in prev_cons.post_cons_str and
        z not in prev_cons.post_cons_str and
        w not in prev_cons.post_cons_str):
        x.hmz = tatw+hmz_ab

  outstr = build_str(cons_list)
  return outstr

do_test = False
if do_test:
  word_list = ["ءِسْلَام", "ءَامَنَ", "ءَسْلَمَ", "ءُرِيدُ", "ءِسْلَام", "ءِيمَان", "ءُوخِذَ", "دُعَاءُ", "سُوءُ", "جِيءَ", "ضَوْءَ", "شَيْءَ", "بُطْءُ", "عِبْءُ", "شَطْءُ", "تَبَوُّءُ", "يُهَدِّء", "سَيِّء", "بَطُء", "يَهْدَء", "مُبْتَدَء", "هَيْءَة", "خَطِيءَة", "بَرِيءُونَ", "بَرِيءَانِ", "بَرِيءِينَ", "بَرِيءَيْنِ", "شَيْءُهُ", "شَيْءَهُ", "شَيْءِهِ", "شَيْءَانِ", "شَيْءَيْنِ", "مَجِيءُهُ", "مَجِيءَهُ", "مَجِيءِهِ", "سُوءِهِ", "ضَوْءِهِ", "سُوءَهُ", "سُوءَانِ", "تَوْءَم", "ضَوْءَهُ", "ضَوْءَانِ", "سُوءُهُ", "يَسُوءُونَ", "سَاءِل", "تَسَاءُل", "تَسَاءَلَ", "قِرَاءَات", "جُزْءَانِ", "عِبْءَانِ", "عِبْءَيْنِ", "بُطْءَهُ", "بُطْءُهُ", "بُطْءِهِ", "مَسْءُول", "تَرْءِيس", "مِرْءَاة", "ظَمْءَان", "مَسْءَلَة", "الْمَرْءَة", "بِءْسَ", "سُءْلَكَ", "كَءْس", "سُءِلَ", "يَءِسَ", "مُتَّكِءِينَ", "رَءِيس", "سُءَال", "رُءُوس", "لُءَيّ", "شَنَءَان", "سَءَلَ", "رَءَىٰ", "رَءَسَ", "يُرَءِسُ", "رُءِّسَ", "تَفَءُّل", "يُبَرِّءُونَ", "يُبَرَّءُونَ", "سَءَّال", "لَءَّال"]

  for x in word_list:
    print(hamzate(x))

#import sys
#print(hamzate(sys.argv[1]))

