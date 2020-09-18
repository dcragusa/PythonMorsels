# Timer revisited

This week I'd like you to recreate a new variation of the `Timer` context manager we've already made. Feel free to 
peek at your solutions previously if you need some help.

This time I'd like your context manager to start with an elapsed attribute and a runs attribute:

    >>> from time import sleep
    >>> with Timer() as timer:
    ...     sleep(1.5)
    ...
    >>> timer.elapsed
    1.5001550229990244
    >>> timer2 = Timer()
    >>> with timer2:
    ...     x = sum(range(2**24))
    ...
    >>> timer2.elapsed
    0.29633196399845474
    >>> with timer:
    ...     x = sum(range(2**25))
    ...
    >>> timer2.elapsed
    0.29633196399845474
    >>> timer.runs
    [1.5001550229990244, 0.5478551739997783]

#### Bonus 1

For the first bonus, I'd like your `Timer` context manager to have a `split` method which will create a sub-timer. 
The `split` method should accept an optional name for the split:

    >>> from time import sleep
    >>> with Timer() as timer:
    ...     with timer.split():
    ...         sleep(0.5)
    ...     with timer.split():
    ...         sleep(2)
    ...     with timer.split():
    ...         pass
    ...

Each of these splits should be accessible via indexing numerically or looking up splits by their name (for named 
splits):

    >>> timer.elapsed
    2.503067784011364
    >>> timer[0].elapsed
    0.5007675330271013
    >>> timer[1].elapsed
    2.002220475987997
    >>> timer[2].elapsed
    2.1249870769679546e-06

Using a split timer when its parent timer isn't running should raise a `RuntimeError` exception:

    >>> from time import sleep
    >>> with Timer() as timer:
    ...     pass
    >>> with timer.split():
    ...     pass
    ...
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    RuntimeError: Cannot split because parent timer is not running

#### Bonus 2

For the second bonus I'd like your `Timer` object's `split` method to accept an optional name which can be used for 
reusing a sub-timer of the same name:

    >>> from time import sleep
    >>> with Timer() as timer:
    ...     for i in range(3):
    ...         with timer.split('loop'):
    ...             sleep(0.2)
    ...
    >>> timer['loop'].runs
    [0.20035718497820199, 0.20025292108766735, 0.2010224419645965]

#### Bonus 3

For the third bonus I'd like you to accept an optional name to your `Timer` objects. Timers created with the same 
name should act the same. You can think of creating a timer with the same name as "reusing" the same timer.

    >>> from time import sleep
    >>> with Timer('sleep'):
    ...     sleep(0.2)
    ...
    >>> with Timer('sleep') as timer:
    ...     sleep(0.2)
    ...
    >>> timer.runs
    [0.20043494799756445, 0.20049414699315093]

Hint: for the last bonus you may want to look into sharing state between multiple classes or overriding the class 
constructor to reuse previous class instances.
