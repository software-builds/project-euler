def special_pythogorean_triplet(maximal):
    for a in range(1, maximal):
        for b in range(1, maximal):
            for c in range(1, maximal):
                if a + b + c == maximal and pow(a, 2) + pow(b, 2) == pow(c, 2):
                    return a * b * c

if __name__ == "__main__":
    print(special_pythogorean_triplet(1_000))
