import requests, json

class Geocoder():
    def __init__(self, request=None):
        """
        """

        self.request = request
        self.coordinates = ()
        self.address = ""

    def get_coordinates(self):
        """
        """

        r = requests.get(
            "https://nominatim.openstreetmap.org/search.php?q={}&format=json&addressdetails=[0|1]".format(self.request)
        )

        req = r.json()
        self.coordinates = (float(req[0]["lat"]), float(req[0]["lon"]))
        self.address = req[0]["display_name"]

        return self.coordinates
