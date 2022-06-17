import numpy as np


class Anchor:
    # A default anchor will be created which is 20mm diameter, in a 22mm hole, 3m in length with a steel strength of 275N/mm2
    # Andrea, to update these parameters, see my example at the bottom of the code.
    def __init__(self, anchor_diameter= 20, hole_diameter=22, length= 3, steel_strength=275, ):
        self.anchor_diameter = anchor_diameter
        self.length = length
        self.steel_strength = steel_strength 
        self.hole_diameter = hole_diameter
        self.soil_type = 8
        self.grout_stength = 55
        self.pressure = 55

        self.grout_method = 1
        self.design_load = 0


    def update_soil(self, soil_type,):
        #In which kind of soil is the foundation? 
        # 0 - Gravel 
        # 1 - Sandy gravel 
        # 2 -  Gravely sand 
        # 3 - Coarse sand 
        # 4 -  Medium sand 
        # 5 - Fine sand
        # 6 -  Silty sand
        # 7 -  Silt
        # 8 -  Clay
        # 9 -  Marl
        # 10 - Marly limestone
        # 11 - Altered or fractured limestone
        # 12 - Altered or fractured rock
        self.soil_type = soil_type


    def update_grout(self, grout_stength, pressure, grout_method):
        # For grout method:
        # 0 - Multiple high pressure injection
        # 1 - Single low pressure injection 
        self.grout_stength = grout_stength
        self.pressure = pressure
        self.grout_method = grout_method


    def update_load(self, design_load):
        self.design_load = design_load

    def calculate_worst_resistance(self):
        # Table from Bustamante & Doix
        Alpha = np.array([[1.8, 1.6, 1.5, 1.4, 1.4, 1.4, 1.4, 1.4, 1.8, 1.8, 1.8, 1.8, 1.2],
                        [1.3, 1.2, 1.2, 1.1, 1.1, 1.1, 1.5, 1.1, 1.2, 1.1, 1.1, 1.1, 1.1]])
        alfa_d = (Alpha[[self.grout_method], [self.soil_type]])  # Choice of the value from table
        A_s = np.pi * (self.anchor_diameter / 2) ** 2  # Area of the steel section
        D_s = alfa_d * self.hole_diameter  # Corrected diameter of the foundation
        # Determination of fctk
        if self.grout_stength < 50:
            f_ctk = 0.7 * self.grout_stength ** (2 / 3)
        else:
            f_ctk = 2.12 * np.log(1+(self.grout_stength+8/10))
        # Determination of q_s
        if self.soil_type < 6:  # Incoherent soils
            if self.grout_method == 0:
                q_s = 1.0188 * self.pressure + 0.0541
            else:
                q_s = 1.0099 * self.pressure + 0.0041
        elif self.soil_type < 8:  # Fine grained soils
            if self.grout_method == 0:
                if self.pressure < 1:
                    q_s = -0.1307 * (self.pressure ** 2) + 0.302 * self.pressure + 0.0117
                else:
                    q_s = 0.08 * self.pressure + 0.103
            else:
                if self.pressure < 1:
                    q_s = -0.0693 * (self.pressure ** 2) + 0.17 * self.pressure - 0.0007
                else:
                    q_s = 0.0552 * self.pressure + 0.0448
        elif self.soil_type < 10:  # Marl and limestone
            if self.grout_method == 0:
                q_s = 0.07 * self.pressure + 0.14
            else:
                q_s = 0.0493 * self.pressure + 0.1157
        else:  # Fractured rock
            if self.grout_method == 0:
                q_s = 0.1227 * self.pressure + 0.066
            else:
                q_s = 0.0973 * self.pressure + 0.064

        if self.anchor_diameter < 32:
            eta = 1
        elif self.anchor_diameter == 32:
            eta = 1
        else:
            eta = (132 - self.anchor_diameter) / 100

        t_d = 2.25 * eta * f_ctk / 1.5

        # Slip resistance at the interface soil-grout
        slip_resistance_soil_grout = np.pi * D_s * self.length * q_s / 1000


        print('Soil-grout resistance: ' + str(format(float(slip_resistance_soil_grout), '.2f')) + ' kN')

        # Tension resistance of the steel anchor
        tension_resistance = self.steel_strength * A_s / (1.15 * 1000)
        print('Steel resistance: ' + str(format(float(tension_resistance), '.2f')) + ' kN')

        # Slip resistance at the interface steel-grout
        slip_resistance_steel_grout = np.pi * self.anchor_diameter * t_d * self.length / 1000
        print('Steel-grout resistance: ' + str(format(float(slip_resistance_steel_grout), '.2f')) + ' kN')
        return min(slip_resistance_soil_grout, tension_resistance, slip_resistance_steel_grout) 



# Andrea, here creating a new object called 'test' and setting the call of this object as an anchor.
# I'm updating the diameter as 30mm and the hole size as 32mm and the length of 4m.
test = Anchor(anchor_diameter= 30, hole_diameter=32, length= 4,)
test.update_soil(8)
test.update_load(100)
result = test.calculate_worst_resistance()
print(result)