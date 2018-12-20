# Print Fibonacci
# return Fibonacci series up to n
def get_me_fib(name, number):
    print("I'm ", name, "number ", number)
    result = []
    a, b = 0, 1
    while b < number:
        result.append(b)
        a, b = b, a + b
    return result


def get_me_even(name, number):
    print("I'm ", name, "number ", number)
    return number % 2 == 0


def is_positive(name, number):
    print("I'm ", name, "number ", number)
    return number > 0


if __name__ == '__main__':
    print("Im called")
    is_positive("From utilities", -100)
    get_me_even("From utilities", 2)
    get_me_fib("From utilities", 100)
