# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# print(fibonacci(9))    



def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_prev = 0
        fib_curr = 1
        for i in range(2, n+1):
            fib_next = fib_prev + fib_curr
            fib_prev = fib_curr
            fib_curr = fib_next
        return fib_curr
    
print(fibonacci(9))    
