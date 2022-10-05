# the one and only Dev.E.L'Peer  https://github.com/develpeer
##
# A bunch of examples explaining dictionaries and related 
# concepts like  in python
##

import math

#list equality?
t = ("hello", None)
u = ("hello",)
v = ("hello",)
print(f"t = {t}, t==v :{t == v}, u==v :{u == v}")

#sets
a = set('tyler')
b = set('nol')
print("Set Diff:", a - b)
print("Set Union:", a | b)
print("Set intersection:", a & b)
print("Set XOR", (a | b) - (a & b))
print("Set XOR", a ^ b)

# zip joins two lists sequentially
q = ['name', 'quest', 'favorite color']
a = ['lancelot', 'the holy grail', 'blue']
for k, v in zip(q, a):
    print(k, v)
print(dict(zip(q, a)))

# filtering a list using agenrator
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = [(k + 1) for k in raw_data if not math.isnan(k)]
print("Filtered data is ", filtered_data)

# are sets usable as dicts?
s = {"a", "b"}
print(s, type(s))
try:
    print(s.keys(), s.items())
except:
    print("calling .keys() or .items() will fail")
    try:
        s["a"] = 0
    except:
        print("assigning values to a set will also fail")

print(s, type(s))

try:
    print (None < "b")
except TypeError:
    print ("Comparing objects of different types with < or > is legal provided that the objects have appropriate comparison methods")


########################################################
# Understanding maps and lambda functions
# lambda functions are just shortcut functions. 
# Maps take two arguments a function, and a list, and 
# then map the function to members of the list (or maybe even a tuple?) 
# ....
# list () = []
########################################################
def doubler(i):
    return i*2

doubler_using_lambda = lambda j:j*2


