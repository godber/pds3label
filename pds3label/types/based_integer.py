class BasedInteger(object):
    """
    An integer number in based notation specifies the number base explicitly.
    The number base must be in the range 2 to 16, which allows for
    representations in the most popular number bases, including binary (base
    2), octal (base 8) and hexadecimal (base 16). In general, for a number base
    X the digits 0 to X-1 are used. For example, in octal (base 8) the digits 0
    to 7 are allowed. If X is greater than 10, then the letters A, B, C, D, E,
    F (or their lower case counterparts) are used as needed for the additional
    digits.
    """

    def __init__(self, based_integer_string):
        self.based_integer_string = based_integer_string
        self.base, self.value, _ = based_integer_string.split('#')
        self.base = int(self.base)
        self.int_value = int(self.value, self.base)

    def __repr__(self):
        return self.based_integer_string
