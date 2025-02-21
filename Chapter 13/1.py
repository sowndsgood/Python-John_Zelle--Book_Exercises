#  Recursive Fibonacci program

def fib(n):
    print(f"Computing fib({n})")
    print("...")
    if n<3:
        ans=1
        print(f"Leaving fib({n}) returning {ans}")
        return ans
    else:
        ans=fib(n-1)+fib(n-2)
        print(f"Leaving fib({n}) returning {ans}")
        return ans

print(fib(4))