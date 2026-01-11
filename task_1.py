def caching_fibonacci():
    """Function for closure of fibonacci sequence"""
    cache = {}

    def fibonacci(n):
        """Calculates the n-th Fibonacci number using recursion and caching."""
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        #recurse counting and saving to cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

fib = caching_fibonacci()
print(fib(10))
print(fib(15))
