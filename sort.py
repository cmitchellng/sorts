from time import time
from functions import *
from algorithms import *

def main():
    for list_size in range(500, 3001, 500):
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