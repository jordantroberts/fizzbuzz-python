def fizzbuzz(n):
    if n % 15 == 0:
        return 'FizzBuzz'
    if n % 3 == 0:
        return 'Fizz'
    if n % 5 == 0:
        return 'Buzz'
    else:
        return n


def play():
    n = 0

    while n <= 100:
        print(fizzbuzz(n))
        n += 1

play()