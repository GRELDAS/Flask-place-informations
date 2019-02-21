from gpapp.parser import Parser

class TestParser():

    def setup(self):
        self.parser = Parser()

    def test_parser(self):
        assert type(self.parser).__name__ == "Parser"

    def test_split(self):
        variable = "Bonjour monsieur"
        text_list = self.parser.split(text=variable)
        assert text_list == ["Bonjour", "monsieur"]
