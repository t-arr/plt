import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_translator_get(self):
        translator = PigLatin("Hello world")
        self.assertEqual("Hello world", translator.get_phrase())

    def test_empty_string(self):
        translator = PigLatin("")
        self.assertEqual("nil", translator.get_phrase())