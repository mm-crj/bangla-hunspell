# Suddo Bangla-hunspell
## To Do
 - [ ] Generate word frequency lists from corpus of old books in wikisource(in progess)
 - [ ] [To understand the dic aff format]([url](https://sites.google.com/a/chromium.org/dev/developers/how-tos/editing-the-spell-checking-dictionaries)).
 - [ ] Find a way to test find word coverage, preferably in firefox or libre writer.
 - [ ] Use wikisource to classify words in to parts of speach (helps with suffixies)

## Progess
1. Generate word frequency lists from the books proofread by bn.wikisource.
  1. Download the epub files by hand from [wikisource](https://bn.wikisource.org/wiki/%E0%A6%9F%E0%A7%87%E0%A6%AE%E0%A6%AA%E0%A7%8D%E0%A6%B2%E0%A7%87%E0%A6%9F:%E0%A6%A8%E0%A6%A4%E0%A7%81%E0%A6%A8_%E0%A6%B2%E0%A7%87%E0%A6%96%E0%A6%BE) to [here](),(machine downloads not permited).
  2. Convert them to txt by using [epub_to_txt.sh]() 
  3. Generate the most frequent words using [word_frequency.py]() .
2. Coverage testing can be done in Python using the hunspell package.
3. Post made at wikisource requesting help to transcribe dictionaries. 
## Resources
- [ ] [SNLTR](https://nltr.itewb.gov.in/downloads.php)
- [ ] [Hindi-hunspell](https://github.com/Shreeshrii/hindi-hunspell).
- [ ] [sanskrit-hunspell](https://github.com/Shreeshrii/hindi-hunspell/issues/1)
- [ ] [Bangla TypeFoundry](https://banglatypefoundry.com/spellchecker/)
