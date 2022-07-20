import foobonacci
from foobonacci import *

# importing stuff in foobonacci properly
whoami()
fib2(10)
try:
    sub_foob.whoami()
except:
    print("Sub Foob will not be imported")

try:
    foobonacci.sub_foob.whoami()
except:
    print("sub_foob cannot be accessed by reference")

print("sub_foob has to be explicitly imported..and will be initialized ")
import foobonacci.sub_foob
foobonacci.sub_foob.whoami()

print("sub_foob can be imported again..but will not be re-initialized ")
import foobonacci.sub_foob as xyz
xyz.whoami()


print("==>",foobonacci.__test_param)






