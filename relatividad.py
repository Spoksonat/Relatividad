import numpy as np
from sympy import *
from sympy.tensor.tensor import TensorIndexType, tensorhead, TensorType,tensor_indices
from gravipy import *

print('Crear documento con cantidades relativistas importantes')
print('Por: Ozymandias' + '\n')
print('Metricas disponibles: ')
print('Minkowski')
print('Schwarchild')
print('FLRW')
print('Manual')
print('\n')
met = raw_input("Seleccione la metrica: ")

#Parte modificable
#****************************************************************

#Coordenadas y sus simbolos en LaTeX
#t,r,theta,phi = symbols('t,r,\\theta,\\phi') #Coord.esfericas
#t,r,theta,z = symbols('t,r,\\theta,z') #Coord.cilindricas
#t,x,y,z = symbols('t,x,y,z') #Coord.cartesianas

#Vector de coordenadas
#co = Coordinates(r'\chi',[t,r,theta,phi]) #esfericas
#co = Coordinates(r'\chi',[t,r,theta,z]) #cilindricas
#co = Coordinates(r'\chi',[t,x,y,z]) #cartesianas

#Definicion de constantes 
#k = symbols('k') #Para FLRW
pi,G = symbols('\\pi,G') #Constante gravitacional


#Funciones
#a= Function('a')(t) #Para FLRW

#Metrica diagonal
#Metric = diag(-1,a**2/(1-k*r**2) , a**2*r**2, a**2*r**2*sin(theta)**2) #Para FLRW
#Metric = diag(-(1- 2*G*M/r),1/(1- 2*G*M/r) ,r**2, r**2*sin(theta)**2) #Para Schwarchild
#Metric = diag(-1,1,1,1) #Para Minkowski cartesianas
#Metric = diag(-1,1,r**2,r**2*sin(theta)**2) #Para Minkowski esfericas

if(met == 'FLRW'):
    t,r,theta,phi = symbols('t,r,\\theta,\\phi') #Coord.esfericas
    co = Coordinates(r'\chi',[t,r,theta,phi]) #esfericas
    k = symbols('k') #Para FLRW
    a= Function('a')(t) #Factor de escala para FLRW
    Metric = diag(-1,a**2/(1-k*r**2) , a**2*r**2, a**2*r**2*sin(theta)**2) #Para FLRW
    g = MetricTensor('g', co, Metric)
    coords = 'Esfericas'

elif(met== 'Schwarchild'):
    t,r,theta,phi = symbols('t,r,\\theta,\\phi') #Coord.esfericas
    co = Coordinates(r'\chi',[t,r,theta,phi]) #esfericas
    M= symbols('M') #Para Schwarchild
    Metric = diag(-(1- 2*G*M/r),1/(1- 2*G*M/r) ,r**2, r**2*sin(theta)**2)
    g = MetricTensor('g', co, Metric)
    coords = 'Esfericas'

elif(met == 'Minkowski'):
    coords = raw_input("Coord. Esfericas, Cilindricas o Cartesianas?:")
    if(coords == 'Esfericas'):
        t,r,theta,phi = symbols('t,r,\\theta,\\phi') #Coord.esfericas
        co = Coordinates(r'\chi',[t,r,theta,phi]) #esfericas
        Metric = diag(-1,1,r**2,r**2*sin(theta)**2) #Para Minkowski esfericas
        g = MetricTensor('g', co, Metric)
    elif(coords == 'Cilindricas'):
        t,r,theta,z = symbols('t,r,\\theta,z') #Coord.esfericas
        co = Coordinates(r'\chi',[t,r,theta,z]) #esfericas
        Metric = diag(-1,1,r**2,1) #Para Minkowski esfericas
        g = MetricTensor('g', co, Metric)
    elif(coords == 'Cartesianas'):
        t,x,y,z = symbols('t,x,y,z') #Coord.cartesianas
        co = Coordinates(r'\chi',[t,x,y,z]) #cartesianas
        Metric = diag(-1,1,1,1)
        g = MetricTensor('g', co, Metric)
    else:
        print ('Error')


        
elif(met == 'Manual'):

    nombre = raw_input("Nombre de la metrica: ")
    met = nombre
    coords = raw_input("Coord. Esfericas, Cilindricas o Cartesianas?:")
    if(coords == 'Esfericas'):
        t,r,theta,phi = symbols('t,r,\\theta,\\phi') #Coord.esfericas
        co = Coordinates(r'\chi',[t,r,theta,phi]) #esfericas

        c_1,c_2,c_3,c_4,c_5,c_6 = symbols('c_1,c_2,c_2,c_4,c_5,c_6')

        f_1 = Function('f_{1}')
        f_2 = Function('f_{2}') 
        f_3 = Function('f_{3}') 
        f_4 = Function('f_{4}') 
        f_5 = Function('f_{5}') 
        f_6 = Function('f_{6}') 
        f_7 = Function('f_{7}') 
        f_8 = Function('f_{8}')

 
        g00 = eval(raw_input('Introducir g00:' ))
        g01 = eval(raw_input('Introducir g01:' ))
        g02 = eval(raw_input('Introducir g02:' ))
        g03 = eval(raw_input('Introducir g03:' ))
        g10 = eval(raw_input('Introducir g10:' ))
        g11 = eval(raw_input('Introducir g11:' ))
        g12 = eval(raw_input('Introducir g12:' ))
        g13 = eval(raw_input('Introducir g13:' ))
        g20 = eval(raw_input('Introducir g20:' ))
        g21 = eval(raw_input('Introducir g21:' ))
        g22 = eval(raw_input('Introducir g22:' ))
        g23 = eval(raw_input('Introducir g23:' ))
        g30 = eval(raw_input('Introducir g30:' ))
        g31 = eval(raw_input('Introducir g31:' ))
        g32 = eval(raw_input('Introducir g32:' ))
        g33 = eval(raw_input('Introducir g33:' ))
        gmat = np.array([[g00,g01,g02,g03],[g10,g11,g12,g13],[g20,g21,g22,g23],[g30,g31,g32,g33]])
        Metric = diag(1,1,1,1)
        gp = MetricTensor('gp', co, Metric)

        

        gpp = Tensor('g',2,gp)       

        def gpp_new_method(idxs):
            component = gmat[idxs[0]-1][idxs[1]-1]
            gpp.components.update({idxs: component}) 
            return component
        gpp._compute_covariant_component = gpp_new_method 

        Metric = gpp(All,All)
        g = MetricTensor('g', co, Metric)

    elif(coords == 'Cilindricas'):
        t,r,theta,z = symbols('t,r,\\theta,z') #Coord.cilindricas
        co = Coordinates(r'\chi',[t,r,theta,z])

        c_1,c_2,c_3,c_4,c_5,c_6 = symbols('c_1,c_2,c_2,c_4,c_5,c_6')

        f_1 = Function('f_{1}')
        f_2 = Function('f_{2}') 
        f_3 = Function('f_{3}') 
        f_4 = Function('f_{4}') 
        f_5 = Function('f_{5}') 
        f_6 = Function('f_{6}') 
        f_7 = Function('f_{7}') 
        f_8 = Function('f_{8}')


        g00 = eval(raw_input('Introducir g00:' ))
        g01 = eval(raw_input('Introducir g01:' ))
        g02 = eval(raw_input('Introducir g02:' ))
        g03 = eval(raw_input('Introducir g03:' ))
        g10 = eval(raw_input('Introducir g10:' ))
        g11 = eval(raw_input('Introducir g11:' ))
        g12 = eval(raw_input('Introducir g12:' ))
        g13 = eval(raw_input('Introducir g13:' ))
        g20 = eval(raw_input('Introducir g20:' ))
        g21 = eval(raw_input('Introducir g21:' ))
        g22 = eval(raw_input('Introducir g22:' ))
        g23 = eval(raw_input('Introducir g23:' ))
        g30 = eval(raw_input('Introducir g30:' ))
        g31 = eval(raw_input('Introducir g31:' ))
        g32 = eval(raw_input('Introducir g32:' ))
        g33 = eval(raw_input('Introducir g33:' ))
        gmat = np.array([[g00,g01,g02,g03],[g10,g11,g12,g13],[g20,g21,g22,g23],[g30,g31,g32,g33]])
        Metric = diag(1,1,1,1)
        gp = MetricTensor('gp', co, Metric)

        

        gpp = Tensor('g',2,gp)       

        def gpp_new_method(idxs):
            component = gmat[idxs[0]-1][idxs[1]-1] 
            gpp.components.update({idxs: component}) 
            return component
        gpp._compute_covariant_component = gpp_new_method 

        Metric = gpp(All,All)
        g = MetricTensor('g', co, Metric)

    elif(coords == 'Cartesianas'):
        t,x,y,z = symbols('t,x,y,z') #Coord.cartesianas
        co = Coordinates(r'\chi',[t,x,y,z]) #cartesianas

        c_1,c_2,c_3,c_4,c_5,c_6 = symbols('c_1,c_2,c_2,c_4,c_5,c_6')

        f_1 = Function('f_{1}')
        f_2 = Function('f_{2}') 
        f_3 = Function('f_{3}') 
        f_4 = Function('f_{4}') 
        f_5 = Function('f_{5}') 
        f_6 = Function('f_{6}') 
        f_7 = Function('f_{7}') 
        f_8 = Function('f_{8}')


        g00 = eval(raw_input('Introducir g00:' ))
        g01 = eval(raw_input('Introducir g01:' ))
        g02 = eval(raw_input('Introducir g02:' ))
        g03 = eval(raw_input('Introducir g03:' ))
        g10 = eval(raw_input('Introducir g10:' ))
        g11 = eval(raw_input('Introducir g11:' ))
        g12 = eval(raw_input('Introducir g12:' ))
        g13 = eval(raw_input('Introducir g13:' ))
        g20 = eval(raw_input('Introducir g20:' ))
        g21 = eval(raw_input('Introducir g21:' ))
        g22 = eval(raw_input('Introducir g22:' ))
        g23 = eval(raw_input('Introducir g23:' ))
        g30 = eval(raw_input('Introducir g30:' ))
        g31 = eval(raw_input('Introducir g31:' ))
        g32 = eval(raw_input('Introducir g32:' ))
        g33 = eval(raw_input('Introducir g33:' ))
        gmat = np.array([[g00,g01,g02,g03],[g10,g11,g12,g13],[g20,g21,g22,g23],[g30,g31,g32,g33]])
        Metric = diag(1,1,1,1)
        gp = MetricTensor('gp', co, Metric)

        

        gpp = Tensor('g',2,gp)       

        def gpp_new_method(idxs):
            component = gmat[idxs[0]-1][idxs[1]-1] 
            gpp.components.update({idxs: component}) 
            return component
        gpp._compute_covariant_component = gpp_new_method 

        Metric = gpp(All,All)
        g = MetricTensor('g', co, Metric)

    else:
        print ('Error')

else:
    print ('Error')
        

#*****************************************************************

file = open("Titulop.tex","w")
file.write("\\begin{center}" + "\n" + "\\textbf{\\Huge{Metrica de "+ met + "}}" + "\n"+"\\end{center}" + "\n" +  "\\begin{center}" + "\n" + "\\huge{Coordenadas: " + coords + "}" + "\n" + "\\end{center}")
file.close()


Ga= Christoffel('Ga',g)
#print (latex(g(All,All)))

file = open("gp.tex","w")
file.write("\\begin{align*}" + "\n" + "g_{\\mu\\nu}" + "=" + (latex(g(All,All))) + "\n" + "\\end{align*}")
file.close()

file = open("Christoffelp.tex","w")
file.write("\\begingroup" + "\n")
file.write("\\allowdisplaybreaks" + "\n")
file.write("\\begin{dmath}" + "\n")


for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            file.write("\Gamma^{" + str(i-1) + "}" + "_{" + str(j-1) + str(k-1) + "}" + "&=" + (latex(Ga(-i,j,k).simplify())) + "\\" + "\\" + "\n" ) #Ga(-i,j,k)= Gamma^{i}_{j,k}, Ga(i,j,k) = gamma_{i,j,k}


file.write("\\end{dmath}"+ "\n")
file.write("\\endgroup" )

file.close()


Ri = Ricci('Ri',g)

file = open("Riccip.tex","w")
file.write("\\begingroup" + "\n")
file.write("\\allowdisplaybreaks" + "\n")
file.write("\\begin{dmath}" + "\n")


for i in range(1,5):
    for j in range(1,5):

        file.write("R_{" + str(i-1) + str(j-1) + "}" + "&=" + (latex(Ri(i,j))) + "\\" + "\\" + "\n" )

file.write("\\end{dmath}"+ "\n")
file.write("\\endgroup" )

file.close()

G = Einstein('G',Ri)

file = open("Einsteinp.tex","w")
file.write("\\begingroup" + "\n")
file.write("\\allowdisplaybreaks" + "\n")
file.write("\\begin{dmath}" + "\n")


for i in range(1,5):
    for j in range(1,5):

        file.write("G_{" + str(i-1) + str(j-1) + "}" + "&=" + (latex(G(i,j))) + "\\" + "\\" + "\n" )

file.write("\\end{dmath}"+ "\n")
file.write("\\endgroup" )

file.close()

#Tensor de Estres-Energia
#****************************************************************


p = Function('p')(t)
rho = Function('\\rho')(t)
T = Tensor('T',2,g)
u = Tensor('u',1,g)

ucontra = np.array([1,0,0,0])

def u_new_method(idxs):
    component = g(idxs[0],1)*ucontra[0]
    for i in range(2,5):
        component += g(idxs[0],i)*ucontra[i-1]
    u.components.update({idxs: component}) 
    return component
u._compute_covariant_component = u_new_method 



def T_new_method(idxs):
    component = (p+rho)*u(idxs[0])*u(idxs[1]) + p*g(idxs[0],idxs[1]) 
    T.components.update({idxs: component}) 
    return component
T._compute_covariant_component = T_new_method 

file = open("estresp.tex","w")
file.write("\\begin{align*}" + "\n" + "T_{\\mu\\nu}" + "=" + (latex(T(All,All))) + "\n" + "\\end{align*}")
file.close()

#****************************************************************


#Ecuaciones de campo de Einstein

#****************************************************************

file = open("campop.tex","w")
file.write("\\begingroup" + "\n")
file.write("\\allowdisplaybreaks" + "\n")



for i in range(1,5):
    for j in range(1,5):
  
        if(G(i,j)== 0 and T(i,j)== 0):
            continue
        else: 
            file.write("\\begin{dmath}" + "\n" + latex(G(i,j)) + "=" + "8\\pi G" + "\\left(" +(latex(T(i,j))) + "\\right)" + "\n" + "\\end{dmath}"+ "\n" ) 

file.write("\\endgroup" )

file.close()

#****************************************************************

#Determinante de la metrica
#**************************************************************** 

det_g = g(All,All).det()

file = open("detgp.tex","w")

file.write("\\begin{dmath}" + "\n" + "g" + "=" + latex(det_g) + "\n" + "\\end{dmath}" + "\n")


file.close()

#****************************************************************


#Tensor de Riemann y Curvatura Gaussiana
#****************************************************************

Rm = Riemann('Rm',g)
kappa = Rm(1,2,1,2)/det_g

file = open("curvaturap.tex","w")

file.write("\\begin{dmath}" + "\n" + "\\kappa" + "=" + "\\frac{" + "R_{1212}" + "}{" + "g" + "}" + "=" + "\\frac{" + latex(Rm(1,2,1,2)) + "}{" + latex(det_g) + "}" +  "="  + latex(kappa) + "\n" + "\\end{dmath}" + "\n")


file.close()



#****************************************************************




#Ecuaciones de la geodesica
#****************************************************************
tau = symbols('\\tau')
w = Geodesic('w',g,tau)

geo1= co(-1).diff(tau,2)
geo2= co(-2).diff(tau,2)
geo3= co(-3).diff(tau,2)
geo4= co(-4).diff(tau,2)

for i in range(1,5):
    for j in range(1,5):
        geo1 += Ga(-1,i,j).simplify()*co(-i).diff(tau)*co(-j).diff(tau)
        geo2 += Ga(-2,i,j).simplify()*co(-i).diff(tau)*co(-j).diff(tau)
        geo3 += Ga(-3,i,j).simplify()*co(-i).diff(tau)*co(-j).diff(tau)
        geo4 += Ga(-4,i,j).simplify()*co(-i).diff(tau)*co(-j).diff(tau)
        geo1.simplify()
        geo2.simplify()
        geo3.simplify()
        geo4.simplify()

file = open("geo1p.tex","w")
file.write("\\begin{dmath}" + "\n" + "0" + "=" + (latex(geo1)) + "\n" + "\\end{dmath}")
file.close()

file = open("geo2p.tex","w")
file.write("\\begin{dmath}" + "\n" + "0" + "=" + (latex(geo2)) + "\n" + "\\end{dmath}")
file.close()

file = open("geo3p.tex","w")
file.write("\\begin{dmath}" + "\n" + "0" + "=" + (latex(geo3)) + "\n" + "\\end{dmath}")
file.close()

file = open("geo4p.tex","w")
file.write("\\begin{dmath}" + "\n" + "0" + "=" + (latex(geo4)) + "\n" + "\\end{dmath}")
file.close()
#****************************************************************

#Lagrangiano
#****************************************************************


Lcua1 = g(1,1)*co(-1).diff(tau)*co(-1).diff(tau)
Lcua2 = g(2,1)*co(-2).diff(tau)*co(-1).diff(tau)
Lcua3 = g(3,1)*co(-3).diff(tau)*co(-1).diff(tau)
Lcua4 = g(4,1)*co(-4).diff(tau)*co(-1).diff(tau)

for j in range(2,5):
    Lcua1 += g(1,j)*co(-1).diff(tau)*co(-j).diff(tau)
    Lcua2 += g(2,j)*co(-2).diff(tau)*co(-j).diff(tau)
    Lcua3 += g(3,j)*co(-3).diff(tau)*co(-j).diff(tau)
    Lcua4 += g(4,j)*co(-4).diff(tau)*co(-j).diff(tau)

Lcua = Lcua1+  Lcua2 + Lcua3 + Lcua4

file = open("lagrangianop.tex","w")

file.write("\\begin{dmath}" + "\n" + "\mathcal{L}" + "=" + "\\left[" +  latex(Lcua) + "\\right]^{1/2}" + "\n" + "\\end{dmath}" + "\n")


file.close()
        


#****************************************************************

#Derivada Covariante Tensor de Estres-Energia
#****************************************************************

#nu=0
covT1 = T(-1,-1).diff(co(-1))
covT2 = T(-1,-2).diff(co(-1))
covT3 = T(-1,-3).diff(co(-1))
covT4 = T(-1,-4).diff(co(-1))

for i in range(2,5):
    covT1 += T(-i,-1).diff(co(-i))
    covT2 += T(-i,-2).diff(co(-i))
    covT3 += T(-i,-3).diff(co(-i))
    covT4 += T(-i,-4).diff(co(-i))

for i in range(1,5):
    for j in range(1,5):
        covT1 += Ga(-i,i,j).simplify()*T(-j,-1) + Ga(-1,i,j).simplify()*T(-i,-j)
        covT2 += Ga(-i,i,j).simplify()*T(-j,-2) + Ga(-2,i,j).simplify()*T(-i,-j)
        covT3 += Ga(-i,i,j).simplify()*T(-j,-3) + Ga(-3,i,j).simplify()*T(-i,-j)
        covT4 += Ga(-i,i,j).simplify()*T(-j,-4) + Ga(-4,i,j).simplify()*T(-i,-j)

        covT1.simplify()
        covT2.simplify()
        covT3.simplify()
        covT4.simplify()

file = open("covT1p.tex","w")
file.write("\\begin{dmath}" + "\n"  + (latex(covT1)) + "=" + "0" + "\n" + "\\end{dmath}")
file.close()

file = open("covT2p.tex","w")
file.write("\\begin{dmath}" + "\n" + (latex(covT2))+ "=" + "0" + "\n" + "\\end{dmath}")
file.close()

file = open("covT3p.tex","w")
file.write("\\begin{dmath}" + "\n"  + (latex(covT3)) + "=" + "0" + "\n" + "\\end{dmath}")
file.close()

file = open("covT4p.tex","w")
file.write("\\begin{dmath}" + "\n" + (latex(covT4))+ "=" + "0" + "\n" + "\\end{dmath}")
file.close()



#****************************************************************








