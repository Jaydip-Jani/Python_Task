def count(s, c):
    res = 0

    for i in range(len(s)):
        if (s[i] == c):
            res = res + 1
    return res


str = "United States"
c = 'e'
print(count(str, c))
