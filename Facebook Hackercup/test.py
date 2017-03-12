def subset_sum(numbers, target, res , max_len, partial=[]):
    s = sum(partial)
    if len(partial) > max_len:
        return
    if s >= target:
        res += 1
        return res
    if len(numbers) == 0:
        return res
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, res, 2, partial + [n])
if __name__ == '__main__':
    subset_sum([1,1,2,2,3,3], 5, 0, 2)