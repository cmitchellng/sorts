from random import randint
from time import time

def random_list(size):
    num_list = []
    for i in range(0, size):
        random_number = randint(1, 1000)
        num_list.append(random_number)
    return num_list

def info(string, data):
    with open(r"C:\Users\cmitc\OneDrive\Documents\CS317\sorts.txt", 'a') as f:
        if string == "Size of List:":
            f.write('\n\n\n')
            f.write(string + " ")
            f.write(data)
            f.write('\n\n')
        else:
            f.write(string + "(Elapsed Time):\n")
            f.write(data)
            f.write(" seconds.\n")


def selection_sort(num_list):

    for i in range(len(num_list)):
        min = i

        for j in range(i+1, len(num_list)):
            if num_list[j] < num_list[min]:
                min = j;
        num_list[i], num_list[min] = num_list[min], num_list[i]

    return num_list

def insertion_sort(num_list):

    for i in range(1, len(num_list)):
        key = i
        value = num_list[i]

        while key > 0 and num_list[key - 1] > value:
            num_list[key] = num_list[key - 1]
            key = key - 1
        num_list[key] = value

    return num_list


def partition(num_list, start, end):
    i = (start - 1)
    pivot = num_list[end]

    for j in range(start, end):
        if num_list[j] <= pivot:
            i = i + 1
            num_list[i], num_list[j] = num_list[j], num_list[i]
    num_list[i + 1], num_list[end] = num_list[end], num_list[i + 1]

    return (i + 1)


def quick_sort(num_list, start, end):

    if len(num_list) == 1:

        return num_list

    if start < end:
        pi = partition(num_list, start, end)
        quick_sort(num_list, start, pi - 1)
        quick_sort(num_list, pi + 1, end)

        return num_list


def main():
    for list_size in range(5000, 30001, 5000):
        list = random_list(list_size)
        info("Size of List:", str(list_size))

        # Selection Sort
        start = time()
        selection_sort(list[:])
        total = time() - start
        selection_sort_time = str(total)
        info("Selection Sort", selection_sort_time)

        # Insertion Sort
        start = time()
        insertion_sort(list[:])
        total = time() - start
        insertion_sort_time = str(total)
        info("Insertion Sort", insertion_sort_time)

        # Quick Sort
        start = time()
        quick_sort(list[:], 0, list_size-1)
        total = time() - start
        quick_sort_time = str(total)
        info("Quick Sort", quick_sort_time)

main()