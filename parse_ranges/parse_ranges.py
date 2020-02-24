# def parse_ranges(input_string):
#
#     output = []
#     ranges = [item.strip() for item in input_string.split(',')]
#
#     for item in ranges:
#         start, end = [int(i) for i in item.split('-')]
#         output.extend(range(start, end + 1))
#
#     return output

# def parse_ranges(input_string):
#
#     ranges = [item.strip() for item in input_string.split(',')]
#
#     for item in ranges:
#         start, end = [int(i) for i in item.split('-')]
#         yield from range(start, end + 1)

# def parse_ranges(input_string):
#
#     ranges = [range_.strip() for range_ in input_string.split(',')]
#
#     for item in ranges:
#         if '-' in item:
#             start, end = [int(i) for i in item.split('-')]
#             yield from range(start, end + 1)
#         else:
#             yield int(item)


def parse_ranges(input_string):

    ranges = [range_.strip() for range_ in input_string.split(',')]

    for item in ranges:
        if '->' in item:
            yield int(item.split('-')[0])
        elif '-' in item:
            start, end = [int(i) for i in item.split('-')]
            yield from range(start, end + 1)
        else:
            yield int(item)
