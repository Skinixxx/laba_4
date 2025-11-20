def curry(func):
    
    def curried(*args, **kwargs):
       
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        
        
        def partial(*more_args, **more_kwargs):
            new_args = args + more_args
            new_kwargs = {**kwargs, **more_kwargs}
            return curried(*new_args, **new_kwargs)
        
        return partial
    
    return curried

@curry
def multiply_three_numbers(a, b, c):
    return a * b * c


double = multiply_three_numbers(2)        
triple = double(3)                        
result = triple(4)                         

print("Карринг умножения трех чисел:")
print(f"multiply_three_numbers(2, 3, 4) = {multiply_three_numbers(2, 3, 4)}")
print(f"Каррированное: multiply_three_numbers(2)(3)(4) = {multiply_three_numbers(2)(3)(4)}")