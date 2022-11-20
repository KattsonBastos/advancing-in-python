
# this is a bad example: for large numbers, it will take and eternity to run
def normal_fib(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a+b

    return a

def rec_fib(n):
    pass

if __name__ == '__main__':
    n = 0
    print(normal_fib(n))
