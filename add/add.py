from itertools import zip_longest

# def add(matrix1, matrix2):
#     return [
#         [sum(elements) for elements in zip(row1, row2)]
#         for row1, row2 in zip(matrix1, matrix2)
#     ]


# def add(*matrices):
#     return [
#         [sum(elements) for elements in zip(*rows)]
#         for rows in zip(*matrices)
#     ]


def add(*matrices):
    try:
        return [
            [sum(elements) for elements in zip_longest(*rows)]
            for rows in zip_longest(*matrices)
        ]
    except TypeError:
        # this will happen due to adding a number to None if the lists don't match up in size
        raise ValueError("Given matrices are not the same size.")
