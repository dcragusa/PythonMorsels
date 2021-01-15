# condense_csv

This week I'd like you to write a function, `condense_csv`, which groups CSV text by the first column.

The input CSV text will always contain 3 columns: ID, attribute name, attribute value.

Example:

    >>> text = """\
    ... ball,color,purple
    ... ball,size,4
    ... ball,notes,it's round
    ... cup,color,blue
    ... cup,size,1
    ... cup,notes,none"""
    >>> print(condense_csv(text, id_name='object'))
    object,color,size,notes
    ball,purple,4,it's round
    cup,purple,1,none

So given a file, `songs.txt` like this:

    01,Artist,Otis Taylor
    01,Title,Ran So Hard the Sun Went Down
    01,Time,3:52
    02,Artist,Waylon Jennings
    02,Title,Honky Tonk Heroes (Like Me)
    02,Time,3:29

We could get text containing a "condensed" version of this data like this:

    >>> print(condense_csv(open('songs.txt').read(), id_name='Track'))
    Track,Artist,Title,Time
    01,Otis Taylor,Ran So Hard the Sun Went Down,3:52
    02,Waylon Jennings,Honky Tonk Heroes (Like Me),3:29

At first you don't need to worry about our input data containing commas. Just assume all commas are column separators.

#### Bonus 1

For the first bonus, you should handle CSV files that contain data with commas:

    >>> text = 'A,prop1,"value, with comma"\nA,prop2,value without comma'
    >>> print(condense_csv(text, id_name='Name'))
    Name,prop1,prop2
    A,"value, with comma",value without comma

#### Bonus 2

For the second bonus, if no `id_name` argument is specified the `condense_csv` function should consider the 
first column as a header and should use the first header as the `id_name`.

    >>> text = """\
    ... object,property,value
    ... ball,color,purple
    ... ball,size,4
    ... ball,notes,it's round
    ... cup,color,blue
    ... cup,size,1
    ... cup,notes,none"""
    >>> print(condense_csv(text))
    object,color,size,notes
    ball,purple,4,it's round
    cup,purple,1,none

#### Bonus 3

For the third bonus, your `condense_csv` function should allow missing properties and out-of-order properties. 
All property columns should be presented in the order the property was first seen and missing properties should 
be represented with an empty string.

    >>> text = 'A,prop1,x\nA,prop2,y\nB,prop2,z'
    >>> print(condense_csv(text, id_name='Name'))
    Name,prop1,prop2
    A,x,y
    B,,z
