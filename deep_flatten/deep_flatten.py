
# def deep_flatten(to_flatten):
#     output = []
#
#     for item in to_flatten:
#         if isinstance(item, (list, tuple)):
#             output.extend(deep_flatten(item))
#         else:
#             output.append(item)
#
#     return output


# def deep_flatten(to_flatten):
#     output = []
#
#     for item in to_flatten:
#         if hasattr(item, '__iter__'):
#             # check for any iterator by seeing if it has the __iter__ function
#             output.extend(deep_flatten(item))
#         else:
#             output.append(item)
#
#     return output


# def deep_flatten(to_flatten):
#
#     for item in to_flatten:
#         if hasattr(item, '__iter__'):
#             yield from deep_flatten(item)
#         else:
#             yield item


def deep_flatten(to_flatten):

    for item in to_flatten:
        if not isinstance(item, str) and hasattr(item, '__iter__'):
            # add an exception for strings
            yield from deep_flatten(item)
        else:
            yield item
