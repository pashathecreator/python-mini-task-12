import pytest
from coroutine_decorator import coroutine

@coroutine
def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)

def test_storage_coroutine():
    generator = storage()  
    assert generator.send(42) == False
    assert generator.send(42) == True
    

