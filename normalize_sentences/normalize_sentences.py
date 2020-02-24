import re

# def normalize_sentences(s):
#     regex = re.compile(r'''
#         ([.!?])  # capturing group, any of . ! or ?
#         \ +      # 1 or more spaces
#     ''', re.M | re.X)  # multiline / verbose modes
#     return re.sub(regex, r'\1  ', s)

# We get bonus 1 for free!

# def normalize_sentences(s):
#     regex = re.compile(r'''
#         (?<!.\..) # don't match abbreviations (char dot char before the separator)
#         ([.!?])   # capturing group, any of . ! or ?
#         \ +       # 1 or more spaces
#     ''', re.M | re.X)  # multiline / verbose modes
#     return re.sub(regex, r'\1  ', s)


def normalize_sentences(s):
    regex = re.compile(r'''
        (?<![A-Z][a-z])      # don't match 2-letter honorifics (capital char, char before the separator)
        (?<![A-Z][a-z][a-z]) # don't match 3-letter honorifics (capital char, char, char before the separator)
        (?<!.\..)            # don't match abbreviations (char, dot, char before the separator)
        ([.!?])              # capturing group, any of . ! or ?
        \ +                  # 1 or more spaces
    ''', re.M | re.X)  # multiline / verbose modes
    return re.sub(regex, r'\1  ', s)
