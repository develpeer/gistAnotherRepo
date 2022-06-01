import random
# Foobonacci numbers module
print(f"{'++'*20}\nStuff outside declaration of FIB \n{'++'*20}")
def fib1(n):    # write Fibonacci series up to n
    a=0
    while a < n:
        print("fib1",random.randint(1,100))
        a+=1
    print()


print(f"{'++'*20}\nStuff outside declaration for FIB2\n{'++'*20}")

def fib2(n):    # write Fibonacci series up to n
    a=0
    while a < n:
        print("fib2",random.randint(1,100))
        a+=1
    print()

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))