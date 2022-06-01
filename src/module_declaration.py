print("<<< Only importing fib")
from foobonaci import fib1 as fib2,fib2 as fib1

print(">>>import done")
fib2(3)
print("We just flipped the names after import")
fib1(3)

