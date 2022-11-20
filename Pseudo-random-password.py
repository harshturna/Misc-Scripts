from copy import copy
from random import choices
from string import ascii_letters
from string import punctuation

class Password:
    """A password of customize strengh and length.
    
    Encapsulate a randomble generated password depending on the user-specified strength and length, where the latter is optional
    and automatically set depending on the strength (low -> 8, mid -> 12, high -> 16). 
    If a length is user-specified these presets are overridden regardless of the strength.
    
    :param strength: a measure of the password's effectivess against brute-force guessing
    :type strength: str, optional

    :param length: the length of the password
    :type length: int, optional
    """


    INPUT_UNIVERSE = {
        "numbers": list(range(10)), 
        "letters": list(ascii_letters), 
        "punctuation": list(punctuation)
    }

    DEFAULT_LENGTHS = {
        "low": 8, 
        "mid": 12, 
        "high": 16
    }

    @classmethod
    def show_input_universe(cls):
        """Return the complete input universe from which characters are sampled
        
        :return: The universe of characters from which random sampling is done to generate passwords
        :rtype: dict (of list-s)
        """
        
        return cls.INPUT_UNIVERSE
    
    def __init__(self, strength="mid", length=12):
        """Constructor method"""

        self.strength = strength
        self.length = length

        self._generate_password()

    def _generate_password(self):
        """Generates the password according to the strength and length specified at initializtion

        :return: the randomly generated password
        :rtype: str
        """
        
        population = copy(self.INPUT_UNIVERSE["letters"])
        length = self.length or self.DEFAULT_LENGTHS.get(self.strength)

        if self.strength == "high":
            population += self.INPUT_UNIVERSE["numbers"] + self.INPUT_UNIVERSE["punctuation"]
        elif self.strength == "mid": 
            population += self.INPUT_UNIVERSE["numbers"]

        self.password = "".join(list(map(str, choices(population, k=length))))

            
            
