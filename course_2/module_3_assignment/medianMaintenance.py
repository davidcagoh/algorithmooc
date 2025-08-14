# input: series of 10,000 numbers
# output: sum of successive medians m_1 to m_10000

# pseudocode

# parse input into an array of 10,000
# initialize k = 1 which counts where we're at
# initialize a max heap H_low and a min heap H_high
# add first input x_1 to H_low
# initialize Sum to x_1, which will be a dynamic sum of the medians

# for every successive x_k that comes in from 2 to 10,000
# increment k
# AddToHeaps(x_k, H_low, H_high)
# Rebalance (H_low, H_high)
# ComputeNewMedian (k, H_low, H_high)
# add new median to Sum

# done

# AddToHeaps subroutine
# if x_k is smaller than the max of H_low, add to H_low, otherwise add to H_high

# Rebalance
# check if H_low and H_high are equal or if H_low is larger than H_high by 1
# if not, pop from the larger heap and add to smaller heap

# ComputeNewMedian subroutine
# return max of H_low (should work for even or odd cases because of how we set up rebalance)

import heapq

def median_maintenance(filename):
    with open(filename) as f:
        nums = [int(line.strip()) for line in f]

    H_low = []   # max heap via negative numbers
    H_high = []  # min heap
    Sum = 0

    # first number
    heapq.heappush(H_low, -nums[0])
    Sum += nums[0]

    for x in nums[1:]:
        # AddToHeaps
        if x <= -H_low[0]:
            heapq.heappush(H_low, -x)
        else:
            heapq.heappush(H_high, x)

        # Rebalance
        if len(H_low) > len(H_high) + 1:
            heapq.heappush(H_high, -heapq.heappop(H_low))
        elif len(H_high) > len(H_low):
            heapq.heappush(H_low, -heapq.heappop(H_high))

        # ComputeNewMedian
        median = -H_low[0]
        Sum += median

    return Sum % 10000

if __name__ == "__main__":
    print(median_maintenance("input.txt"))