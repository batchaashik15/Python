'''
Fibonacci sequence generator
Step 1: get the input from the user on how many sequence required
step 2: Iterate using the logic to generate and display the numbers
'''


def fibonacci(number):
    '''
    Function to do the logic of iterating and return the
    results in form of list
    '''
    first = 0
    second = 1
    for n in range(number):
        yield first
        first, second = second, first + second


if __name__ == '__main__':
    '''
    Main function to get the input from the user and call the fibonacci
    function
    '''
    while True:
        number = input("Please enter the number of sequence needed :")
        result = fibonacci(int(number))
        print("Generated sequence is: " + str(tuple(result)))
        break
