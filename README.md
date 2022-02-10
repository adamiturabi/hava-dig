# hava-dig

A modified digital edition based on *Arabic-English Dictionary for the Use of Students* by J.G. Hava.

The modification is generally in formatting, sometimes in orthography, and occasionally in the text as well.

Work in progress output: https://adamiturabi.github.io/hava-dig/

## To build

1. Install Python3 as `/usr/bin/python3`
2. From a terminal in the root dir: `./run.sh`

## Methodology

An OCR of Hava's dictonary is available from archive.com. However, only the English text has been digitized correctly. The Arabic text is basically garbled Roman characters. Also, due to the hybrid left-to-right/right-to-left direction of the columns and pages in the printed volume, the OCR'ed English text needs some page reordering.

So, our methodology is to purge the garbled Latin text which is the output of the OCR of Arabic characters, and to re-order the pages of English text correctly.

Then we manually enter the Arabic text in a separate file. Arabic text may be entered either in Unicode Arabic, Buckwalter transliteration, or using word codes (described below).

These text files are to be found in the `txt` subdirectory.

### Arabic word codes

In order to expedite the manual text input, we make use of word codes. Hamza orthography is automatically derived.

Capital Roman numerals are for verb forms. Besides `I` for a triliteral root, these Roman numerals will output the preterite (فعل ماضي) of the current root. 

To suppress the preterite, append the numeral by `x`. For example, 

`VIII` for root `fEl` will output `VIII AifotaEala`  
`VIIIx` for root `fEl` will output `VIII`

For form I triliteral roots `A`, `!` , and `U` will output the preterite with the vowels `a`, `i`, and `u` respectively.

To indicate the vowel for the aorist (فعل مضارع) use `a`, `i`, and either `u` or `o`.

Arabic numerals 1 through 70 will output nouns based on the coding devised by Salmone in his dictionary, with some additions.

For example numeric code `1003` for `current-root=Eml` will output `AisotiEomaAl`

Prefixes and suffixes may be added to the numeric code. Suffixes, if they are integral to the word (like ة) are appended directly to the numeric code. If not integral (like dual and plural suffixes and attached pronouns), they are separated by a `"` double-quote character. This is for correct hamza orthography. 

For example:

for `current root=bd'` the numeric code `1ap` will output `bado>ap`  
for `current root=bd'` the numeric code `4"aAt` will output `bada'aAt`  

For the definite article prefix (prefix that ends with `l`), sun and moon letters are automatically derived. For example 

`Alo1` for root `$ms` will output `Al$~amos`  
`ll1` for root `$ms` will output `ll$~amos`  

To override the current root for any verb or noun append the new root to the numeric code separated by `.`. For example, if the current root is `bdr`, then `I.bydr` will output `I bayodara`

### Foreign borrowings

Hava uses abreviations like P, T, etc. to indicate foreign borrowings. Use the following format: `[Ps]{.fbr}`.

### Roots

Roots are entered preceded by the `@` character on a new line by itself, and only in the Arabic text. For example,

```
@bd'
```

For foreign borrowings, Hava does not show a new root but we do if the root letters are different than the preceding root. Root letters for foreign words are triliteral.

Sometimes Hava will add a new root unalphabetically. For example, `bydr` directly after `bdr`. In this case we won't enter a new root. Instead use the `.<new-root>` format if you need to use a numeric word code.

