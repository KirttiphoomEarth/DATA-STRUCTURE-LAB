def search(l, r, arr, x):
    m = (r + l) // 2

    if r < l:
        if l == len(arr):
            return 'No First Greater Value'
        return arr[l]

    if x < arr[m]:
        return search(l, m - 1, arr, x)
    elif x > arr[m]:
        return search(m + 1, r, arr, x)
    else:
        if arr[m] is not arr[-1]:
             return arr[m + 1]
        return 'No First Greater Value'


inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), inp[1]

for a in k.split():
    print(search(0, len(arr) - 1, sorted(arr), int(a)))