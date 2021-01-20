from functools import total_ordering


roman_to_int_mapping = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}
int_to_roman_mapping = {k: v for v, k in roman_to_int_mapping.items()}


@total_ordering
class RomanNumeral:
    def __init__(self, num):
        self.num = num if isinstance(num, int) else self.roman_to_int(num)

    @property
    def roman_num(self):
        return self.int_to_roman(self.num)

    @staticmethod
    def roman_to_int(roman_num_str):
        num = 0
        idx = 0
        while idx < len(roman_num_str):
            if roman_num_str[idx:idx+2] in roman_to_int_mapping:
                num += roman_to_int_mapping[roman_num_str[idx:idx+2]]
                idx += 2
            else:
                num += roman_to_int_mapping[roman_num_str[idx]]
                idx += 1
        return num

    @staticmethod
    def int_to_roman(num):
        roman_num_str = ''
        for val_int, val_roman in int_to_roman_mapping.items():
            while num >= val_int:
                num -= val_int
                roman_num_str += val_roman
        return roman_num_str

    @staticmethod
    def from_int(num):
        return RomanNumeral(num)

    def __int__(self):
        return self.num

    def __str__(self):
        return self.roman_num

    def __repr__(self):
        return f'RomanNumeral({repr(self.roman_num)})'

    def __add__(self, other):
        if isinstance(other, (int, RomanNumeral)):
            return RomanNumeral(self.num + int(other))
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, (int, RomanNumeral)):
            return self.num == int(other)
        elif isinstance(other, str):
            return self.roman_num == other
        else:
            return NotImplemented

    def __lt__(self, other):
        # with total_ordering we get the rest of the comparison operators for free with __eq__ and __lt__
        if isinstance(other, (int, RomanNumeral)):
            return self.num < int(other)
        else:
            return NotImplemented
