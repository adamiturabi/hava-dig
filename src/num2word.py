from src.translit import *
def num2word(numstr_in, root_in):
  numstr = numstr_in
  dot_index = numstr_in.find('.')
  root = root_in
  if dot_index != -1:
    numstr = numstr_in[:dot_index]
    rootsub = numstr_in[(dot_index+1):]
    for index in range(0, len(rootsub)):
      if rootsub[index] != '-':
        #root[index] = rootsub[index]
        new_root = root[0:index] + rootsub[index]
        if index < len(root):
          new_root += root[(index+1):]
        root = new_root

  r1 = root[0]
  r2 = root[-1]
  r3 = root[-1]
  r4 = root[-1]
  if (len(root) > 1):
    r2 = root[1]
  if (len(root) > 2):
    r3 = root[2]
  if (len(root) > 3):
    r4 = root[3]

  basenum_str = ''
  suffix_str = ''
  for x in numstr:
    if ord(x) >= ord('0') and ord(x) <= ord('9'):
      basenum_str += x
    else:
      suffix_str += x
  basenum = int(basenum_str)
  basestr = ''
  if basenum == 1:
    basestr = r1 + a + r2 + o + r3
    if r2 == r3:
      basestr = r1 + a + r2 + ss
  elif basenum == 2:
    basestr = r1 + i + r2 + o + r3
    if r2 == r3:
      basestr = r1 + i + r2 + ss
  elif basenum == 3:
    basestr = r1 + u + r2 + o + r3
    if r2 == r3:
      basestr = r1 + u + r2 + ss
  elif basenum == 4:
    basestr = r1 + a + r2 + a + r3
  elif basenum == 5:
    basestr = r1 + a + r2 + i + r3
  elif basenum == 6:
    basestr = r1 + a + r2 + u + r3
  elif basenum == 7:
    basestr = r1 + i + r2 + a + r3
  elif basenum == 8:
    basestr = r1 + i + r2 + i + r3
  elif basenum == 9:
    basestr = r1 + u + r2 + a + r3
  elif basenum == 10:
    basestr = r1 + u + r2 + u + r3
  elif basenum == 11:
    basestr = r1 + u + r2 + ss + a + r3
  elif basenum == 12:
    basestr = r1 + i + r2 + a + r3 + ss
  elif basenum == 13:
    basestr = r1 + u + r2 + u + r3 + ss
  elif basenum == 14:
    basestr = E + a + r1 + o + r2 + a + r3 + u
  elif basenum == 15:
    basestr = E + a + r1 + o + r2 + i + r3
  elif basenum == 16:
    basestr = E + a + r1 + o + r2 + u + r3
  elif basenum == 17:
    basestr = m + a + r1 + o + r2 + a + r3
  elif basenum == 18:
    basestr = m + a + r1 + o + r2 + i + r3
  elif basenum == 19:
    basestr = m + a + r1 + o + r2 + u + r3
  elif basenum == 20:
    basestr = m + i + r1 + o + r2 + a + r3
  elif basenum == 21:
    basestr = r1 + a + A + r2 + i + r3
  elif basenum == 22:
    basestr = r1 + a + r2 + a + A + r3
  elif basenum == 23:
    basestr = r1 + i + r2 + a + A + r3
  elif basenum == 24:
    basestr = r1 + u + r2 + a + A + r3
  elif basenum == 25:
    basestr = r1 + a + r2 + i + y + r3
  elif basenum == 26:
    basestr = r1 + a + r2 + u + w + r3
  elif basenum == 27:
    basestr = r1 + u + r2 + u + w + r3
  elif basenum == 28:
    basestr = r1 + a + r2 + ss + a + A + r3
  elif basenum == 29:
    basestr = r1 + u + r2 + ss + a + A + r3
  elif basenum == 30:
    basestr = r1 + i + r2 + ss + i + y + r3
  elif basenum == 31:
    basestr = r1 + a + r2 + ss + u + w + r3
  elif basenum == 32:
    basestr = r1 + u + r2 + ss + u + w + r3
  elif basenum == 33:
    basestr = r1 + a + r2 + o + r3 + a + A + n + u
  elif basenum == 34:
    basestr = r1 + i + r2 + o + r3 + a + A + n
  elif basenum == 35:
    basestr = r1 + u + r2 + o + r3 + a + A + n
  elif basenum == 36:
    basestr = r1 + a + r2 + a + r3 + a + A + n
  elif basenum == 37:
    basestr = E + a + r1 + a + A + r2 + i + r3 + u
  elif basenum == 38:
    basestr = E + a + r1 + o + r2 + a + A + r3
  elif basenum == 39:
    basestr = E + i + r1 + o + r2 + i + y + r3
  elif basenum == 40:
    basestr = r1 + a + A + r2 + u + w + r3
  elif basenum == 41:
    basestr = r1 + a + w + a + A + r2 + i + r3
  elif basenum == 42:
    basestr = r1 + a + r2 + o + r3 + a + A + E + u
  elif basenum == 43:
    basestr = r1 + u + r2 + a + r3 + a + A + E + u
  elif basenum == 44:
    basestr = m + a + r1 + a + A + r2 + i + r3 + u
  elif basenum == 45:
    basestr = m + i + r1 + o + r2 + a + A + r3
  elif basenum == 46:
    basestr = r1 + a + r2 + a + A + E + i + r3 + u
  elif basenum == 47:
    basestr = r1 + a + r2 + a + A + r3 + i + r4 + u
  elif basenum == 48:
    basestr = r1 + a + r2 + o + r3 + a + A + r4
  elif basenum == 49:
    basestr = r1 + i + r2 + o + r3 + a + A + r4
  elif basenum == 50:
    basestr = r1 + u + r2 + o + r3 + a + A + r4
  elif basenum == 51:
    basestr = r1 + a + r2 + o + r3 + a + r4
  elif basenum == 52:
    basestr = r1 + i + r2 + o + r3 + a + r4
  elif basenum == 53:
    basestr = r1 + i + r2 + o + r3 + i + r4
  elif basenum == 54:
    basestr = r1 + u + r2 + o + r3 + u + r4
  elif basenum == 55:
    basestr = r1 + u + r2 + a + r3 + i + r4
  elif basenum == 56:
    basestr = r1 + a + r2 + a + r3 + ss + a + r4
  elif basenum == 57:
    basestr = r1 + u + r2 + a + r3 + ss + a + r4
  elif basenum == 58:
    basestr = r1 + i + r2 + o + r3 + a + r4 + ss
  elif basenum == 59:
    basestr = r1 + a + r2 + o + r3 + a + r4 + i + r4
  elif basenum == 60:
    basestr = r1 + a + r2 + o + r3 + u + w + t
  elif basenum == 61:
    basestr = t + a + r1 + a + r2 + o + r3 + u + r4
  elif basenum == 62:
    basestr = t + a + r1 + o + r2 + a + A + r3
  elif basenum == 63:
    basestr = t + a + r1 + a + A + r2 + i + r3
  elif basenum == 64:
    basestr = t + a + r1 + a + A + r2 + i + y + r3
  elif basenum == 65:
    basestr = m + a + r1 + a + A + r2 + i + y + r3 + u
  elif basenum == 66:
    basestr = r1 + a + w + a + A + r2 + i + y + r3 + u
  elif basenum == 67:
    basestr = r1 + a + r2 + a + A + r3 + i + y + r4 + u
  elif basenum == 68:
    basestr = E + a + r1 + o + r2 + i + r3 + a + A + E + u
  elif basenum == 69:
    basestr = E + a + r1 + a + A + r2 + i + y + r3 + u
  elif basenum == 70:
    basestr = r1 + a + r2 + a + A + r2 + i + y + r3 + u
  elif basenum == 101:
    basestr = r1 + a + A + r2 + i + r3
    if r1 == E and (r3 == w or r3 == y):
      basestr = E + a + A + r2 + K
    elif r3 == w or r3 == y:
      basestr = r1 + a + A + r2 + K
    elif r1 == E and r2 == r3:
      basestr = E + a + A + r2 + ss
    elif r2 == w or r2 == y:
      if r1 == E:
        basestr = E + a + A + E + i + r3
      else:
        basestr = r1 + a + A + E + i + r3
    elif r1 == E:
      basestr = E + a + A + r2 + i + r3
    elif r2 == r3:
      basestr = r1 + a + A + r2 + ss
  elif basenum == 102:
    basestr = m + a + r1 + o + r2 + u + w + r3
    if r3 == w:
      basestr = m + a + r1 + o + r2 + u + w + ss
    elif r3 == w:
      basestr = m + a + r1 + o + r2 + i + y + ss
  elif basenum == 201:
    basestr = m + u + r1 + a + r2 + ss + i + r3
    if r3 == w or r3 == y:
      basestr = m + u + r1 + a + r2 + ss + K
  elif basenum == 202:
    basestr = m + u + r1 + a + r2 + ss + a + r3
    if r3 == w or r3 == y:
      basestr = m + u + r1 + a + r2 + ss + F + Y
  elif basenum == 203:
    basestr = t + a + r1 + o + r2 + i + y + r3
  elif basenum == 204:
    basestr = t + a + r1 + o + r2 + i + r3 + a + O
  elif basenum == 301:
    basestr = m + u + r1 + a + A + r2 + i + r3
    if r3 == w or r3 == y:
      basestr = m + u + r1 + a + A + r2 + K
    elif r2 == r3:
      basestr = m + u + r1 + a + A + r2 + ss
  elif basenum == 302:
    basestr = m + u + r1 + a + A + r2 + a + r3
    if r3 == w or r3 == y:
      basestr = m + u + r1 + a + A + r2 + F + Y
    elif r2 == r3:
      basestr = m + u + r1 + a + A + r2 + ss
  elif basenum == 303:
    basestr = m + u + r1 + a + A + r2 + a + r3 + a + O
    if r2 == r3:
      basestr = m + u + r1 + a + A + r2 + ss + a + O
    elif r3 == w or r3 == y:
      basestr = m + u + r1 + a + A + r2 + a + A + O
  elif basenum == 401:
    basestr = m + u + r1 + o + r2 + i + r3
    if r3 == w or r3 == y:
      basestr = m + u + r1 + o + r2 + K
    elif r2 == r3:
      basestr = m + u + r1 + i + r2 + ss
    elif r2 == w or r2 == y:
      basestr = m + u + r1 + i + y + r3
  elif basenum == 402:
    basestr = m + u + r1 + o + r2 + a + r3
    if r3 == w or r3 == y:
      basestr = m + u + r1 + o + r2 + F + Y
    elif r2 == r3:
      basestr = m + u + r1 + a + r2 + ss
    elif r2 == w or r2 == y:
      basestr = m + u + r1 + a + A + r3
  elif basenum == 403:
    basestr = E + i + r1 + o + r2 + a + A + r3
    if r1 == E and r3 == w or r3 == y:
      basestr = E + i + y + r2 + a + A + E
    elif r3 == w or r3 == y:
      basestr = E + i + r1 + o + r2 + a + A + E
    elif r1 == E:
      basestr = E + i + y + r2 + a + A + r3
    elif r2 == w or r2 == y:
      basestr = E + i + r1 + a + A + r3 + O
  elif basenum == 501:
    basestr = 'muta' + r1 + a + r2 + ss + i + r3
    if r3 == w or r3 == y:
      basestr = 'muta' + r1 + a + r2 + ss + K
  elif basenum == 502:
    basestr = 'muta' + r1 + a + r2 + ss + a + r3
    if r3 == w or r3 == y:
      basestr = 'muta' + r1 + a + r2 + ss + F + Y
  elif basenum == 503:
    basestr = 'ta' + r1 + a + r2 + ss + u + r3
    if r3 == w or r3 == y:
      basestr = 'ta' + r1 + a + r2 + ss + K
  elif basenum == 601:
    basestr = 'muta' + r1 + a + A + r2 + i + r3
    if r3 == w or r3 == y:
      basestr = 'muta' + r1 + a + A + r2 + K
    elif r2 == r3:
      basestr = 'muta' + r1 + a + A + r2 + ss
  elif basenum == 602:
    basestr = 'muta' + r1 + a + A + r2 + a + r3
    if r3 == w or r3 == y:
      basestr = 'muta' + r1 + a + A + r2 + F + Y
    elif r2 == r3:
      basestr = 'muta' + r1 + a + A + r2 + ss
  elif basenum == 603:
    basestr = 'ta' + r1 + a + A + r2 + u + r3
    if r3 == w or r3 == y:
      basestr = 'ta' + r1 + a + A + r2 + K
    elif r2 == r3:
      basestr = 'ta' + r1 + a + A + r2 + ss
  elif basenum == 701:
    basestr = 'muno' + r1 + a + r2 + i + r3
    if r3 == w or r3 == y:
      basestr = 'muno' + r1 + a + r2 + K
    elif r2 == r3:
      basestr = 'muno' + r1 + a + r2 + ss
    elif r2 == w or r2 == y:
      basestr = 'muno' + r1 + a + A + r3
  elif basenum == 702:
    basestr = 'muno' + r1 + a + r2 + a + r3
    if r3 == w or r3 == y:
      basestr = 'muno' + r1 + a + r2 + F + Y
    elif r2 == r3:
      basestr = 'muno' + r1 + a + r2 + ss
    elif r2 == w or r2 == y:
      basestr = 'muno' + r1 + a + A + r3
  elif basenum == 703:
    basestr = '{ino' + r1 + i + r2 + a + A + r3
    if r3 == w or r3 == y:
      basestr = '{ino' + r1 + i + r2 + a + A + E
    elif r2 == w:
      basestr = '{ino' + r1 + i + y + a + A + r3
  elif basenum == 801:
    basestr = 'mu' + r1 + 'ota' + r2 + i + r3
    if r3 == w or r3 == y:
      basestr = 'mu' + r1 + 'ota' + r2 + K
    elif r2 == r3:
      basestr = 'mu' + r1 + 'ota' + r2 + ss
    elif r2 == w or r2 == y:
      basestr = 'mu' + r1 + 'otaA' + r3
  elif basenum == 802:
    basestr = 'mu' + r1 + 'ota' + r2 + a + r3
    if r3 == w or r3 == y:
      basestr = 'mu' + r1 + 'ota' + r2 + F + Y
    elif r2 == r3:
      basestr = 'mu' + r1 + 'ota' + r2 + ss
    elif r2 == w or r2 == y:
      basestr = 'mu' + r1 + 'otaA' + r3
  elif basenum == 803:
    basestr = '{i' + r1 + 'oti' + r2 + a + A + r3
    if r3 == w or r3 == y:
      basestr = '{i' + r1 + 'oti' + r2 + A + E
    elif r2 == w:
      basestr = '{i' + r1 + 'oti' + y + a + A + r3
  elif basenum == 1001:
    basestr = 'musota' + r1 + o + r2 + i + r3
    if r3 == w or r3 == y:
      basestr = 'musota' + r1 + o + r2 + K
    elif r2 == r3:
      basestr = 'musota' + r1 + i + r2 + ss
    elif r2 == w or r2 == y:
      basestr = 'musota' + r1 + 'iy' + r3
  elif basenum == 1002:
    basestr = 'musota' + r1 + o + r2 + a + r3
    if r3 == w or r3 == y:
      basestr = 'musota' + r1 + o + r2 + F + Y
    elif r2 == r3:
      basestr = 'musota' + r1 + a + r2 + ss
    elif r2 == w or r2 == y:
      basestr = 'musota' + r1 + 'aA' + r3
  elif basenum == 1003:
    basestr = '{isoti' + r1 + o + r2 + a + A + r3
    if r3 == w or r3 == y:
      basestr = '{isoti' + r1 + o + r2 + a + A + E
    elif r2 == w or r2 == y:
      basestr = '{isoti' + r1 + a + A + r3 + a + O

  #printstr = 'input='+numstr_in+',root='+root_in+',out='+basestr
  #print(printstr)

  outstr = basestr
  if suffix_str != '':
    if basestr[-1] == 'u':
      basestr = basestr[:-1]
    elif basestr[-1] == 'K':
      basestr = basestr[:-1] + 'iy'
    elif basestr[-2:] == 'FY':
      basestr = basestr[:-2] + 'aA'
  if suffix_str == 't':
    outstr = basestr + a + O
  elif suffix_str == 'ya':
    outstr = basestr + a + Y + dagA
  elif suffix_str == 'yi':
    outstr = basestr + i + y + ss
  elif suffix_str == 'yit':
    outstr = basestr + i + y + ss + a + O

  return outstr
