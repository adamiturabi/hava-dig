from translit import *

def conj_tri_form1(root, past_vowel, pres_vowel, voice):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  if voice == "passive":
    past_verb = r1 + u + r2 + i + r3 + a
    pres_verb = "yu" + r1 + o + r2 + a + r3 + u
  else:
    past_verb = r1 + "a" + r2 + past_vowel + r3 + "a"
    pres_verb = "ya" + r1 + "o" + r2 + pres_vowel + r3 + "u"
  if r2+r3 == "yy":
    if voice == "passive":
      past_verb = r1 + "u" + r2 + "~a"
    else:
      if past_vowel == "a":
        past_verb = r1 + "a" + r2 + "~a"
      if pres_vowel == "a":
        pres_verb = "ya" + r1 + "o" + "yaY"
      else:
        pres_verb = "ya" + r1 + "o" + "yiy"
  elif r2+r3 == "wy":
    if voice == "passive":
      pass
    else:
      if past_vowel == "a":
        past_verb = r1 + "a" + "waY"
      if pres_vowel == "a":
        pres_verb = "ya" + r1 + "o" + "waY"
      else:
        pres_verb = "ya" + r1 + "o" + "wiy"
  elif r1 == "w" and r3 == "y":
    if voice == "passive":
      pass
    else:
      if past_vowel == "a":
        past_verb = r1 + "a" + r2 + past_vowel + "aY"
      if pres_vowel == "a":
        pres_verb = "ya" + r2 + "aY"
      else:
        pres_verb = "ya" + r2 + "iy"
  elif r2+r3 == "y'":
    if voice == "passive":
      pass
    else:
      if past_vowel != "i":
        past_verb = r1 + "aA'a"
      if pres_vowel == "a":
        pres_verb = "ya" + r1 + "aA'u"
      elif pres_vowel == "i":
        pres_verb = "ya" + r1 + "iy'u"
      else:
        pres_verb = "ya" + r1 + "uwiu"
  elif r3 == "y":
    if voice == "passive":
      pass
    else:
      if past_vowel == "a":
        past_verb = r1 + "a" + r2 + "a" + "Y"
      if pres_vowel == "a":
        pres_verb = "ya" + r1 + "o" + r2 + "aY"
      else:
        pres_verb = "ya" + r1 + "o" + r2 + "iy"
  elif r3 == "w":
    if voice == "passive":
      past_verb = r1 + u + r2 + i + "ya"
    else:
      if past_vowel == "a":
        if r2 == hmz:
          past_verb = r1 + "a" + r2 + "a" + "Y"
        else:
          past_verb = r1 + "a" + r2 + "a" + "A"
      if pres_vowel == "u":
        pres_verb = "ya" + r1 + "o" + r2 + "uw"
  elif r2 == "w":
    if voice == "passive":
      pass
    else:
      if past_vowel != "i":
        past_verb = r1 + "aA" + r3 + "a"
      if pres_vowel == "a":
        pres_verb = "ya" + r1 + "aA" + r3 + "u"
      else:
        pres_verb = "ya" + r1 + "uw" + r3 + "u"
  elif r2 == "y":
    if voice == "passive":
      pass
    else:
      if past_vowel != "i":
        past_verb = r1 + "aA" + r3 + "a"
      if pres_vowel == "a":
        pres_verb = "ya" + r1 + "aA" + r3 + "u"
      else:
        pres_verb = "ya" + r1 + "iy" + r3 + "u"
  elif r1 == "w":
    if voice == "passive":
      pass
    else:
      pres_verb = "ya" + r2 + pres_vowel + r3 + "u"
  elif r2 == r3:
    if voice == "passive":
      past_verb = r1 + u + r2 + "~a"
    else:
      past_verb = r1 + "a" + r2 + "~a"
      pres_verb = "ya" + r1 + pres_vowel + r3 + "~u"
  return (past_verb, pres_verb)

def conj_tri_form2(root, voice):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  if voice == "passive":
    past_verb = r1 + u + r2 + ss + i + r3 + a
    pres_verb = "yu" + r1 + a + r2 + ss + a + r3 + u
  else:
    past_verb = r1 + a + r2 + ss + a + r3 + a
    pres_verb = "yu" + r1 + "a" + r2 + ss + i + r3 + u

  if r3 == y or r3 == w:
    if voice == "passive":
      past_verb = r1 + u + r2 + ss + i + y + a
      pres_verb = "yu" + r1 + a + r2 + ss + a + Y
    else:
      past_verb = r1 + a + r2 + ss + a + Y
      pres_verb =  y + u + r1 + a + r2 + ss + i + y;
  return (past_verb, pres_verb)

def conj_tri_form3(root, voice):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  if voice == "passive":
    past_verb = r1 + u + w + r2 + i + r3 + a
    pres_verb = "yu" + r1 + "aA" + r2 + a + r3 + u
  else:
    past_verb = r1 + a + A + r2 + a + r3 + a
    pres_verb = "yu" + r1 + "aA" + r2 + i + r3 + u

  if r3 == y or r3 == w:
    past_verb = r1 + a + A + r2 + a + Y
    pres_verb =  y + u + r1 + a + A + r2 + i + y;
    if voice == "passive":
      past_verb = r1 + u + w + r2 + i + y + a
  elif r2 == r3:
    past_verb = r1 + a + A + r2 + ss + a
    pres_verb =  y + u + r1 + a + A + r2 + ss + u
    if voice == "passive":
      past_verb = r1 + u + w + r2 + ss + a
  return (past_verb, pres_verb)

def conj_tri_form4(root, voice):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  if voice == "passive":
    past_verb = hmz + u + r1 + o + r2 + i + r3 + a
    pres_verb = "yu" + r1 + o + r2 + a + r3 + u
  else:
    past_verb = hmz + a + r1 + o + r2 + a + r3 + a
    pres_verb = "yu" + r1 + o + r2 + i + r3 + u

  if r3 == y or r3 == w:
    past_verb = hmz + a + r1 + o + r2 + a + Y
    pres_verb = "yu" + r1 + o + r2 + i + y
    if voice == "passive":
      past_verb = hmz + u + r1 + o + r2 + i + y + a
  elif r2 == r3:
    if r1 == hmz:
      past_verb = hmz + a + A + r2 + ss + a
      if voice == "passive":
        past_verb = hmz + u + hmz + i + r2 + ss + a
    else:
      past_verb = hmz + a + r1 + a + r2 + ss + a
      if voice == "passive":
        past_verb = hmz + u + r1 + i + r2 + ss + a
    pres_verb = "yu" + r1 + i + r2 + ss + u
  return (past_verb, pres_verb)

def conj_tri_form5(root, voice):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  past_verb = t + a + r1 + a + r2 + ss + a + r3 + a
  pres_verb = "yata" + r1 + a + r2 + ss + a + r3 + u
  if voice == "passive":
    past_verb = t + u + r1 + u + r2 + ss + i + r3 + a
  if r3 == y or r3 == w:
    past_verb = t + a + r1 + a + r2 + ss + a + Y
    pres_verb = "yata" + r1 + a + r2 + ss + a + Y
    if voice == "passive":
      past_verb = t + u + r1 + u + r2 + ss + i + y + a
  return (past_verb, pres_verb)

def conj_tri_form6(root, voice):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  past_verb = t + a + r1 + a + A + r2 + a + r3 + a
  pres_verb = "yata" + r1 + "aA" + r2 + a + r3 + u
  if voice == "passive":
    past_verb = t + u + r1 + a + A + r2 + a + r3 + a
  if r3 == y or r3 == w:
    past_verb = t + a + r1 + a + A + r2 + a + Y
    pres_verb = "yata" + r1 + "aA" + r2 + a + Y
    if voice == "passive":
      past_verb = t + u + r1 + a + A + r2 + a + Y
  elif r2 == r3:
    past_verb = t + a + r1 + a + A + r2 + ss + a
    pres_verb = "yata" + r1 + "aA" + r2 + ss + u
    if voice == "passive":
      past_verb = t + u + r1 + a + A + r2 + ss + a
  return (past_verb, pres_verb)

def conj_tri_form7(root, voice):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  past_verb = '{ino' + r1 + a + r2 + a + r3 + a
  pres_verb = "yano" + r1 + a + r2 + i + r3 + u
  if voice == "passive":
    past_verb = '{uno' + r1 + u + r2 + i + r3 + a
  if r3 == y or r3 == w:
    past_verb = '{ino' + r1 + a + r2 + a + Y
    pres_verb = "yano" + r1 + a + r2 + i + y
    if voice == "passive":
      past_verb = '{uno' + r1 + u + r2 + i + y + a
  elif r2 == y or r2 == w:
    past_verb = '{ino' + r1 + 'aA' + r3 + a
    pres_verb = "yano" + r1 + 'aA' + r3 + u
    if voice == "passive":
      past_verb = '{uno' + r1 + 'iy' + r3 + a
  elif r2 == r3:
    past_verb = '{ino' + r1 + a + r2 + ss + a
    pres_verb = "yano" + r1 + a + r2 + ss + u
    if voice == "passive":
      past_verb = '{uno' + r1 + i + r2 + ss + a
  return (past_verb, pres_verb)

def conj_tri_form8(root, voice):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  past_verb = '{i' + r1 + 'ota' + r2 + a + r3 + a
  pres_verb = "ya" + r1 + 'ota' + r2 + i + r3 + u
  if r3 == y or r3 == w:
    past_verb = '{i' + r1 + 'ota' + r2 + a + Y
    pres_verb = "ya" + r1 + 'ota' + r2 + i + y
  elif r2 == y or r2 == w:
    past_verb = '{i' + r1 + 'otaA' + r3 + a
    pres_verb = "ya" + r1 + 'otaA' + r3 + u
  elif r2 == r3:
    past_verb = '{i' + r1 + 'ota' + r2 + ss + a
    pres_verb = "ya" + r1 + 'ota' + r2 + ss + u
  return (past_verb, pres_verb)

def conj_tri_form9(root, voice):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  past_verb = '{i' + r1 + 'o' + r2 + a + r3 + ss + a
  pres_verb = "ya" + r1 + 'o' + r2 + a + r3 + ss + u
  return (past_verb, pres_verb)

def conj_tri_form10(root, voice):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  past_verb = '{isota' + r1 + o + r2 + a + r3 + a
  pres_verb = "yasota" + r1 + o + r2 + i + r3 + u
  if r3 == y or r3 == w:
    past_verb = '{isota' + r1 + o + r2 + a + Y
    pres_verb = "yasota" + r1 + o + r2 + i + y
  elif r2 == y or r2 == w:
    past_verb = '{isota' + r1 + 'aA' + r3 + a
    pres_verb = "yasota" + r1 + 'iy' + r3 + u
  elif r2 == r3:
    past_verb = '{isota' + r1 + a + r2 + ss + a
    pres_verb = "yasota" + r1 + i + r2 + ss + u
  return (past_verb, pres_verb)

def conj_tri(root, form, past_vowel, pres_vowel, voice):
  if form == 'I':
    return conj_tri_form1(root, past_vowel, pres_vowel, voice)
  elif form =="II":
    return conj_tri_form2(root, voice)
  elif form =="III":
    return conj_tri_form3(root, voice)
  elif form =="IV":
    return conj_tri_form4(root, voice)
  elif form =="V":
    return conj_tri_form5(root, voice)
  elif form =="VI":
    return conj_tri_form6(root, voice)
  elif form =="VII":
    return conj_tri_form7(root, voice)
  elif form =="VIII":
    return conj_tri_form8(root, voice)
  elif form =="IX":
    return conj_tri_form9(root, voice)
  elif form =="X":
    return conj_tri_form10(root, voice)
  else:
    return ('', '')
def conj_quad(root, form):
  r1 = root[0]
  r2 = root[1]
  r3 = root[2]
  r4 = root[3]
  if form == 'I':
    return r1 + a + r2 + o + r3 + a + r4 + a
  elif form == 'II':
    return t + a + r1 + a + r2 + o + r3 + a + r4 + a
  elif form == 'III':
    return A + i + r1 + o + r2 + a + n + o + r3 + a + r4 + a
  elif form == 'IV':
    return A + i + r1 + o + r2 + a + r3 + a + r4 + ss + a
  else:
    assert False
    return ''
def conj(root, form, vowel="a", tense="pret", voice="active"):
  pret = form
  if len(root) == 2:
    root = root + root[1]
  if len(root) == 3:
    verb_pair = conj_tri(root, form, vowel, vowel, voice)
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
  if len(root) == 4:
    return conj_quad(root, form)
  return verb.replace('{', 'A')


