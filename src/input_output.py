
# using a while loop with readline
# and also using the != expression which assigns value of intermediate expressions to variables (e.g) 
with open("README.md") as f:
    while l := f.readline():
        print(repr(l))
