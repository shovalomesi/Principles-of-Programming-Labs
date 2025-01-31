# ------------------------------------------------
#                       Q1
# ------------------------------------------------
x=5
def func(y):
    print(y)
    print(x)
    x=x+1
#func(3)

# ------------------------------------------------
#                       Q2
# ------------------------------------------------
x=5
def func(y):
    print(y)
    x=10
    x=x+1
    print(x)
#func(3)

# ------------------------------------------------
#                       Q3
# ------------------------------------------------
x=5
def func(x):
    x+=1
    print(x)
#func(3)
    
# ------------------------------------------------
#                       Q4
# ------------------------------------------------
def g(u):
    def f(i):
            return u+i
    return f(10)
#g(20)

# ------------------------------------------------
#                       Q5
# ------------------------------------------------
def g(u):
    return f(u,10)
def f(i,j):
    return i+j
#g(20)

# ------------------------------------------------
#                       Q6
# ------------------------------------------------
x=3
def boring(x):
        def why(y):
            x=y
        why(5)
        return x
#boring(4)

# ------------------------------------------------
#                       Q7
# ------------------------------------------------
x=3
def interesting(x):
        def because(y):
            def fn(y):
                nonlocal x
                x=y
            fn(y+4)
        because(5)
        return x
print(interesting(4))
print(x)

# ------------------------------------------------
#                       Q8
# ------------------------------------------------
x=3
def boring(x):
    def why(y):
        global x
        x=y
    why(5)
    return x
#boring(4)
#x

# ------------------------------------------------
#                       Q9
# ------------------------------------------------
def outer():
    x=1
    def inner(z):
        x+=1
        print(x)
    return inner(3)
#outer()

# ------------------------------------------------
#                       Q10
# ------------------------------------------------
def factorial(x):
    if x==0:
        return 1
    return x*factorial(x-1)

# ------------------------------------------------
#                       Q11
# ------------------------------------------------
x=5
def f():
    y=10
    global x
    x+=y
    return y
#f()
#x
#a=f()
#a
# ------------------------------------------------
