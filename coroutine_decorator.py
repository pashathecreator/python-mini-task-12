from typing import Callable

def coroutine(func: Callable):
    def wrapper(*args, **kwargs):
        generator = func(*args, **kwargs)
        next(generator)
        return generator
    return wrapper