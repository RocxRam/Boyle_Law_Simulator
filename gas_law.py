from settings import R

"""Calculates the variables using Ideal Gas Law"""

def calculate_pressure(V,n,T):
    return n*R*T/V

def calculate_volume(P,n,T):
    return n*R*T/P

def calculate_temp(P,V,n):
    return P*V/(n*R)

def calculate_moles(P,V,T):
    return P*V/(R*T)

print(calculate_pressure(1,1,1))




