#!/Users/pablogarcia/opt/anaconda3/envs/ibm_cloud/bin/python3.9
from machinetranslation import traslator 
from traslator import english_to_french,french_to_english
import unittest

class TestHello(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'),"Bonjour")
        
class TestBonjour(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'),"Hello")

class TestNullEng(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(''),"error")

class TestNullFr(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(''),"error")


unittest.main()