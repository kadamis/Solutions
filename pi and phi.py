import random

pi = 0

for i in range(100):

	pi = pi + (1/16**i)*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))

print("pi =",pi)

r = random.randint(0,255)

print("L =",2*pi*r,"m")
print("E =",pi*r**2,"m2")
print("V =",4*pi*r**3/3,"m3")

n = int(input("Give number: "))

assert n>=0, "Wrong. Must be natural number!"

def factorial(n):
    
    factorial = 1
    
    for i in range (1,n+1):

        factorial = factorial*i

    return factorial

res = factorial(n)
print("Factorial of number:",res)

φ = 13/8

for i in range(100):

    φ = φ + ((-1)**(i+1)*factorial(2*i+1))/(4**(2*i+3)*factorial(i)*factorial(i+2))

print("golden ratio =",φ)
