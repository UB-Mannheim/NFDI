from dataclasses import dataclass, field, asdict
from pprint import pprint
from .data import raw
import requests


@dataclass
class infrastructure:
    def print(self):
        pprint(asdict(self))

    def dict(self):
        return asdict(self)

    def _wikidata(self, json=False):
        r = requests.get(self.wikidata + '.json')
        r.raise_for_status()
        if raw:
            wikidata = r.json()
        else:
            wikidata = r.json().get('entities').get(self.wikidata.split('/')[-1])
        return wikidata


@dataclass()
class consortium(infrastructure):
    label: str
    homepage: str = field(init=False, repr=False)
    wikidata: str = field(init=False, repr=False)
    github: str = field(init=False, repr=False)
    google: str = field(init=False, repr=False)
    linkedin: str = field(init=False, repr=False)
    twitter: str = field(init=False, repr=False)
    youtube: str = field(init=False, repr=False)
    inception: str = field(init=False, repr=False)
    zenodo: str = field(init=False, repr=False)

    def __post_init__(self):
        if self.label not in raw.keys():
            print('WARNING: Empty instance of consortium is returned. The label', f"'{self.label}'", 'is not in',
                  list(raw.keys()))
        else:
            self.homepage: str = raw.get(self.label).get("Homepage", "")
            self.wikidata: str = raw.get(self.label).get('Wikidata', "")
            self.github: str = raw.get(self.label).get('GitHub', "")
            self.google: str = raw.get(self.label).get('Google', "")
            self.linkedin: str = raw.get(self.label).get('Linkedin', "")
            self.twitter: str = raw.get(self.label).get('Twitter', "")
            self.youtube: str = raw.get(self.label).get('YouTube', "")
            self.inception: str = raw.get(self.label).get('Inception', "")
            self.zenodo: str = raw.get(self.label).get('Zenodo', "")


@dataclass
class consortia(infrastructure):
    label: str = "National Research Data Infrastructure"
    homepage: str = "https://www.nfdi.de"
    wikidata: str = "https://www.wikidata.org/entity/Q61658497"
    github: str = ""
    google: str = "https://www.google.com/search?kgmid=/g/11h3k116k1"
    linkedin: str = "https://www.linkedin.com/company/nfdi-de"
    twitter: str = "https://twitter.com/NFDI_de"
    youtube: str = ""
    zenodo: str = "https://zenodo.org/communities/nfdi"
    labels: list = field(default_factory=lambda: list(raw.keys()))
    consortia: list = field(init=False)

    def __post_init__(self):
        self.consortia = [consortium(label) for label in self.labels]
