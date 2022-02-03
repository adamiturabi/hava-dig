def get_roots_divs(roots_set):
  out_str = ''
  for root in roots_set:
    out_str += '<div style="visibility: hidden;" id="'+root+'"></div>\n'
  return out_str


