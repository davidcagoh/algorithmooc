def parse_array(filename):
    with open(filename) as f:
        return [int(line.strip()) for line in f]

def check_sums(integers):
    arr = sorted(set(integers))   # dedup helps
    lo, hi = 0, len(arr) - 1
    valid = set()
    
    while lo < hi:
        s = arr[lo] + arr[hi]
        if s < -10000:
            lo += 1
        elif s > 10000:
            hi -= 1
        else:
            # record all sums involving arr[lo] with hi moving inward
            k = hi
            while lo < k and arr[lo] + arr[k] >= -10000:
                if arr[lo] + arr[k] <= 10000:
                    valid.add(arr[lo] + arr[k])
                k -= 1
            lo += 1
    return len(valid)

if __name__ == "__main__":
    print(check_sums(parse_array("input.txt")))