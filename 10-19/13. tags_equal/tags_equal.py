
# def tags_equal(s1, s2):
#     tags_s1 = set([s for s in s1[1:-1].casefold().split(' ')])
#     tags_s2 = set([s for s in s2[1:-1].casefold().split(' ')])
#     return tags_s1 == tags_s2


# def parse_tags(s):
#     tags = set()
#     attrs_seen = set()
#     for item in s[1:-1].split(' '):
#         if '=' in item:
#             attr = item.split('=')[0]
#             if attr in attrs_seen:
#                 continue
#             else:
#                 tags.add(item)
#                 attrs_seen.add(attr)
#         else:
#             tags.add(item)
#     return tags
#
# def tags_equal(s1, s2):
#     return parse_tags(s1.casefold()) == parse_tags(s2.casefold())


# we get bonus 2 for free!


def parse_tags(s):
    tags = set()
    attrs_seen = set()
    item = ''
    in_quotes = False
    discard_item = False
    for char in s[1:]:
        if char in [' ', '>']:
            if in_quotes:
                # if we are inside quotes, the space is not a separator
                item += char
            else:
                if discard_item:
                    # we are discarding the rest of a repeated attribute
                    item = ''
                    discard_item = False
                else:
                    tags.add(item)
                    item = ''
        elif discard_item:
            # we are discarding the rest of a repeated attribute
            continue
        elif char in ['\'', '"']:
            # enter/exit quote mode
            in_quotes = not in_quotes
        elif char == '=':
            if item in attrs_seen:
                # enter discard mode
                discard_item = True
            else:
                attrs_seen.add(item)
                item += char
        else:
            item += char
    return tags


def tags_equal(s1, s2):
    return parse_tags(s1.casefold()) == parse_tags(s2.casefold())
