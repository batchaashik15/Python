def prime_factor(num, num_list):
    '''
    Recursive function to find the prime factorization
    Returns the list of factorials
    '''
    reminder = 0
    if not num <= 1:
        for i in range(2, num+1):
            if num % i == 0:
                num_list.append(str(i))
                reminder = int(num/i)
                break
        prime_factor(reminder, num_list)
    else:
        return num_list


if __name__ == '__main__':
    while True:
        number = int(input("Please povide the value to find the prime factorization :"))
        number_list = []
        # recursive function call to itearte and append the reults to the list
        prime_factor(number, number_list)
        print("Please find the results below : ")
        print('*'.join(number_list))
        break
