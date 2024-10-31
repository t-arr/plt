class PigLatin:

    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        return self._phrase

    def translate(self) -> str:
        phrase = self.get_phrase()
        if not phrase:
            return "nil"

        vowels = ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'å']
        translated = []

        for word in phrase.split():
            first_char, last_char = word[0], word[-1]

            if first_char not in vowels:
                if word[1] not in vowels:
                    translated.append(word[2:] + first_char + word[1] + 'ay')
                else:
                    translated.append(word[1:] + first_char + 'ay')
            elif last_char == 'y':
                translated.append(word + 'nay')
            elif last_char in vowels:
                translated.append(word + 'yay')
            else:
                translated.append(word + 'ay')

        return ' '.join(translated)