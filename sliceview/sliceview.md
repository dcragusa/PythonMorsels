# SliceView

This week I'd like you to invent your own helper utility to make "slice views".

#### Our motivation

During my team Python trainings new Pythonistas sometimes ask me "why do slices of lists and tuples make a whole new 
tuple instead of just giving us a view into the tuple"?

My answer is either "for convenience and consistency" (with a bit of discussion of the alternatives) or "because 
that's how the Python core devs choose to do things" (which is a non-answer, but it's true... we're someone stuck 
with their decisions, good or bad).

So this week I'd like you to create a callable which allows us to lazily slice a given sequence (such as a list, 
tuple, or string).

#### The specifications

I'd like you to make a `SliceView` callable which accepts a sequence as well as optional `start`, `stop`, and `step` 
values and returns an lazy iterable (such as an iterator) of the sliced values.

    >>> colors = ['red', 'purple', 'pink', 'blue', 'green', 'black']
    >>> colors[:3]
    ['red', 'purple', 'pink']
    >>> list(SliceView(colors, stop=3))
    ['red', 'purple', 'pink']
    >>> colors[-2:]
    ['green', 'black']
    >>> list(SliceView(colors, start=-2))
    ['green', 'black']
    >>> colors[0::2]
    ['red', 'pink', 'green']
    >>> list(SliceView(colors, start=0, step=2))
    ['red', 'pink', 'green']
    >>> colors[::-1]
    ['black', 'green', 'blue', 'pink', 'purple', 'red']
    >>> list(SliceView(colors, step=-1))
    ['black', 'green', 'blue', 'pink', 'purple', 'red']

All of the ways other sequences can be sliced should be supported.

This week's problem is challenging! I highly recommend solving the base problem before attempting any of the bonuses.

#### Bonus 1

For the first bonus, make your `SliceView` return an iterable which can be looped over multiple times.

    >>> colors = ['red', 'purple', 'pink', 'blue', 'green', 'black']
    >>> view = SliceView(colors, start=1, stop=3)
    >>> list(view)
    ['purple', 'pink']
    >>> list(view)
    ['purple', 'pink']

A hint: you'll want `SliceView` to provide you with an iterable which is not an iterator.

#### Bonus 2

For the second bonus, you can allow your `SliceView` objects (you'll likely be using a class at this point) to have 
a length.

    >>> colors = ['red', 'purple', 'pink', 'blue', 'green', 'black']
    >>> view = SliceView(colors, start=1, stop=3)
    >>> len(view)
    2
    >>> view = SliceView(colors, step=2)
    >>> len(view)
    3

#### Bonus 3

For the third bonus, you can add the ability for your `SliceView` objects to be sliced (using the `[:]` slicing 
notation) and indexed.

    >>> colors = ['red', 'purple', 'pink', 'blue', 'green', 'black']
    >>> view = SliceView(colors)
    >>> list(view[:2])
    ['red', 'purple']
    >>> list(view[::-1][:2])
    ['black', 'green']
    >>> view[-3]
    'blue'

When your `SliceView` objects are sliced, they should return another `SliceView` object.

Is this actually useful?

You might be thinking `SliceView` seems no better than `itertools.islice`. But these two tools are quite different: 
one is specialized for iterators and the other is specialized for sequences.

So while this will take many seconds to run: `list(itertools.islice(range(10**11), 10**9, 10**9+5))`

This will run very quickly: `list(SliceView(range(10**11), 10**9, 10**9+5))`

You can think of `SliceView` as a lazy slice operation that is special-purposed for sequences (whereas `islice` 
assumes a no-sequence has been passed to it).

This might not be something you'd use often, but this kind of class could be useful at times.

In fact, Python has a `memoryview` class built-in that's essentially like a `SliceView` that is optimized for (and 
only works on) byte arrays objects.
