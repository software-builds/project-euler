def smallest_multiple(maximal):
    found = False
    count = 1

    while not found:
        fouds = 0

        for i in range(1, maximal + 1):
            if count % i != 0:
                count += 1
                continue

            fouds += 1

            
        if fouds == maximal:
            found = True

    return count

if __name__ == "__main__":
    print(smallest_multiple(20))
