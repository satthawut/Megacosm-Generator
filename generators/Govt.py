
import random
import json
from generators.Generator import Generator
from generators.Country import Country
#from generators.City import 
from util import Filters

class Govt(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)

        self.generate_features('govt'+self.kind)

        if not hasattr(self, 'body'):
            #TODO this should have an if statement on kind and also do cities
            self.body=Country(self.redis)
