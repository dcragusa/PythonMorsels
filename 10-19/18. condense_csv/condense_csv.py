import csv

# def condense_csv(csv_text, id_name):
#     objects = []
#     attrs = []
#     values = {}
#     for row in csv.reader(csv_text.splitlines()):
#         if (obj := row[0]) not in objects:
#             objects.append(obj)
#         if (attr := row[1]) not in attrs:
#             attrs.append(attr)
#         values[(obj, attr)] = row[2]
#
#     output = [[id_name] + attrs]
#     for obj in objects:
#         obj_row = [obj]
#         for attr in attrs:
#             obj_row.append(values[(obj, attr)])
#         output.append(obj_row)
#
#     return '\n'.join([','.join(row) for row in output])

# def condense_csv(csv_text, id_name):
#     objects = []
#     attrs = []
#     values = {}
#     for row in csv.reader(csv_text.splitlines()):
#         if (obj := row[0]) not in objects:
#             objects.append(obj)
#         if (attr := row[1]) not in attrs:
#             attrs.append(attr)
#         values[(obj, attr)] = row[2]
#
#     output = [[id_name] + attrs]
#     for obj in objects:
#         obj_row = [obj]
#         for attr in attrs:
#             val = values[(obj, attr)]
#             obj_row.append(rf'"{val}"' if ',' in val else val)
#         output.append(obj_row)
#
#     return '\n'.join([','.join(row) for row in output])

# def condense_csv(csv_text, id_name=None):
#     objects = []
#     attrs = []
#     values = {}
#     for idx, row in enumerate(csv.reader(csv_text.splitlines())):
#         if idx == 0 and id_name is None:
#             id_name = row[0]
#             continue
#         if (obj := row[0]) not in objects:
#             objects.append(obj)
#         if (attr := row[1]) not in attrs:
#             attrs.append(attr)
#         values[(obj, attr)] = row[2]
#
#     output = [[id_name] + attrs]
#     for obj in objects:
#         obj_row = [obj]
#         for attr in attrs:
#             val = values[(obj, attr)]
#             obj_row.append(rf'"{val}"' if ',' in val else val)
#         output.append(obj_row)
#
#     return '\n'.join([','.join(row) for row in output])


def condense_csv(csv_text, id_name=None):
    objects = []
    attrs = []
    values = {}
    for idx, row in enumerate(csv.reader(csv_text.splitlines())):
        if idx == 0 and id_name is None:
            id_name = row[0]
            continue
        if (obj := row[0]) not in objects:
            objects.append(obj)
        if (attr := row[1]) not in attrs:
            attrs.append(attr)
        values[(obj, attr)] = row[2]

    output = [[id_name] + attrs]
    for obj in objects:
        obj_row = [obj]
        for attr in attrs:
            val = values.get((obj, attr), '')
            obj_row.append(rf'"{val}"' if ',' in val else val)
        output.append(obj_row)

    return '\n'.join([','.join(row) for row in output])
