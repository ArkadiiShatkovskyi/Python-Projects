class Hack:
    def __init__(self):
        self.hacks = {'a': 1, 'b': 2, 'c': 3}  # definition of letters power
        self.special_phrases = {'baa': 20, 'ba': 10}  # special phrases definition

    # method take a phase and count it, return int
    def hack_calculator(self, hack: str):
        counter = {'a': 1, 'b': 1, 'c': 1}
        result = 0
        if self.check_if_hack_contain_other_letters(hack):
            for letter in hack:
                result += self.hacks.get(letter) * counter.get(letter)
                counter[letter] = counter.get(letter) + 1
            result += self.special_phrases_counter(hack)
        return result

    # method check if hack contain any other letter from dictionary
    def check_if_hack_contain_other_letters(self, hack):
        for letter in hack:
            if not self.hacks.keys().__contains__(letter):
                return False
        return True

    # method check and count special phases in hack
    def special_phrases_counter(self, phase):
        result = 0
        while any(x in phase for x in self.special_phrases.keys()):
            for key in self.special_phrases.keys():
                if key in phase:
                    result += self.special_phrases.get(key)
                    phase = phase.replace(key, '', 1)
        return result
