def collatz(n):
    if n % 2 == 0:
        return int(n/2)
    return 3*n + 1

print("gimma numba")

n = int(input())

print("hola ")

for i in range(1, n + 1):

    seq = []
    seq.append(i)

    while (collatz(i) != 1):
        # print(collatz(n))
        i = collatz(i)
        seq.append(i)
    seq.append(collatz(i))
    print(seq)