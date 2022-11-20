# Decorators



<p align="justify">
&ensp;&ensp;&ensp;&ensp;The basic idea of decorators is that they add new functionalities to a function. In Python, a decorator basically doest some functionality and then calls the target function (we can also do something else after calling the function). To better understand that, a decorator looks like the following:
</p>

```python
def my_decorator(function):
    
    def wrapper():
        print("Doing something before calling the function..")

        function()

    return wrapper
```

<p align="justify">
&ensp;&ensp;&ensp;&ensp;The argument received by the `decorator` is the function we want to decorate.
At the end, we are just returning another function that calls the initial function. However, the thing here, again, is that we are going to execute our target function with aditional code. Note that the name of our inner function, the `wrapper`, can be anything, we just have to keep in mind that the function we're returning at the end must be that inner function. 
</p>

<p align="justify">
&ensp;&ensp;&ensp;&ensp; Let's better understand what that mean by using that decorator. The following code block creates a decorated function that sum two numbers:
</p>

```python
@my_decorator
def add_numbers():

    print(2 + 3)
```

<p align="justify">
&ensp;&ensp;&ensp;&ensp; We can decorate functions by using both the `@` or calling the decorator function and passing the target one as argument:
</p>

```python
my_decorator(add_numbers())
```

<p align="justify">
&ensp;&ensp;&ensp;&ensp; Both methods do the same thing and `@my_decorator` is a more easy,simple way of decorating our function.
</p>

<p align="justify">
&ensp;&ensp;&ensp;&ensp; Awesome! But what should we do if we need to pass two numbers ()arguments) to the function? Here, we need both to pass the parameters in the definition and to add the args to the decorator wrapper. The following code block shows that:
</p>

```python
# creating the decorator
def my_decorator(function):
    def wrapper(*args, **kwargs):
        print("Doing something before calling the function..")

        function(*args, **kwargs)

    return wrapper

# creating our target function
@my_decorator
def add_numbers(a, b):

    print(a + b)
```

<p align="justify">
&ensp;&ensp;&ensp;&ensp;  Here, `args` and `kwargs` do the magic for us. They will allow for arbitrary numbers of arguments. So, no matter what function and arguments we pass, it will run.
</p>

<p align="justify">
&ensp;&ensp;&ensp;&ensp; However, we still have a problem: and if we need the `add_numbers` to return the result? If we add the `return` to our function, the output still gonna be `None`. That happens because the `wrapper` doest not explicitly return anything. We can fix this by adding a return to it as the following:
</p>

```python
def my_decorator(function):
    
    def wrapper(*args, **kwargs):
        print("Doing something before calling the function..")

        result = function(*args, **kwargs)

        return result

@my_decorator
def add_numbers(a, b):
    print(a + b)
    
    return a + b
```

<p align="justify">
&ensp;&ensp;&ensp;&ensp; Now, if we call our function passing two numbers, like 2 and 3, it should return the value (which is 5, in this case).
</p>



