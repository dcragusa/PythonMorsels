from collections import deque

# def window(iterable, window_size):
#     if window_size == 0:
#         return []
#     tuple_list = []
#     current_tuple = deque(maxlen=window_size)
#     for item in iterable:
#         current_tuple.append(item)
#         if len(current_tuple) == window_size:
#             tuple_list.append(tuple(current_tuple))
#     return tuple_list

# def window(iterable, window_size):
#     if window_size == 0:
#         return []
#     current_tuple = deque(maxlen=window_size)
#     for item in iterable:
#         current_tuple.append(item)
#         if len(current_tuple) == window_size:
#             yield tuple(current_tuple)

# def window(iterable, window_size):
#     if window_size == 0:
#         return []
#     current_tuple = deque(maxlen=window_size)
#     for item in iterable:
#         current_tuple.append(item)
#         if len(current_tuple) == window_size:
#             yield tuple(current_tuple)
#     if (size_difference := (window_size - len(current_tuple))) > 0:
#         current_tuple.extend([None] * size_difference)
#         yield tuple(current_tuple)


def window(iterable, window_size, *, fillvalue=None):
    if window_size == 0:
        return []
    current_tuple = deque(maxlen=window_size)
    for item in iterable:
        current_tuple.append(item)
        if len(current_tuple) == window_size:
            yield tuple(current_tuple)
    if (size_difference := (window_size - len(current_tuple))) > 0:
        current_tuple.extend([fillvalue] * size_difference)
        yield tuple(current_tuple)
