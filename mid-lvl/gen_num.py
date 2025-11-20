import random

def random_range_generator(start, end):

    while True:
        yield random.randint(start, end)

def get_random_numbers(count, start, end):
    generator = random_range_generator(start, end)
    return [next(generator) for _ in range(count)]

print("5 случайных чисел от 1 до 100:")
print(get_random_numbers(5, 1, 100))