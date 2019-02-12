# 10001st PRIME - 5%
def primes(n):
    for i in range(2,int(n/2)):
        if n % i == 0:
            return False
    return True
    
def countprimes(target):
    '''
    Finds the nth prime, starting 2 (n = 1)
    '''
    counter = 1
    num = 3
    while counter <= target:
        if primes(num):
            counter += 1
        if counter == target:
            return num
        num +=2
    return num
        
