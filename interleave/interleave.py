import itertools
import more_itertools

# def interleave(iter1, iter2):
#     return itertools.chain.from_iterable(zip(iter1, iter2))

# bonus 1 for free

# def interleave(*args):
#     return itertools.chain.from_iterable(zip(*args))

# def interleave(*args):
#     return itertools.chain.from_iterable(zip(*args))


# def interleave(*args):
#     # as suggested by the python itertools documentation
#     return more_itertools.roundrobin(*args)

# alternatively if this too much of a shortcut...

sentinel = object


def interleave(*args):
    for item in itertools.chain.from_iterable(itertools.zip_longest(*args, fillvalue=sentinel)):
        if item is not sentinel:
            yield item
        else:
            continue
