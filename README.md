# rm-rf
Python 2 and 3 almost compatible POSIX rm -rf.

## Introduction
POSIX `rm -rf` command can delete a directory (or a file) and also all of its subdirectories/file recursively, like Python's `shutil.rmtree`, but `rm -rf` doesn't raise any error when the directory does not exists or when the path is a file.
Therefore, the `rm_rf` function in this package just use Python's `os.remove` and `shutil.rmtree` and catch their errors:

```python
from rm_rf import rm_rf
rm_rf("path/to/the/dir/")
```
Note: function does not handle Unix character and block devices.

## Installation

```
pip install rm-rf
```
