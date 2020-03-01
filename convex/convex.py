#! /usr/bin/python                                                                                                                                 

from __future__ import division
import math
import sys
from init import *
import os.path
from os import path

def main():
    print("\nThanks for using this programme.\n")

if __name__== "__main__":
    cwd = os.getcwd()
    wd = os.path.dirname(sys.argv[0]) 
    e1,e2,e3 = take_basic_input()
    name=str(e1)+str(e2)+str(e3)
    if len(sys.argv) < 2:
        A, B, C, ID, E = ternary_dec_input(e1,e2,e3)
    else:
        A, B, C, ID, E = read_file(e1,e2,e3)
    X,Y,Z,I = bary2cart(A,B,C,ID,E)
    make_input(X,Y,Z,I,name,wd)
    cmd1 = str(wd)+'/calculator.py '+ str(wd) + '/temp/'+ name + '.dat '+ str(wd) 
    os.system(cmd1)
    save_objects(e1,e2,e3,name,X,Y,Z,I,wd)
    cmd2 = str(wd)+'/plot.py '+ str(wd) + '/temp/'+ name + '.npz ' + str(wd)
    os.system(cmd2)
    cmd3 = 'mv ' + str(cwd) + '/temp-plot.html ' + str(cwd) + '/' + name + '.html'
    os.system(cmd3)
    cmd4 = 'rm '+str(wd)+'/temp/*'
    os.system(cmd4)
    out_file = str(cwd)+'/'+name+'.out'
    if os.path.exists(out_file):
        sys.exit()
    else:
        print("Ran into a problem? Check out the Troubleshooting section at the end of README\n Can't see the problem? Contact me on usingh1@ch.iitr.ac.in with your error\n                                      - Utkarsh Singh")
    main()
