def bubble_sort_ascending(data: list) -> list:
    n = len(data)

    for i in range (n):
        swapped = False
        for j in range (0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True

        if not swapped:
            break

    return data

def bubble_sort_descending(data: list) -> list:
    n = len(data)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if data[j] < data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True

        if not swapped:
            break

    return data