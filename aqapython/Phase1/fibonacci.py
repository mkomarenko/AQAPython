def fib(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    n1 = 0
    n2 = 1
    count = 0

    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        result.append(n1);
    else:
        while count < n:
         result.append(n1)
         nth = n1 + n2
         n1 = n2
         n2 = nth
         count += 1

    return result


print(fib(10))