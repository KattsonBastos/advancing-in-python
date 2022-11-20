
# first function

def mydecorator(function):

    def wrapper(*args, **kwargs):
        print("Decorating..")

        returned_value = function(*args, **kwargs)

        return returned_value

    return wrapper

def hello(name):
    print('Not Elegant Hi, ', name)

# this is not how it is done in python
mydecorator(hello)("Linux")

# a more elegant way of calling
@mydecorator
def elegant_hello(name):
    result = 'Elegant Hi, ' + name

    return result

    
print(elegant_hello("Linux"))
