# scraper/test_nasa_scraper.py
import unittest
from Scrapper import NasaDataScraper

class TestNasaDataScraper(unittest.TestCase):
    def test_fetch_data(self):
        scraper = NasaDataScraper()
        data = scraper.fetch_data()
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()