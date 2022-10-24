from xxlimited import foo
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

##
# Private module variables are visible, underscore or not
##
print("==>",foobonacci.__test_param)

##
# Module symbols/attributes are modifiable outside the module. (stupid stupid python. math.get_screen_size() anyone?)
##
try:
    from foobonacci import x  
except Exception as e:
    print("Import error",e)

foobonacci.x  = 90
from foobonacci import x
print("You can introduce attributes into modules. x was not declared within the module foobonacci",x)
del foobonacci.x
try:
    from foobonacci import x  
except Exception as e:
    print(f"Attribute x has now been deleted: Importing will throw error '{e}'")

