def summation_of_primes(maximal):
    sum = 0

    for i in range(1, maximal):
        if isPrime(i):
            print(i)
            sum += i

    return sum

def isPrime(number):
    if number < 2: return False

    for i in range(2, number):
        if number % i == 0:
            return False
        
    return True

if __name__ == "__main__":
    print(summation_of_primes(2_000_000))
