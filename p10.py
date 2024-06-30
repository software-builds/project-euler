def summation_of_primes(maximal):
    primes = [True for i in range(maximal)]
    p = 2

    while p * p <= maximal:

        if primes[p] == True:
            for i in range(p * p, maximal, p):
                primes[i] = False
    
        p += 1

    sum = 0
    for p in range(2, maximal):
        if primes[p]:
            sum += p

    return sum

if __name__ == "__main__":
    print(summation_of_primes(2_000_000))
