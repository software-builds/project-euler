def sum_square_difference(maximal):
    sumOfSquares = 0
    squareOfSum = 0

    for i in range(1, maximal + 1):
        sumOfSquares += pow(i, 2)
        squareOfSum += i

    squareOfSum = pow(squareOfSum, 2)

    return abs(squareOfSum - sumOfSquares)

if __name__ == "__main__":
    print(sum_square_difference(100))
