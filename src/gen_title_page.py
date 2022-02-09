def gen_title_page(num_letters): #, roots_divs):
  with open('docs/index.html', 'w') as fout:
    from src import write_html_pre
    write_html_pre.write_html_pre(fout)
    out_str = """
    <!--
        <div class="container">
          <div class="row justify-content-center"><div class="col-auto text-center" dir="ltr" lang="en"><h1>Arabic-English Dictionary for the Use of Students</h1></div></div>
          <div class="row justify-content-center"><div class="col-auto" dir="ltr" lang="en">by</div></div>
          <div class="row justify-content-center"><div class="col-auto" dir="ltr" lang="en"><h3>J.G. Hava</h3></div></div>
          <div class="row justify-content-center"><div class="col-auto" dir="ltr" lang="en">(Digitization project. Work in progress.)</div></div>
          -->
          <div class="row pt-4 justify-content-end"><div class="col-auto" dir="ltr" lang="en">
"""
    for i in range(1, num_letters+1):
      from src import index2letter
      out_str +='<p><a href="'+str(i)+'.html">Browse roots beginning with ' + index2letter.index2letter(i) + '</a></p>\n'

    out_str += '</div></div>\n'

    #out_str += roots_divs

    out_str += '</div></body></html>\n'
    fout.write(out_str)
