# concat_check

This week I'd like you to write a program, `concat_check.py` which accepts one or more Python files and will print 
an error if any of them seem to have implicit string concatenation (aka string literal concatenation) in them.

I'm not a big fan of implicit string concatenation and I could use such a program to make a git pre-commit hook 
which errors-out if our code includes implicit string concatenation.

For this file, `file1.py`:

    print("implicit" "string concatenation")
    print("no", "string concatenation")
    print('more implicit' 'string concatenation')
    print("explicit" + "string concatenation")

And this file, `file2.py`:

    words = ['hello', 'there']
    names = ['Edmond', 'Kayla' 'Gary', 'Laura']

Running `concat_check.py` and passing in these files would print errors on all lines where implicit string 
concatenation occurs:

    $ python concat_check.py file1.py file2.py
    file1.py, line 1: implicit concatenation
    file1.py, line 3: implicit concatenation
    file2.py, line 2: implicit concatenation

The error you show could be more helpful than the above, but it doesn't need to be.

Initially you can treat a "string" as starting with either a single or double quote, followed by any number of 
characters which are not that same single or double quote, and ending with the same single or double quote. 
Implicit string concatenation occurs when any number of space characters can appear between these "strings".

Follow that definition above at first. Don't worry about f/b/u/r-strings, multi-line strings, newline characters, 
docstrings, escaped quote characters, etc.

If you get stuck on the base problem, check out the second hint for a regular expression that should match these 
"easier" cases (it won't work for the bonuses though).

#### Bonus 1

For the first bonus, I'd like you to ensure your script matches strings spread over multiple lines of code (due to 
an implicit line continuation).

For example with `my_code.py`:

    print(
        "implicit concatenation "
        "over multiple lines"
    )

This error should be printed:

    $ python concat_check.py my_code.py
    my_code.py, line 2: implicit concatenation

Note that the error is for line 2, not line 3. The error for implicit concatenation over multiple line should show 
the line number of the first string, not the second.

#### Bonus 2

For the second bonus I'd like you to make sure implicit concatenation works for multiline strings and also for raw 
strings (`r"\n"`), byte strings (`b'bytes'`), and unicode strings (`u"this"` and `U"this"`). The tests don't check for 
f-strings, but you can support those too if you like.

This file, `my_regex.py`:

import re

pattern = re.compile(
r"implicit\n"
u"line continuation"
)
m = pattern.search("""
implicit
"""
'line continuation')
print('match' if m else 'no match')

Will result in the following errors:

    $ python concat_check.py my_regex.py
    my_regex.py, line 4: implicit concatenation
    my_regex.py, line 9: implicit concatenation

Note that the end line of the first multi-line string is matched, not the beginning.

#### Bonus 3

For the third bonus, I'd like you to print out the strings between which the implicit line concatenation happened.

For example the above `my_regex.py` file would print:

    $ python concat_check.py my_regex.py
    my_regex.py, line 4 between r"implicit\n" and u"line continuation"
    my_regex.py, line 9 between """
    implicit
    """ and 'line continuation'
