# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.'

## Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

## From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

## Number of Arguments
# By default, a function must be called with the correct number of arguments.

## Arbitrary Arguments, *args
# If you do not know `how many arguments` that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a `tuple` of arguments, and can access the items accordingly:
# `Arbitrary Arguments are often shortened to *args`

## Keyword Arguments (kwargs)
# You can also send arguments with the key = value syntax.
## Arbitrary Keyword Arguments, **kwargs
# If you do not know `how many keyword arguments` that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a `dictionary` of arguments, and can access the items accordingly


# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

# The pass Statement
## function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

# Positional-Only Arguments
## `a function can have ONLY positional arguments`
## add , / after the arguments

# Keyword-Only Arguments
## `a function can have only keyword arguments`
## add *, before the arguments

# Combine Positional-Only and Keyword-Only
## Any argument before the / , are positional-only, and any argument after the *, are keyword-only.