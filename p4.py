def largest_palindrom_product(maximum):
    biggestPalindrom = 0

    minimum = maximum
    count = 0

    while minimum > 0:
        minimum //= 10
        count += 1

    minimum = pow(10, count - 1)

    first = maximum
    while first >= minimum:
        second = maximum
        
        while second >= first:
            calculated = first * second
            
            if calculated <= biggestPalindrom:
                break

            if reverse(calculated) == calculated:
                biggestPalindrom = calculated

            second -= 1

        first -= 1

    return biggestPalindrom

def reverse(number):
    reversed = 0

    while number > 0:
        tmp = number % 10
        reversed = reversed * 10 + tmp
        number //= 10

    return reversed

if __name__ == "__main__":
    print(largest_palindrom_product(999))
