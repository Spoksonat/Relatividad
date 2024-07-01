# Generator of Relativistic Equations from the Metric Tensor (Linux)

[![es](https://img.shields.io/badge/lang-es-yellow.svg)](https://github.com/Spoksonat/Relatividad/blob/master/README.md)
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Spoksonat/Relatividad/blob/master/README.en.md)

Generator of relativistic equations and variables using Simpy, which are then saved in a pdf file using a LaTeX template.

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)
  - [Instructions](#instructions)
  - [Variables](#variables)
  - [Execution](#execution)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About the Project

Python program and LaTeX document to obtain a pdf file (called Cantidades_relativistas.pdf) with the relevant quantities of General Relativity for a given metric (Metric tensor, Christoffel symbols, Ricci tensor, Einstein tensor, stress-energy tensor for a perfect fluid, Einstein field equations, metric tensor determinant, Gaussian curvature, geodesic equations, and the Lagrangian). For this case, c=1 is used.

It can be run for three predefined metrics plus another that can be manually entered. The three predefined metrics are: Minkowski, Schwarzschild, and FLRW (Friedman-Lemaitre-Robertson-Walker). The manual mode allows naming the metric, selecting the coordinates (Spherical, Cylindrical, or Cartesian), and entering each component of the metric tensor. A recommended metric to test the manual mode is the Rindler metric in Cartesian coordinates (![equation](https://latex.codecogs.com/gif.latex?g_%7B00%7D%3D%20-x%5E2), ![equation](https://latex.codecogs.com/gif.latex?g_%7B11%7D%3Dg_%7B22%7D%3Dg_%7B33%7D%3D1),![equation](https://latex.codecogs.com/gif.latex?g_%7B%5Cmu%5Cnu%7D%3D0%20%28%5Cmu%5Cneq%20%5Cnu%29)). The manual mode allows using six symbolic constants c_1, c_2, c_3, c_4, c_5, c_6 and eight functions f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8 to be used when entering each component of the metric tensor. The eight functions can depend on any variable, so the variable dependence has to be specified in the console. For example, if you want the 00 component of the metric tensor to be a function of the variable theta in spherical coordinates, then in the console, you enter: Introduce g00: f_1(theta).

As a bonus, two examples of the resulting pdf files from running the program are provided. The example called Ejemplo_FLRW.pdf is for the FLRW metric, and the example called Ejemplo_Manual_Rindler.pdf is for the Rindler metric with manual mode in Cartesian coordinates.

## Getting Started

To get started, you need to follow the installation process:

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Spoksonat/Relatividad.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Relatividad-main
   ```
3. Install Simpy and Gravipy:
   ```sh
   pip install sympy, gravipy 
   ```
4. Install the LaTeX compiler called pdflatex:
   ```sh
   sudo apt-get install texlive-latex-base  
   ```

## Usage

### Instructions

If in manual mode and you want to introduce some known functions into the components of the metric tensor, the way to introduce them is as follows:

1. Exponential:

g00: exp(c_1 * y) (Console command which in LaTeX looks like ![equation](https://latex.codecogs.com/gif.latex?e%5E%7Bc_1y%7D))

2. Powers:

g00: -x**2 (Console command which in LaTeX looks like ![equation](https://latex.codecogs.com/gif.latex?-x%5E2))

3. Trigonometric functions:

g00: sin(theta) (Console command which in LaTeX looks like ![equation](https://latex.codecogs.com/gif.latex?%5Csin%28%5Ctheta%29))

g00: cos(phi) (Console command which in LaTeX looks like ![equation](https://latex.codecogs.com/gif.latex?%5Ccos%28%5Cphi%29))

g00: tan(r) (Console command which in LaTeX looks like ![equation](https://latex.codecogs.com/gif.latex?%5Ctan%28r%29))

### Variables

The coordinate systems (with their respective representative variables) considered for this code are as follows:

1. Cartesian Coordinates:

t, x, y, z (in console) = ![equation](https://latex.codecogs.com/gif.latex?t%2Cx%2Cy%2Cz) (in LaTeX)

2. Cylindrical Coordinates:

t, r, theta, z (in console) = ![equation](https://latex.codecogs.com/gif.latex?t%2Cr%2C%5Ctheta%2Cz) (in LaTeX)

3. Spherical Coordinates:

t, r, theta, phi (in console) = ![equation](https://latex.codecogs.com/gif.latex?t%2Cr%2C%5Ctheta%2C%5Cphi) (in LaTeX)

### Execution

The program runs simply by executing the Makefile:

```sh
make  
```

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. **Any contributions you make are greatly appreciated**.

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

Distributed under the MIT License. See [LICENSE.txt](LICENCE.txt) for more information.

## Contact

Manuel Fernando Sánchez Alarcón - mf.sanchez17@uniandes.edu.co

Project Link: [https://github.com/Spoksonat/Relatividad](https://github.com/Spoksonat/Relatividad)
