# the one and only Dev.E.L'Peer  https://github.com/develpeer
##
# A bunch of examples explaining modules in python
##

print("<<< Only importing 'whoami'")
from foobonacci.sub_foob import whoami
whoami()
print(">>>import done, Entire chain of modules is initialized.")

print("<<< Only importing fib")
from foobonacci import fib1 as fib2,fib2 as fib1
print(">>>import done. Nothing gets re-initialized")
fib2(3)
print("We just flipped the names after import")
fib1(3)

import sys, site

print("Module names", sys.builtin_module_names)
# print("System path",sys.path)
# print("Prefixes:",site.PREFIXES)
# print("User site:",site.USER_SITE)

print("sys tiene",dir(sys))
print("global namespace",dir())