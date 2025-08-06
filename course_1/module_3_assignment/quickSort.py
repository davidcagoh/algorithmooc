# input: a txt file containing 100,000 numbers to parse into unsorted array
# output: a sorted array AND the int number of comparisons used in the entire routine

import math
import sys


def main(A): 
    l = 0
    r = len(A) - 1
    count = quickSort(A, l, r)
    return count


def quickSort(A, l, r):
    if l >= r:
        return 0
    p = choosePivotMedianOfThree(A, l, r) # you can modify this one
    A[l], A[p] = A[p], A[l]
    p = partition(A, l, r)
    left_count = quickSort(A, l, p - 1)
    right_count = quickSort(A, p + 1, r)
    return (r - l) + left_count + right_count

# assignment is to explore three pivoting rules 
# hence, I plan to create three different choosePivot subroutines that operate on A to get pivot position p, 
# then pass p to the partition subroutine which should work for any given pivot. 

def choosePivotFirst(A, l, r):
    return l

def choosePivotFinal(A, l, r):
    return r

def choosePivotMedianOfThree(A, l, r):
    k = (l + r) // 2
    trio = [(A[l], l), (A[k], k), (A[r], r)]
    trio.sort()
    return trio[1][1]

def partition(A, l, r):
    pivot = A[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[l], A[i - 1] = A[i - 1], A[l]
    return i - 1

# test
# arr = [3, 8, 2, 5, 1, 4, 7, 6]
# count = main(arr)
# print("Sorted array:", arr)
# print("Comparisons:", count)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 quickSort.py <input_file>")
        sys.exit(1)
    filepath = sys.argv[1]
    with open(filepath, 'r') as f:
        arr = [int(line.strip()) for line in f if line.strip()]    
    count = main(arr)
    print(count)