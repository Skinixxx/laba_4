import random
import string

def random_data_generator():

    

    data_types = ['int', 'float', 'str', 'bool', 'list']
    
    while True:
        data_type = random.choice(data_types)
        

        if data_type == 'int':

            yield random.randint(-1000, 1000)
        
        elif data_type == 'float':
 
            yield random.uniform(-1000.0, 1000.0)
        
        elif data_type == 'str':
 
            length = random.randint(1, 20)
 
            characters = string.ascii_letters + string.digits
            yield ''.join(random.choices(characters, k=length))
        
        elif data_type == 'bool':
            
            yield random.choice([True, False])
        
        elif data_type == 'list':
            
            list_length = random.randint(1, 5)
            yield [random.randint(1, 100) for _ in range(list_length)]


def process_random_data():
    generator = random_data_generator()
    
    for i in range(10):
        data = next(generator)
        data_type = type(data).__name__
        
        
        if isinstance(data, int):
            print(f"Целое число: {data}")
        elif isinstance(data, float):
            print(f"Вещественное число: {data:.2f}")
        elif isinstance(data, str):
            print(f"Строка (длина {len(data)}): '{data}'")
        elif isinstance(data, bool):
            print(f"Логическое значение: {data}")
        elif isinstance(data, list):
            print(f"Список: {data}")

process_random_data()