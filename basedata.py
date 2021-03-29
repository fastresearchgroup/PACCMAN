#Example of possible input data

TC = 15.
#coolant temperature celsius
PP = 980.
#density of plastic part kg/m^3
CP = 1300.
#specific heat capacity of plastic part J/KG*K
LP = 0.001
#half the plastic part thickness m
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
L = 1.15
#coolant line length

moldmatname1 = "316 Steel" 
#name of first mold material
moldmatname2 = "6061 Aluminum"
#name of second mold material
moldmatname3 = "Copper"
#name of third mold material
mat1PM = 7930.
#First comparison Mold density kg/m^3: 316 steel
mat2PM = 2700
#Second comparison Mold density kg/m^3: aluminum 6061
mat3PM = 8960
#Third comparison Mold density kg/m^3: copper
mat1CM = 510.
#First comparison Mold specific heat 316 steel
mat2CM = 896
#Second comparison Mold specific heat aluminum
mat3CM = 380
#Third comparison Mold specific heat copper
mat1fancye = 0.00015
#First comparison average height of pipe surface irregularities (m) 316 steel
mat2fancye =  0.000001
#Second comparison average height of pipe surface irregularities (m) aluminum
mat3fancye = 0.000001
#Third comparison average height of pipe surface irregularities (m) copper
mat1KM = 16.5
#First comparison thermal conductivity of mold: 316 steel
mat2KM = 180
#Second comparison thermal conductivity of mold: aluminum 6061
mat3KM = 402
#Third comparison thermal conductivity of mold: copper