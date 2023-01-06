# Fibonacci

# f0 = 0
# f1 = 1


def fibonacci(end):

    tab = [0, 1]

    i = 2
    while len(tab) <= end:
        tab.append(tab[i-1] + tab[i-2])
        i += 1

    return tab


print(fibonacci(10))
