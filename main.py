def fibonacci(number):
    if number <= 1:
        return number
    else:
        return fibonacci(number-1) + fibonacci(number-2)


nth_term = 20

print("Fibonacci sequence: ")
for i in range(nth_term):
    print(fibonacci(i), end=" ")

"""print(fibonacci(0), fibonacci(1), fibonacci(2), fibonacci(3), fibonacci(4), fibonacci(5), fibonacci(6), fibonacci(7),
      fibonacci(8), fibonacci(9), fibonacci(10), fibonacci(11), fibonacci(12), fibonacci(13), fibonacci(14),
      fibonacci(15), fibonacci(16), fibonacci(17), fibonacci(18), fibonacci(19))"""
