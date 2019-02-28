""" Searcher """

from gpapp.scripts.searcher import Searcher


class TestSearcher():

    def setup(self):
        """
        """

        self.searcher = Searcher(request="OpenClassrooms")

    def test_searcher(self):
        """
        """

        assert type(self.searcher).__name__ == "Searcher"

    def test_get_data(self):
        """
        """

        assert self.searcher.get_data() == "OpenClassrooms est une école en ligne qui propose à ses membres des cours certifiants et des parcours débouchant sur un métier d'avenir, réalisés en interne, par des écoles, des universités, ou encore par des entreprises partenaires comme Microsoft ou IBM. Jusqu'en 2018, n'importe quel membre du site pouvait être auteur, via un outil nommé \"Course Lab\". De nombreux cours sont issus de la communauté, mais ne sont plus mis en avant."