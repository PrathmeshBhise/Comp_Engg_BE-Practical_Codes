def fibonacci_iter(n):
    if n < 0:
        return -1, 1, []
    if n == 0:
        return 0, 1, [0]
    if n == 1:
        return 1, 1, [0, 1]
    
    steps = 0
    a = 0
    b = 1
    series = [a, b]
    
    for i in range(2, n + 1):
        c = a + b
        series.append(c)
        a = b
        b = c
        steps += 1
    
    return series[-1], steps + 1, series

def fibonacci_recur(n):
    if n < 0:
        return -1, 1, []
    if n == 0:
        return 0, 1, [0]
    if n == 1:
        return 1, 1, [0, 1]
    
    fib1, steps1, series1 = fibonacci_recur(n - 1)
    fib2, steps2, series2 = fibonacci_recur(n - 2)
    
    # Combine the two series and remove the duplicate last element
    series = series1 + [fib1] if fib1 != series1[-1] else series1
    series.append(fib1 + fib2)
    
    return fib1 + fib2, steps1 + steps2 + 1, series

# Sample direct function calls (replace n with any value you want to test):
n = int(input("Enter a number: "))

# Iterative approach
iter_result, iter_steps, iter_series = fibonacci_iter(n)
print("Iterative Fibonacci:", iter_result)
print("Steps:", iter_steps)
print("Series:", iter_series)

# Recursive approach
recur_result, recur_steps, recur_series = fibonacci_recur(n)
print("Recursive Fibonacci:", recur_result)
print("Steps:", recur_steps)
print("Series:", recur_series)
