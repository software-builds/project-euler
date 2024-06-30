def even_fibonacci_numbers(maximum):
    sum = 0

    first = 1
    second = 2

    while second < maximum:
        if second % 2 == 0:
            if second > maximum:
                return sum

            sum += second

        tmpFirst = first
        first = second
        second = tmpFirst + second

    return sum

if __name__ == "__main__":
    print(even_fibonacci_numbers(4_000_000))
