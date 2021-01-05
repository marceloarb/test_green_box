from class1 import math

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_square():
    assert math(4,4), "Should be 16"

def test_green():
    assert sum([1,3,4]) == 8, "Should be 8"
def test_print_all_the_numbers_greater_than_Y():
    array = [100,45,2435,5,4,4,3,325,4,5,6,532,54,4,54,52,3]
    y = 99
    for i in array:
        if i > y:
            print(f"I is greated than Y i = {i}")

def test_get_green():
    print("Hello World")
    print("Hello World 1")
    print("Hello World 2")
    

test_print_all_the_numbers_greater_than_Y()
