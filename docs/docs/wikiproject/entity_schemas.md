# Entity schemas

The entities related to NFDI at Wikidata can be validated via [ShEx2 — Simple Online Validator](http://shex.io/webapps/shex.js/doc/shex-simple.html).


We created [Entity Schema E326](https://www.wikidata.org/wiki/EntitySchema:E326) at Wikidata:

``` shex
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# Query:
# SELECT ?i WHERE { ?i wdt:P31 wd:Q98270496 . }
start = @<accepted-nfdi-consortium>
<accepted-nfdi-consortium> {
    wdt:P31 [wd:Q98270496 # instance of accepted NFDI consortium
             wd:Q96678469 # intance of disciplinary research data infrastructure
             wd:Q1298668 # instance of research project
             ] {3} ; # exactly three
    wdt:P279 [wd:Q43229] ; # default exactly one subclass of organization
    wdt:P361 [wd:Q61658497] ; # default exactly one part of National Research Data Infrastructure
    wdt:P571 xsd:dateTime ; # default exactly one date of inception
    wdt:P101 IRI + ; # one or more fields of works
    # At GEPRIS there are "Spokesperson" and "Co-Spokespersons". Wikidata does not have it.
    # Let's use "chairperson" (P488) for "Spokesperson" & "represented by" (P1875) for "Co-Spokespersons".
    wdt:P488 IRI ; # default exactly one chairperson
    wdt:P1875 IRI + ; # one or more represented by
    wdt:P749 [wd:Q61658497] ; # default exactly one parent organization is National Research Data Infrastructure
    wdt:P2652 IRI + ; # one or more partnership with
    wdt:P1416 IRI + ; # one or more affiliation
    wdt:P859 [wd:Q707283] ; # default exactly one sponsor German Research Foundation
    wdt:P710 IRI + ; # one or more participants
    wdt:P968 . + ; # one or more email addresses
    wdt:P856 . + ; # one or more official websites
}
 ```
 
You can already validate the entities of the accepted NFDI consortia against [E326](https://www.wikidata.org/wiki/EntitySchema:E326). Just [try it](https://shex-simple.toolforge.org/wikidata/packages/shex-webapp/doc/shex-simple.html?data=Endpoint:%20https://query.wikidata.org/sparql&hideData&textMapIsSparqlQuery&schemaURL=%2F%2Fwww.wikidata.org%2Fwiki%2FSpecial%3AEntitySchemaText%2FE326).