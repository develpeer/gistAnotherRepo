##
# List prepend test
##
list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Before prepend list_1 : {list_1}")
list_1[:0] = [666]
print(f"After prepend list_1 : {list_1}")
list_1 = [665] + list_1
print(f"After prepend list_1 : {list_1}")
list_1[:] = 664, *list_1
print(f"After prepend list_1 : {list_1}")
list_1.insert(0, 663)
print(f"After prepend list_1 : {list_1}")
list_1.insert(2, 664.5)
print(f"After insert list_1 : {list_1}")
list_1[4:4] = 655.5,
print(f"After insert list_1 : {list_1}")

print("-=-" * 25)
# Square all digits using a generator
print([x ** 2 for x in range(10)])
# Square all even digits
print([(x,x ** 2) for x in range(10) if not x % 2])
# this expression is a generator
gee = (x*2 for x in range(10) )
print(next(gee))  # first element
print(next(gee))  # second element
print(*gee)  # remaining elements
