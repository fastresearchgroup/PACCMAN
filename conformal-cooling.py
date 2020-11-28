import matplotlib.pyplot as plt

import math
from scipy.integrate import odeint
from scipy.optimize import fsolve
import numpy as np

from scipy.integrate import odeint

heat_coefficient_correlation = input ("Please choose a heat transfer correllation. D for Dittus-Boelter, G for Gnielinski, S for Sieder-Tate: ")
savegraphs = input ("Would you like to save an image of the average cycle temperature graphs? Y for yes, N for no: ")

TC = 15.
#coolant temperature celsius
PP = 980.
#density of plastic part kg/m^3
CP = 1300.
#specific heat capacity of plastic part J/KG*K
LP = 0.001
#half the plastic part thickness m
KM = 16.5
#thermal conductivity of mold 316 steel
W = 0.010
#cooling line pitch distance m
D = 0.005
#cooling line diameter m
LM = 0.004
#distance from cooling line to mold wall
TMelt = 180.
#Part melted temperature
TEject = 64.9
#Part ejection temperature
TCycle = 10.
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
WDV = 0.0009775
#coolant dynamic viscosity when near wall
KC = 0.5918
#thermal conductivity of coolant
PC = 998.2
#coolant density
CC = 4187
#specific heat capacity of coolant
fancye = 0.00015
#average height of pipe surface irregularities (m)
L = 1.15
#coolant line length (m)

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

DF = (1/(-1.8*np.log(((fancye/(3.7*D))**1.11)+(6.9/RE))))**2
#Darcy friction factor
print ("Darcy friction factor:", DF)

if heat_coefficient_correlation == "D":
    chosenNU = (0.023*RE**0.8)*PR**0.4
elif heat_coefficient_correlation == "G":
        chosenNU = ((DF/8)*(RE-1000)*PR)/(1+(12.7*((DF/8)**0.5)*(PR**(2/3)-1)))
elif heat_coefficient_correlation == "S":
        chosenNU = 0.027*(RE**(4/5))*(PR**(1/3))*((DV/WDV)**0.14)
#chosen correlation to Nusselt number

h = (KC/D)* chosenNU
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
y = TM + ((TMO-TM)*math.e**(-x/TConstant)) 
plt.plot(x,y,'r')
plt.axis([0,100,0,35])

if savegraphs == "Y":
	plt.savefig("conformal-cooling.png")
	plt.savefig("conformal-cooling.eps")
	
pdrop = (DF*L/D)*(PC/2)*CVV**2
#coolant pressure drop
print ("coolant pressure drop:", pdrop)
