def get_roots_divs(roots_set):
  out_str = ''
  for root in sorted(roots_set):
    out_str += '<div style="visibility: hidden;" id="index_'+root+'"></div>\n'
  return out_str


