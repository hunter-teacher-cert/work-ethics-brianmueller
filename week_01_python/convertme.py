def factorial(num):
    prod = 1
    i = num
    while i > 1:
        prod = prod * i
        i = i-1
    return prod

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print("Good News Everyone!")
print(f"1! = {factorial(1)}" )
print(f"fib(1) = {fib(1)}" )
# print(f"5! = {factorial(5)}" )
# print(f"fib(5) = {fib(5)}" )
