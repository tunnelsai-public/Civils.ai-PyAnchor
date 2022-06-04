

# ---Import section---

import numpy as np

#  ---Input section---
# testing update


E_d = int(input('Design force in N: '))
phi = int(input('Diameter of the anchor in mm: '))
D_d = 0
while D_d < phi + 10:
    D_d = int(input('Drilling diameter in mm: '))
    if D_d < phi + 10:
        print('the drilling diameter is too small. At least 10 mm more than the anchor '
              'diameter have to be set to inject the grout.')
L = int(input('Length of the foundation in mm: '))
q_e = float(input('Menard limit pressure in MPa: '))
F_yk = int(input('Characteristic yield stress of steel in MPa: '))
F_ck = int(input('Characteristic compressive strength of the foundation grout in MPa: '))
i = int(input("In which kind of soil is the foundation? \n0. Gravel \n1. Sandy gravel \n2.  Gravely sand \n3.  "
              "Coarse sand \n4.  Medium sand \n5.  Fine sand \n6.  Silty sand \n7.  Silt \n8.  Clay \n9.  Marl \n"
              "10. Marly limestone \n11. Altered or fractured limestone \n12. Altered or fractured rock \n"))

j = int(input("Which method of grouting is used? \n"
              "0. Multiple high pressure injection \n1. Single low pressure injection \n"))

#  ---Computing section---

# Table from Bustamante & Doix
Alpha = np.array([[1.8, 1.6, 1.5, 1.4, 1.4, 1.4, 1.4, 1.4, 1.8, 1.8, 1.8, 1.8, 1.2],
                  [1.3, 1.2, 1.2, 1.1, 1.1, 1.1, 1.5, 1.1, 1.2, 1.1, 1.1, 1.1, 1.1]])
alfa_d = (Alpha[[j], [i]])  # Choice of the value from table
A_s = np.pi * (phi / 2) ** 2  # Area of the steel section
D_s = alfa_d * D_d  # Corrected diameter of the foundation
# Determination of fctk
if F_ck < 50:
    f_ctk = 0.7 * F_ck ** (2 / 3)
else:
    f_ctk = 2.12 * np.log(1+(F_ck+8/10))
# Determination of q_s
if i < 6:  # Incoherent soils
    if j == 0:
        q_s = 1.0188 * q_e + 0.0541
    else:
        q_s = 1.0099 * q_e + 0.0041
elif i < 8:  # Fine grained soils
    if j == 0:
        if q_e < 1:
            q_s = -0.1307 * (q_e ** 2) + 0.302 * q_e + 0.0117
        else:
            q_s = 0.08 * q_e + 0.103
    else:
        if q_e < 1:
            q_s = -0.0693 * (q_e ** 2) + 0.17 * q_e - 0.0007
        else:
            q_s = 0.0552 * q_e + 0.0448
elif i < 10:  # Marl and limestone
    if j == 0:
        q_s = 0.07 * q_e + 0.14
    else:
        q_s = 0.0493 * q_e + 0.1157
else:  # Fractured rock
    if j == 0:
        q_s = 0.1227 * q_e + 0.066
    else:
        q_s = 0.0973 * q_e + 0.064

if phi < 32:
    eta = 1
elif phi == 32:
    eta = 1
else:
    eta = (132 - phi) / 100

t_d = 2.25 * eta * f_ctk / 1.5  # Adherence bond between steel and grout

#  ---Results printer---

print()
print('RESULTS')
print()
E_D = E_d / 1000
print('E_d: ' + str(format(float(E_D), '.2f')) + ' kN')
# Slip resistance at the interface soil-foundation
R_ac = np.pi * D_s * L * q_s / 1000
print('R_ac: ' + str(format(float(R_ac), '.2f')) + ' kN')
# Traction resistance of the steel anchor
R_tc = F_yk * A_s / (1.15 * 1000)
print('R_tc: ' + str(format(float(R_tc), '.2f')) + ' kN')
# Slip resistance at the interface steel-foundation
N_u = np.pi * phi * t_d * L / 1000
print('N_u: ' + str(format(float(N_u), '.2f')) + ' kN')
# Hierarchy of resistances check
if R_tc < min(R_ac, N_u):
    print('Hierarchy of resistances not verified. N_u or R_ac cannot be lower than R_tc.')
elif E_D < min(R_ac, N_u, R_tc):
    print('All the requirements are satisfied')
else:
    print('Not satisfied')
