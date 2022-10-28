
class My_First_Class:
    """Should class names be camel case? 
    Who the fuck knows? And honestly how does it matter in a language 
    that actually uses white space for control flow. And  declarations 
    and semantics are implied by bullshit like __ and 3 quotes(which is idiotic) and stupid"""

    class_var = 100

    __private_var__ = 200

    def __init__(self, param):
        self.o_var_1 = 300
        self.o_var_2 = param

    def __repr__(self) -> str:
        return f"""
                classvar:{My_First_Class.class_var},
                o_var_1:{self.o_var_1},
                o_var_2:{self.o_var_2},                
                """
                
        pass

o = My_First_Class(-1)
print(o)

print(dir(o))
print(dir(My_First_Class))

del o.o_var_1

print(o.o_var_1)



    