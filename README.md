# NFDI

The Python library **NFDI** provides:
* basic information about [NFDI](https://www.nfdi.de) (also known as Nationale ForschungsDatenInfrastruktur and [National Research Data Infrastructure](https://www.dfg.de/en/research_funding/programmes/nfdi/index.html)) and all funded NFDI consortia,
* support for [Wikidata WikiProject NFDI](https://www.wikidata.org/wiki/Wikidata:WikiProject_NFDI) aimed to create and edit the Wikidata entities and entity schemas relevant for NFDI.

## Table of contents
* [Installation](#installation)
* [How to use](#how-to-use)
* [NFDI Jupyter Book](#nfdi-jupyter-book)

## Installation

```shell
pip install NFDI
```

## How to use

### Module `info`

The module `info` has classes `consortium` and `consortia`:

```python
from nfdi import info
nfdi = info.consortia()
berd = info.consortium('BERD@NFDI')
```

The instance `nfdi` has the following attributes: 'label', 'homepage', 'wikidata', 'github', 'google', 'linkedin', 'twitter', 'youtube', 'zenodo', 'labels', 'consortia'. For example:
```python
nfdi.twitter
```
prints
```shell
"https://twitter.com/NFDI_de"
```

The instances `nfdi` and `berd` have the methods `print`, `dict` and `_wikidata`:
 ```python
json = berd._wikidata()
nfdi.print()
```

The `json` variable contains JSON representation of the corresponding entity at Wikidata including labels, aliases and descriptions:
```python
print('LABELS', json.get('labels'))
print('DESCRIPTIONS', json.get('descriptions'))
print('ALIASES', json.get('aliases'))
```
It prints:
```shell
LABELS {'en': {'language': 'en', 'value': 'BERD@NFDI'}, 'de': {'language': 'de', 'value': 'BERD@NFDI'}, 'fr': {'language': 'fr', 'value': 'BERD@NFDI'}, 'bar': {'language': 'bar', 'value': 'BERD@NFDI'}, 'de-at': {'language': 'de-at', 'value': 'BERD@NFDI'}, 'de-ch': {'language': 'de-ch', 'value': 'BERD@NFDI'}, 'de-formal': {'language': 'de-formal', 'value': 'BERD@NFDI'}, 'en-ca': {'language': 'en-ca', 'value': 'BERD@NFDI'}, 'en-gb': {'language': 'en-gb', 'value': 'BERD@NFDI'}, 'es': {'language': 'es', 'value': 'BERD@NFDI'}, 'nl': {'language': 'nl', 'value': 'BERD@NFDI'}, 'pt': {'language': 'pt', 'value': 'BERD@NFDI'}, 'simple': {'language': 'simple', 'value': 'BERD@NFDI'}}
DESCRIPTIONS {'en': {'language': 'en', 'value': 'NFDI consortium for Business, Economic and Related Data (Social and Behavioural Sciences)'}, 'de': {'language': 'de', 'value': 'NFDI für Wirtschaftsdaten und Verwandtes (Sozial- und Verhaltenswissenschaften)'}}
ALIASES {'en': [{'language': 'en', 'value': 'BERD-NFDI'}], 'de': [{'language': 'de', 'value': 'BERD-NFDI'}], 'fr': [{'language': 'fr', 'value': 'BERD-NFDI'}], 'bar': [{'language': 'bar', 'value': 'BERD-NFDI'}], 'de-at': [{'language': 'de-at', 'value': 'BERD-NFDI'}], 'de-ch': [{'language': 'de-ch', 'value': 'BERD-NFDI'}], 'de-formal': [{'language': 'de-formal', 'value': 'BERD-NFDI'}], 'en-ca': [{'language': 'en-ca', 'value': 'BERD-NFDI'}], 'en-gb': [{'language': 'en-gb', 'value': 'BERD-NFDI'}], 'es': [{'language': 'es', 'value': 'BERD-NFDI'}], 'nl': [{'language': 'nl', 'value': 'BERD-NFDI'}], 'pt': [{'language': 'pt', 'value': 'BERD-NFDI'}], 'simple': [{'language': 'simple', 'value': 'BERD-NFDI'}]}
```

### Module `data`

The module `data` has raw data as a dictionary:
```python
from nfdi import data
data.raw()
```

### Module `nel`

The module `nel` provides simple rule-based named entity linker for the NFDI consortia. In Jupyter Notebook use
```python
from nfdi.nel import linker, test
t = linker(test)
t.render()
```
where `test` stores the following sentences:
```shell
What are BERD@NFDI, NFDI4Earth, NFDI4DataScience, NFDI-MatWerk, PUNCH4NFDI, FAIRmat and Text+? How are they related to NFDI4Ing, NFDI4Culture, NFDI4Chem and NFDIGHGA?
```

In Python console use:
```python
from nfdi.nel import linker, test
t = linker(test)
t.serve()
```

The Wikidata QIDs are stored in `.ent_id_`:
```python
from nfdi.nel import linker, test
t = linker(test)
for span in t.doc.ents:
    print((span.text, span.ent_id_, span.label_))
```

It prints:
```shell
('BERD@NFDI', 'Q108542181', 'ORG')
('NFDI4Earth', 'Q108542504', 'ORG')
('NFDI4DataScience', 'Q108542422', 'ORG')
('NFDI-MatWerk', 'Q108542607', 'ORG')
('PUNCH4NFDI', 'Q108542637', 'ORG')
('FAIRmat', 'Q108542373', 'ORG')
('Text+', 'Q98271443', 'ORG')
('NFDI4Ing', 'Q98380344', 'ORG')
('NFDI4Culture', 'Q98276929', 'ORG')
('NFDI4Chem', 'Q96678459', 'ORG')
('NFDIGHGA', 'Q98380337', 'ORG')
```

## NFDI Jupyter Book

Check out [NFDI Jupyter Book](https://ub-mannheim.github.io/NFDI). It describes:
* how to use the library,
* how to send SPARQL queries to Wikidata and to get visualisations for NFDI consortia,
* [Wikidata WikiProject NFDI](https://www.wikidata.org/wiki/Wikidata:WikiProject_NFDI) and relevant entity schemas,
* how we parsed the data,
* how we edited Wikidata.