
class MY_FIRST_CLASS:
    """Should class names be camel case? 
    Who the fuck knows? And honestly how does it matter in a language 
    that actually uses white space for control flow. And  declarations 
    and semantics are implied by bullshit like __ and 3 quotes(which is idiotic) and stupid"""

    class_var = 100
    class_var_2 = class_var+100

    __private_var__ = 200

    def __init__(self, param):
        self.o_var_1 = 300
        self.o_var_2 = param

    def __repr__(self) -> str:
        # this here is a great example of the bulshitteryu that is python control flow 
        # If you want to remove leading spaces, you have to stick the lines to the left, which breaks 
        # the visual control flow bullshit that python developers love so much 
        return f"""
                classvar:{MY_FIRST_CLASS.class_var},
                classvar_2:{MY_FIRST_CLASS.class_var_2},
                o_var_1:{getattr(self,"o_var_1","UNDEFINED")},
                o_var_2:{self.o_var_2},                
                """
                
        pass

    def f1(*args):
        for arg in args:
            print("I got me some args y'all, because python " 
            "uses an implicit invocation context to differentiate betwwen instance and class methods"
            "\n That is if this method is an object method, you must declare its firt arg as 'self', which fuck that ..i'm going to"
            "just call python_sucks..see next method"
            "\n Stupid stupid python", f"arg = {arg}")
        return "you get what you so.. do not deserve "

    def f2(python_sucks):
        return python_sucks.o_var_2 *100
        

o = MY_FIRST_CLASS(3.14)
print(o)

print("-"*40,"\n","All the attribites of o:\n","\n * ".join(dir(o)))
print("-"*40,"\n","All the attribites of MyFirstClass:\n","\n * ".join(dir(MY_FIRST_CLASS)))

del o.o_var_1
try:
    print(o.o_var_1)
except AttributeError as ae:
    print(ae,("\n!!!!You can delete attributes of an object from outside the object.. WTF!!\n"
            "So much for encapsulation"))    

print(f"MY_FIRST_CLASS.f1 {MY_FIRST_CLASS.f1}")
print(f"MY_FIRST_CLASS.f1() {MY_FIRST_CLASS.f1()}")
print(f"o.f1 {o.f1}")
print(f"o.f1 {o.f1()}")
print(f"o.f2 {o.f2}")
print(f"o.f2 returned {o.f2()}")

