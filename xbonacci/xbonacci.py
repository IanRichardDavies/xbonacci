def Xbonacci(signature, n):
    fibs = list(signature)
    num = len(signature)
    if n == 0:
        return []
    elif n <= num:
        return fibs[:n]
    else:
        for i in range(n-num):
            total = [fibs[-x] for x in range(1,num+1)]
            fibs.append(sum(total))
        return fibs