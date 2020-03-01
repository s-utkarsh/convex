#! /usr/bin/python                                                                                                                                              
from __future__ import division
import math
import sys
import os.path
import numpy as np

# will take user input for whether a binary or ternary hull is needed
def take_basic_input():
    while True:
        try:
            print('1. Binary\n')
            print('2. Ternary\n')
            isbinary = input("Out of these options\(1,2), which one do you want?\n")
            isbinary = int(isbinary)
        except ValueError:
            print("I need a valid positive integer input!\n")
            continue
        else:
            break
    if isbinary == 1:
        print("A binary phase diagram. Routine not implemented yet. Sorry \n")
        exit()
    else:
        print("Wonderful! 3-D convex hull. I'll do my best for you \n")
    e1 = str(raw_input("Enter the first parent element:\n"))
    e2 = str(raw_input("Enter the second parent element:\n"))
    if isbinary == 1:
        e3 = None
        print("Thanks for the info! I would like some more information\n")
    else:
        e3 = str(raw_input("Enter the third parent element:\n"))
        print("Thanks for the info!\n")
    return e1,e2,e3

def ternary_dec_input(e1=None,e2=None,e3=None):
    print("Please enter all possible decompositions now ==>\n Enter numeric zero for when there are no parts of one of the elements")
    exit = 'y'
    A,B,C,D,E,ID=[],[],[],[],[],[]
    while (exit != 'n' or exit != 'N'):
        if(exit == 'y' or exit == 'Y'):
            a = float(input('Please enter parts of '+str(e1)+':\n'))
            A.append(a)
            b = float(input('Please enter parts of '+str(e2)+':\n'))
            B.append(b)
            c = float(input('Please enter parts of '+str(e3)+':\n'))
            C.append(c)
            identity=str(e1+str(a)+e2+str(b)+e3+str(c))
            ID.append(identity)
            e = float(input('Please enter formation enthalpy of ' + identity +':'))
            E.append(e)
        else:
            print("Thanks! You'll find your input and output in corresponding .in and .out files \n A 2-d contour plot of the hull will be generated now.")
            break
        exit = str(raw_input("\nMore decompositons to enter?(y/n)\n"))
    return A, B, C, ID, E

def bary2cart(A=None,B=None,C=None,ID=None,E=None):
    X,Y,Z,I=[],[],[],[]
    for i in range(len(A)):
        y = 100.0*B[i]/(A[i]+B[i]+C[i])
        Y.append(y)
        if A[i]+C[i] == 0:
            x = 0.5*y
            X.append(x)
        else:
            x = A[i]*(100-y)/(A[i]+C[i]) + 0.5*y
            X.append(x)
        Z.append(E[i])
        I.append(ID[i])
    return X , Y, Z, I

def make_input(X=None,Y=None,Z=None,I=None,name=None,wd=None):
    try:
        indata = open(str(wd)+"/temp/"+str(name)+".dat", "w")
        indata.write(str(len(X)) + '\n')
        for i in range(len(X)):
            indata.write(str(X[i]) + '  ' + str(Y[i]) + '  ' + str(Z[i]) + '   #' + str(I[i]) +'\n')
    finally:
        indata.close()

def save_objects(e1=None,e2=None,e3=None,name=None,X=None,Y=None,Z=None,I=None,wd=None):
    e=[]
    e.append(e1)
    e.append(e2)
    e.append(e3)
    np.savez(os.path.join(str(wd)+'/temp/',name), e = e, X = X, Y = Y, Z = Z, I=I)

def read_file(e1=None,e2=None,e3=None):
    A,B,C,E,ID = [],[],[],[],[]
    data = open(sys.argv[1], "r")
    num = int(data.readline())
    for line in data:
        line = line.rstrip()
        if line:
            line = line.partition('#')[0]
            a = map(float, line.split())
            A.append(a[0])
            B.append(a[1])
            C.append(a[2])
            E.append(a[3])
            identity = str(e1)+str(a[0])+str(e2)+str(a[1])+str(e3)+str(a[2])
            ID.append(identity)
    if num < 4:
        print "Too few points(less than 4),so 1D or 2D hull"
        sys.exit()
    data.close()
    return A,B,C,ID,E
