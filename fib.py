n = int(input("Give number: "))

assert n>=0, "Wrong. Must be natural number!"

def factorial(x):
    
    factorial = 1
    
    for i in range (1,x+1):

        factorial = factorial*i

    return factorial

φ = 13/8

for i in range(100):

    φ = φ + ((-1)**(i+1)*factorial(2*i+1))/(4**(2*i+3)*factorial(i)*factorial(i+2))

print("golden ratio =",φ)

def fib(n):

    for i in range(n):

        Fn = (φ**n-(-φ)**(-n))/(2*φ-1)
        
    return(Fn)

print(fib(n))
