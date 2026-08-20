def fibonacci(i):
    ...


# fib: 1, 1, 2, 3, 5, 8, 13...
# idx: 0, 1, 2, 3, 4, 5, 6...

assert fibonacci(0) == 1
assert fibonacci(6) == 13
assert fibonacci(1_000_000_000) == ?
# Time: O(n)    Mem: O(1)
