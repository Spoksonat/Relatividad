# Relatividad

Descripción: Programa en Python y documento en LaTeX para obtener un archivo pdf (llamado Cantidades_relativistas.pdf) con las cantidades relevantes de Relatividad General para cierta métrica (Se obtiene el tensor métrico, Símbolos de Christoffel, Tensor de Ricci, Tensor de Einstein, Tensor de estres-energía para un fluido perfecto , las ecuaciones de campo de Einstein, el determinante del tensor métrico, la curvatura Gaussiana, las ecuaciones de la geodésica y el Lagrangiano). Se usa para este caso c=1.

Se puede ejecutar para tres métricas predeterminadas más otra que puede ser introducida manualmente. Las tres métricas predeterminadas son: Minkowski, Schwarchild y FLRW(Friedman-Lemaitre-Robertson-Walker). El modo manual permite dar un nombre a la métrica, seleccionar las coordenadas (Esféricas, Cilíndricas o Cartesianas) e introducir cada componente del tensor métrico. Una métrica recomendada para probar el modo manual es la métrica de Rindler en coordenadas Cartesianas (![equation](https://latex.codecogs.com/gif.latex?g_%7B00%7D%3D%20-x%5E2), ![equation](https://latex.codecogs.com/gif.latex?g_%7B11%7D%3Dg_%7B22%7D%3Dg_%7B33%7D%3D1),![equation](https://latex.codecogs.com/gif.latex?g_%7B%5Cmu%5Cnu%7D%3D0%20%28%5Cmu%5Cneq%20%5Cnu%29)). El modo manual permite hacer uso de seis constantes simbólicas c_1.c_2,c_3,c_4,c_5,c_6 para que sean usadas al momento de introducir cada componente del tensor métrico.

Como extra, se ponen dos ejemplos de los archivos pdf resultantes de ejecutar el programa. El ejemplo llamado Ejemplo_FLRW.pdf es para la métrica de FLRW, el ejemplo llamado Ejemplo_Manual_Rindler.pdf es para la métrica de Rindler con el modo manual en coordenadas Cartesianas.

# Pasos para ejecutar:

1. Instalar Sympy y Gravipy:

Para instalar Sympy: sudo pip install sympy
Para instalar Gravipy: sudo pip install gravipy

2. Verificar que se tenga el compilador de LaTeX pdflatex

Para instalar pdflatex en Ubuntu se usa: sudo apt-get install texlive-latex-base 

3. Ejecutar:

Se ejecuta solo con poner make y enter en la consola de Linux (Ejecutando el Makefile).

# Notas

Si están en modo manual y quieren introducir algunas funciones conocidas en las componentes del tensor métrico, la forma de introducirlas son las siguientes:

1. Exponencial:

g00: exp(c_1* y) (Comando en consola que en LaTeX se ve como ![equation](https://latex.codecogs.com/gif.latex?e%5E%7Bc_1y%7D))

2. Potencias:

g00: -x**2 (Comando en consola que en LaTeX se ve como ![equation](https://latex.codecogs.com/gif.latex?-x%5E2))

3. Funciones trigonométricas:

g00: sin(theta) ((Comando en consola que en LaTeX se ve como ![equation](https://latex.codecogs.com/gif.latex?%5Csin%28%5Ctheta%29))

g00: cos(phi)   (Comando en consola que en LaTeX se ve como ![equation](https://latex.codecogs.com/gif.latex?%5Ccos%28%5Cphi%29))

g00: tan(r)   (Comando en consola que en LaTeX se ve como![equation](https://latex.codecogs.com/gif.latex?%5Ctan%28r%29))

# Variables

1. Coordenadas Cartesianas:

t,x,y,z (en consola) = ![equation](https://latex.codecogs.com/gif.latex?t%2Cx%2Cy%2Cz) (en LaTeX)


2. Coordenadas Cilíndricas:

t,r,theta,z (en consola) =  ![equation](https://latex.codecogs.com/gif.latex?t%2Cr%2C%5Ctheta%2Cz) (en LaTeX)

3. Coordenadas Esféricas:

t,r,theta,phi (en consola) =  ![equation](https://latex.codecogs.com/gif.latex?t%2Cr%2C%5Ctheta%2C%5Cphi) (en LaTeX)

