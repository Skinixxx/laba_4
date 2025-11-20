def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_first_n_fibonacci(n):
    fib = fibonacci_generator()
    return [next(fib) for _ in range(n)]

print("Первые 10 чисел Фибоначчи:")

for i in get_first_n_fibonacci(10):
    print(i,end=" ")
