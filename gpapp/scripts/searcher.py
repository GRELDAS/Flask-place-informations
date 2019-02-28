import requests, json

class Searcher():
    def __init__(self, request=None):
        """
        """

        self.request = request
        self.data = ""

    def get_data(self):
        """
        """

        r = requests.get("https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&explaintext&exsentences=2&format=json&titles={}".format(self.request))
        req = r.json()
        for key in req['query']['pages'].keys():
            page_id = key

        self.data = req['query']['pages'][page_id]['extract']

        return self.data