# Relatividad

Descripción: Programa en Python y documento en LaTeX para obtener un archivo pdf (llamado Cantidades_relativistas.pdf) con las cantidades relevantes de Relatividad General para cierta métrica (Se obtiene el tensor métrico, Símbolos de Christoffel, Tensor de Ricci, Tensor de Einstein, Tensor de estres-energía para un fluido perfecto , las ecuaciones de campo de Einstein, el determinante del tensor métrico, la curvatura Gaussiana, las ecuaciones de la geodésica y el Lagrangiano). Se usa para este caso c=1.

Se puede ejecutar para tres métricas predeterminadas más otra que puede ser introducida manualmente. Las tres métricas predeterminadas son: Minkowski, Schwarchild y FLRW(Friedman-Lemaitre-Robertson-Walker). El modo manual permite dar un nombre a la métrica, seleccionar las coordenadas (Esféricas, Cilíndricas o Cartesianas) e introducir cada componente del tensor métrico. Una métrica recomendada para probar el modo manual es la métrica de Rindler en coordenadas Cartesianas (g_{00}= -x^2, g_{11}=g_{22}=g_{33}= 1). El modo manual permite hacer uso de seis constantes simbólicas c_1.c_2,c_3,c_4,c_5,c_6 para que sean usadas al momento de introducir cada componente del tensor métrico.

Como extra, se ponen dos ejemplos de los archivos pdf resultantes de ejecutar el programa. El ejemplo llamado Ejemplo_FLRW.pdf es para la métrica de FLRW, el ejemplo llamado Ejemplo_Manual_Rindler.pdf es para la métrica de Rindler con el modo manual en coordenadas Cartesianas.

# Pasos para ejecutar:

1. Instalar Sympy y Gravipy:

Para instalar Sympy: sudo pip install sympy
Para instalar Gravipy: sudo pip install gravipy

2. Ejecutar:

Se ejecuta solo con poner make y enter en la consola de Linux (Ejecutando el Makefile).


