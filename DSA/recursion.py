
def func(i,n):
    if i>n:
        return
    func(i+1,n)
    print(i)
   

func(2,10)


def func(n):
    if n==0:
        return
    func(n-1)
    print(n)
    
    
func(10)


def func(sum,i,n):
    if i>n:
        return i
    func(sum+i,i+1,n)
func(0,1,10)

factorial 

def func(n):
    if n==1 or n==0:
        return 1
    return n*func(n-1)
print(func(7))


