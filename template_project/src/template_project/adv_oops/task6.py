class A:
    def greet(self):
        return "Hello from A"


class B(A):
    def greet(self):
        return "Hello from B"


class C(A):
    def greet(self):
        return "Hello from C"


class D(B, C):
    pass


class E(C, B):
    pass


d = D()
print(d.greet())

e = E()
print(e.greet())


print(D.mro())
print(E.mro())
