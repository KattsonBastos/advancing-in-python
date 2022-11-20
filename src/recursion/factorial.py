
n = 3

fact = 1

while n > 0:
    fact = fact * n

    n -= 1

print(fact)

n = 3
def factorial(n):
    if n < 1:
        return 1

    else:
        result = n * factorial(n - 1)

        return result

if __name__ == '__main__':
    print(factorial(n))
