from translit import *

def add_prefix(prefix_str, basestr):
  sun_letters = { 't', 'v', 'd', '*', 'r', 'z', 's', '$', 'S', 'D', 'T', 'Z', 'l', 'n' }
  def_art = (len(prefix_str) >= 2 and prefix_str[-1:] == 'l')  or (len(prefix_str) >= 3 and prefix_str[-2:] == 'lo') # or (len(prefix_str) >= 3 and prefix_str[-3:] == 'lil')
  if def_art and basestr[0] in sun_letters:
    if prefix_str[-1] == 'o':
      prefix_str = prefix_str[:-1]
    return prefix_str + basestr[0] + ss + basestr[1:]
  else:
    return prefix_str + basestr

def get_base_str(basenum, root):
  r1 = root[0]
  r2 = root[-1]
  r3 = root[-1]
  r4 = root[-1]
  r5 = root[-1]
  if (len(root) > 1):
    r2 = root[1]
  if (len(root) > 2):
    r3 = root[2]
  if (len(root) > 3):
    r4 = root[3]
  if (len(root) > 4):
    r5 = root[4]

  basestr = ''
  diptote = False
  if basenum == 1:
    basestr = "1a2o3"
    if r2 == r3:
      basestr = "1a2~"
    elif r2 == A:
      basestr = "1aA3"
  elif basenum == 2:
    basestr = "1i2o3"
    if r2 == r3:
      basestr = "1i2~"
    elif r2 == w or r2 == y:
      basestr = "1iy3"
  elif basenum == 3:
    basestr = "1u2o3"
    if r2 == r3:
      basestr = "1u2~"
    elif r2 == w or r2 == y:
      basestr = "1uw3"
  elif basenum == 4:
    basestr = "1a2a3"
  elif basenum == 5:
    basestr = "1a2i3"
  elif basenum == 6:
    basestr = "1a2u3"
  elif basenum == 7:
    basestr = "1i2a3"
  elif basenum == 8:
    basestr = "1i2i3"
  elif basenum == 9:
    basestr = "1u2a3"
  elif basenum == 10:
    basestr = "1u2u3"
  elif basenum == 11:
    basestr = "1u2~a3"
  elif basenum == 12:
    basestr = "1i2a3~"
  elif basenum == 13:
    basestr = "1u2u3~"
  elif basenum == 14:
    basestr = "'a1o2a3"
    diptote = True
    if r2 == r3:
      basestr = "'a1a2~"
    elif r3 == w or r4 == y:
      basestr = "'a1o2aY"
  elif basenum == 15:
    basestr = "'a1o2i3"
  elif basenum == 16:
    basestr = "'a1o2u3"
  elif basenum == 17:
    basestr = "ma1o2a3"
  elif basenum == 18:
    basestr = "ma1o2i3"
  elif basenum == 19:
    basestr = "ma1o2u3"
  elif basenum == 20:
    basestr = "mi1o2a3"
  elif basenum == 21:
    basestr = "1aA2i3"
  elif basenum == 22:
    basestr = "1a2aA3"
  elif basenum == 23:
    basestr = "1i2aA3"
  elif basenum == 24:
    basestr = "1u2aA3"
  elif basenum == 25:
    basestr = "1a2iy3"
  elif basenum == 26:
    basestr = "1a2uw3"
  elif basenum == 27:
    basestr = "1u2uw3"
  elif basenum == 28:
    basestr = "1a2~aA3"
  elif basenum == 29:
    basestr = "1u2~aA3"
  elif basenum == 30:
    basestr = "1i2~iy3"
  elif basenum == 31:
    basestr = "1a2~uwo3"
  elif basenum == 32:
    basestr = "1u2~awo3"
  elif basenum == 33:
    basestr = "1a2o3aAn"
    diptote = True
  elif basenum == 34:
    basestr = "1i2o3aAn"
  elif basenum == 35:
    basestr = "1u2o3aAn"
  elif basenum == 36:
    basestr = "1a2a3aAn"
  elif basenum == 37:
    basestr = "'a1aA2i3"
    diptote = True
  elif basenum == 38:
    basestr = "'a1o2aA3"
  elif basenum == 39:
    basestr = "'i1o2iy3"
  elif basenum == 40:
    basestr = "1aA2uw3"
  elif basenum == 41:
    basestr = "1awaA2i3"
    if r3 == w or r3 == y:
      basestr = "1awaA2K"
    diptote = True
  elif basenum == 42:
    basestr = "1a2o3aA'"
    diptote = True
  elif basenum == 43:
    basestr = "1u2a3aA'"
    diptote = True
  elif basenum == 44:
    basestr = "ma1aA2i3"
    diptote = True
  elif basenum == 45:
    basestr = "mi1o2aA3"
  elif basenum == 46:
    basestr = "1a2aA'i3"
    diptote = True
  elif basenum == 47:
    basestr = "1a2aA3i4"
    diptote = True
  elif basenum == 48:
    basestr = "1a2o3aA4"
  elif basenum == 49:
    basestr = "1i2o3aA4"
  elif basenum == 50:
    basestr = "1u2o3aA4"
  elif basenum == 51:
    basestr = "1a2o3a4"
  elif basenum == 52:
    basestr = "1i2o3a4"
  elif basenum == 53:
    basestr = "1i2o3i4"
  elif basenum == 54:
    basestr = "1u2o3u4"
  elif basenum == 55:
    basestr = "1u2a3i4"
  elif basenum == 56:
    basestr = "1a1a3~a4"
  elif basenum == 57:
    basestr = "1u1a3~a4"
  elif basenum == 58:
    basestr = "1i2o3a4~"
  elif basenum == 59:
    basestr = "1a2o3a4i5"
  elif basenum == 60:
    basestr = "1a2o3uwt"
  elif basenum == 61:
    basestr = "ta1a2o3u4"
  elif basenum == 62:
    basestr = "ta1o2aA3"
  elif basenum == 63:
    basestr = "ta1aA2i3"
  elif basenum == 64:
    basestr = "ta1aA2iy3"
  elif basenum == 65:
    basestr = "ma1aA2iy3"
    diptote = True
  elif basenum == 66:
    basestr = "1awaA2iy3"
    diptote = True
  elif basenum == 67:
    basestr = "1a2aA3iy4"
    diptote = True
  elif basenum == 68:
    basestr = "'a1o2i3aA'"
    diptote = True
  elif basenum == 69:
    basestr = "'a1aA2iy3"
    diptote = True
  elif basenum == 70:
    basestr = "1a2aA2iy3"
    diptote = True
  elif basenum == 101:
    if len(root) == 4:
      basestr = m + u + r1 + a + r2 + o + r3 + i + r4
    else:
      basestr = r1 + a + A + r2 + i + r3
      if r1 == hmz and (r3 == w or r3 == y):
        basestr = hmz + a + A + r2 + K
      elif r3 == w or r3 == y:
        basestr = r1 + a + A + r2 + K
      elif r1 == hmz and r2 == r3:
        basestr = hmz + a + A + r2 + ss
      elif r2 == w or r2 == y:
        if r1 == hmz:
          basestr = hmz + a + A + hmz + i + r3
        else:
          basestr = r1 + a + A + hmz + i + r3
      elif r1 == hmz:
        basestr = hmz + a + A + r2 + i + r3
      elif r2 == r3:
        basestr = r1 + a + A + r2 + ss
  elif basenum == 102:
    if len(root) == 4:
      basestr = m + u + r1 + a + r2 + o + r3 + a + r4
    else:
      basestr = m + a + r1 + o + r2 + u + w + r3
      if r3 == w:
        basestr = m + a + r1 + o + r2 + u + w + ss
      elif r3 == w:
        basestr = m + a + r1 + o + r2 + i + y + ss
  elif basenum == 103:
    basestr = r1 + a + r2 + o + r3 + a + r4 + a + p
  elif basenum == 201:
    if len(root) == 4:
      basestr = m + u + t + a + r1 + a + r2 + o + r3 + i + r4
    else:
      basestr = m + u + r1 + a + r2 + ss + i + r3
      if r3 == w or r3 == y:
        basestr = m + u + r1 + a + r2 + ss + K
  elif basenum == 202:
    if len(root) == 4:
      basestr = m + u + t + a + r1 + a + r2 + o + r3 + a + r4
    else:
      basestr = m + u + r1 + a + r2 + ss + a + r3
      if r3 == w or r3 == y:
        basestr = m + u + r1 + a + r2 + ss + F + Y
  elif basenum == 203:
    if len(root) == 4:
      basestr = t + a + r1 + a + r2 + o + r3 + u + r4
    else:
      basestr = t + a + r1 + o + r2 + i + y + r3
  elif basenum == 204:
    basestr = t + a + r1 + o + r2 + i + r3 + a + p
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
    basestr = m + u + r1 + a + A + r2 + a + r3 + a + p
    if r2 == r3:
      basestr = m + u + r1 + a + A + r2 + ss + a + p
    elif r3 == w or r3 == y:
      basestr = m + u + r1 + a + A + r2 + a + A + p
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
    basestr = hmz + i + r1 + o + r2 + a + A + r3
    if r1 == hmz and r3 == w or r3 == y:
      basestr = hmz + i + y + r2 + a + A + hmz
    elif r3 == w or r3 == y:
      basestr = hmz + i + r1 + o + r2 + a + A + hmz
    elif r1 == hmz:
      basestr = hmz + i + y + r2 + a + A + r3
    elif r2 == w or r2 == y:
      basestr = hmz + i + r1 + a + A + r3 + p
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
      basestr = '{ino' + r1 + i + r2 + a + A + hmz
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
      basestr = '{i' + r1 + 'oti' + r2 + A + hmz
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
      basestr = '{isoti' + r1 + o + r2 + a + A + hmz
    elif r2 == w or r2 == y:
      basestr = '{isoti' + r1 + a + A + r3 + a + p

  basestr = basestr.replace("aAo", "aA")
  basestr = basestr.replace("iyo", "iy")
  basestr = basestr.replace("uwo", "uw")
  basestr = basestr.replace("1", r1)
  basestr = basestr.replace("2", r2)
  basestr = basestr.replace("3", r3)
  basestr = basestr.replace("4", r4)
  basestr = basestr.replace("5", r5)
  basestr = basestr.replace('{', 'A')
  #printstr = 'input='+numstr_in+',root='+root_in+',out='+basestr
  #if diptote:
  #  basestr += "u"
  return (basestr, diptote)


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

  basenum_str = ''
  post_str = ''
  suffix_str = ''
  prefix_str = ''
  num_started = False
  suf_started = False
  for x in numstr:
    if ord(x) >= ord('0') and ord(x) <= ord('9'):
      num_started = True
      basenum_str += x
    else:
      if x == '"':
        suf_started = True
      else:
        if not num_started:
          prefix_str += x
        else:
          if suf_started:
            suffix_str += x
          else:
            post_str += x

  basenum = int(basenum_str)

  (basestr, is_diptote) = get_base_str(basenum, root)

  if suffix_str != '' or post_str != '':
    if basestr[-1] == 'u':
      basestr = basestr[:-1]
    elif basestr[-1] == 'K':
      if (len(suffix_str) >= 2 and suffix_str[:2] == u+w) or (len(post_str) >= 2 and post_str[:2] == u+w):
        basestr = basestr[:-1]
      else:
        basestr = basestr[:-1] + 'iy'
    elif basestr[-2:] == 'FY':
      basestr = basestr[:-2] + 'aA'

  import hamzater
  hamzated = hamzater.hamzate(basestr+post_str, suffix_str)
  outstr = add_prefix(prefix_str, hamzated)
  #if root == "bd'":
  #  print(str(basenum)+" "+numstr+" "+" "+basestr+" "+hamzated)

  #if suffix_str == 't':
  #  outstr = basestr + a + p
  #elif suffix_str == 'ya':
  #  outstr = basestr + a + Y
  #elif suffix_str == 'yi':
  #  outstr = basestr + i + y + ss
  #elif suffix_str == 'yit':
  #  outstr = basestr + i + y + ss + a + p
  #elif suffix_str == 'At':
  #  if outstr[-1] == p:
  #    outstr = outstr[:-1]
  #  outstr = basestr + a + A + t
  #elif suffix_str == 'uwn':
  #  outstr = basestr + u + w + n

  #remove alef wasla
  return outstr

def test():
  import csv
  with open("num2word_testdata_in.txt") as fin:
    csv_reader = csv.reader(fin, skipinitialspace=True, delimiter=',')
    for line in csv_reader:
      got = num2word(line[0], line[1])
      assert got == line[2], "in="+line[0]+"."+line[1]+", exp="+line[2]+", got="+got

test()

