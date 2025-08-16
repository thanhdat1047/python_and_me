## File handling
# Python has several functions for creating, reading, updating, and deleting files.

# The key function for working with files in Python is the `open()` function.
# The `open()` function takes two parameters; `filename`, and `mode`.
# There are four different methods (modes) for opening a file
# `r` - Read - Default value. Opens a file for reading, error if the file does not exist
# `a` - Append - Opens a file for appending, creates the file if it does not exist
# `w` - Write - Opens a file for writing, creates the file if it does not exist
# `x` - Create - Creates the specified file, returns an error if the file exists

## The file should be handled as binary or text mode
# `t` - Text - Default value. Text mode
# `b` - Binary - Binary mode (e.g. images)

## Syntax: `f = open("demofile.txt", "rt")`

# The `open()` function returns a file object, which has a `read()` method for reading the content of the file

# Use the `with()` statement when opening a file
# do not have to worry about closing your files, the with statement takes care of that.

# Close Files `close()`

# By default the `read()` method returns the whole text, but you can also specify how many characters you want to return 
# exp: `f.read(5)`

# You can return one line by using the `readline()` method

## Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:
# `a` - Append - will append to the end of the file
# `w` - Write - will overwrite any existing content

## Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
# `x` - Create - will create a file, returns an error if the file exists
# `a` - Append - will create a file if the specified file does not exists
# `w` - Write - will create a file if the specified file does not exists

## Delete a File
# To delete a file, you must import the OS module, and run its o`s.remove()` function

## Check if File exist `os.path.exists("demofile.txt")`
## To delete an entire folder, use the `os.rmdir()` method


