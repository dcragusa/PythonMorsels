# alias

This week I'd like you to create a callable helper utility, called alias, for making classes with attributes that act as "aliases" to other attributes. The alias callable should work like this:

    class DataRecord:
        title = alias('serial')
        def __init__(self, serial):
            self.serial = serial

This should allow title to mirror the value of serial when being read:

    >>> record = DataRecord("148X")
    >>> record.title
    '148X'
    >>> record.serial = "149S"
    >>> record.title
    '149S'

You don't need to worry about what happens when you write to title, until the first bonus.

Hint: you can solve the main exercise using just the built-in property decorator, but you'll likely need to reach for the descriptor protocol eventually.

#### Bonus 1

For the first bonus, I'd like you to make sure an AttributeError exception is raised when your aliases are assigned to.

    >>> record = DataRecord("148X")
    >>> record.title = "149S"
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: can't set attribute

#### Bonus 2

For the second bonus, I'd like you to accept a write keyword argument to allow your aliased attribute to be written to. Using that attribute would look like this:

    class DataRecord:
        title = alias('serial', write=True)
        def __init__(self, serial):
            self.serial = serial

And writing to the alias should update the value of the attribute being aliased:

    >>> record = DataRecord("148X")
    >>> record.title = "149S"
    >>> record.serial
    '149S'

#### Bonus 3

For the third bonus, I'd like you to support class-level aliases and not just instance-level aliases.

This class that maintains a _registry attribute and a read-only registry attribute aliasing it:

    class RegisteredObject:
        _registry = ()
        registry = alias('_registry')
        def __init__(self, name):
            RegisteredObject._registry += (self,)
            self.name = name

Accessing the registry attribute at the class level should work properly:

    >>> object = RegisteredObject("Trey")
    >>> object.name
    'Trey'
    >>> RegisteredObject.registry
    (<__main__.RegisteredObject object at 0x7f06ca5bf9b0>,)
