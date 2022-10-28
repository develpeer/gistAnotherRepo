# the one and only Dev.E.L'Peer  https://github.com/develpeer
##
# A bunch of examples explaining i/o in python
##
# using a while loop with readline
# and also using the != expression which assigns value of intermediate expressions to variables (e.g) 
f = None
try:
    f =  open("README.md")
except FileNotFoundError as e:
    print("Failed to find readme file..Trying an alternate location")
    try:
        f =  open("../../gistAnotherRepo/README.md")
    except FileNotFoundError as e:    
            print("File not found at all. Give up completely?")
finally:
    if f:
        while l := f.readline():
            print(repr(l))
    else:
        # Is this fatal?
        # if it is fatal, then you don't need the 2nd try/catch
        pass

    

