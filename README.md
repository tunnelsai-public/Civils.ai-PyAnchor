# PyAnchor
A python package for soil anchor design using the Bustamante &amp; Doix (1985) empirical method. This module allows for the following parameters:
- Specification of a steel ground anchor.
- Calculate the strength of the soil-grout interface resistance.
- Calculate the strength of the steel-grout interface resistance.
- Calculate the strength of the steel anchor.

This module will calculate and return the minimum resistance of the three parameters considered

## Project Purpose
The purpose of this project is to create a free module for calculating ground anchor resistance for integration with retaining wall and ground improvement design software.

## Functionality and usage

A typical use case of the `pyanchorgeo` package involves the following steps:
1. Create an `Anchor` object.
2. Assign a soil class to the Anchor.
3. Assign a grouting specification to the anchor.
4. Calculate the minimum anchor resistance.

### Creating an Anchor

The creation of an `Anchor` involves the input of the following:
- Anchor diameter (mm)
- Hole diameter (mm)
- Anchor length (Andrea?)
- Steel strength (N/mm^2)

By default the following parameters are used for an anchor 20mm, hole diameter 22mm, anchor length 3m and steel strength of 275N/mm^2.

```python
anchor = Anchor(anchor_diameter=22, hole_diameter=24, length=33, steel_strength = 275)
```


### Assigning a soil class

After an `Anchor` Object is created a soil class can be assigned to the anchor by calling the update_soil function and providing a soil class represented by an integer from 1 to 12 which best represents the soil.
0. Gravel
1. Sandy gravel
2.  Gravely sand
3. Coarse sand
4. Medium sand
5. Fine sand
6.  Silty sand
7.  Silt
8.  Clay
9.  Marl
10. Marly limestone
11. Altered or fractured limestone
12. Altered or fractured rock

```python
anchor.update_soil(4)
```

### Assigning a grout class

After an `Anchor` Object is created a grout class can be assigned to the anchor by calling the update_grout function and providing the following parameters:
- Grout strength (N/mm^2)
- Grout pressure (kPa)
- Grouting method represented by an integer:
    0. Multiple high pressure injection
    1. Single low pressure injection

```python
anchor.update_grout(grout_strength=55, pressure=60, grout_method=1)
```

### Calculating the minimum resistance

To analyse the `Anchor` the calculate_worst_resistance() method is called.

```python
print(anchor.calculate_worst_resistance())
```


## Installing the package

If you want to install the `pyanchorgeo` package, you run this one-liner:

```shell
pip install pyanchorgeo
```

> **NOTE**: You need Python 3 to install this package (you may need to write `pip3` instead of `pip`).

The library dependencies are listed in the file `requirements.txt`, but you only need to look at them if you clone the repository.
If you install the package via `pip`, the listed dependencies should be installed automatically.

## License

https://github.com/tunnelsai-public/PyAnchor/blob/main/LICENSE
