# pyfsig

A python library for identifying files by headers (magic bytes)

based on info from: ['Wikipedia - List of file signatures'](https://en.wikipedia.org/wiki/List_of_file_signatures)

Still alpha, but code should be easy enough to follow and expand upon.


## `file_signatures.compare(header, test_hex_string)`

A method that compares a two file headers, the first one directly read from a file, the second is a a string containing space delimited hexidecimal byte codes. its a string becuase 'nn' is used to represent a wildcard byte.

### header

This is the first x bytes of a file, this can be obtained by opening the file using `open(file_name, 'rb')` mode. 

To obtain only the first few bytes use the following:

```python
with open(file_name, 'rb') as f:
    header = f.read(32)
```

### test_hex_string

This is the string of space delimited hexidecimal byte codes representing the file signature. 

'nn' is used to represent a wildcard byte

example:
```python
# for example, "%PDF"
test_hex_string = "25 50 44 46"

# showing wildcards, %P**DF
test_hex_string = "25 50 nn nn 44 46"
```


## `get_from_file(f, max_header=32)`

Return a Match object of all the matching Signatures for this file

### f

'f' is the open file object. 

> Note: you can use textIO to get a file like object from a string

### max_header

This is the length in bytes read from the start of the file used as the file header.


## `get_from_path(path, max_header=32)`

Return a Match object of all the matching signatures for this file, using the path rather than a file object now.

### path

'path' is the path to a file, it is passed into open() so it can be relative if you like.

### max_header

This is the length in bytes read from the start of the file used as the file header.


## `file_signatures.Signature`

A class that reimplements a dictionary. These are initialised and returned as part of the Match class when a Byte signature is tested using the `file_signatures.compare()` function.

### file_extension

A suggested file extension for this type of file

### description

A brief description of the file type taken from ['List of file signatures'](https://en.wikipedia.org/wiki/List_of_file_signatures).

### offset

Not implemented yet...

### ascii

ASCII interpretation of the file signature eg. '%PDF'

### hex

The space delimited hexidecimal byte codes representing the file signature.

example:
```python
# for example, "%PDF"
test_hex_string = "25 50 44 46"
```

(see above test_hex_string)


## `file_signatures.Match`

This is a list reimplemented, it is returned by get_from_file and get_from_path defs. It holds a list Signature objects.


## file_signatures.signatures

a list of dictionary items representing a file signature class. Used to check against and initialise new `Signatures`.

example:

```python
# example entry from file_signatures.signatures list
{'ascii': 'v/1.',
 'description': 'OpenEXR image',
 'file_extension': 'exr',
 'hex': '76 2F 31 01',
 'offset': '0'}
```