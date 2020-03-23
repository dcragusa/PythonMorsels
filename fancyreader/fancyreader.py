import csv


class Row:
    def __init__(self, fieldnames, line):
        self.fieldnames = fieldnames
        for pair in zip(fieldnames, line):
            setattr(self, pair[0], pair[1])

    def __repr__(self):
        return f"Row({', '.join([f'{field}={repr(getattr(self, field))}' for field in self.fieldnames])})"

    def __iter__(self):
        for field in self.fieldnames:
            yield getattr(self, field)


class FancyReader:
    def __init__(self, lines, fieldnames=None):
        self.reader = csv.reader(lines)
        self.fieldnames = fieldnames if fieldnames else next(self.reader)

    def __iter__(self):
        return self

    def __next__(self):
        return Row(self.fieldnames, next(self.reader))

    @property
    def line_num(self):
        return self.reader.line_num
