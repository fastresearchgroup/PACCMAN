#data pulled from: "Analysis of thermal cycling efficiency and optimal design of heating/coolingsystems for rapid heat cycle injection molding process" (2010) by Wang Guilong, Zhao Guoqun, Li Huiping, and Guan Yanjin.

pipetype = "straight"

TC = 20
#coolant temperature celsius
PP = 1059.2
#density of plastic part kg/m^3
CP = 1903
#specific heat capacity of plastic part J/KG*K
LP = 0.003/2
#half the plastic part thickness m
W = 0.015
#cooling line pitch distance m
D = 0.01
#cooling line diameter m
LM = 0.025
#distance from cooling line to mold wall
TMelt = 120
#Part melted temperature
TEject = 104.5
#Part ejection temperature
TCycle = 60
#Cycle time seconds
TMO = 250
#Initial mold temperature
CVV = 0.157
#coolant velocity liters/sec
DV = 9.82*10**-4
#coolant dynamic viscosity
WDV = 0.0009775
#coolant dynamic viscosity when near wall
KC = 0.683
#thermal conductivity of coolant
PC = 926
#coolant density
CC = 4186
#specific heat capacity of coolant
L = 1.15
#coolant line length

moldmatname = "6262 Aluminum" 
#name of first mold material
rho_m = 2810
#First comparison Mold density kg/m^3
Cp_m = 960
#First comparison Mold specific heat
eps = 0.001 * 10**-3
#First comparison average height of pipe surface irregularities (m) 
KM = 130
#First comparison thermal conductivity of mold