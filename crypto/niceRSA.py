from sympy import *
from Crypto.Util.number import getStrongPrime


def getPrime():
    p=getStrongPrime(512)
    q=nextprime(p)
    return p,q


f=open("flag.txt","r")
flag=f.readline()
f.close()
flag=int(flag.encode().hex(),16)

e=65537

p,q=getPrime()
n=p*q 
fi=(p-1)*(q-1)
d=pow(e,-1,fi)
ct=pow(flag,e,n)

print("n=", n)
print("e=",e)
print("ct=",ct)

