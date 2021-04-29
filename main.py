# Python program to display the Fibonacci sequence
def fibonacci(number):
    # ensuring that only positive numbers are accpeted
    if number <= 1:
        return number
    # the formula that calculates the fibonacci sequence
    else:
        return fibonacci(number-1) + fibonacci(number-2)

# the number of terms of the fibonacci sequence that are wanted
nth_term = 20

print("Fibonacci sequence: ")
# setting a range from the first term to the nth_term 
for i in range(nth_term):
    # printing the answers. The "end" parameter appends space 
    # instead of allowing each term to start on a new line.
    # The space between the inverted commas signify
    # that there should be spaces between each term.
    print(fibonacci(i), end=" ")
