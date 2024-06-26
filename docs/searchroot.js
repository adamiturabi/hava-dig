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
  //let root_found = document.getElementById('index_'+normalized_root);
  let root_found = root_index_set.has(normalized_root);
  if (!root_found) {
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
const root_index_set = new Set();
root_index_set.add("أ");
root_index_set.add("أب");
root_index_set.add("أبت");
root_index_set.add("أبث");
root_index_set.add("أبجد");
root_index_set.add("أبد");
root_index_set.add("أبر");
root_index_set.add("أبز");
root_index_set.add("أبس");
root_index_set.add("أبش");
root_index_set.add("أبض");
root_index_set.add("أبط");
root_index_set.add("أبق");
root_index_set.add("أبل");
root_index_set.add("أبن");
root_index_set.add("أبه");
root_index_set.add("أبو");
root_index_set.add("أبي");
root_index_set.add("أتب");
root_index_set.add("أتد");
root_index_set.add("أتش");
root_index_set.add("أتل");
root_index_set.add("أتم");
root_index_set.add("أتن");
root_index_set.add("أتو");
root_index_set.add("أتي");
root_index_set.add("أث");
root_index_set.add("أثر");
root_index_set.add("أثف");
root_index_set.add("أثل");
root_index_set.add("أثم");
root_index_set.add("أثو");
root_index_set.add("أج");
root_index_set.add("أجر");
root_index_set.add("أجز");
root_index_set.add("أجص");
root_index_set.add("أجط");
root_index_set.add("أجل");
root_index_set.add("أجم");
root_index_set.add("أجن");
root_index_set.add("أح");
root_index_set.add("أحد");
root_index_set.add("أحن");
root_index_set.add("أخ");
root_index_set.add("أخذ");
root_index_set.add("أخر");
root_index_set.add("أخو");
root_index_set.add("أخي");
root_index_set.add("أد");
root_index_set.add("أدب");
root_index_set.add("أدر");
root_index_set.add("أدل");
root_index_set.add("أدم");
root_index_set.add("أدو");
root_index_set.add("أدي");
root_index_set.add("أذ");
root_index_set.add("أذر");
root_index_set.add("أذن");
root_index_set.add("أذي");
root_index_set.add("أرب");
root_index_set.add("أرث");
root_index_set.add("أرج");
root_index_set.add("أرخ");
root_index_set.add("أرز");
root_index_set.add("أرس");
root_index_set.add("أرش");
root_index_set.add("أرض");
root_index_set.add("أرف");
root_index_set.add("أرق");
root_index_set.add("أرك");
root_index_set.add("أرم");
root_index_set.add("أرن");
root_index_set.add("أري");
root_index_set.add("أز");
root_index_set.add("أزأ");
root_index_set.add("أزب");
root_index_set.add("أزج");
root_index_set.add("أزح");
root_index_set.add("أزد");
root_index_set.add("أزذ");
root_index_set.add("أزر");
root_index_set.add("أزف");
root_index_set.add("أزق");
root_index_set.add("أزل");
root_index_set.add("أزم");
root_index_set.add("أزي");
root_index_set.add("أس");
root_index_set.add("أست");
root_index_set.add("أسد");
root_index_set.add("أسر");
root_index_set.add("أسف");
root_index_set.add("أسل");
root_index_set.add("أسم");
root_index_set.add("أسن");
root_index_set.add("أسو");
root_index_set.add("أسي");
root_index_set.add("أش");
root_index_set.add("أشب");
root_index_set.add("أشر");
root_index_set.add("أشن");
root_index_set.add("أص");
root_index_set.add("أصد");
root_index_set.add("أصر");
root_index_set.add("أصف");
root_index_set.add("أصل");
root_index_set.add("أض");
root_index_set.add("أط");
root_index_set.add("أطر");
root_index_set.add("أطل");
root_index_set.add("أطم");
root_index_set.add("أف");
root_index_set.add("أفد");
root_index_set.add("أفر");
root_index_set.add("أفس");
root_index_set.add("أفق");
root_index_set.add("أفك");
root_index_set.add("أفل");
root_index_set.add("أفن");
root_index_set.add("أقط");
root_index_set.add("أك");
root_index_set.add("أكد");
root_index_set.add("أكر");
root_index_set.add("أكف");
root_index_set.add("أكل");
root_index_set.add("أكم");
root_index_set.add("أل");
root_index_set.add("ألب");
root_index_set.add("ألج");
root_index_set.add("ألد");
root_index_set.add("ألذ");
root_index_set.add("ألس");
root_index_set.add("ألف");
root_index_set.add("ألق");
root_index_set.add("ألك");
root_index_set.add("ألم");
root_index_set.add("أله");
root_index_set.add("ألو");
root_index_set.add("ألي");
root_index_set.add("أم");
root_index_set.add("أمت");
root_index_set.add("أمج");
root_index_set.add("أمد");
root_index_set.add("أمر");
root_index_set.add("أمس");
root_index_set.add("أمع");
root_index_set.add("أمل");
root_index_set.add("أمن");
root_index_set.add("أمه");
root_index_set.add("أمو");
root_index_set.add("أن");
root_index_set.add("أنب");
root_index_set.add("أنت");
root_index_set.add("أنث");
root_index_set.add("أنس");
root_index_set.add("أنض");
root_index_set.add("أنف");
root_index_set.add("أنق");
root_index_set.add("أنك");
root_index_set.add("أنم");
root_index_set.add("أني");
root_index_set.add("أه");
root_index_set.add("أهب");
root_index_set.add("أهر");
root_index_set.add("أهل");
root_index_set.add("أهن");
root_index_set.add("أو");
root_index_set.add("أوب");
root_index_set.add("أوج");
root_index_set.add("أوح");
root_index_set.add("أوخ");
root_index_set.add("أود");
root_index_set.add("أور");
root_index_set.add("أوز");
root_index_set.add("أوس");
root_index_set.add("أوض");
root_index_set.add("أوف");
root_index_set.add("أوق");
root_index_set.add("أول");
root_index_set.add("أوم");
root_index_set.add("أون");
root_index_set.add("أوه");
root_index_set.add("أوي");
root_index_set.add("أي");
root_index_set.add("أيد");
root_index_set.add("أير");
root_index_set.add("أيس");
root_index_set.add("أيض");
root_index_set.add("أيك");
root_index_set.add("أيم");
root_index_set.add("أين");
root_index_set.add("أيه");
root_index_set.add("ب");
root_index_set.add("بأبأ");
root_index_set.add("بأج");
root_index_set.add("بأر");
root_index_set.add("بأس");
root_index_set.add("بأش");
root_index_set.add("بأط");
root_index_set.add("بأل");
root_index_set.add("بأو");
root_index_set.add("بب");
root_index_set.add("ببج");
root_index_set.add("ببر");
root_index_set.add("ببغ");
root_index_set.add("ببل");
root_index_set.add("ببن");
root_index_set.add("بت");
root_index_set.add("بتر");
root_index_set.add("بتع");
root_index_set.add("بتك");
root_index_set.add("بتل");
root_index_set.add("بث");
root_index_set.add("بثبث");
root_index_set.add("بثر");
root_index_set.add("بثع");
root_index_set.add("بثق");
root_index_set.add("بثن");
root_index_set.add("بثو");
root_index_set.add("بج");
root_index_set.add("بجبج");
root_index_set.add("بجح");
root_index_set.add("بجد");
root_index_set.add("بجر");
root_index_set.add("بجرم");
root_index_set.add("بجس");
root_index_set.add("بجع");
root_index_set.add("بجل");
root_index_set.add("بجم");
root_index_set.add("بح");
root_index_set.add("بحبح");
root_index_set.add("بحت");
root_index_set.add("بحتر");
root_index_set.add("بحث");
root_index_set.add("بحثر");
root_index_set.add("بحر");
root_index_set.add("بحز");
root_index_set.add("بحش");
root_index_set.add("بحص");
root_index_set.add("بحلس");
root_index_set.add("بخ");
root_index_set.add("بخبخ");
root_index_set.add("بخت");
root_index_set.add("بختر");
root_index_set.add("بخثر");
root_index_set.add("بخر");
root_index_set.add("بخز");
root_index_set.add("بخس");
root_index_set.add("بخش");
root_index_set.add("بخشش");
root_index_set.add("بخص");
root_index_set.add("بخع");
root_index_set.add("بخق");
root_index_set.add("بخل");
root_index_set.add("بخنق");
root_index_set.add("بخو");
root_index_set.add("بد");
root_index_set.add("بدأ");
root_index_set.add("بدح");
root_index_set.add("بدخ");
root_index_set.add("بدر");
root_index_set.add("بدرق");
root_index_set.add("بدز");
root_index_set.add("بدع");
root_index_set.add("بدغ");
root_index_set.add("بدل");
root_index_set.add("بدن");
root_index_set.add("بده");
root_index_set.add("بدو");
root_index_set.add("بذ");
root_index_set.add("بذأ");
root_index_set.add("بذج");
root_index_set.add("بذح");
root_index_set.add("بذخ");
root_index_set.add("بذر");
root_index_set.add("بذرق");
root_index_set.add("بذع");
root_index_set.add("بذعر");
root_index_set.add("بذق");
root_index_set.add("بذل");
root_index_set.add("بذم");
root_index_set.add("بذن");
root_index_set.add("بذو");
root_index_set.add("بر");
root_index_set.add("برأ");
root_index_set.add("برأل");
root_index_set.add("بربخ");
root_index_set.add("بربر");
root_index_set.add("بربز");
root_index_set.add("بربس");
root_index_set.add("بربط");
root_index_set.add("بربك");
root_index_set.add("برت");
root_index_set.add("برتع");
root_index_set.add("برث");
root_index_set.add("برثن");
root_index_set.add("برج");
root_index_set.add("برجد");
root_index_set.add("برجس");
root_index_set.add("برجم");
root_index_set.add("برح");
root_index_set.add("برخ");
root_index_set.add("برد");
root_index_set.add("بردخ");
root_index_set.add("بردق");
root_index_set.add("بردو");
root_index_set.add("برذع");
root_index_set.add("برذن");
root_index_set.add("برز");
root_index_set.add("برزخ");
root_index_set.add("برزغ");
root_index_set.add("برس");
root_index_set.add("برسم");
root_index_set.add("برش");
root_index_set.add("برشق");
root_index_set.add("برشم");
root_index_set.add("برص");
root_index_set.add("برض");
root_index_set.add("برطس");
root_index_set.add("برطش");
root_index_set.add("برطل");
root_index_set.add("برطم");
root_index_set.add("برع");
root_index_set.add("برعم");
root_index_set.add("برغث");
root_index_set.add("برغز");
root_index_set.add("برغش");
root_index_set.add("برغل");
root_index_set.add("برغي");
root_index_set.add("برفر");
root_index_set.add("برق");
root_index_set.add("برقش");
root_index_set.add("برقط");
root_index_set.add("برقع");
root_index_set.add("برقل");
root_index_set.add("برك");
root_index_set.add("بركع");
root_index_set.add("بركن");
root_index_set.add("برم");
root_index_set.add("برمل");
root_index_set.add("برمه");
root_index_set.add("برنج");
root_index_set.add("برنس");
root_index_set.add("برني");
root_index_set.add("بره");
root_index_set.add("برهم");
root_index_set.add("برهمن");
root_index_set.add("برهن");
root_index_set.add("برو");
root_index_set.add("بري");
root_index_set.add("بز");
root_index_set.add("بزبز");
root_index_set.add("بزج");
root_index_set.add("بزخ");
root_index_set.add("بزر");
root_index_set.add("بزع");
root_index_set.add("بزغ");
root_index_set.add("بزق");
root_index_set.add("بزل");
root_index_set.add("بزم");
root_index_set.add("بزمخ");
root_index_set.add("بزن");
root_index_set.add("بزو");
root_index_set.add("بس");
root_index_set.add("بسأ");
root_index_set.add("بسبس");
root_index_set.add("بستن");
root_index_set.add("بسر");
root_index_set.add("بسط");
root_index_set.add("بسق");
root_index_set.add("بسل");
root_index_set.add("بسم");
root_index_set.add("بسمل");
root_index_set.add("بسن");
root_index_set.add("بش");
root_index_set.add("بشبش");
root_index_set.add("بشر");
root_index_set.add("بشع");
root_index_set.add("بشق");
root_index_set.add("بشك");
root_index_set.add("بشكر");
root_index_set.add("بشلك");
root_index_set.add("بشلل");
root_index_set.add("بشم");
root_index_set.add("بشن");
root_index_set.add("بشنس");
root_index_set.add("بشنن");
root_index_set.add("بص");
root_index_set.add("بصبص");
root_index_set.add("بصر");
root_index_set.add("بصع");
root_index_set.add("بصق");
root_index_set.add("بصل");
root_index_set.add("بصم");
root_index_set.add("بصو");
root_index_set.add("بض");
root_index_set.add("بضر");
root_index_set.add("بضع");
root_index_set.add("بيدر");
