# instance_tracker

This week I'd like you to make a "class factory" which will allow classes to track instances of themselves.

This `instance_tracker` class factory will return a class when called and can be used like this:

    class Account(instance_tracker()):
        def __init__(self, number):
            self.number = number
            super().__init__()
        def __repr__(self):
            return 'Account({!r})'.format(self.number)

Now the `Account` class will have an `instances` attribute which will keep track of all instances of the 
`Account` class.

    >>> a1 = Account('4056')
    >>> a2 = Account('8156')
    >>> print(*Account.instances, sep='\n')
    Account('4056')
    Account('8156')

At first you can assume that subclasses of `instance_tracker` never override `__init__` without 
calling `super().__init__(...)`.

#### Bonus 1

For the first bonus, allow your `instance_tracker` class factory to optionally accept an attribute name to 
use for storing the instances (instead of the default `instances`).

    class Person:
        def __init__(self, name):
            self.name = name
        def __repr__(self):
            return "Person({!r})".format(self.name)
    
    class TrackedPerson(instance_tracker('registry'), Person):
        """Example of inheritance and renaming 'instances' to 'registry'."""

That class should have a `registry` attribute instead of an `instances` attribute:

    >>> brett = TrackedPerson("Brett Cannon")
    >>> guido = TrackedPerson("Guido van Rossum")
    >>> carol = TrackedPerson("Carol Willing")
    >>> list(TrackedPerson.registry)
    [Person('Brett Cannon'), Person('Guido van Rossum'), Person('Carol Willing')]

#### Bonus 2

For the second bonus, make sure your `instance_tracker` factory works even for subclasses that don't call 
`super().__init__(...).`

For example this class:

    class Person(instance_tracker()):
        def __init__(self, name):
            self.name = name
        def __repr__(self):
            return "Person({!r})".format(self.name)

Should work as expected:

    >>> nick = Person("Nick Coghlan")
    >>> brett = Person("Brett Cannon")
    >>> list(Person.instances)
    [Person('Nick Coghlan'), Person('Brett Cannon')]

#### Bonus 3

For the third bonus, I'd like you to make sure that objects which are not referenced anywhere else will be 
deleted from memory as usual.

Take this class for example:

    class Account(instance_tracker()):
        def __init__(self, number):
            self.number = number
        def __repr__(self):
            return 'Account({!r})'.format(self.number)

Making three instances where one is no longer referenced (we're using `a1` twice below) and one has had its 
last reference removed (using `del a2`) should result in just one reference:

    >>> a1 = Account('4056')
    >>> a2 = Account('8156')
    >>> a1 = Account('3168')
    >>> del a2
    >>> list(Account.instances)
    [Account('3168')]
