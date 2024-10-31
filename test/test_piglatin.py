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

    def test_string_starts_with_y_double_consonants(self):
        translator = PigLatin("yhello")
        self.assertEqual("elloyhay", translator.translate())

    def test_string_starts_with_vowel_ends_with_consonant(self):
        translator = PigLatin("open")
        self.assertEqual("openay", translator.translate())

    def test_string_starts_with_more_consonants(self):
        translator = PigLatin("known")
        self.assertEqual("ownknay", translator.translate())

    def test_string_starts_with_y_single_consonant(self):
        translator = PigLatin("youtube")
        self.assertEqual("outubeyay", translator.translate())