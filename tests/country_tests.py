
from generators.Country import Country
import unittest2 as unittest
from mock import MagicMock

import redis
import ConfigParser, os
from util.Seeds import *


config = ConfigParser.RawConfigParser()
config.read('data/config.ini')
url = config.get('redis', 'url')

class TestCountry(unittest.TestCase):

    def setUp(self):
        """  """
        
        self.redis=redis.from_url(url)
        self.seed=set_seed( "3" )

    def test_random_country(self):
        """  """
        country = Country(self.redis )
#        country.add_regions()
#        self.assertEqual(1,len(country.regions))


    def test_country_region(self):
        """  """
        country = Country(self.redis, {'regioncount':25})
#        country.add_regions()
#        self.assertEqual(25,len(country.regions))
#        print country.__dict__






