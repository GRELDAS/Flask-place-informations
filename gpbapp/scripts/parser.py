""" Parser """

# -*- coding: utf-8 -*-
import re
import unicodedata, unidecode


class Parser():

    def __init__(self):
        """ Take a french sentence as parameters.
            Return a keyword.

            sentence              (str ): french sentence only.
            request_keywords      (str ): result of sentence_parsing. """

        self.sentence = None
        self.request_keywords = ""

    def sentence_parsing(self, sentence=None):
        """ We check that the sentence received by GrandPapyBot is
        syntactically correct.

        In french, a question must have one of the following three form :

        1. Subject + verb + complement + question mark (?)
        2. Verb + subject + complement + question mark (?)
        3. "Est-ce que" + subject + verb + complement + question mark (?) """

        self.sentence = sentence

        sentence_type = 0
        sentence_keywords = ""

        self.sentence = unidecode.unidecode(self.sentence)

        # 1. We check if exist a greeting form
        self.sentence = re.sub(r"^(Salut|Bonjour|Coucou)[ a-zA-z]*[!,.]\s", "", self.sentence)

        if re.match(r"^(Je|Tu|Il|Nous|Vous|Ils) ?[ \-'a-zA-z]*\?$", self.sentence):
            sentence_type = 1
        elif re.match(r"^(Est[ -]?ce que)\s{1}([jJ]e|[Tt]u|[Ii]l|[Nn]ous|[Vv]ous|[Ii]ls){1}\s{1}[a-zA-z]*\s{1}[ \-'a-zA-Z]*\?$", self.sentence):
            sentence_type = 2
        elif re.match(r"^[a-zA-z]*[-\s]{1}([jJ]e|[Tt]u|[Ii]l|[Nn]ous|[Vv]ous|[Ii]ls){1}[ \-'a-zA-Z]*\s{1}\?$", self.sentence):
            sentence_type = 3
        else:
            sentence_type = 0

        if sentence_type != 0:
            search_result = re.search(r"(((de\sla|du|de|d'|le|la|l'[^adresse]){1}[\s\-'a-zA-ZÉé]*\?$))", self.sentence)
            sentence_keywords = search_result.group(1)

            self.request_keywords = re.sub(r"^(de\sla\s|du\s|de\s|d'|la\s|le\s|l'|les\s)", "", sentence_keywords)
            self.request_keywords = re.sub(r"(\s\?)$", "", self.request_keywords)

        return self.request_keywords
