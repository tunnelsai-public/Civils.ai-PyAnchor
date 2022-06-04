import numpy as np


# phi is the diameter of the steel thread in mm
# Fyk is the characteristic yield stress of the steel in MPa
class Thread:
    def __init__(self, phi=32, fyk=1050):
        self.phi = phi
        self.fyk = fyk
    def steel_resistance = (Thread.phi**2)/4 * self.fyk * np.pi/1.15

# length is the length of the foundation in mm
# Dd is the drilling diameter in mm
# Fck is the characteristic compressive stress of the grout in MPa
class Foundation:
    def __init__(self, length=4000, dd=40, fck=30):
        self.length = length
        self.dd = dd
        self.fck = fck


# method is the injection method of the grout
# qe is the injection pressure
# soil is the type of soil in which the foundation is grouted
class Grouting:
    def __init_(self, method=1, qe=10, soil=2):
        self.method = method
        self.qe = qe
        self.soil = soil


# Ed is the design force