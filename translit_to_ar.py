translit_map = {
  'E': chr(int('0x0621', 16)),
  '|': chr(int('0x0622', 16)),
  '>': chr(int('0x0623', 16)),
  '&': chr(int('0x0624', 16)),
  '<': chr(int('0x0625', 16)),
  '}': chr(int('0x0626', 16)),
  'A': chr(int('0x0627', 16)),
  'b': chr(int('0x0628', 16)),
  'O': chr(int('0x0629', 16)),
  't': chr(int('0x062a', 16)),
  'v': chr(int('0x062b', 16)),
  'j': chr(int('0x062c', 16)),
  'H': chr(int('0x062d', 16)),
  'x': chr(int('0x062e', 16)),
  'd': chr(int('0x062f', 16)),
  'p': chr(int('0x0630', 16)),
  'r': chr(int('0x0631', 16)),
  'z': chr(int('0x0632', 16)),
  's': chr(int('0x0633', 16)),
  'c': chr(int('0x0634', 16)),
  'S': chr(int('0x0635', 16)),
  'D': chr(int('0x0636', 16)),
  'T': chr(int('0x0637', 16)),
  'P': chr(int('0x0638', 16)),
  'e': chr(int('0x0639', 16)),
  'g': chr(int('0x063a', 16)),
  '_': chr(int('0x0640', 16)),
  'f': chr(int('0x0641', 16)),
  'q': chr(int('0x0642', 16)),
  'k': chr(int('0x0643', 16)),
  'l': chr(int('0x0644', 16)),
  'm': chr(int('0x0645', 16)),
  'n': chr(int('0x0646', 16)),
  'h': chr(int('0x0647', 16)),
  'w': chr(int('0x0648', 16)),
  'Y': chr(int('0x0649', 16)),
  'y': chr(int('0x064a', 16)),
  'F': chr(int('0x064b', 16)),
  'N': chr(int('0x064c', 16)),
  'K': chr(int('0x064d', 16)),
  'a': chr(int('0x064e', 16)),
  'u': chr(int('0x064f', 16)),
  'i': chr(int('0x0650', 16)),
  '~': chr(int('0x0651', 16)),
  'o': chr(int('0x0652', 16)),
  '`': chr(int('0x0670', 16)),
  '{': chr(int('0x0671', 16))
}
def translit_to_ar(instr):
  outstr = ''
  for x in instr:
    if x in translit_map:
      outstr += translit_map[x]
    else:
      outstr += x
  return outstr
