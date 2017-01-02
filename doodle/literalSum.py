def digit_sum(n):
    n = str(n).strip()
    n = list(map(lambda x : int(x),n))
    return sum(n)
print(digit_sum(999))
