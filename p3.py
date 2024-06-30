def largest_prime_factor(maximum):
    solution = []
    
    i = 0

    calculatedSolution = 1

    downgrade = maximum

    while calculatedSolution != maximum:
        calculatedSolution = 1

        if isPrime(i):
            if downgrade % i == 0:
                downgrade /= i
                solution.append(i)
        
        for j in solution:
            calculatedSolution *= j

        i += 1

    return max(solution)

def isPrime(number):
    if number < 2: return False

    for i in range(2, number):
        if number % i == 0:
            return False
        
    return True

if __name__ == "__main__":
    print(largest_prime_factor(600_851_475_143))
