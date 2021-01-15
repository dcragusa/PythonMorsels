from collections import UserString
from collections.abc import MutableSequence


class MutableString(UserString, MutableSequence):

    def __init__(self, value):
        UserString.__init__(self, value)

    def __len__(self):
        return super().__len__()

    def __getitem__(self, index):
        return MutableString(''.join(list(self.data)[index]))

    def __setitem__(self, key, value):
        datalist = list(self.data)
        datalist[key] = value
        self.data = ''.join(datalist)

    def __delitem__(self, key):
        datalist = list(self.data)
        del datalist[key]
        self.data = ''.join(datalist)

    def insert(self, idx, obj):
        datalist = list(self.data)
        datalist.insert(idx, obj)
        self.data = ''.join(datalist)
