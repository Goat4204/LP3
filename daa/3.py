def knapsack(w, p, c):
    ratio = [p[i] / w[i] for i in range(len(w))]
    items = sorted(zip(ratio, w, p), reverse=True)
    profit = 0

    for r, wt, val in items:
        if c >= wt:
            profit += val
            c -= wt
        else:
            profit += r * c
            break

    print("Maximum Profit:", profit)

w = list(map(int, input("Enter weights: ").split()))
p = list(map(int, input("Enter profits: ").split()))
c = int(input("Enter capacity: "))

knapsack(w, p, c)