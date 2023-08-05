# Ìrànlọ́wọ́
[![Build Status](https://travis-ci.com/ruohoruotsi/iranlowo.svg?token=DjfQAQyyoxFCdeCmWju3&branch=master)](https://travis-ci.com/ruohoruotsi/iranlowo)
[![PyPI](https://img.shields.io/pypi/v/iranlowo.svg)](https://pypi.org/project/iranlowo)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/iranlowo.svg)
[![License](https://black.readthedocs.io/en/stable/_static/license.svg)](https://github.com/ruohoruotsi/iranlowo/blob/master/LICENSE)
[![Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Ìrànlọ́wọ́ is a set of utilities to analyze &amp; process Yorùbá text for NLP tasks. The initial focus is on help for diacritic restoration or machine translation.

## Features

### ADR tools
* Strip all diacritics from word-types
* Verify that text is NFC or NFD
* Canonicalize a corpus (from MS Word or elsewhere) &rarr; NFC
* Split long sentences on certain characters like `;`,`:`, etc
* Compute a score of diacritic ambiguity in a given corpus
* Find all variants of all word-type in a given corpus
* Automatically restore correct diacritics using a pre-trained model
* Partially strip diacritics from word-types

### Ready to use webpage scrapers
* Bíbélì Mímọ́
* Yoruba Bible - Bible Society of Nigeria
* Yorùbá Blog
* BBC Yorùbá

### Corpus analysis tools
* Dataset scoring (proximity to correctly diacritized text, lm perplexity, KL divergence)
* dataset character distribution
* dataset ambuiguity statistics &rarr; Lexdif, etc
