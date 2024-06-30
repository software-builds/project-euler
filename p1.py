def multiples_of_3_or_5(maximum):
    sum = 0

    for i in range(0, maximum):
        if i % 3 == 0 or i % 5 == 0:
            sum+=i
    
    return sum

if __name__ == "__main__":
    print(multiples_of_3_or_5(1_000))
