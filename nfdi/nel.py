import spacy


class linker():
    def __init__(self, text="", language="en"):
        nlp = spacy.blank(language)
        ruler = nlp.add_pipe("entity_ruler")
        patterns = [{'label': 'ORG', 'pattern': 'BERD@NFDI', 'id': 'Q108542181'},
                    {"label": "ORG", "pattern": "BERD-NFDI", "id": "Q108542181"},
                    {"label": "ORG", "pattern": "Business, Economic and Related Data", "id": "Q108542181"},
                    {'label': 'ORG', 'pattern': 'DAPHNE4NFDI', 'id': 'Q108542327'},
                    {'label': 'ORG', 'pattern': 'DAta for PHoton and Neutron Experiments', 'id': 'Q108542327'},
                    {'label': 'ORG', 'pattern': 'DataPlant', 'id': 'Q98380336'},
                    {'label': 'ORG', 'pattern': 'NFDI4Plant', 'id': 'Q98380336'},
                    {'label': 'ORG', 'pattern': 'FAIRmat', 'id': 'Q108542373'},
                    {'label': 'ORG',
                     'pattern': 'FAIR Data Infrastructure for Condensed-Matter Physics and the Chemical Physics of Solids',
                     'id': 'Q108542373'},
                    {'label': 'ORG', 'pattern': 'GHGA', 'id': 'Q98380337'},
                    {'label': 'ORG', 'pattern': 'NFDIGHGA', 'id': 'Q98380337'},
                    {'label': 'ORG', 'pattern': 'German Human Genome-Phenome Archive', 'id': 'Q98380337'},
                    {'label': 'ORG', 'pattern': 'KonsortSWD', 'id': 'Q98380340'},
                    {'label': 'ORG',
                     'pattern': 'Konsortium für die Sozial-, Verhaltens-, Bildungs- und Wirtschaftswissenschaften',
                     'id': 'Q98380340'},
                    {'label': 'ORG', 'pattern': 'MaRDI', 'id': 'Q108327788'},
                    {'label': 'ORG', 'pattern': 'Mathematical Research Data Initiative', 'id': 'Q108327788'},
                    {'label': 'ORG', 'pattern': 'NFDI-MatWerk', 'id': 'Q108542607'},
                    {'label': 'ORG', 'pattern': 'NFDI consortium for Materials Science and Engineering',
                     'id': 'Q108542607'},
                    {'label': 'ORG', 'pattern': 'NFDI4BioDiversity', 'id': 'Q98380341'},
                    {'label': 'ORG', 'pattern': 'NFDI4BioDiversität', 'id': 'Q98380341'},
                    {'label': 'ORG', 'pattern': 'NFDI4Cat', 'id': 'Q98380342'},
                    {'label': 'ORG', 'pattern': 'NFDI for Catalysis-Related Sciences', 'id': 'Q98380342'},
                    {'label': 'ORG', 'pattern': 'NFDI4Chem', 'id': 'Q96678459'},
                    {'label': 'ORG', 'pattern': 'Chemistry Consortium in the NFDI', 'id': 'Q96678459'},
                    {'label': 'ORG', 'pattern': 'NFDI4Culture', 'id': 'Q98276929'},
                    {'label': 'ORG',
                     'pattern': 'Consortium for Research Data on Material and Immaterial Cultural Heritage',
                     'id': 'Q98276929'},
                    {'label': 'ORG', 'pattern': 'NFDI4DataScience', 'id': 'Q108542422'},
                    {'label': 'ORG', 'pattern': 'NFDI4DS', 'id': 'Q108542422'},
                    {'label': 'ORG', 'pattern': 'National Data Infrastrukture for Data Science', 'id': 'Q108542422'},
                    {'label': 'ORG', 'pattern': 'NFDI4Earth', 'id': 'Q108542504'},
                    {'label': 'ORG', 'pattern': 'NFDI Consortium Earth System Sciences', 'id': 'Q108542504'},
                    {'label': 'ORG', 'pattern': 'NFDI4Health', 'id': 'Q98380343'},
                    {'label': 'ORG', 'pattern': 'National Research Data Infrastructure for Personal Health Data',
                     'id': 'Q98380343'},
                    {'label': 'ORG', 'pattern': 'NFDI4Ing', 'id': 'Q98380344'},
                    {'label': 'ORG', 'pattern': 'National Research Data Infrastructure for Engineering Sciences',
                     'id': 'Q98380344'},
                    {'label': 'ORG', 'pattern': 'NFDI4Microbiota', 'id': 'Q99534506'},
                    {'label': 'ORG', 'pattern': 'National Research Data Infrastructure in microbiology',
                     'id': 'Q99534506'},
                    {'label': 'ORG', 'pattern': 'PUNCH4NFDI', 'id': 'Q108542637'},
                    {'label': 'ORG',
                     'pattern': 'NFDI consortium of particle, astro-, astroparticle, hadron and nuclear physics',
                     'id': 'Q108542637'},
                    {'label': 'ORG', 'pattern': 'Text+', 'id': 'Q98271443'},
                    {'label': 'ORG', 'pattern': 'NFDI consortium for text- and language-based research data',
                     'id': 'Q98271443'}]
        ruler.add_patterns(patterns)
        self.doc = nlp(text)

    def print(self):
        print([(ent.text, ent.label_, ent.ent_id_) for ent in self.doc.ents])

    def serve(self):
        try:
            params = {"text": self.doc.text,
                      "ents": [{"start": ent.start_char,
                                "end": ent.end_char,
                                "label": ent.label_,
                                "kb_id": ent.ent_id_,
                                "kb_url": "https://www.wikidata.org/entity/" + ent.ent_id_}
                               for ent in self.doc.ents],
                      "title": None}
            spacy.displacy.serve(params, style="ent", manual=True)
        except Exception:
            print('Are you trying to serve in Jupyter Notebook? Use render() instead.')

    def render(self):
        try:
            params = {"text": self.doc.text,
                      "ents": [{"start": ent.start_char,
                                "end": ent.end_char,
                                "label": ent.label_,
                                "kb_id": ent.ent_id_,
                                "kb_url": "https://www.wikidata.org/entity/" + ent.ent_id_}
                               for ent in self.doc.ents],
                      "title": None}
            spacy.displacy.render(params, style="ent", manual=True)
        except Exception:
            print('Are you trying to render without a running server? Use serve() instead.')


test = """What are BERD@NFDI, NFDI4Earth, NFDI4DataScience, NFDI-MatWerk, PUNCH4NFDI, FAIRmat and Text+? How are they related to NFDI4Ing, NFDI4Culture, NFDI4Chem and NFDIGHGA?"""
