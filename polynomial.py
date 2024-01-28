class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        def div_sub(p):
            return "( " + repr(p) + " )" if isinstance(p, (Add, Sub, Div)) else repr(p)

        repr_p1 = div_sub(self.p1)
        repr_p2 = div_sub(self.p2)
        return repr_p1 + " * " + repr_p2
    
    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        repr_p1 = repr(self.p1) if not isinstance(self.p1, Add) else "( " + repr(self.p1) + " )"
        repr_p2 = repr(self.p2) if not isinstance(self.p2, Add) else "( " + repr(self.p2) + " )"
        return repr_p1 + " / " + repr_p2

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        def wrapper(p):
            return "( " + repr(p) + " )" if isinstance(p, (Add, Sub)) else repr(p)

        repr_p1 = repr(self.p1)
        repr_p2 = wrapper(self.p2)
        return repr_p1 + " - " + repr_p2

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)