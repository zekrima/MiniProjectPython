from tkinter import Tk, StringVar, Entry, Button

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("400x500")
        master.config(bg="gray")

        self.equation = StringVar()
        self.entry_value = ""
        Entry(master, width=17, bg="#fff", font=("Arial Bold", 28),textvariable=self.equation).place(x=10, y=10)


        Button(width=10, height=3, text="(", relief="flat", bg="white", command=lambda: self.show('(')).place(x=10, y=70)
        Button(width=10, height=3, text=")", relief="flat", bg="white", command=lambda: self.show(')')).place(x=110, y=70)
        Button(width=10, height=3, text="%", relief="flat", bg="white", command=lambda: self.show('%')).place(x=210, y=70)
        Button(width=10, height=3, text="C", relief="flat", bg="white", command=self.clear).place(x=310, y=70)

        Button(width=10, height=3, text="7", relief="flat", bg="white", command=lambda: self.show(7)).place(x=10, y=140)
        Button(width=10, height=3, text="8", relief="flat", bg="white", command=lambda: self.show(8)).place(x=110, y=140)
        Button(width=10, height=3, text="9", relief="flat", bg="white", command=lambda: self.show(9)).place(x=210, y=140)
        Button(width=10, height=3, text="/", relief="flat", bg="white", command=lambda: self.show("/")).place(x=310, y=140)

        Button(width=10, height=3, text="4", relief="flat", bg="white", command=lambda: self.show(4)).place(x=10, y=210)
        Button(width=10, height=3, text="5", relief="flat", bg="white", command=lambda: self.show(5)).place(x=110, y=210)
        Button(width=10, height=3, text="6", relief="flat", bg="white", command=lambda: self.show(6)).place(x=210, y=210)
        Button(width=10, height=3, text="x", relief="flat", bg="white", command=lambda: self.show('X')).place(x=310, y=210)

        Button(width=10, height=3, text="1", relief="flat", bg="white", command=lambda: self.show(1)).place(x=10, y=280)
        Button(width=10, height=3, text="2", relief="flat", bg="white", command=lambda: self.show(2)).place(x=110, y=280)
        Button(width=10, height=3, text="3", relief="flat", bg="white", command=lambda: self.show(3)).place(x=210, y=280)
        Button(width=10, height=3, text="-", relief="flat", bg="white", command=lambda: self.show('-')).place(x=310, y=280)

        Button(width=10, height=3, text="0", relief="flat", bg="white", command=lambda: self.show(0)).place(x=10, y=350)
        Button(width=10, height=3, text=",", relief="flat", bg="white", command=lambda: self.show(',')).place(x=110, y=350)
        Button(width=10, height=3, text="=", relief="flat", bg="white", command=self.solve).place(x=210, y=350)
        Button(width=10, height=3, text="+", relief="flat", bg="white", command=lambda:self.show('+')).place(x=310, y=350)

        Button(master, width=10, height=3, text="<-", relief="flat", bg="white", command=self.backspace).place(x=10, y=420)
        

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def backspace(self):
        self.entry_value = self.entry_value[:-1]
        self.equation.set(self.entry_value)


    def solve(self):
        try:
            result = eval_expr(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            self.equation.set("error")

def eval_expr(expr):
    import ast
    import operator as op

    operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv}

    def _eval(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return operators[type(node.op)](_eval(node.left), _eval(node.right))
        else:
            raise TypeError(node)

    return _eval(ast.parse(expr, mode='eval').body)

root = Tk()
Calculator(root)
root.mainloop()
