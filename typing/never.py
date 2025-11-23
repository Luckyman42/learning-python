from typing import Never

def infit_loop():
    while True:
        pass

def never_loop() -> Never:
    while True:
        pass

def not_return(x: object) ->Never:
    infit_loop()
    #here we know the command can't continure but the idea not know
    reveal_type(x)
    never_loop()
    reveal_type(x)
    # Now like return statement it will tell the ide 
    # That command can't retrun


def for_raise() -> Never:
    raise RuntimeError("After this command the next one can't continue")


def exit(status : int) -> Never:
    import sys
    sys.exit(status)
