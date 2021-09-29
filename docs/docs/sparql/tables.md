# Tables

We can get information about the funded NFDI consortia from Wikidata using its SPARQL endpoint. Let's get data about various identifiers for accepted NFDI consortia in tabular form:

```sparql
SELECT ?i ?iLabel ?iDescription ?inception ?gepris ?affiliation ?affiliationLabel ?city ?cityLabel ?twitter ?github ?youtube ?url 
WHERE 
{
  ?i wdt:P31 wd:Q98270496.
  OPTIONAL {?i wdt:P571 ?inception.}
  OPTIONAL {?i wdt:P856 ?url.}
  OPTIONAL {?i wdt:P4870 ?gepris.}
  OPTIONAL {?i wdt:P2002 ?twitter.}
  OPTIONAL {?i wdt:P2037 ?github.}
  OPTIONAL {?i wdt:P2397 ?youtube.}
  OPTIONAL {?i p:P1416 [ ps:P1416 ?affiliation; pq:P3831 wd:Q105906729 ].
            OPTIONAL {?affiliation wdt:P159 ?city.}}
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
```

[Try it!](https://query.wikidata.org/embed.html#SELECT%20%3Fi%20%3FiLabel%20%3FiDescription%20%3Finception%20%3Fgepris%20%3Faffiliation%20%3FaffiliationLabel%20%3Fcity%20%3FcityLabel%20%3Ftwitter%20%3Fgithub%20%3Fyoutube%20%3Furl%20%0AWHERE%20%0A%7B%0A%20%20%3Fi%20wdt%3AP31%20wd%3AQ98270496.%0A%20%20OPTIONAL%20%7B%3Fi%20wdt%3AP571%20%3Finception.%7D%0A%20%20OPTIONAL%20%7B%3Fi%20wdt%3AP856%20%3Furl.%7D%0A%20%20OPTIONAL%20%7B%3Fi%20wdt%3AP4870%20%3Fgepris.%7D%0A%20%20OPTIONAL%20%7B%3Fi%20wdt%3AP2002%20%3Ftwitter.%7D%0A%20%20OPTIONAL%20%7B%3Fi%20wdt%3AP2037%20%3Fgithub.%7D%0A%20%20OPTIONAL%20%7B%3Fi%20wdt%3AP2397%20%3Fyoutube.%7D%0A%20%20OPTIONAL%20%7B%3Fi%20p%3AP1416%20%5B%20ps%3AP1416%20%3Faffiliation%3B%20pq%3AP3831%20wd%3AQ105906729%20%5D.%0A%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%3Faffiliation%20wdt%3AP159%20%3Fcity.%7D%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20"%5BAUTO_LANGUAGE%5D%2Cen".%20%7D%0A%7D)