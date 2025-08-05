#!/usr/bin/env python3
import os
import sys
import re
import math

# standard_g = 9.80665
# radius_earth = 6371.

escape_velocities_kms = {
    "Earth": 11.186,
    "Sun(from_Earth_orbit)": 42.1,
    "Sun": 617.5
}

if __name__ == "__main__":
    print("Compare speed of spaceship with cosmic velocities of Earth, Sun")
    input_txt = input("Enter your spaceship velocity in km/s [or add units like m/s, km/h]\n>>")
    velocity = 0. 
    units_mul = 1.
    try:
        input_data = re.split('(\\d+)', input_txt) # list with at least one element
        units = False

        if len(input_data[-1]) > 0 and input_data[-1][-1] not in '0123456789':
            units = True
            velocity = float(''.join(''.join(input_data[:-1]).split()))
        else:
            velocity = float(''.join(''.join(input_data[:]).split()))

        if units:
            units_str = ''.join(input_data[-1].split()).lower()
            match units_str:
                case 'km/s':
                    units_mul = 1.
                case 'm/s':
                    units_mul = 1e-3
                case 'km/h':
                    units_mul = 1./3600
                case _:
                    print('Default unit km/s used')
        print(f"Input: {velocity:.2g} * units multiplier {units_mul:.2g} = {velocity * units_mul:.2g} km/s")
    except Exception as e:
        print(f"Error in input: {e}, try something like 50 km/s")
        exit()


    for k, v in escape_velocities_kms.items():
        final_velocity = abs(velocity * units_mul)
        if final_velocity >= v:
            print(f'[+ESC] exceeds {v} km/s and is sufficient to escape the {k}')
        else:
            print(f'[-ESC] is less than {v} km/s and is NOT sufficient to escape the {k}')
            if final_velocity * math.sqrt(2.) >= v:
                print(f'[+ORB] exceeds {v}/sqrt2={v/math.sqrt(2.):.2g} km/s and is sufficient to orbit the {k}')
            else:
                print(f'[-ORB] is less than {v}/sqrt2={v/math.sqrt(2.):.2g}  km/s and is NOT sufficient to orbit the {k}')
