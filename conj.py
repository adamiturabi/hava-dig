from translit import *

def conj_tri_form1(root, past_vowel, pres_vowel):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  past_verb = r1 + "a" + r2 + past_vowel + r3 + "a"
  pres_verb = "ya" + r1 + "o" + r2 + pres_vowel + r3 + "u"
  if r2+r3 == "yy":
    if past_vowel == "a":
      past_verb = r1 + "a" + r2 + "~a"
    if pres_vowel == "a":
      pres_verb = "ya" + r1 + "o" + "yaY`"
    else:
      pres_verb = "ya" + r1 + "o" + "yiy"
  elif r2+r3 == "wy":
    if past_vowel == "a":
      past_verb = r1 + "a" + "waY`"
    if pres_vowel == "a":
      pres_verb = "ya" + r1 + "o" + "waY`"
    else:
      pres_verb = "ya" + r1 + "o" + "wiy"
  elif r1 == "w" and r3 == "y":
    if past_vowel == "a":
      past_verb = r1 + "a" + r2 + past_vowel + "aY`"
    if pres_vowel == "a":
      pres_verb = "ya" + r2 + "aY`"
    else:
      pres_verb = "ya" + r2 + "iy"
  elif r2+r3 == "y'":
    if past_vowel != "i":
      past_verb = r1 + "aA'a"
    if pres_vowel == "a":
      pres_verb = "ya" + r1 + "aA'u"
    elif pres_vowel == "i":
      pres_verb = "ya" + r1 + "iy'u"
    else:
      pres_verb = "ya" + r1 + "uwiu"
  elif r3 == "y":
    if past_vowel == "a":
      past_verb = r1 + "a" + r2 + "a" + "Y`"
    if pres_vowel == "a":
      pres_verb = "ya" + r1 + "o" + r2 + "aY`"
    else:
      pres_verb = "ya" + r1 + "o" + r2 + "iy"
  elif r3 == "w":
    if past_vowel == "a":
      past_verb = r1 + "a" + r2 + "a" + "A"
    if pres_vowel == "u":
      pres_verb = "ya" + r1 + "o" + r2 + "uw"
  elif r2 == "w":
    if past_vowel != "i":
      past_verb = r1 + "aA" + r3 + "a"
    if pres_vowel == "a":
      pres_verb = "ya" + r1 + "aA" + r3 + "u"
    else:
      pres_verb = "ya" + r1 + "uw" + r3 + "u"
  elif r2 == "y":
    if past_vowel != "i":
      past_verb = r1 + "aA" + r3 + "a"
    if pres_vowel == "a":
      pres_verb = "ya" + r1 + "aA" + r3 + "u"
    else:
      pres_verb = "ya" + r1 + "iy" + r3 + "u"
  elif r1 == "w":
    pres_verb = "ya" + r2 + pres_vowel + r3 + "u"
  elif r2 == r3:
    past_verb = r1 + "a" + r2 + "~a"
    pres_verb = "ya" + r1 + pres_vowel + r3 + "~u"
  return (past_verb, pres_verb)

def conj_tri_form2(root):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  past_verb = r1 + a + r2 + ss + a + r3 + a
  pres_verb = "yu" + r1 + "a" + r2 + ss + i + r3 + u
  if r3 == y or r3 == w:
    past_verb = r1 + a + r2 + ss + a + Y + dagA; 
    pres_verb =  y + u + r1 + a + r2 + ss + i + y;
  return (past_verb, pres_verb)

def conj_tri_form3(root):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  past_verb = r1 + a + A + r2 + a + r3 + a
  pres_verb = "yu" + r1 + "aA" + r2 + i + r3 + u
  if r3 == y or r3 == w:
    past_verb = r1 + a + A + r2 + a + Y + dagA; 
    pres_verb =  y + u + r1 + a + A + r2 + i + y;
  elif r2 == r3:
    past_verb = r1 + a + A + r2 + ss + a
    pres_verb =  y + u + r1 + a + A + r2 + ss + u
  return (past_verb, pres_verb)

def conj_tri_form4(root):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  past_verb = E + a + r1 + o + r2 + a + r3 + a
  pres_verb = "yu" + r1 + o + r2 + i + r3 + u
  if r3 == y or r3 == w:
    past_verb = E + a + r1 + o + r2 + a + Y + dagA 
    pres_verb = "yu" + r1 + o + r2 + i + y
  elif r2 == r3:
    past_verb = E + a + r1 + a + r2 + ss + a
    pres_verb = "yu" + r1 + i + r2 + ss + u
  return (past_verb, pres_verb)

def conj_tri_form5(root):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  past_verb = t + a + r1 + a + r2 + ss + a + r3 + a
  pres_verb = "yata" + r1 + a + r2 + ss + a + r3 + u
  if r3 == y or r3 == w:
    past_verb = t + a + r1 + a + r2 + ss + a + Y + dagA 
    pres_verb = "yata" + r1 + a + r2 + ss + a + Y + dagA 
  return (past_verb, pres_verb)

def conj_tri_form6(root):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  past_verb = t + a + r1 + a + A + r2 + a + r3 + a
  pres_verb = "yata" + r1 + "aA" + r2 + a + r3 + u
  if r3 == y or r3 == w:
    past_verb = t + a + r1 + a + A + r2 + a + Y + dagA 
    pres_verb = "yata" + r1 + "aA" + r2 + a + Y + dagA 
  elif r2 == r3:
    past_verb = t + a + r1 + a + A + r2 + ss + a
    pres_verb = "yata" + r1 + "aA" + r2 + ss + u
  return (past_verb, pres_verb)

def conj_tri_form7(root):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  past_verb = '{ino' + r1 + a + r2 + a + r3 + a
  pres_verb = "yano" + r1 + a + r2 + i + r3 + u
  if r3 == y or r3 == w:
    past_verb = '{ino' + r1 + a + r2 + a + Y + dagA 
    pres_verb = "yano" + r1 + a + r2 + i + y
  elif r2 == r3:
    past_verb = '{ino' + r1 + a + r2 + ss + a
    pres_verb = "yano" + r1 + a + r2 + ss + u
  return (past_verb, pres_verb)

def conj_tri_form8(root):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  past_verb = '{i' + r1 + 'ota' + r2 + a + r3 + a
  pres_verb = "ya" + r1 + 'ota' + r2 + i + r3 + u
  if r3 == y or r3 == w:
    past_verb = '{i' + r1 + 'ota' + r2 + a + Y + dagA 
    pres_verb = "ya" + r1 + 'ota' + r2 + i + y
  elif r2 == r3:
    past_verb = '{i' + r1 + 'ota' + r2 + ss + a
    pres_verb = "ya" + r1 + 'ota' + r2 + ss + u
  return (past_verb, pres_verb)

def conj_tri_form9(root):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  past_verb = '{i' + r1 + 'o' + r2 + a + r3 + ss + a
  pres_verb = "ya" + r1 + 'o' + r2 + a + r3 + ss + u
  return (past_verb, pres_verb)

def conj_tri_form10(root):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  past_verb = '{isota' + r1 + o + r2 + a + r3 + a
  pres_verb = "yasota" + r1 + o + r2 + i + r3 + u
  if r3 == y or r3 == w:
    past_verb = '{isota' + r1 + o + r2 + a + y + dagA
    pres_verb = "yasota" + r1 + o + r2 + i + y
  elif r2 == r3:
    past_verb = '{isota' + r1 + a + r2 + ss + a
    pres_verb = "yasota" + r1 + i + r2 + ss + u
  return (past_verb, pres_verb)

def conj_tri(root, form, past_vowel, pres_vowel):
  if form == 'I':
    return conj_tri_form1(root, past_vowel, pres_vowel)
  elif form =="II":
    return conj_tri_form2(root)
  elif form =="III":
    return conj_tri_form3(root)
  elif form =="IV":
    return conj_tri_form4(root)
  elif form =="V":
    return conj_tri_form5(root)
  elif form =="VI":
    return conj_tri_form6(root)
  elif form =="VII":
    return conj_tri_form7(root)
  elif form =="VIII":
    return conj_tri_form8(root)
  elif form =="IX":
    return conj_tri_form9(root)
  elif form =="X":
    return conj_tri_form10(root)
  else:
    return ('', '')
def conj(root, form, vowel="a", tense="pret"):
  pret = form
  if len(root) == 2:
    root = root + root[1]
  if len(root) == 3:
    verb_pair = conj_tri(root, form, vowel, vowel)
    #print(verb_pair[0])
    #print(bw_to_ar(verb_pair[1]))
    verb = verb_pair[0]
    if tense == "ao":
      #verb = verb_pair[1]
      arvowel = ''
      if vowel == 'a':
        arvowel = a
      elif vowel == 'i':
        arvowel = i
      elif vowel == 'o' or vowel == 'u':
        arvowel = u
      verb = chr(int('0x25cc', 16)) + arvowel
  return verb


