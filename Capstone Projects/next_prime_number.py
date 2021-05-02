def is_prime(number):
    ''' Function to check the given number is prime or not '''
    for n in range(2, number):
        if number % n == 0:
            return False
    return True


def find_next_prime(number):
    '''
    Function to iterate and return the next
    prime numbers until user exits
    '''
    got_prime = 0
    number += 1
    while got_prime == 0:
        if is_prime(number):
            return number
        else:
            number += 1
            continue


if __name__ == '__main__':
    '''
    Main to orchestrate the logic
    '''
    prime_number = 2
    print(f"Here's the first prime number in the list ==> {prime_number}")
    user_choice = ""
    while user_choice.lower() != "n":
        user_choice = input("Do you want to see the next Prime No., Press N or Q for Exit ==> ")
        if user_choice.lower() == "q":
            print("Thanks You!!!")
            break
        elif user_choice.lower() == "n":
            prime_number = find_next_prime(prime_number)
            print(f"Here's the next prime number in the list ==> {prime_number}")
            user_choice = ""
            continue
        else:
            print("Sorry I dont understand you, Please type N or Q to proceed.")
            continue
