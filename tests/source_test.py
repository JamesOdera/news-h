import unittest
from models import Source,Articles

class SourceTest(unittest.TestCase):
  

    def setUp(self):
      
        self.new_source = Source('https://newsapi.org/v2/sources?apikey={}&query={}')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


class ArticlesTest(unittest.TestCase):
  

    def setUp(self):
        
        self.new_article = Articles('')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))