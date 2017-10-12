def primeNumbers(n):
    prime_list = []
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        return True
    if i == True:
        prime_list.append(i)
    else:
        return False

