def print_pattern_05(n_pat):
    for i in range(0, n_pat):
        for j in range(i+1, 0):
            print("*", end=" ")
        print()


print_pattern_05(5)