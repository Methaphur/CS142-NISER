#!/usr/bin/env python
base = 1.000001
exp = 10**5
counter = 0

def _2logm_exp(base, exp):
    global counter
    if exp == 1:
        return base
    if exp%2 == 0:
         reduced_exp = _2logm_exp(base, exp/2)
         counter += 1
         return reduced_exp*reduced_exp
    else:
        reduced_exp = _2logm_exp(base, (exp-1)/2)
        counter += 2
        return base*reduced_exp*reduced_exp

print(f"val = {_2logm_exp(base, exp)}")
print(f"counter = {counter}")
