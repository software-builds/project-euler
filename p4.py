def largest_palindrom_product(maximum):
    first = maximum
    second = maximum

    calculated = first * second
    reversed = reverse(calculated)

    palindroms = []

    while not first == 100 and not second == 100:
        if calculated == reversed:
            palindroms.append(calculated)

        first-=1
        
        if (first == 100):
            first = maximum
            second -= 1

        calculated = first * second
        reversed = reverse(calculated)

    return max(palindroms)

def reverse(number):
    reversed = 0

    print(number)

    while number > 0:
        tmp = number % 10
        reversed = reversed * 10 + tmp
        number //= 10

    return reversed

if __name__ == "__main__":
    print(largest_palindrom_product(999))
