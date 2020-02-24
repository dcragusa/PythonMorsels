# record_calls

This week I'd like you to write a decorator function that will record the number of times a function is called.

Your decorator function should be called record_calls and it'll work like this:

    @record_calls
    def greet(name):
        """Greet someone by their name."""
        print(f"Hello {name}")

That record_calls-decorated greet function will now have a call_count attribute that keeps track of the number of times it was called:

    >>> greet("Trey")
    Hello Trey
    >>> greet.call_count
    1
    >>> greet()
    Hello world
    >>> greet.call_count
    2

Decorator functions are functions which accept another function and return a new version of that function to replace it.

So this should be the same thing as what we typed above:

    greet = record_calls(greet)

If you haven't ever made a decorator function before, you'll want to look up how to make one.

If you've made a decorator function before, you might want to attempt one of the bonuses.

#### Bonus 1

For the first bonus I'd like you to make sure your decorator function preserves the name and the docstring of the original function.

So if we ask for help on the function above:

    >>> help(greet)

We should see something like this:

    Help on function greet in module __main__:
    
    greet(name)
        Greet someone by their name.

#### Bonus 2

For the second bonus I'd like you to keep track of a "calls" attribute on our function that records the arguments and keyword arguments provided for each call to our function.

    >>> greet("Trey")
    Hello Trey
    >>> greet.calls[0].args
    ('Trey',)
    >>> greet.calls[0].kwargs
    {}
    >>> greet(name="Trey")
    Hello Trey
    >>> greet.calls[1].args
    ()
    >>> greet.calls[1].kwargs
    {'name': 'Trey'}
    
#### Bonus 3

For the third bonus, add a return_value and an exception attribute to each of the objects in our calls list. If the function returned successfully, return_value will contain the return value. Otherwise, exception will contain the exception raised.

When an exception is raised a special NO_RETURN value should be returned. Your module should have a NO_RETURN attribute that contains this special value.

    >>> @record_calls
    ... def cube(n):
    ...     return n**3
    ...
    >>> cube(3)
    27
    >>> cube.calls
    [Call(args=(3,), kwargs={}, return_value=27, exception=None)]
    >>> cube(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 9, in wrapper
      File "<stdin>", line 3, in cube
    TypeError: unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'
    >>> cube.calls[-1].exception
    TypeError("unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'")
    >>> cube.calls[-1].return_value == NO_RETURN
    True
