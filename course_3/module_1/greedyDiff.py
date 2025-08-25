# input: some big file of jobs with top row being number of jobs and each subsequent row being weight then length
# output: sum of weighted completion times of the resulting schedule when sorted in decreasing order of difference weight minus length

## main algorithm
# parse file so you make two arrays of size number of jobs called weights and lengths and populate them as you go through the file
# make a new array of the same size called score where each entry is weights minus lengths 
# sort the score array by quicksort # should i have used a dictionary or a hash table because i am trying to track the order??
# do the weighted completion times thing: 
    # go through the lengths array and basically using the order of jobs, turn the entries of lengths into the completion times (have a value called Time Passed or something which increments as you go through the array in the job order)
    # get the sum of the product of updated lengths array (which is completion times) and the weights array
# return

def schedule_jobs(filename, key_func):
    with open(filename) as f:
        n = int(f.readline())
        jobs = []
        for line in f:
            w, l = map(int, line.split())
            jobs.append((w, l))
    jobs.sort(key=lambda x: key_func(*x), reverse=True)
    time, total = 0, 0
    for w, l in jobs:
        time += l
        total += w * time
    return total


def diff_key(w, l):
    return (w - l, w) # this is the tiebreaking part


def ratio_key(w, l):
    return (w / l, w) # this is the tiebreaking part

import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python greedyDiff.py [diff|ratio]")
        sys.exit(1)

    mode = sys.argv[1].lower()
    if mode == "diff":
        result = schedule_jobs("jobs.txt", diff_key)
        print("Difference-based:", result)
    elif mode == "ratio":
        result = schedule_jobs("jobs.txt", ratio_key)
        print("Ratio-based:", result)
    else:
        print("Invalid mode. Use 'diff' or 'ratio'.")

