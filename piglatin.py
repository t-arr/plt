class PigLatin:

    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        return self._phrase

    def translate(self) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'ä', 'ö', 'å']
        if self.get_phrase() == "":
            return "nil"
        last_character = self._phrase[-1]
        if last_character == 'y':
            return self.get_phrase() + 'nay'
        if last_character in vowels:
            return self.get_phrase() + 'yay'
        if last_character not in vowels:
            return self.get_phrase() + 'ay'

