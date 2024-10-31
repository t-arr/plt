class PigLatin:

    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        return self._phrase

    def translate(self) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'å']
        if self.get_phrase() == "":
            return "nil"
        last_char = self._phrase[-1]
        first_char = self._phrase[0]
        if first_char not in vowels:
            if self._phrase[1] not in vowels:
                return self._phrase[2:] + first_char + self._phrase[1] + 'ay'
            return self._phrase[1:] + first_char + 'ay'
        elif last_char == 'y':
            return self.get_phrase() + 'nay'
        elif last_char in vowels:
            return self.get_phrase() + 'yay'
        elif last_char not in vowels:
            return self.get_phrase() + 'ay'

