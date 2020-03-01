#!/usr/bin/python 

from __future__ import division
import math
import os
import sys
import plotly
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as tri
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

def cart2bary(arg=None,wd=None):
    X,Y,Z,E,I = [],[],[],[],[]
    element = np.load(sys.argv[1])
    npzfile = np.load(str(wd)+'/temp/temp.npz')
    for i in range(len(npzfile['x'])):
        if ((float(npzfile['y'][i]) == 100) & (float(npzfile['x'][i]) == 50)):
            a = float(0.0)
            X.append(a)
            b = float(1.0)
            Y.append(b)
            c = float(0.0)
            Z.append(c)
        else:
            b = float(npzfile['y'][i]/100)
            Y.append(b)
            a = float((float(npzfile['x'][i]) - 0.5*float(npzfile['y'][i]))*0.01)
            X.append(a)
            c = float(1.0 - float(a) - float(b))
            Z.append(c)
        E.append(npzfile['z'][i])
        I.append(str(element['e'][0])+str(a)+str(element['e'][1])+str(b)+str(element['e'][2])+str(c))
    return X, Y, Z, E, I

def write_output(arg=None,X=None,Y=None,Z=None,E=None,I=None):
    npzfile = np.load(arg)
    indata = open(str(npzfile['e'][0]) + str(npzfile['e'][1]) + str(npzfile['e'][2])+".out", "w")
    indata.write("number  of vertices of convex hull (number of stable compositions):  " + str(len(X)) +'\n')
    indata.write('Parts of: ' + str(npzfile['e'][0]) + '          '+str(npzfile['e'][1])+ '        '+ str(npzfile['e'][2])+'         '+'Formation Enthalpy (eV)'+'         '+'Alloy name'+'\n')
    for i in range(len(X)):
        indata.write('          '+str(X[i]) + '       ' + str(Y[i]) + '       ' + str(Z[i]) + '             '+  str(E[i]) + '                   #' + str(I[i]) +'\n')
    indata.close()


def plot(arg=None,X=None,Y=None,Z=None,E=None,I=None):
    npzfile = np.load(arg)
    x = np.array(X)
    y = np.array(Y)
    z = np.array(Z)
    e = np.array(E)
    alloy_name = str(npzfile['e'][0] + npzfile['e'][1] + npzfile['e'][2])
    fig = ff.create_ternary_contour(np.array([x,y,z]), e, pole_labels=[npzfile['e'][0], npzfile['e'][1], npzfile['e'][2]], interp_mode='cartesian', ncontours=5, colorscale='Viridis', showscale=True, showmarkers=True, title=str(alloy_name))
    htmlfile = str(alloy_name) +'.html'
    filename = htmlfile
    plotly.offline.plot(fig, filename , auto_open=False)
    return htmlfile



######## Following two definitions to be implemented when I find a plotting library better than matplotlib ########
#def denormalize(X=None,Y=None,Z=None):
#    x,y,z=[],[],[]
#    for i in range(len(X)):
#        denorm = (X[i],Y[i],Z[i])
#        j = denorm.index(min(X[i],Y[i],Z[i])
#        x[i] = X[i]/denorm[j][i]
#        y[i] = Y[i]/denorm[j][i]
#        z[i] = Z[i]/denorm[j][i]
#    return x,y,z
#
#
#def plot2(arg=None,X=None,Y=None,Z=None):
#    x1=[]
#    y1=[]
#    element = np.load(sys.argv[1])
#    npzfile = np.load('temp.npz')
#    x,y,z = denormalize(X,Y,Z)
#    text = str(element['e'][0])+str(X)+str(element['e'][1])+str(Y)+str(element['e'][2])+str(Z)
#    T = tri.Triangulation(npzfile['x'],npzfile['y'])
#    plt.tricontourf(npzfile['x'],npzfile['y'],T.triangles,npzfile['z'])
## T.triangles, if not specified, is delaunay triangulation  
#    triangle = tri.Triangulation(npzfile['x'],npzfile['y'])
#    for i in range(len(npzfile['x'])):
#            x1.append(npzfile['x'][i])
#            y1.append(npzfile['y'][i])
#    point_annotate=(x1,y1)
#    plt.annotate(text,point_annotate)
#    plt.axis('off')
#    plt.triplot(triangle,'o-',c='black',clip_on=False)
#    plt.show()
########################################### COMING SOON, probably json elements needed #############################


def main(htmlfile):
    endmessage = "\n The plot has been generated.\n Please use any web-browser to open "+ str(htmlfile)+"\n Click on 'Export to plotly' and customize to your needs. \n\n\n Thanks for using this programme. \n"
    print(endmessage)

if __name__ == '__main__':
    X,Y,Z,E,I = cart2bary(sys.argv[1],sys.argv[2])
    write_output(sys.argv[1],X,Y,Z,E,I)
    htmlfile = plot(sys.argv[1],X,Y,Z,E,I)
    main(htmlfile)
