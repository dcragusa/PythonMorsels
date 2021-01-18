from itertools import zip_longest


def strict_zip(*sequences):
    sentinel = object()
    for tup in zip_longest(*sequences, fillvalue=sentinel):
        if sentinel in tup:
            raise ValueError('value out of range')
        yield tup
