# hava-dig

A modified digital edition based on *Arabic-English Dictionary for the Use of Students* by J.G. Hava.

The modification is generally in formatting, sometimes in orthography, and occasionally in the text as well.

Work in progress output: https://adamiturabi.github.io/hava-dig/

## To build

1. Install Python3 as `/usr/bin/python3`
2. From a terminal in the root dir: `./run.sh`

## Differences from Hava's original text

There are the following differences (mostly in typesetting) from Hava's original text.

### Addition of Roman numerals for verb forms

We add Roman numerals (I, II, III, IV, etc.) in the beginning of each verb form.

### Middle vowel for the imperfect verb indicated using Arabic vowel diacritics

We indicate the middle vowel for the imperfect verb indicated using Arabic vowel diacritics instead of the Latin characters: a, i, o. Example:

Original:
<span lang="ar" dir="rtl">بَثَرَ i ، بَثِرَ a</span>

Modified:
<span lang="ar" dir="rtl">بَثَرَ ◌ِ ، بَثِرَ ◌َ</span>

### Masdars in parenthesis

Verbs' masdars in the original text are in the accusative in the original separated by و. Instead, we enclose them in parentheses without any case, and separated by Arabic comma ،. Example:

Original:
<span lang="ar" dir="rtl">بَثَرَ i ، بَثِرَ a بَثْرًا وبَثَرًا وبُثُورًا</span>

Modified:
<span lang="ar" dir="rtl">بَثَرَ ◌ِ ، بَثِرَ ◌َ (بَثْر ، بَثَر ، بُثُور)</span>

## Methodology

An OCR digital text of Hava's dictonary is available from archive.com. However, only the English text has been digitized reliably. Evidently, the OCR did not recognize the Arabic text and output it as garbled Roman characters. Also, due to the hybrid left-to-right/right-to-left direction of the columns and pages in the printed volume, the OCR'ed English text needs some internal page reordering.

So, our methodology is to purge the garbled characters which is the output of the OCR of Arabic characters, and to re-order the pages of English text correctly.

Then we manually enter the Arabic text in a separate file. Arabic text may be entered either in Unicode Arabic, Buckwalter transliteration, or using word codes (described below).

These text files are to be found in the `txt` subdirectory.

### Transliteration

We use the Buckwalter transliteration system with the following additions:

```
c = $ = ش
C = * = ذ
% = U+0653 (maddah above)
^ = U+0654 (hamza above)
/ = U+0655 (hamza below)
```

### Arabic word codes

In order to expedite the manual text input, we make use of word codes. Hamza orthography is automatically derived.

Capital Roman numerals are for verb forms. Besides `I` for a triliteral root in active voice, these Roman numerals will output the preterite (فعل ماضي) of the current root. 

To suppress the preterite, append the numeral by `x`. For example, 

`VIII` for root `fEl` will output `VIII AifotaEala`  
`VIIIx` for root `fEl` will output `VIII`

To get the passive voice append the numeral by `p`. For example,

`VIIIp` for root `bCl` will output `VIII AubotuCila`  

For form I triliteral roots `A`, `!` , and `U` will output the active voice preterite with the vowels `a`, `i`, and `u` respectively.

To indicate the vowel for the aorist (فعل مضارع) use `a`, `i`, and either `u` or `o`.

Arabic numerals 1 through 70 will output nouns based on the coding devised by Salmone in his dictionary, with some additions:

![codes 1-70](https://raw.githubusercontent.com/adamiturabi/hava-dig/master/etc/codes1-70.png)

![codes 100+](https://raw.githubusercontent.com/adamiturabi/hava-dig/master/etc/codes100+.png)

For example numeric code `1003` for `current-root=Eml` will output `AisotiEomaAl`

The intention is that changes due to weak letters should be automatically be taken care of, although this is a work in progress. For example numeric code `403` for `current-root=qwm` should output `<iqaAmap`, not `<iqowaAm`.

Prefixes and suffixes may be added to the numeric code. Suffixes, if they are integral to the word (like ة) are appended directly to the numeric code. If not integral (like dual and plural suffixes and attached pronouns), they are separated by a `"` double-quote character. This is for correct hamza orthography. 

For example:

for `current root=bd'` the numeric code `1ap` will output `bado>ap`  
for `current root=bd'` the numeric code `4"aAt` will output `bada'aAt`  

For the definite article prefix (prefix that ends with `l`), sun and moon letters are automatically derived. For example 

`Alo1` for root `$ms` will output `Al$~amos`  
`ll1` for root `$ms` will output `ll$~amos`  

To override the current root for any verb or noun append the new root to the numeric code separated by `.`. For example, if the current root is `bdr`, then `I.bydr` will output `I bayodara`

In overriding the current root, you may use hyphens for the radicals you don't want to override. For example:

With root `bdw` numeric code `22.--'` will output `badaA'`

### Foreign borrowings

Hava uses abreviations like P, T, etc. to indicate foreign borrowings. Use the following format: `[Ps]{.fbr}`.

### Roots

Roots are entered preceded by the `@` character on a new line by itself, and only in the Arabic text. For example,

```
@bd'
```

For foreign borrowings, Hava does not show a new root but we do if the root letters are different than the preceding root. Root letters for foreign words are usually triliteral, unless they conform to Arabic word patterns in which case they may have more than 3 letters.

Sometimes Hava will add a new root unalphabetically. For example, `bydr` directly after `bdr`. In this case we won't enter a new root. Instead use the `.<new-root>` format if you need to use a numeric word code.

### Colloquialisms

Hava marks colloquialisms with two characters: a four-pointed star, and a square. Use the characters `+` and `=` respectively in the raw text input and the processing scripts will substitute them with similar unicode characters.

### Italic text in English

Use the HTML tags `<i>some text</i>` around text that you want to italicize.

### Arabic inline text in the English definition

If there is some Arabic inline text in the English definition then enclose it thus:

```
To  say  to  a.o.:  (<span lang="ar" dir="rtl">بِأَبِي أَنْتَ</span>)  I  will ransom  thee  with  my  father. 
```

See the root `'by` for the above example.
