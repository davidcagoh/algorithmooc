# goal: compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array.
# input: some txt file containing n integers (the final one is 100,000)
# output: an int
# test case: make a txt file with 1,3,5,2,4,6

import math 

def countInv(x):
    if len(x) <= 1:
        return x, 0
    mid = len(x) // 2
    left, inv_left = countInv(x[:mid])
    right, inv_right = countInv(x[mid:])
    merged, inv_split = merge_and_count(left, right)
    return merged, inv_left + inv_right + inv_split


# input for this one is two sorted arrays C and D
# output is the merged sorted array B and a number  

def merge_and_count(C, D):
    B = []
    i = j = splitInv = 0
    while i < len(C) and j < len(D):
        if C[i] <= D[j]:
            B.append(C[i])
            i += 1
        else:
            B.append(D[j])
            splitInv += len(C) - i
            j += 1
    B.extend(C[i:])
    B.extend(D[j:])
    return B, splitInv

if __name__ == "__main__":
    test_array = [1, 3, 5, 2, 4, 6]
    _, inv_count = countInv(test_array)
    print(f"Inversion count: {inv_count}")