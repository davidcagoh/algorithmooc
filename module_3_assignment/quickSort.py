# input: a txt file containing 100,000 numbers to parse into unsorted array
# output: a sorted array AND the int number of comparisons used in the entire routine

import math
import sys


def main(A): 
    l = 1
    r = n
    count = 0
    return quickSort(A,l,r,count)


def quickSort(A, l, r, count):
    if len(A) == 1:
        return (A, 0)
    p = choosePivot(A,l,r)
    A = partition(A,l,r,p)
    left_A, left_count = quickSort(A[l:p])
    right_A, right_count = quickSort(A[p+1:r])

    return (left_A.append(right_A), left_count+right_count)

# assignment is to explore three pivoting rules 
# hence, I plan to create three different choosePivot subroutines that operate on A to get pivot position p, 
# then pass p to the partition subroutine which should work for any given pivot. 

def choosePivotFirst(A, l, r):
    return l

def choosePivotFinal(A, l, r):
    return r

def choosePivotMedianOfThree(A,l,r):
    if len(A) is odd
        k = (l + r) // 2
    else 
        k = (l + r - 1 ) // 2
    return median(A[l],A[k],A[r])

def partition(A, l, r, p):
    # swap p to the front
    c = A[l]
    p_value= A[p]
    A[l] = A[p]
    A[p] = c
    # linear scan
    i = l +1 
    for j in l+1:r
        if A[j] < p_value
            c = A[i]
            A[i] = A[j]
            A[j] = c
            i = i+1
    # swap p back to the appropriate spot
    c = A[l] # this is the p value
    A[l] = A[i-1]
    A[i-1] = c
    return A


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 quickSort.py <input_file>")
        sys.exit(1)
    filepath = sys.argv[1]
    with open(filepath, 'r') as f:
        arr = [int(line.strip()) for line in f if line.strip()]    
    _, count = main(arr)
    print(count)