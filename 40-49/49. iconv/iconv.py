import sys
from argparse import ArgumentParser

# parser = ArgumentParser()
# parser.add_argument('input')
# parser.add_argument('-o', '--output')
# parser.add_argument('-f', '--from-code', default=sys.getdefaultencoding())
# parser.add_argument('-t', '--to-code', default=sys.getdefaultencoding())
# args = parser.parse_args()
#
# if __name__ == '__main__':
#     with open(args.input, 'r', encoding=args.from_code) as input_f:
#         with open(args.output, 'w', encoding=args.to_code) as output_f:
#             output_f.write(input_f.read())


# parser = ArgumentParser()
# parser.add_argument('input')
# parser.add_argument('-o', '--output')
# parser.add_argument('-f', '--from-code', default=sys.getdefaultencoding())
# parser.add_argument('-t', '--to-code', default=sys.getdefaultencoding())
# args = parser.parse_args()
#
# if __name__ == '__main__':
#     with open(args.input, 'r', encoding=args.from_code) as input_f:
#         if args.output:
#             with open(args.output, 'w', encoding=args.to_code) as output_f:
#                 output_f.write(input_f.read())
#         else:
#             sys.stdout.reconfigure(encoding=args.to_code)
#             sys.stdout.write(input_f.read())


# parser = ArgumentParser()
# parser.add_argument('input', nargs='?', default='-')
# parser.add_argument('-o', '--output')
# parser.add_argument('-f', '--from-code', default=sys.getdefaultencoding())
# parser.add_argument('-t', '--to-code', default=sys.getdefaultencoding())
# args = parser.parse_args()
#
# if __name__ == '__main__':
#     if args.input != '-':
#         with open(args.input, 'r', encoding=args.from_code) as input_f:
#             contents = input_f.read()
#     else:
#         sys.stdin.reconfigure(encoding=args.from_code)
#         contents = sys.stdin.read()
#
#     if args.output:
#         with open(args.output, 'w', encoding=args.to_code) as output_f:
#             output_f.write(contents)
#     else:
#         sys.stdout.reconfigure(encoding=args.to_code)
#         sys.stdout.write(contents)


parser = ArgumentParser()
parser.add_argument('input', nargs='?', default='-')
parser.add_argument('-o', '--output')
parser.add_argument('-f', '--from-code', default=sys.getdefaultencoding())
parser.add_argument('-t', '--to-code', default=sys.getdefaultencoding())
parser.add_argument('-c', dest='skip_errors', action='store_true')
args = parser.parse_args()

if __name__ == '__main__':
    errors = 'ignore' if args.skip_errors else None

    if args.input != '-':
        with open(args.input, 'r', encoding=args.from_code, errors=errors) as input_f:
            contents = input_f.read()
    else:
        sys.stdin.reconfigure(encoding=args.from_code, errors=errors)
        contents = sys.stdin.read()

    if args.output:
        with open(args.output, 'w', encoding=args.to_code) as output_f:
            output_f.write(contents)
    else:
        sys.stdout.reconfigure(encoding=args.to_code)
        sys.stdout.write(contents)
