import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_translator_get(self):
        translator = PigLatin("hello world")
        self.assertEqual("hello world", translator.get_phrase())

    def test_empty_string(self):
        translator = PigLatin("")
        self.assertEqual("nil", translator.translate())

    def test_string_ends_with_y(self):
        translator = PigLatin("any")
        self.assertEqual("anynay", translator.translate())

    def test_string_ends_with_vowel(self):
        translator = PigLatin("apple")
        self.assertEqual("appleyay", translator.translate())

    def test_string_ends_with_consonant(self):
        translator = PigLatin("ask")
        self.assertEqual("askay", translator.translate())

    def test_string_starts_with_consonant(self):
        translator = PigLatin("hello")
        self.assertEqual("ellohay", translator.translate())

    def test_string_starts_with_y(self):
        translator = PigLatin("yhello")
        self.assertEqual("helloyay", translator.translate())