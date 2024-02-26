def szukaj_idola(arr):
    n = len(arr)
    kandydat = 0
    jest_kandydat = False
    while kandydat < n and not jest_kandydat:
        i = 0
        arr[kandydat][kandydat] = False
        while i <n and not arr[kandydat][i]:
            i= i+ 1
        if i == n:
            jest_kandydat = True
        else:
            kandydat = kandydat +1
    if jest_kandydat == False:
        return -1
    i = 0
    arr[kandydat][kandydat] = True
    while i < n and arr[i][kandydat]:
        i+=1
    if i == n:
        return kandydat
    else:
        return -1







tab = [
    [0, 0, 1, 1, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
]

print(szukaj_idola(tab))