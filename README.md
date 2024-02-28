# pyfsig

A python library for identifying files by headers (magic bytes).
You may notice that on MS windows systems files will not open properly if you
change the file extension, this is becuase MS windows only pays attention to
the file header.
Magic bytes/file headers serve as a way to discover the type of file without
using the file extension.
This library was written to assist python programmers in identifying what type
of file something is from its magic bytes/file header.
It was originally written by the author to reconstruct BLOB's from a legacy
database which did not store the original file extensions.

based on info from: ['Wikipedia - List of file signatures'](https://en.wikipedia.org/wiki/List_of_file_signatures)

## Usage

The libraries use should fairly self explainatory, here are some examples:

### Find matches for a file when you have the file path

```python
file_path = "some/file/path.abc"
matches = find_matches_for_file_path(file_path=file_path)
```

### Find matches for a file header you have read yourself

> [!IMPORTANT]
> The "rb" here is very important, you must read the file as "bytes"!

```python
with open(file_path, "rb") as f:
    file_header = f.read(32)
matches = find_matches_for_file_header(header=file_header)
```

### Find matches against your own list of file signatures

You will need to create a `FileSignatureDict` with atleast the following keys:

* `file_extension`
* `hex`
* `offset`

```python
custom_signatures = [
    {
        "file_extension": "abc",
        "hex": [1, 2, 3, None, 5],
        "offset": 0,
    }
]

file_path = "some/file/path.abc"
matches = find_matches_for_file_path(file_path=file_path, signatures=custom_signatures)
```

Alternatively, you can extend the built in file signatures with your custom
file signatures.

```python
from pyfsig import SIGNATURES

extended_signatures = [
    *SIGNATURES,
    {
        "file_extension": "abc",
        "hex": [1, 2, 3, None, 5],
        "offset": 0,
    }
]

file_path = "some/file/path.abc"
matches = find_matches_for_file_path(file_path=file_path, signatures=extended_signatures)
```

## Contributors

Author: Patty C ([schlerp](https://github.com/schlerp))

![GitHub Contributors Image](https://contrib.rocks/image?repo=schlerp/pyfsig)

Thanks to all contributors!!
