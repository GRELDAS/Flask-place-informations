""" TestGeocoder """

from gpapp.scripts.geocoder import Geocoder
import urllib.request
from io import BytesIO


class TestGeocoder():

    def setup(self):
        """
        """
        self.geocoder = Geocoder(request="OpenClassrooms")

    def test_geocoder(self):
        """
        """

        assert type(self.geocoder).__name__ == "Geocoder"

    def test_nominatim_request(self):
        """
        """

        assert self.geocoder.get_coordinates() == (48.8747786, 2.3504885)