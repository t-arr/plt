class PigLatin:

    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        return self._phrase

    def translate(self) -> str:
        if self.get_phrase() == "":
            return "nil"
        last_character = self._phrase[-1]
        if last_character == 'y':
            return self.get_phrase() + 'nay'
