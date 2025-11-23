from typing import Literal, LiteralString

Color = Literal["black","white","yellow"] # you can create constant list here where enum like

def run_sql(query : LiteralString)-> None:
    pass

run_sql("Hello constans string")
s = "insert this into an other string"
reveal_type(s)
f = f"Hello {s} string"
reveal_type(f)
run_sql(f)
n = 42
fn = f"Hello {n} string"
reveal_type(fn)
run_sql(fn)


def fun(param : str):
    reveal_type(param)
    tmp : LiteralString = "Hello {param}"
    reveal_type(tmp)
    reveal_type(tmp.format(param=param))
    if param == "foo":
        reveal_type(param)
        reveal_type(tmp.format(param=param))
    
