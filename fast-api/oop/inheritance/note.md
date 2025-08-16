### Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

Any class can be a parent class, so the syntax is the same as creating any other class
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

## Add the __init__() Function
So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).

Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function

## Use the super() Function
Python also has a super() function that will make the child class inherit all the methods and properties from its parent

By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

## Add Properties
To do so, add another parameter in the __init__() function

## Add Methods
If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.