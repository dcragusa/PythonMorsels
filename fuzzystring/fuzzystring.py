from unicodedata import normalize


def normalized(s):
    return normalize('NFKD', s.casefold())


class FuzzyString:

    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __repr__(self):
        return f"'{self.string}'"

    def __eq__(self, other):
        return isinstance(other, str) and normalized(self.string) == normalized(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        return normalized(self.string) > normalized(other)

    def __ge__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        return normalized(self.string) >= normalized(other)

    def __lt__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        return normalized(self.string) < normalized(other)

    def __le__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        return normalized(self.string) <= normalized(other)

    def __contains__(self, item):
        if not isinstance(item, str):
            return NotImplemented
        return normalized(item) in normalized(self.string)

    def __add__(self, other):
        return FuzzyString(self.string + other)
