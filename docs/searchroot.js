function normalize(instr) {
  let outstr = '';
  for (let i = 0; i < instr.length; i++) {
    let x = instr.charAt(i);
    if (x == 'ء' || x == 'أ' || x == 'a' || x == '\'' || x == 'إ' || x == 'ؤ' || x == 'ئ' || x == 'ا' || x == 'A' || x == '>' || x == '<' || x == '&' || x == '}') {
      outstr += 'أ';
    } else if (x == 'ب' || x == 'b') {
      outstr += 'ب';
    } else if (x == 'ت' || x == 't') {
      outstr += 'ت';
    } else if (x == 'ث' || x == 'v') {
      outstr += 'ث';
    } else if (x == 'ج' || x == 'j') {
      outstr += 'ج';
    } else if (x == 'ح' || x == 'H') {
      outstr += 'ح';
    } else if (x == 'خ' || x == 'x') {
      outstr += 'خ';
    } else if (x == 'د' || x == 'd') {
      outstr += 'د';
    } else if (x == 'ذ' || x == '*') {
      outstr += 'ذ';
    } else if (x == 'ر' || x == 'r') {
      outstr += 'ر';
    } else if (x == 'ز' || x == 'z') {
      outstr += 'ز';
    } else if (x == 'س' || x == 's') {
      outstr += 'س';
    } else if (x == 'ش' || x == '$') {
      outstr += 'ش';
    } else if (x == 'ص' || x == 'S') {
      outstr += 'ص';
    } else if (x == 'ض' || x == 'D') {
      outstr += 'ض';
    } else if (x == 'ط' || x == 'T') {
      outstr += 'ط';
    } else if (x == 'ظ' || x == 'Z') {
      outstr += 'ظ';
    } else if (x == 'ع' || x == 'E') {
      outstr += 'ع';
    } else if (x == 'غ' || x == 'g') {
      outstr += 'غ';
    } else if (x == 'ف' || x == 'f') {
      outstr += 'ف';
    } else if (x == 'ق' || x == 'q') {
      outstr += 'ق';
    } else if (x == 'ك' || x == 'k' || x == 'ک') {
      outstr += 'ك';
    } else if (x == 'ل' || x == 'l') {
      outstr += 'ل';
    } else if (x == 'م' || x == 'm') {
      outstr += 'م';
    } else if (x == 'ن' || x == 'n') {
      outstr += 'ن';
    } else if (x == 'ه' || x == 'h') {
      outstr += 'ه';
    } else if (x == 'و' || x == 'w') {
      outstr += 'و';
    } else if (x == 'ي' || x == 'y' || x == 'Y' || x == 'ى' || x == 'ی') {
      outstr += 'ي';
    }
  }
  return outstr;
}
function searchRoot() {
  let searched_root = document.getElementById('search_input').value;
  let normalized_root = normalize(searched_root);
  let root_found = document.getElementById('index_'+normalized_root);
  if (root_found == null) {
    document.getElementById("outputsearched").innerHTML = 'Submitted root '+normalized_root + ' not found. Either it doesn\'t exist or it hasn\'t been entered yet. You may try to search for roots nearby, or substitute the weak radicals for others (if any), or browse the root entries from the index page.'
  } else {
    document.getElementById("outputsearched").innerHTML = ''
    let filename = '';
    let first_char = normalized_root.charAt(0);
    if (first_char === 'أ') {
      filename = '1.html';
    } else if (first_char === 'ب') {
      filename = '2.html';
    }
    if (filename != '') {
      window.open(filename + '#' + normalized_root, "_self");
    }
  }
}
function clearSearchInput() {
  // clear input text field
  document.getElementById('search_input').value = "";
  document.getElementById("outputsearched").innerHTML = ''
  // put focus back on input text field
  document.getElementById("search_input").focus();
}
$(function(){
  $('#search_input').keypress(function(e){
    if(e.which == 13) {
      e.preventDefault(); // needed otherwise doesn't work on deployment
      //dosomething
      searchRoot();
    }
  })
})
