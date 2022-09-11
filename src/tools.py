# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:02:51 2020

@author: quent
"""

import matplotlib.pyplot as plt
import numpy as np

def invert_backslash(e):
    return e.replace('\\', "/")
    return e





def float2(a):
    if len(a) > 5:
        if a[-3] == '-':
            b=float(a[:4])*10**(float(a[-3:]))
            return b
    if a == '':
        return 0
    
    else:
        return float(a)

def sort_number(e):
    t=""
    for i in range(len(e)):
        if e[i]=='0' or e[i]=='1' or e[i]=='2' or e[i]== '3' or e[i]=='4' or e[i]=='5' or e[i]=='6' or e[i]=='7' or e[i]=='8' or e[i]=='9' or e[i]=='-':
            t=t+e[i]
        if e[i]==',':
            t=t+"."
    return t

def list_to_float(M):
    k=[]
    for i in range(len(M)):
        k.append(float(M[i]))
    return k

def tr5(t):
    """
    Parameters
    ----------
    t : Liste t=[temp, position

    Returns temps de reponse à 5%
    -------
    """
    m=max(t[1])
    m1=0.05*m
    i=len(t[1])
    while t[1][i-1] <= m1:
        i=i-1
    print("tr5 =", t[0][i] ," secondes")
    return t[0][i]
    
def tr1(t):
    """
    Parameters
    ----------
    t : Liste t=temp, position

    Returns temps de reponse à 5%
    -------
    """
    # print(max(t[1]))
    m=max(t[1])
    
    m1=0.03*m
    i=len(t[1])
    while t[1][i-1] <= m1:
        i=i-1
    # print("tr5 =", t[0][i] ," secondes")
    return t[0][i]
    
def slicing_radius(T,a):
    """
    Parameters
    ----------
    T : Tabbleau de tableau de valeurs
        La variable contenant en colonne paires: le temps en colonne impaires: l'angle'
    a : float
        radian.

    Returns :L,K
        L = slicing de T à partir duquel ne passera plus devant l'aimant
        K = slicing après L
    -------
    """
    L=[]
    K=[]
    for i in range(len(T)):
        L.append([])
        K.append([])
    for i in range(len(T)//2):
        for j in range(1,len(T[2*i])):
            if T[2*i+1][-j] > a:
                z=j

                break
        L[2*i]=T[2*i][:(len(T[2*i])-z)]
        L[2*i+1]=T[2*i+1][:(len(T[2*i])-z)]
        K[2*i]=T[2*i][(len(T[2*i])-z):]
        K[2*i+1]=T[2*i+1][(len(T[2*i+1])-z):]
    return L,K

def derivee(A):
    """
    A=(T,C) avec T le temps, C avec la courbe en question
    
    Returns:
        A=derivee aproximée grace à l'approximation du taux d'accroissement
    """
    T,C=A
    A=[]
    for i in range(len(T)-1):
       A.append((C[i+1]-C[i])/(T[i+1]-T[i]))
    return A

def derivee1(A):
    """
    A=(T,C) avec T le temps, C avec la courbe en question
    
    Returns:
        A=derivee aproximée grace à l'approximation du taux d'accroissement
    """
    T,C=A
    A=[]
    for i in range(len(T)-1):
       A.append((C[i+1]-C[i])/(T[i+1]-T[i])*0.1)
    return A


def nb_oscillation3(A):
    """
    fonctionne pr nb de points <600
      Parameters
    ----------
    A=(t,x)
    t : Table
        Time
    x : Table
        x=f(time).

    Returns n=nb de période
    -------
    """   
    t,x=A
    tmax =t.index(tr1(A))
    p=0
    k=x[:tmax+1]
    i=0
    n=0
    lim=x[tmax]*180/3.14
    # print(tmax,"lim",lim)
    for i in range(1,len(k)):
        # k=x[p:tmax]
        # print(k[i-1]*180/3.14)
        if abs(k[i-1]*180/3.14)>lim and abs(k[i]*180/3.14) <lim:
            n=n+1
        
        # print("a")
        # while abs(k[i]) > 0.5:
        #     print("b")
        #     i=i+1
        # p=i+10
        # n=n+1
    return n #nb d'oscillation

def hauteur(A,l):
    """
    A=(T,C) avec T le temps, C avec la courbe en question    

    Returns:
        H = tableau de la hauteur en fonction du temps
    """

    T,C=A
    A=[]
    for i in range(len(T)):
       # A.append(l/np.cos(C[i]*3.14/180)-l)
       A.append(l-l*np.cos(C[i]))
    return A

def opti(T,n):
    """

    Parameters
    ----------
    T : list
    n : int

    Returns O liste de n points
    -------
    None.

    """
    l=len(T)
    k=len(T)/n
    if n >l :
        k=1
        l=n
    O=[]
    for i in range(n):
        O.append(T[int(i*k)])
    return O

def EM(V,H):
    """
    Parameters
    ----------
    V : Tableau de points vitesse angulaire en rad/s
    H : Tableau de point de la hauteur en m

    Returns :
        M tableau de point de l'EM en fc du temps
    -------

    """
    H=H[1:]
    E=[]
    for i in range(len(V)):
        E.append(0.5*m*(l*V[i])**2 + m*g*H[i])
    return E

def proj_X(theta,l):
    
    """
    Parameters
    ----------
    theta : angle en degrés ou radian
    l = rayon
    Returns:
        x : abscisse sur x du point M
    ----------
    
    """
    return l*np.sin(theta)
    
def  magnetic_field_intensity(x):
    """

    Parameters
    ----------
    x : scalar, coordonnée en x
        DESCRIPTION. The default is proj_X(theta).

    Returns:
        B en mT
    -------
    donne la valeur du champ magnétique aproximé à l'aide de la densité surfacique
    densité mesurée pour un demi plaque
    """
    T=[94.1,126.4,90.2,67.2,52.4,40.9,31.65,25.1,20.55,16.7,14,11.95,9.95,8.75,7.52,2.45]
    if 0 <=x < 0.5:
        return 94.1
    i=0.5
    n=1
    while i<=15.5:
        if i <= x < i+1:
            return T[n]
        i=i+1
        n=n+1
    if 15.5 <= x <= 16:
        return T[n-1]
    return 0
#print(magnetic_field_intensity(15.6))





def extract_data_list(loc):
    """input:  loc: l'arborescence du fichier en .csv
        c=à partir de quelle ligne on veut l'extraire
        
        leters are filtred via sort()
        values are converted in float
        
        les colonnes impaires sont transformees en radian 
        output T tableau des colonnes T=[C1,C2,C3,...]
    en radian
    """
    r=invert_backslash(loc)
    print(r)
    a=1
    a=open(invert_backslash(loc),'r')
    t=a.readlines()
    a.close()
    tab=[]
    for chn in t:
        tab.append(chn.split(";"))
    n=len(tab[0])
    i=len(tab)
    T=[]
    J=[]
    """
    on remplace la virgule par un point
    """
    for j in range(n):
        T.append([])
        J.append([])
    for j in range(0,n):
       for k in range(1,i):
           if tab[k][j] != '':
               T[j].append(float2(sort_number(tab[k][j])))
    


    #enlever les '' qui restent

    """
    on fait passer les valerus des colonnes impaires de degres en radian
    """
    for i in range(len(T)//2):
        for j in range(len(T[2*i+1])):
            T[2*i+1][j]=T[2*i+1][j]*3.14/180
        
    for i in range(len(T)):
        J[i]=T[i][:len(T[(i//2)*2])]
        
    return J
A=extract_data_list(r"/Volumes/USB/scope_2.csv")