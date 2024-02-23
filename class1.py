class Hello:
    def __init__(self, str):
        self.str = str
class NewClass:
    word = 'KOtokBAs'  # Class-level attribute to store the word

    @classmethod
    def set_word(cls, word):
        cls.word = word
    @classmethod
    def current_word(cls):
        return cls.word
    def __str__(cls):
        return cls.word



