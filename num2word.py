from translit import *
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
    basestr = r1 + a + w + a + A + r2 + i + w + r3
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
    pass
  elif basenum == 48:
    pass
  elif basenum == 49:
    pass
  elif basenum == 50:
    pass
  elif basenum == 51:
    pass
  elif basenum == 52:
    pass
  elif basenum == 53:
    pass
  elif basenum == 54:
    pass
  elif basenum == 55:
    pass
  elif basenum == 56:
    pass
  elif basenum == 57:
    pass
  elif basenum == 58:
    pass
  elif basenum == 59:
    pass
  elif basenum == 60:
    pass
  elif basenum == 61:
    pass
  elif basenum == 62:
    pass
  elif basenum == 63:
    pass
  elif basenum == 64:
    pass
  elif basenum == 65:
    pass
  elif basenum == 66:
    pass
  elif basenum == 67:
    pass
  elif basenum == 68:
    pass
  elif basenum == 69:
    pass
  elif basenum == 70:
    pass
  #printstr = 'input='+numstr_in+',root='+root_in+',out='+basestr
  #print(printstr)

  outstr = basestr
  if suffix_str != '':
    if basestr[-1] == 'u':
      basestr = basestr[:-1]
  if suffix_str == 't':
    outstr = basestr + a + O
  elif suffix_str == 'ya':
    outstr = basestr + a + Y + dagA
  elif suffix_str == 'yi':
    outstr = basestr + i + y + ss
  elif suffix_str == 'yit':
    outstr = basestr + i + y + ss + a + O

  return outstr
