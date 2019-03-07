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
        self.request_keyword = {
            "status" : "", # EMPTY, FOUND, NOT FOUND
            "greeting_form" : "",
            "sentence_type" : "",
            "keyword" : ""
        }

    def sentence_parsing(self, sentence=None):
        """ We check that the sentence received by GrandPapyBot is
        syntactically correct.

        In french, a question must have one of the following three form :

        1. Subject + verb + complement + question mark (?)
        2. Verb + subject + complement + question mark (?)
        3. "Est-ce que" + subject + verb + complement + question mark (?) """

        # 0. Initialization
        self.sentence = sentence
        self.request_keyword = {
            "status" : "",
            "greeting_form" : "",
            "sentence_type" : "",
            "keyword" : ""
        }

        status = ""
        sentence_type = ""
        keyword = ""
        greeting_form = ""

        # 1. We remove the spaces too
        self.sentence = " ".join(self.sentence.split())

        # 2. We retired accents
        self.sentence = unidecode.unidecode(self.sentence)

        if len(self.sentence) == 0:
            status = "EMPTY"
        else:

            # 1. We check if exist a greeting form
            if re.match(r"^(Salut|Bonjour|Coucou)[ a-zA-z]*[!,.]\s", self.sentence) is not None:
                greeting_form = "TRUE"
                self.sentence = re.sub(r"^(Salut|Bonjour|Coucou)[ a-zA-z]*[!,.]\s", "", self.sentence)
            else:
                greeting_form = "FALSE"

            # 2. We check if the sentence is a question
            if re.match(r"^(Je|Tu|Il|Nous|Vous|Ils) ?[ \-'a-zA-z]*\?$", self.sentence):
                sentence_type = "TYPE ONE"
            elif re.match(r"^(Est[ -]?ce que)\s{1}([jJ]e|[Tt]u|[Ii]l|[Nn]ous|[Vv]ous|[Ii]ls){1}\s{1}[a-zA-z]*\s{1}[ \-'a-zA-Z]*\?$", self.sentence):
                sentence_type = "TYPE TWO"
            elif re.match(r"^[a-zA-z]*[-\s]{1}([jJ]e|[Tt]u|[Ii]l|[Nn]ous|[Vv]ous|[Ii]ls){1}[ \-'a-zA-Z]*\s{1}\?$", self.sentence):
                sentence_type = "TYPE THREE"
            else:
                sentence_type = "NO SENTENCE"
                status = "NO SENTENCE"

            # 4. We execute the code
            if sentence_type != "NO SENTENCE":

                search_result = re.search(r"(((de\sla|du|de|d'|le|la|l'[^adresse]){1}[\s\-'a-zA-ZÉé]*\?$))", self.sentence)
                sentence_keywords = search_result.group(1)

                req_keyword = re.sub(r"^(de\sla\s|du\s|de\s|d'|la\s|le\s|l'|les\s)", "", sentence_keywords)
                req_keyword = re.sub(r"(\s\?)$", "", req_keyword)

                status = "FOUND"
                keyword = req_keyword

        self.request_keyword["status"] = status
        self.request_keyword["sentence_type"] = sentence_type
        self.request_keyword["greeting_form"] = greeting_form
        self.request_keyword["keyword"] = keyword

        return self.request_keyword
