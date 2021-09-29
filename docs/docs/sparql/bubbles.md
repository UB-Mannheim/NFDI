# Bubbles

The next query plots a bubble chart. It shows the number of accepted NFDI consortia per city where the main applicant is located.

```sparql
#defaultView:BubbleChart
SELECT ?cityLabel (count(*) as ?count)
WHERE 
{
  ?item wdt:P31 wd:Q98270496.
  OPTIONAL {?item wdt:P571 ?inception.}
  OPTIONAL {?item wdt:P856 ?url.}
  OPTIONAL {?item wdt:P2002 ?twitter.}
  OPTIONAL {?item wdt:P2037 ?github.}
  OPTIONAL {?item wdt:P2397 ?youtube.}
  OPTIONAL {?item p:P1416 [
                    ps:P1416 ?affiliation;
                    pq:P3831  wd:Q105906729 ] . OPTIONAL {?affiliation wdt:P159 ?city.} }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
GROUP BY ?cityLabel
ORDER BY DESC(?count) ASC(?item)
```

[Try it!](https://query.wikidata.org/embed.html#%23defaultView%3ABubbleChart%0ASELECT%20%3FcityLabel%20%28count%28%2a%29%20as%20%3Fcount%29%0AWHERE%20%0A%7B%0A%20%20%3Fitem%20wdt%3AP31%20wd%3AQ98270496.%0A%20%20OPTIONAL%20%7B%3Fitem%20wdt%3AP571%20%3Finception.%7D%0A%20%20OPTIONAL%20%7B%3Fitem%20wdt%3AP856%20%3Furl.%7D%0A%20%20OPTIONAL%20%7B%3Fitem%20wdt%3AP2002%20%3Ftwitter.%7D%0A%20%20OPTIONAL%20%7B%3Fitem%20wdt%3AP2037%20%3Fgithub.%7D%0A%20%20OPTIONAL%20%7B%3Fitem%20wdt%3AP2397%20%3Fyoutube.%7D%0A%20%20OPTIONAL%20%7B%3Fitem%20p%3AP1416%20%5B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ps%3AP1416%20%3Faffiliation%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20pq%3AP3831%20%20wd%3AQ105906729%20%5D%20.%20OPTIONAL%20%7B%3Faffiliation%20wdt%3AP159%20%3Fcity.%7D%20%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20"%5BAUTO_LANGUAGE%5D%2Cen".%20%7D%0A%7D%0AGROUP%20BY%20%3FcityLabel%0AORDER%20BY%20DESC%28%3Fcount%29%20ASC%28%3Fitem%29)