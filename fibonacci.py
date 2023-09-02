from functools import reduce
from math import gcd
import time

def fibonacci_number_naive(n):
    if n <= 1:
        return n
    return fibonacci_number_naive(n-1) + fibonacci_number_naive(n-2)

def fibonacci_number(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


def fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    return (fibonacci_last_digit_naive(n-1) + fibonacci_last_digit_naive(n-2)) % 10

def fibonacci_last_digit(n):
    fib = [0, 1]
    last_digit_list = [0, 1]
    for i in range(2, 60):
        fib.append(fib[i - 1] + fib[i - 2])
        last_digit_list.append(fib[i] % 10)
    return last_digit_list[n % 60]


def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1

def calc_fib(n, m):
    p = pisano_period(m)
    n = n % p
    if n <= 1:
        return n
    previous, current = 0, 1
    for i in range(2, n + 1):
        previous, current = current, (previous + current) % m
    return current


def last_digit(n):
    a, b = 0, 1
    for _ in range((n + 2) % 60):
        a, b = b, (a + b) % 10
    return a if a != 0 else 9

def pisano_num_mod10(n):
    fib = [0, 1]
    for _ in range(2, 60):
        fib.append((fib[-1] + fib[-2]) % 10)
    return fib[n % 60]


if __name__ == '__main__':
    n = int(input("Enter the value of n: "))
    m = int(input("Enter the value of m: "))

    print(f"The last digit of the {n}th Fibonacci number is: {fibonacci_last_digit(n)}")
    print(f"The {n}th Fibonacci number is: {fibonacci_number(n)}")
    print(f"The {n}th Fibonacci number modulo {m} is: {calc_fib(n, m)}")
    print(f"The last digit of the {n}th Fibonacci number is: {last_digit(n)}")


    # n = 35
    # start_time = time.time()
    # fibonacci_number(n)
    # end_time = time.time()
    # original_time = end_time - start_time

    # start_time = time.time()
    # fibonacci_number_naive(n)
    # end_time = time.time()
    # naive_time = end_time - start_time

    # start_time = time.time()
    # fibonacci_last_digit(n)
    # end_time = time.time()
    # original_last_digit_time = end_time - start_time

    # start_time = time.time()
    # fibonacci_last_digit_naive(n)
    # end_time = time.time()
    # naive_last_digit_time = end_time - start_time

    # print("Performance Comparison:")
    # print(f"Original Algorithm (fibonacci_number): {original_time} seconds")
    # print(f"Naive Algorithm (fibonacci_number_naive): {naive_time} seconds")
    # print()
    # print(f"Original Algorithm (fibonacci_last_digit): {original_last_digit_time} seconds")
    # print(f"Naive Algorithm (fibonacci_last_digit_naive): {naive_last_digit_time} seconds")

