# Suddo Bangla-hunspell
## To Do
 - [ ] Generate word frequency lists from corpus of old books in wikisource(in progess)
 - [ ] [To understand the dic aff format]([url](https://sites.google.com/a/chromium.org/dev/developers/how-tos/editing-the-spell-checking-dictionaries)).
 - [ ] Find a way to test find word coverage, preferably in firefox or libre writer.
 - [ ] Use wikisource to classify words in to parts of speach (helps with suffixies)

## Progess
1. Generate word frequency lists from the books proofread by bn.wikisource.
   1. Download the epub files by hand from [wikisource](https://bn.wikisource.org/wiki/%E0%A6%9F%E0%A7%87%E0%A6%AE%E0%A6%AA%E0%A7%8D%E0%A6%B2%E0%A7%87%E0%A6%9F:%E0%A6%A8%E0%A6%A4%E0%A7%81%E0%A6%A8_%E0%A6%B2%E0%A7%87%E0%A6%96%E0%A6%BE) to [here](https://github.com/mm-crj/bangla-hunspell/tree/main/epubs/new/),(machine downloads not permited).
    2. Convert them to txt by using [epub_to_txt.sh](https://github.com/mm-crj/bangla-hunspell/blob/main/epub_to_txt.sh) 
    3. Generate the most frequent words using [word_frequency.py](https://github.com/mm-crj/bangla-hunspell/blob/main/word_frequency.py) .
2. Coverage testing can be done in Python using the hunspell package.
3. [Post](https://bn.wikisource.org/wiki/%E0%A6%89%E0%A6%87%E0%A6%95%E0%A6%BF%E0%A6%B8%E0%A6%82%E0%A6%95%E0%A6%B2%E0%A6%A8_%E0%A6%86%E0%A6%B2%E0%A7%8B%E0%A6%9A%E0%A6%A8%E0%A6%BE:%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%A7%E0%A6%BE%E0%A6%A8_%E0%A6%AA%E0%A6%BE%E0%A6%A4%E0%A6%BE#%E0%A6%AC%E0%A6%BE%E0%A6%82%E0%A6%B2%E0%A6%BE_%E0%A6%85%E0%A6%AD%E0%A6%BF%E0%A6%A7%E0%A6%BE%E0%A6%A8_%E0%A6%AE%E0%A7%81%E0%A6%A6%E0%A7%8D%E0%A6%B0%E0%A6%A3_%E0%A6%B8%E0%A6%82%E0%A6%B6%E0%A7%8B%E0%A6%A7%E0%A6%A8) made at wikisource requesting help to transcribe dictionaries. 
## Resources
  ##### Online Resourses
* [SNLTR](https://nltr.itewb.gov.in/downloads.php)
* [Hindi-hunspell](https://github.com/Shreeshrii/hindi-hunspell).
* [sanskrit-hunspell](https://github.com/Shreeshrii/hindi-hunspell/issues/1)
* [Bangla TypeFoundry](https://banglatypefoundry.com/spellchecker/)

###### Description 
Most of the `.dic` and `.aff` files have been extracted and placed in the [resources folder](https://github.com/mm-crj/bangla-hunspell/tree/main/resources). To open any such plugins for firefox, thunderbird or libre office use any archive manager. The Bangla Akademi [word list](https://github.com/mm-crj/bangla-hunspell/tree/main/resources/bangal-akademi-wb) published by SNLTR is in `.doc` format, it has been converted to `.csv` for better utility. Other than that their dictionaries use only the `.dic` file mainly, so it doesn't take advantage of the `.aff` file for compression hence has very low coverage. However I am not well versed in `java` to understand what they are doing with that [plugin](https://github.com/mm-crj/bangla-hunspell/blob/main/resources/snltr/snltrSpellChecker.oxt). Anyhow, the most important resource of all is the [`.dic`](https://github.com/mm-crj/bangla-hunspell/blob/main/resources/bangla-type-foundry/bn-BD.dic) and [`.aff`](https://github.com/mm-crj/bangla-hunspell/blob/main/resources/bangla-type-foundry/bn-BD.aff) files from Bangla Type Foundry. They have done a tremendous job of embedding the grammer rules of the Bangla language into the `dic-aff` format. The idea would be to create a bn-in dictionary following those methods, taking into account the old words(suddo).
