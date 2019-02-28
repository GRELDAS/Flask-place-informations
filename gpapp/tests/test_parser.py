""" TestParser """

from gpapp.scripts.parser import Parser


class TestParser():

    def setup(self):
        self.parser = Parser(
            sentence="Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
            )

    def test_parser(self):
        """ Test if a Parser class is instantiated. """

        assert type(self.parser).__name__ == "Parser"

    def test_sentence_lenght(self):
        """ Test if the function ... """

        assert self.parser.sentence_lenght() is True

    def test_sentence_split(self):
        """ Test if the function ... """

        assert self.parser.sentence_split() == [
            "Salut",
            "GrandPy",
            "!",
            "Est-ce",
            "que",
            "tu",
            "connais",
            "l'adresse",
            "d'OpenClassrooms",
            "?"
        ]

    def test_sentence_words_clean(self):

        self.parser.sentence_words = [
            "Salut",
            "GrandPy",
            "!",
            "Est-ce",
            "que",
            "tu",
            "connais",
            "l'adresse",
            "d'OpenClassrooms",
            "?"
        ]

        assert self.parser.sentence_words_clean() == [
            "Salut",
            "GrandPy",
            "!",
            "Est-ce",
            "que",
            "tu",
            "connais",
            "adresse",
            "OpenClassrooms",
            "?"
        ]

    def test_sentence_words_analysis(self):

        self.parser.sentence_words = [
            "Salut",
            "GrandPy",
            "!",
            "Est-ce",
            "que",
            "tu",
            "connais",
            "adresse",
            "OpenClassrooms",
            "?"
        ]

        assert self.parser.sentence_words_analysis() == [
            [0, 5, True],
            [1, 7, True],
            [2, 1, False],
            [3, 6, True],
            [4, 3, False],
            [5, 2, False],
            [6, 7, False],
            [7, 7, False],
            [8, 14, True],
            [9, 1, False]
        ]

    def test_sentence_keywords(self):
        self.parser.sentence_words = [
            "Salut",
            "GrandPy",
            "!",
            "Est-ce",
            "que",
            "tu",
            "connais",
            "adresse",
            "OpenClassrooms",
            "?"
        ]

        assert self.parser.sentence_keywords() == "OpenClassrooms"

    def test_sentence_parsing(self):

        self.parser.sentence_parsing()

        assert self.parser.request_keywords == "OpenClassrooms"