#!/usr/bin/python

#####################
# Liczebniki Churcha
#					
# Mateusz Danieluk	
#					
#####################

# Liczba naturalna Churcha to funkcja wyzszego rzedu pobierajaca dwa argumenty - funkcje f i argument x, ktora n-krotnie aplikuje f do x.
# Przykladowo:
#
# 0 to x
# 1 to f(x)
# 2 to f(f(x))
# 3 to f(f(f(x)))
# 4 to f(f(f(f(x))))

zero=lambda f: lambda x: x
one=lambda f: lambda x: f(x)
two=lambda f: lambda x: f(f(x))
three=lambda f: lambda x: f(f(f(x)))
four=lambda f: lambda x: f(f(f(f(x))))

# Operacje arytmetyczne moga byc reprezentowane przez funkcje na liczbach Churcha

# funkcja succ zwieksza o 1 podana liczbe Churcha 'n'
def succ(n):
	return lambda f: lambda x: f(n(f)(x))

# funkcja add dodaje dwie liczby liczby Churcha
def add(n,m):
	return lambda f: lambda x : n(f)(m(f)(x))

# funkcja mult mnozy dwie liczby Churcha
def mult(n,m):
	return lambda f: lambda x: n(m(f))(x)

# funkcja exp liczby eksponente dwwch liczb Churcha 
def exp(n,m):
	return n(m)

# funkcja printRun wypisuje argument i wykonuje kod
def printRun(x):
	print x, ' = ', eval(x)

# funkcja church2int konwertuje liczbe Churcha na int
def church2int(n):
	return n(lambda x:x+1)(0)

# testowanie
printRun('church2int(zero)')
printRun('church2int(succ(zero))')
printRun('church2int(add(two, three))')
printRun('church2int(mult(four, four))')
printRun('church2int(exp(two,four))')

































