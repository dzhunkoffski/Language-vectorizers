# Language-vectorizers

## Project description:
This project contains the code, that is used to make the word embedding dictionary (based on the LSM technique) both for Chinese and Bengali languages. 

### Parsers
Building the word embedding dictionary with LSM technique requires texts (literary are preferred). This folder contains scripts I have written to parse online library for Chinese and Bengali literary texts using Selenium. I both cases, the parsing process consists of two stages:

1) Parsing of direct links to a text file (get_text_link.py);
2) Getting the text from the links received below (link2text.py);

### Builders
This folder contains notebooks with code, that is used to preprocess language corpora and make the word embedding dictionary from set of the preprocessed texts.
