import csv


def get_row(fieldnames):

    class Row:
        __slots__ = fieldnames

        def __init__(self, line):
            for pair in zip(fieldnames, line):
                setattr(self, pair[0], pair[1])

        def __repr__(self):
            return f"Row({', '.join([f'{field}={repr(getattr(self, field))}' for field in fieldnames])})"

        def __iter__(self):
            for field in fieldnames:
                yield getattr(self, field)

    return Row


class FancyReader:
    def __init__(self, lines, fieldnames=None, **kwargs):
        self.reader = csv.reader(lines, **kwargs)
        self._fieldnames = fieldnames
        self.row = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.row is None:
            self.row = get_row(self.fieldnames)
        return self.row(next(self.reader))

    @property
    def fieldnames(self):
        if self._fieldnames is None:
            self._fieldnames = next(self.reader)
        return self._fieldnames

    @property
    def line_num(self):
        return self.reader.line_num
