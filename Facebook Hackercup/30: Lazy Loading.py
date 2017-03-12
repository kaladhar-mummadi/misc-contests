def hackercup():
    days = int(input())
    for i in range(days):
        N = int(input())
        weights = []
        for _ in range(N):
            weights.append(int(input()))
        weights = sorted(weights)
        res = 0
        while len(weights) > 0:
            highest_weight = weights.pop()
            to_remove = int(50/(highest_weight+1))
            if to_remove !=0 and len(weights) < to_remove:
                break
            weights = weights[to_remove:]
            res += 1
        print("Case #" + str(i+1) + ": " + str(res))

if __name__ == '__main__':
    hackercup()