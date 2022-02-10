# hava-dig

A modified digital edition based on *Arabic-English Dictionary for the Use of Students* by J.G. Hava.

The modification is generally in formatting, sometimes in orthography, and occasionally in the text as well.

Work in progress output: https://adamiturabi.github.io/hava-dig/

## To build

1. Install Python3 as `/usr/bin/python3`
2. From a terminal in the root dir: `./run.py`

## Methodology

An OCR of Hava's dictonary is available from archive.com. However, only the English text has been digitized correctly. The Arabic text is basically garbled Roman characters. Also, due to the hybrid left-to-right/right-to-left direction of the columns and pages in the printed volume, the OCR'ed English text needs some page reordering.

So, our methodology is to purge the garbled Latin text which is the output of the OCR of Arabic characters, and to re-order the pages of English text correctly.

Then we manually enter the Arabic text in a separate file. Arabic text may be entered either in Unicode Arabic, Buckwalter transliteration, or using word codes (described below).

These text files are to be found in the `txt` subdirectory.

## Arabic word codes

In order to expedite the manual text input, we make use of word codes. The word codes we are using are used by Salmone in his dictionary.
