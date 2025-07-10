def print_sum(n):
    if(n==0):
        return 0
    return print_sum(n-1)+n

result=print_sum(10)
print(result)