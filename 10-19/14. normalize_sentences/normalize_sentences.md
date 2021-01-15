# normalize_sentences

When I write text in a fixed-width font (code, markdown, etc.), I use two spaces after sentences. This can lead 
to inconsistencies when I copy text from elsewhere or I collaborate on a project with someone who isn't a 2-spacer.

So this week I'd like you to write a function, `normalize_sentences`, which accepts a string of text and makes 
sure there are two spaces between the sentences.

Your function should work like this:

    >>> normalize_sentences("I am. I was. I will be.")
    'I am.  I was.  I will be.'
    >>> normalize_sentences("Hello? Yes, this is dog!")
    'Hello?  Yes, this is dog!'

Your function should treat `.`, `?`, and `!` as sentence-ending characters.

#### Bonus 1

For the first bonus, I'd like you to make sure your function doesn't add unnecessary extra spaces if there 
are already two spaces between some sentences. Your function should also ensure that paragraph breaks and 
other whitespace is maintained as it was.

    >>> normalize_sentences("I am.  I was. I will be.")
    'I am.  I was.  I will be.'
    >>> normalize_sentences("I said.  She said.\n\nThey said. We said.")
    'I said.  She said.\n\nThey said.  We said.'

#### Bonus 2

For the second bonus, I'd like you to make sure `normalize_sentences` doesn't make a sentence break after an 
abbreviation or a decimal number:

    >>> normalize_sentences("I sold $5.50 worth of various fruits (i.e. apples).")
    'I sold $5.50 worth of various fruits (i.e. apples).'

#### Bonus 3

For the third bonus I'd like you to see if you can get `normalize_sentences` working with strings like this one:

    >>> normalize_sentences("Have you used searched for Dr. Seuss on google.com?")
    'Have you used searched for Dr. Seuss on google.com?'

A hint: regular expressions may come in handy when solving these.
