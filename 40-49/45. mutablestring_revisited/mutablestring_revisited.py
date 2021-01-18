from collections import UserString
from collections.abc import MutableSequence


class MutableString(MutableSequence, UserString, str):

    def __getitem__(self, index):
        return MutableString(''.join(list(self.data)[index]))

    def __setitem__(self, key, value):
        datalist = list(self.data)
        datalist[key] = value
        self.data = ''.join(str(c) for c in datalist)

    def __delitem__(self, key):
        datalist = list(self.data)
        del datalist[key]
        self.data = ''.join(str(c) for c in datalist)

    def insert(self, idx, obj):
        datalist = list(self.data)
        datalist.insert(idx, obj)
        self.data = ''.join(str(c) for c in datalist)

    def __iadd__(self, other):
        self.data += other
        return self

    def __imul__(self, other):
        self.data *= other
        return self

    def __ne__(self, other):
        return not(self.data == other)
