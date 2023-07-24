class Rectangle:
    a = 0
    b = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __str__(self):
        s = ""
        for k,v in {{gap}}:
            s += f"{k}: {v}\n"
        return s

rc = Rectangle(3, 7)
print(rc)

# exp output
# a: 3
# b: 7
