def selection_sort(num_list: int) -> float:
    """Algorithm for selection sort"""
    for i in range(len(num_list)):
        min = i

        for j in range(i+1, len(num_list)):
            if num_list[j] < num_list[min]:
                min = j;
        num_list[i], num_list[min] = num_list[min], num_list[i]

    return num_list

def insertion_sort(num_list: int) -> float:
    """Algorithm for insertion sort"""
    for i in range(1, len(num_list)):
        key = i
        value = num_list[i]

        while key > 0 and num_list[key - 1] > value:
            num_list[key] = num_list[key - 1]
            key = key - 1
        num_list[key] = value

    return num_list


def partition(num_list: int, start: int, end: int) -> float:
    """Partition function used in quick sort"""
    i = (start - 1)
    pivot = num_list[end]

    for j in range(start, end):
        if num_list[j] <= pivot:
            i = i + 1
            num_list[i], num_list[j] = num_list[j], num_list[i]
    num_list[i + 1], num_list[end] = num_list[end], num_list[i + 1]

    return (i + 1)


def quick_sort(num_list: int, start: int, end: int) -> float:
    """Algorithm for quick sort"""
    if len(num_list) == 1:

        return num_list

    if start < end:
        pi = partition(num_list, start, end)
        quick_sort(num_list, start, pi - 1)
        quick_sort(num_list, pi + 1, end)

        return num_list