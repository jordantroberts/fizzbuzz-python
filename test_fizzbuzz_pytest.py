from fizzbuzz import fizzbuzz

def test_is_divisible_by_15():
    assert fizzbuzz(15) == 'FizzBuzz'

def test_is_divisible_by_3():
    assert fizzbuzz(3) == 'Fizz'

def test_is_divisible_by_5():
    assert fizzbuzz(5) == 'Buzz'

def test_returns_number():
    assert fizzbuzz(13) == 13
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2