import math 

def karatsuba(x: int, y: int) -> int:
    x_str = str(x)
    y_str = str(y)
    #base case
    if len(x_str) == 1 or len(y_str) ==1 :
        return x*y
    #find length and split strings
    # Pad numbers with leading zeros so both are the same length
    max_len = max(len(x_str), len(y_str))
    x_str = x_str.zfill(max_len)
    y_str = y_str.zfill(max_len)

    m = max_len // 2  # exact midpoint

    # Split into high (left) and low (right) parts
    a = int(x_str[:max_len - m])
    b = int(x_str[max_len - m:])
    c = int(y_str[:max_len - m])
    d = int(y_str[max_len - m:])

    #perform recursive calls
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ab_cd = karatsuba(a + b, c + d)

    ad_bc = ab_cd - ac - bd

    return 10 ** (2*m)*ac + 10**(m)*ad_bc + bd

print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))
