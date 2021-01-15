# def format_ranges(input_list):
#     output = []
#     start = end = None
#     for num in input_list:
#         if start is None:
#             # initialise sequence
#             start = end = num
#         elif num == end + 1:
#             # consecutive: continue sequence
#             end = num
#         else:
#             # end sequence: output and reset
#             output.append(f'{start}-{end}')
#             start = end = num
#     output.append(f'{start}-{end}')
#     return ','.join(output)

# def format_ranges(input_list):
#     output = []
#
#     def fmt_str(i, j):
#         # same as before except we hide the second number if equal
#         return f'{i}-{j}' if i != j else f'{i}'
#
#     start = end = None
#     for num in input_list:
#         if start is None:
#             start = end = num
#         elif num == end + 1:
#             end = num
#         else:
#             output.append(fmt_str(start, end))
#             start = end = num
#     output.append(fmt_str(start, end))
#     return ','.join(output)

# def format_ranges(input_list):
#     output = []
#
#     def fmt_str(i, j):
#         return f'{i}-{j}' if i != j else f'{i}'
#
#     start = end = None
#     for num in sorted(input_list):
#         if start is None:
#             start = end = num
#         elif num == end + 1:
#             end = num
#         else:
#             output.append(fmt_str(start, end))
#             start = end = num
#     output.append(fmt_str(start, end))
#     return ','.join(output)


def prepare_ranges(input_list):

    output = []
    duplicates = []

    start = end = None
    for num in sorted(input_list):
        if start is None:
            start = end = num
        elif end == num:
            duplicates.append(num)
        elif num == end + 1:
            end = num
        else:
            output.append((start, end))
            start = end = num
    output.append((start, end))
    if duplicates:
        # these are separate ranges that also need to be added in (out of order)
        output.extend(prepare_ranges(duplicates))
    # sorted will take care of ordering the ranges after duplicates, if any
    return sorted(output)


def format_ranges(input_list):
    ranges = prepare_ranges(input_list)
    output = []
    for start, end in ranges:
        output.append(f'{start}-{end}' if start != end else f'{start}')
    return ','.join(output)
