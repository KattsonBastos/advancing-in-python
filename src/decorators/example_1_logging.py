# a loggin example (just for learning)

def logged(function):

    def wrapper(*args, **kwargs):

        value = function(*args, **kwargs)

        with open('logfile.txt', 'a+') as fp:
            fname = function.__name__
            message = f"{fname} returned value {value}\n"

            print(message)
            
            fp.write(message)
        
        return value

    return wrapper

@logged
def add(x, y):

    return x + y

print(add(10, 20))
