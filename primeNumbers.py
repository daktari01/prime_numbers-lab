def primeNumbers(n):
    prime_list = []
    if type(n) != int:
        raise TypeError
    elif n <= 0:
        return prime_list
    else:
        for x in range(2, n + 1):
            is_prime = True
            for y in range(2, int(x ** 0.5) + 1):
                if x % y == 0:
                    is_prime = False
                    break
            if is_prime:
                #print(x)
                prime_list.append(x)
        
        return prime_list     
print(primeNumbers(10))
