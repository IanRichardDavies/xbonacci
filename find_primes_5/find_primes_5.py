def find_primes(n):
    '''
    Returns all prime numbers up until n
    '''
    primes_list = [2]
    for i in range(3,n):
        prime = True
        if i % 2 != 0:
            for j in range(3,int(sqrt(i)+1),2):
                if i % j == 0:
                    prime = False
        else:
            prime = False
        if prime == True:
            primes_list.append(i)
    return primes_list