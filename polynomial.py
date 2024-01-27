class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    
    def evaluate(self, x):
        return x

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)
    
    def evaluate(self, x):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self, x):
        if isinstance(self.p2, Add):
            a = self.p1.evaluate(x)
            b = self.p2.p1.evaluate(x)
            c = self.p2.p2
            ret = Add(Int(a+b), c).evaluate(x)
        elif isinstance(self.p2, Sub):
            a = self.p1.evaluate(x)
            b = self.p2.p1.evaluate(x)
            c = self.p2.p2
            ret = Add(Int(a+b), c).evaluate(x)
        else:
            val1 = self.p1.evaluate(x)
            val2 =  self.p2.evaluate(x)
            ret = val1 + val2
        
        return ret
    
class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)
    
    def evaluate(self, x):
        if isinstance(self.p2, Add):
            a = self.p1.evaluate(x)
            b = self.p2.p1.evaluate(x)
            c = self.p2.p2
            ret = Add(Int(a-b), c).evaluate(x)
        elif isinstance(self.p2, Sub):
            a = self.p1.evaluate(x)
            b = self.p2.p1.evaluate(x)
            c = self.p2.p2
            ret = Sub(Int(a-b), c).evaluate(x)
        else:
            val1 = self.p1.evaluate(x)
            val2 =  self.p2.evaluate(x)
            ret = val1 - val2
        
        return ret

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub):
            if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
    def evaluate(self, x):
        if isinstance(self.p2, Mul):
            a = self.p1.evaluate(x)
            b = self.p2.p1.evaluate(x)
            c = self.p2.p2
            ret = Mul(Int(a*b), c).evaluate(x)
        elif isinstance(self.p2, Div):
            a = self.p1.evaluate(x)
            b = self.p2.p1.evaluate(x)
            c = self.p2.p2
            ret = Div(Int(a*b), c).evaluate(x)
        else:
            val1 = self.p1.evaluate(x)
            val2 =  self.p2.evaluate(x)
            ret = val1 * val2
        
        return ret

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub):
            if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)

    def evaluate(self, x):
        if self.p2.evaluate(x) == 0 :
            exit("cannot divide by 0")
        else:
            if isinstance(self.p2, Mul):
                a = self.p1.evaluate(x)
                b = self.p2.p1.evaluate(x)
                c = self.p2.p2
                ret = Mul(Int(a/b), c).evaluate(x)
            elif isinstance(self.p2, Div):
                a = self.p1.evaluate(x)
                b = self.p2.p1.evaluate(x)
                c = self.p2.p2
                ret = Div(Int(a/b), c).evaluate(x)
            else:
                val1 = self.p1.evaluate(x)
                val2 =  self.p2.evaluate(x)
                ret = val1 / val2
        return ret

poly = Add(Int(50), Add(Int(5), Add(Int(2), Int(1))))
print(poly)
print(poly.evaluate(-1))

poly = Add(Int(50), Mul(Int(5), Add(Int(2), Int(1))))
print(poly)
print(poly.evaluate(-1))

poly = Sub(Int(50), Sub(Int(5), Sub(Int(2), Int(1))))
print(poly)
print(poly.evaluate(-1))

poly = Sub(Int(50), Add(Int(5), Sub(Int(2), Int(1))))
print(poly)
print(poly.evaluate(-1))

poly = Mul(Int(50), Mul(Int(5), Mul(Int(2), Int(1))))
print(poly)
print(poly.evaluate(-1))

poly = Div(Int(50), Div(Int(5), Div(Int(2), Int(1))))
print(poly)
print(poly.evaluate(-1))

poly = Div(Int(50), Mul(Int(5), Div(Int(2), Int(1))))
print(poly)
print(poly.evaluate(-1))

poly =  Mul(Mul(Int(5), X()), Int(2))
print(poly)
print(poly.evaluate(-1))

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)
print(poly.evaluate(2))

poly = Sub( Sub( Int(4), Int(3)), Sub( X(), Mul( Int(1), Sub( Mul(X(), X()), Int(1)))))
print(poly)
print(poly.evaluate(2))

poly = Add( Add( Int(4), Int(3)), Add( X(), Div( Int(1), Add( Div(X(), X()), Int(1)))))
print(poly)
print(poly.evaluate(2))

poly = Sub( Add( Int(4), Int(3)), Sub( X(), Div( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)
print(poly.evaluate(2))

poly = Add( Sub( Int(4), Int(3)), Add( X(), Mul( Int(1), Sub( Div(X(), X()), Int(1)))))
print(poly)
print(poly.evaluate(2))

poly = Sub( Sub( Int(4), Int(3)), Sub( X(), Div( Int(1), Sub( Div(X(), X()), Int(1)))))
print(poly)
print(poly.evaluate(2))