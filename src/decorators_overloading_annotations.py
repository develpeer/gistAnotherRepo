# the one and only Dev.E.L'Peer  https://github.com/develpeer
##
# This gist explores decorators, type annotations and other advanced features
##

from ast import expr_context
from typing import Type

class GET_SET:
    
    def __init__(self) -> None:        
        self.__somewhat_immutable_private_key = "k1"
        self.public_var= "public_0"
        

    def __setattr__(self, name, value) -> None:        
        if name == 'kinda_immutable_key':
            raise AttributeError("This property is not settable")  
        ###
        # !!!! Set Attribiute must ALWAYS explictly assign bvalue in dict
        # or as i have done call super() (in this case object's __setattr__ )
        ###                   
        super().__setattr__(name,value)

    def __getattr__(self, name):
        if(name == 'kinda_immutable_key'):
            return 'k2'
        val = getattr(self.__dict__,name,"--NOT FOUnd --")  
        if val == "--NOT FOUnd --":
            raise AttributeError(f"Class GET_SET does not have attribute named '{name}'")
        return val    
                  

gs = GET_SET()
#private vars
try:
    print(gs.somewhat_immutable_private_key)
except AttributeError as e:
    print(f"Accessing gs.somewhat_immutable_private__key will throw an error '{e}'" )    

try:
    print(gs.__somewhat_immutable_private__key)
except AttributeError  as e:
    print(f"Accessing gs.__somewhat_immutable_private_key will throw an error '{e}'")    

print("But it is accessible: gs._GET_SET__somewhat_immutable_private_key=", gs._GET_SET__somewhat_immutable_private_key)
print("Public Vars are also accessible:", gs.public_var)

gs.public_var = 100
try:
    gs.kinda_immutable_key 
except AttributeError as e :
    print(f"Assignment to 'gs.kinda_immutable_key' should throw an error '{e}'")    

print("reading gs.kinda_immutable_key is fine:",gs.kinda_immutable_key)
