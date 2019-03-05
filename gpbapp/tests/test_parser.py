""" TestParser """

# -*- coding: utf-8 -*-
from gpbapp.scripts.parser import Parser


class TestParser():

    def setup(self):
        self.parser = Parser()

    def test_parser(self):
        """ Test if a Parser class is instantiated. """

        assert type(self.parser).__name__ == "Parser"

    def test_sentence_parsing(self):

        self.parser.sentence_parsing(sentence="Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")

        assert self.parser.request_keywords == "OpenClassrooms"
