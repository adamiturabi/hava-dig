def write_html_pre(fout):
  outstr = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
    <head><!-- Required meta tags -->
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/><!-- Bootstrap CSS -->
        <!--<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"/>-->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.rtl.min.css" integrity="sha384-gXt9imSW0VcJVHezoNQsP+TNrjYXoGcrqBZJpry9zJt8PCQjobwmhMGaDHTASo9N" crossorigin="anonymous">
        <style> 
          @font-face {
              font-family: AmiriWeb;
              font-style: normal;
              font-weight: 400;
              src: url('./fonts/Amiri-Regular.woff2') format('woff2'),
                   url('./fonts/Amiri-Regular.woff') format('woff');
          }
          :lang(ar) {
            -moz-font-feature-settings:"calt=1, liga=1, clig=1, kern=1";
            -moz-font-feature-settings:"calt", "liga", "clig", "kern";
            -ms-font-feature-settings:"calt", "liga", "clig", "kern";
            -webkit-font-feature-settings:"calt", "liga", "clig", "kern";
            font-feature-settings:"calt", "liga", "clig", "kern";
            text-rendering: optimizeLegibility;
            font-family: "AmiriWeb", serif;
            font-size: 1.0em;
            line-height: 100%;
          }
          :lang(en) {
            font-family: "AmiriWeb", serif;
          }
          .foreignborrowing {
            font-variant: small-caps;
          }
          .container {
            max-width: 400px;
          }
        </style>
        <title>Hava: Arabic-English Dictionary</title>
        <script src="searchroot.js"/>
    </head>
    <body>
        <!--<h1>Hava's Arabic Dictionary</h1>-->
        <!-- Optional JavaScript; choose one of the two! -->
        <!-- Option 1: Bootstrap Bundle with Popper -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
        <!-- Option 2: Separate Popper and Bootstrap JS -->
        <!-- <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
    -->
        <div class="container">
          <div class="row justify-content-center"><div class="col-auto text-center" dir="ltr" lang="en"><h1>Arabic-English Dictionary for the Use of Students</h1></div></div>
          <div class="row justify-content-center"><div class="col-auto" dir="ltr" lang="en">by</div></div>
          <div class="row justify-content-center"><div class="col-auto" dir="ltr" lang="en"><h3>J.G. Hava</h3></div></div>
          <div class="row justify-content-center"><div class="col-auto" dir="ltr" lang="en">
          (Digitization project. Work in progress.)
          </div></div>
          <div class="row pb-3 justify-content-center"><div class="col-auto" dir="ltr" lang="en">
          <a href="https://github.com/adamiturabi/hava-dig">Github development page</a>
          </div></div>
          <!--<div class="row justify-content-center"><div class="col-auto" dir="ltr" lang="en">
          <input type="text" id="textinput" placeholder="Search for root (Buckwalter or Unicode Arabic)"/>
          <button type="button" id="btn2" onclick="searchRoot()">Search</button>
          <p id=outputsearched></p>
          </div></div>-->
          <div class="row justify-content-center"><div class="col-auto" dir="ltr" lang="en">
          <form>
            <div class="mb-3">
              <label for="search_input" class="form-label">Search by root</label>
              <input type="text" class="form-control" id="search_input" aria-describedby="searchHelp" placeholder="Enter root">
              <div id="searchHelp" class="form-text">Use Unicode Arabic or <a href="https://en.wikipedia.org/wiki/Buckwalter_transliteration#Buckwalter_transliteration_table">Buckwalter transliteration</a>, e.g., ءتي or 'ty.</div>
            </div>
            <button type="button" class="btn btn-primary" id="btn_submit" onclick="searchRoot()">Submit</button>
            <button type="button" class="btn btn-secondary" id="btn_clear" onclick="clearSearchInput()">Clear input</button>
          </form>
          </div></div>
"""
  fout.write(outstr)
