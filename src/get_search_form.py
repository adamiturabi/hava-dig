def get_search_form(purpose):
  outstr = """
          <form>
            <div class="mb-3">
              <label for="search_input" class="form-label">Search by root</label>
              <input type="text" class="form-control" id="search_input" aria-describedby="searchHelp" placeholder="Enter root">
              <div id="searchHelp" class="form-text">Enter text in Unicode Arabic or <a href="https://en.wikipedia.org/wiki/Buckwalter_transliteration#Buckwalter_transliteration_table">Buckwalter transliteration</a> format, e.g., اتي or Aty.</div>
            </div>
            <button type="button" class="btn btn-primary" id="btn_submit" onclick="searchRoot()">Submit</button>
            <button type="button" class="btn btn-secondary" id="btn_clear" onclick="clearSearchInput()">Clear input</button>
          </form>
          <p class="py-2" id="outputsearched"></p>
"""
  outstr = outstr.replace('id="search_input"', 'id="'+purpose+'search_input"')
  outstr = outstr.replace('id="searchHelp"', 'id="'+purpose+'searchHelp"')
  outstr = outstr.replace('id="btn_submit"', 'id="'+purpose+'btn_submit"')
  outstr = outstr.replace('id="btn_clear"', 'id="'+purpose+'btn_clear"')
  outstr = outstr.replace('id="outputsearched"', 'id="'+purpose+'outputsearched"')
  outstr = outstr.replace('onclick="searchRoot()"', 'onclick="searchRoot(\''+purpose+'\')"')
  outstr = outstr.replace('onclick="clearSearchInput()"', 'onclick="clearSearchInput(\''+purpose+'\')"')
  return outstr

