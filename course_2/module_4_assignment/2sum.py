# input: file representing array of 1 million integers, positive negative may be repeat
# Your task is to compute the number of target values t in the interval [-10000,10000] such that there are distinct x,y
# such that x + y = t. ensure distinctness

# idea: use a hash table

# main 
# initialize count = 0
# for every integer, lookup in hash table, if not in hash table, insert into hash table
# for every value t in [-10000, 10000], 
# then go through every value x in the array and lookup t - x. if yes, +1 to count and move on to next t in the range
# return count


def parse_array(filename):
    with open(filename) as f:
        integers = [int(line.strip()) for line in f]
    return integers

def check_sums(integers):
    values = set(integers)
    count = 0
    for t in range(-10000, 10001):
        for x in values:
            y = t - x
            if y in values and y != x:
                count += 1
                break
    return count

if __name__ == "__main__":
    print(check_sums(parse_array("input.txt")))


