import sys
from unittest import result
sys.path.append(".")

from PyAnchor import Anchor

def test_minimum_resistance():

    anchor = Anchor(
    anchor_diameter=30,
    hole_diameter=32,
    length=4,
    )
    anchor.update_soil(8)
    anchor.calculate_alpha_d()
    anchor.update_load(100)
    resistance = anchor.calculate_worst_resistance()

    result = is_positive_number(resistance[0])
    assert(result)


def is_positive_number(number):
    if number>=0:
        result=True
    else:
        result=False
    return result
