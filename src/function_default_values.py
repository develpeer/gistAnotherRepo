def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, x):
    print(x)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(f"pos_only:{pos_only}, standard:{standard}, kwd_only:{kwd_only}")


try:
    pos_only_arg(x=7)
except Exception as e:
    print(f"This should not work, since anything preceeding / is a positional argument[{e}]")

try:
    kwd_only_arg(7, x=7)
except Exception as e:
    print(f"This should not work, since anything following * is a kwarg [{e}]")

# either of these work
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)

try:
    combined_example(pos_only=1, standard=2, kwd_only=3)
except Exception as e:
    print(f"This should not work: [{e}]")


def name_collision(name, **kwds):
    print(f"Value of name is '{name}'")


name_collision("Dev")
name_collision(name="Loper")
try:
    name_collision("Dev", name="Loper")
except Exception as e:
    print(f"If the name occurs in both pos and kwarg, that will trow an error:")
