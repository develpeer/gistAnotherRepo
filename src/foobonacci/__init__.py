print(f"{'++'*20}\n Initializing foobonacci \n{'++'*20}")

import random
__test_param = "private value"

# Foobonacci numbers module
print("Declaring fib1")
def fib1(n):    # write Fibonacci series up to n
    a=0
    while a < n:
        print("fib1",random.randint(1,100))
        a+=1
    print()


print("Declaring fib2")
# write Fibonacci series up to n
def fib2(n):
    a=0
    while a < n:
        print("fib2",random.randint(1,100))
        a+=1
    print()

def whoami():
    print("I am: ",__name__)

import sys
if __name__ == "__main__":
    fib1(int(sys.argv[1]))
