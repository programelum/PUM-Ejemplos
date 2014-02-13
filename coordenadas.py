#!/usr/bin/env python
from numpy import *
from sys import argv

grados=pi/180
radianes=1/grados
horas=15

epsilon=23.5*grados

alpha=float(argv[1])*horas*grados
delta=float(argv[2])*grados

beta=arcsin(sin(delta)*cos(epsilon)-cos(delta)*sin(epsilon)*sin(alpha))

p=sin(delta)*sin(epsilon)+cos(delta)*cos(epsilon)*sin(alpha)
q=cos(alpha)*cos(delta)

lambc=arctan(p/q)*radianes

if p*q<0 and q<0:
    lamb=lambc+180
if p*q<0 and q>0:
    lamb=lambc+360
if p+q<0:
    lamb=lambc+180

print beta*radianes,lamb
