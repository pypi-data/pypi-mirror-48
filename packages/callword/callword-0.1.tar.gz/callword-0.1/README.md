# Callword
Represent phone numbers as easy to remember words!

## Setup

`pip install callword`

## Usage

### Map digits to possible words

```
>>> word_dict = callword.read_word_dict()
>>> word_dict['7246837']
['PAINTER']
````

### Find wordified version of phone numbers
```
>>> phone_number = '1-800-724-6837'
>>> wordified_number = callword.number_to_words(phone_number, word_dict)
>>> wordified_number
'1-800-PAINTER'
```


### Find _all_ wordified versions of phone numbers
```
>>> all_wordifications = callword.all_wordifications(phone_number, word_dict)
>>> all_wordifications
['1-800-PAINTER',  '1-800-PAINT-DR', '1-800-SAINT-DR', '1-800-PAINT-37', '1-800-SAINT-37', 
 '1-800-RAG-MUDS', '1-800-RAG-OVER', '1-800-SAG-MUDS', '1-800-SAG-OVER' ...]
```

### Convert wordified phone numbers back to numbers

```
>>> callword.words_to_number(wordified_number) 
'1-800-724-6837'
```

### More Examples

**Checkout our [tests](tests/test_callword.py) for more features...**