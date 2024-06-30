def the10_001st_prime(maximal):
    count = 0
    zahl = 0
    prime = 0

    while count != maximal:
        if isPrime(zahl):
            prime = zahl
            count += 1

        zahl += 1

    return prime

def isPrime(number):
    if number < 2: return False

    for i in range(2, number):
        if number % i == 0:
            return False
        
    return True

if __name__ == "__main__":
    print(the10_001st_prime(10_001))
