def search(l, r, arr, x):
    m = (r + l) // 2

    if r < l:
        return False

    if x < arr[m]:
        return search(l, m - 1, arr, x)
    elif x > arr[m]:
        return search(m + 1, r, arr, x)
    else:
        return True


inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(search(0, len(arr) - 1, sorted(arr), k))