        # compound assignment
        s += x # s = s + x
        s -= x # s = s - x
        s *= x # s = s * x
        s /= x # s = s / x

def fibonacci(n): # 0, 1, 1, 2, 3, 5, 8, 13, ..
    a, b = 0, 1 # a = 0; b = 1
    for _ in range(n):
        print(a)
        next = a + b
        a = b
        b = next
        # kürzer: a, b = b, a + b