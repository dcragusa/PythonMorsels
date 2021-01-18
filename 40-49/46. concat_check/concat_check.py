import sys
import tokenize

# regex is a massive headache and tokenise takes care of all the tedious
# pattern matching for us, allowing us to focus on logic


def process_file(input_file):
    with tokenize.open(input_file) as f:
        first = None
        for token in tokenize.generate_tokens(f.readline):
            if token.type == 3:
                # string type
                if first:
                    print(f'{input_file}, line {first[0]}: between {first[1]} and {token.string}')
                # set line on which string ends and content of string
                first = (token.end[0], token.string)
            elif token.type in (4, 61):
                # newlines allowed in implicit continuation
                pass
            else:
                # any other token means no implicit continuation
                first = None


if __name__ == '__main__':
    for input_file in sys.argv[1:]:
        process_file(input_file)
