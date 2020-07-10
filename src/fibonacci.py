"""
https://en.wikipedia.org/wiki/Fibonacci_number

fib(n + 1) = fib(n) + fib(n - 1) ; n > 0
fib(n) = fib(n - 1) + fib(n - 2)
fib(0) = 0
fib(1) = 1
"""
from typing import Dict


def recursive(n: int) -> int:
    """ 
    Recursive fibonacci. This is a naive approach
    since it would make computations on every 
    function call. It's not efficient and
    obtaining fib(50) could hang up the computer.

    # Base Cases
    if n == 0:
        return 0

    if n == 1:
        return 1

    """
    if n < 2:
        return n

    return recursive(n - 1) + recursive(n - 2)


memo: Dict[int, int] = {0: 0, 1: 1}  # Include base cases


def memoization(n: int) -> int:
    """
    This approach uses Memoization Dynamic Programming Technique
    You can also memoize a function using
    Python's lru_cache
    from functools import lru_cache
    @lru_cache(maxsize=None)

    See Donald Michie: https://en.wikipedia.org/wiki/Memoization

    The problem with this approach is that you can reach
    maximum recursion stack error.
    """
    if n not in memo:
        # This is the recursive approach
        # But with memoization
        memo[n] = memoization(n - 1) + memoization(n - 2)

    return memo[n]


def iterative(n: int) -> int:
    """
    This approach uses Bottom Up Dynamic Programming Technique
    The last two values are the only needed to compute the next
    value. So we just need to save those in order to build
    the Fibonacci sequence.

    This approach requires less memory than memoization.
    """
    last: int = 1
    next: int = 0

    for _ in range(n):
        last = last + next
        next = last - next

    return next
