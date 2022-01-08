from numpy import arange

def uniform_search_method(f, a, b, n=10, extremum=min):
    return extremum( [f(x) for x in arange(a, b, (b-a)/n)] )

def golden_section_method(f, a, b, e, extremum=min):
    F = (5**0.5 + 1) / 2
    while abs(b-a) > e:
        x1 = b - (b-a) / F
        x2 = a + (b-a) / F
        y1, y2 = f(x1), f(x2)
        if extremum==min:
            if y1 >= y2:
                a = x1
            else:
                b = x2
        else:
            if y1 <= y2:
                a = x1
            else:
                b = x2
    x = (a + b) / 2               
    return x, f(x)                  

def dichotomy_method(f, a, b, e):
    while abs(b-a) > e:
        x = (a+b)/2
        if f(x) < 0:
            b = x
        else:
            a = x
    x = (b+a)/2 
    return x, f(x)             

func = lambda x: x**2 + 2*x + 2

print(uniform_search_method(func, 10, 100, n=100, extremum=max))
print(golden_section_method(func, 10, 100, e=0.05, extremum=max))
print(dichotomy_method(func, 10, 100, e=0.05))