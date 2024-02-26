def szukaj_lidera(arr):
    n = len(arr)  # zwraca dlugosc listy
    for i in range(n):
        ile = 0  # licznik
        for j in range(n):
            if arr[j] == arr[i]:  # czy kolejny element jest taki sam
                ile += 1
        if ile > n // 2:  # czy kandydat na lidera ma wiecej niż polowa elementow w liście
            return arr[i], -1

    return "nie ma lidera"


lista = [1,2,3,3,3,3,3,3]  # Przykladowa lista - 3 jest liderem

print(szukaj_lidera(lista))  # wykonanie funkcji szukaj_lidera
