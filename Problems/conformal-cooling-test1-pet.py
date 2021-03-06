import matplotlib.pyplot as plt

import math
from scipy.integrate import odeint
from scipy.optimize import fsolve
import numpy as np

from scipy.integrate import odeint

TC = 35.
#coolant temperature celsius
PP = 1400.
#density of plastic part kg/m^3
CP = 1000.
#specific heat capacity of plastic part J/KG*K
LP = 0.004
#half the plastic part thickness m
KM = 44.5
#thermal conductivity of mold
W = 0.010
#cooling line pitch distance m
D = 0.005
#cooling line diameter m
LM = 0.004
#distance from cooling line to mold wall
TMelt = 300.
#Part melted temperature
TEject = 100
#Part ejection temperature
TCycle = 60.
#Cycle time seconds
PM = 7930.
#Mold density kg/m^3
CM = 510.
#Mold specific heat
TMO = 13.
#Initial mold temperature
CVV = 0.227
#coolant velocity liters/sec
DV = 1.002 * 10**-3
#coolant dynamic viscosity
KC = 0.5918
#thermal conductivity of coolant
PC = 998.2
#coolant density
CC = 4187
#specific heat capacity of coolant

FV = (CVV*0.001)/(np.pi*(D/2)**2)
#flow velocity of coolant m/s
print ("flow velocity:", FV)

KV = DV/PC
#coolant kinematic viscosity
print ("kinematic viscosity:", KV)

RE = FV*D/KV
#Reynolds number of coolant
print ("Reynolds number:", RE)

PR = DV*CC/KC
#Prandl number of coolant
print ("Prandl number:", PR)

h = (KC/D)*(0.023*RE**0.8)*PR**0.4
#Heat transfer coefficient
print ("heat transfer coefficient:", h)

TM = PP*CP*LP*(2.0*KM*W + h*D*LM*np.pi)*(TMelt - TEject)
TM = TM/(h*D*KM*TCycle*np.pi)
TM = TM + TC
#Temperature of the mold
print ("temperature of the mold:", TM)

TConstant = ((PM*CM*LM**2)/KM)*(1+(2.0*W*KM)/(h*D*LM*np.pi))
#Time constant
print ("time constant:", TConstant)

x = np.linspace(0,100)
y = TM + ((TMO-TM)*np.e**(-x/TConstant))
plt.plot(x,y,'r')
plt.axis([0,100,0,100])
plt.savefig("conformal-cooling-pet.png")
plt.savefig("conformal-cooling-pet.eps")