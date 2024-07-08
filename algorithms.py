def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            yield data

def selection_sort(data):
    n = len(data)
    for i in range(n):
        smallest = 1001
        ind = i
        for j in range(i,n):
            if data[j] < smallest:
                smallest = data[j]
                ind = j
            yield data
        data[i], data[ind] = data[ind], data[i]

def insertion_sort(data):
    n = len(data)
    for i in range(1,n):
        curr = data[i]
        j = i-1
        while j>=0 and curr < data[j]:
            data[j+1] = data[j]
            j -= 1
            yield data
        data[j+1] = curr


def merge_sort(data, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from merge_sort(data, start, mid)
    yield from merge_sort(data, mid + 1, end)
    yield from merge(data, start, mid, end)
    yield data

def merge(data, start, mid, end):
    merged = []
    left = start
    right = mid + 1

    while left <= mid and right <= end:
        if data[left] < data[right]:
            merged.append(data[left])
            left += 1
        else:
            merged.append(data[right])
            right += 1

    while left <= mid:
        merged.append(data[left])
        left += 1

    while right <= end:
        merged.append(data[right])
        right += 1

    for i, sorted_val in enumerate(merged):
        data[start + i] = sorted_val
        yield data


def quick_sort(data, start, end):
    if start >= end:
        return

    pivot = data[end]
    i = start

    for j in range(start, end):
        if data[j] < pivot:
            data[j], data[i] = data[i], data[j]
            i += 1
        yield data
    data[end], data[i] = data[i], data[end]
    yield data

    yield from quick_sort(data, start, i - 1)
    yield from quick_sort(data, i + 1, end)
        
                