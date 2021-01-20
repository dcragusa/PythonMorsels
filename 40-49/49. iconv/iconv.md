# iconv

This week I'd like you to make a program that converts text from one character encoding to another. This program 
will be called `iconv.py` because it will work very similarly to the `iconv` Linux command-line tool.

At first your program should accept an input file and an output file (specified via `-o`/`--output` options) 
as well as an optional `-f`/`--from-code` (to customize the input encoding) and `-t`/`--to-code` (to customize the 
output encoding).

Given a UTF-8 file with the text "Hi! ✨" in it, we convert that file to a UTF-16LE file like this:

    $ python iconv.py utf8_file.txt -f utf-8 -o utf16le_file.txt -t utf-16le

Here's what the bytes would look like in the input file (`utf8_file.txt`) and output file (`utf16le_file.txt`):

    >>> open('utf8_file.txt', mode='rb').read()
    b'Hi! \xe2\x9c\xa8'
    >>> open('utf16le_file.txt', mode='rb').read()
    b"H\x00i\x00!\x00 \x00('"

The long form of these options should also be accepted:

    $ python iconv.py utf8_file.txt --from-code=utf-8 --output=utf16le_file.txt --to-code=utf-16le

And these options may be specified in any order.

If `-f`/`--from-code` is not specified, the input encoding should be the default encoding is on your system. 
Likewise, if `-t`/`--to-code` is not specified, the output encoding should be the default encoding is on your system.

#### Bonus 1

For the first bonus, I'd like you to make `-o`/`--output` optional. If unspecified, standard output should be 
written to instead of a file.

    $ python iconv.py utf16le_file.txt -f utf-16le
    Hi! ✨

Note that `-t`/`--to-code` should still work even when writing to standard output.

#### Bonus 2

For the second bonus, I'd like you to allow `iconv.py` to optionally read from standard input instead of from an 
input file.

If no input file is given or if the given input file is `-`, standard input should be read from instead of a file:

    $ cat utf16le_file.txt | python iconv.py -f utf-16le
    Hi! ✨
    $ cat utf16le_file.txt | python iconv.py -f utf-16le -
    Hi! ✨

#### Bonus 3

For the third bonus, I'd like you to ignore unicode decode errors when `-c` is passed. Meaning any bytes which 
cannot be decoded properly will be skipped over.

Given a file `hello.txt` which the text “Hello!” encoded with CP-1252:

    >>> open('hello.txt', mode='wb').write(b'\x93Hello!\x94')

Reading the file with a UTF-8 encoding will skip over those smart quotes (because those bytes aren't understood 
in UTF-8):

    $ python iconv.py hello.txt -f utf-8
    Hello!
    $ python iconv.py hello.txt -f cp1252
    “Hello!”
