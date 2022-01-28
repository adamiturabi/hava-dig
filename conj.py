def bw_to_ar(inval):
  bw_dict = {
    "A": "ا",
    "b": "ب",
    "t": "ت",
    "v": "ث",
    "j": "ج",
    "H": "ح",
    "x": "خ",
    "d": "د",
    "*": "ذ",
    "r": "ر",
    "z": "ز",
    "s": "ي",
    "$": "س",
    "S": "ص",
    "D": "ض",
    "T": "ط",
    "Z": "ظ",
    "E": "ع",
    "g": "غ",
    "f": "ف",
    "q": "ق",
    "k": "ك",
    "l": "ا",
    "m": "م",
    "n": "ن",
    "h": "ه",
    "w": "و",
    "y": "ي",
    "Y": "ى",
    "'": "ء",
    "F": chr(0x064b),
    "N": chr(0x064c),
    "K": chr(0x064d),
    "a": chr(0x064e),
    "u": chr(0x064f),
    "i": chr(0x0650),
    "~": chr(0x0651),
    "o": chr(0x0652),
    "`": chr(0x0670)
  }
  out_str = ""
  for idx in range(0, len(inval)):
    out_str += bw_dict[inval[idx]]
  return out_str
  
def conj_tri_form1(root, form, past_vowel, pres_vowel):
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
def conj_tri(root, form, past_vowel, pres_vowel):
  if form == 'I':
    return conj_tri_form1(root, form, past_vowel, pres_vowel)
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
      verb = verb_pair[1]
  return verb


