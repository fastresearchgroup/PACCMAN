#Example of possible input data

TC = 60
#coolant temperature celsius
PP = 900
#density of plastic part kg/m^3
CP = 3079
#specific heat capacity of plastic part J/KG*K
LP = 0.001
#half the plastic part thickness m
W = 0.004
#cooling line pitch distance m
D = 0.0045
#cooling line diameter m
LM = 0.003
#distance from cooling line to mold wall
TMelt = 215
#Part melted temperature
TEject = 104
#Part ejection temperature
TCycle = 30
#Cycle time seconds
TMO = 30
#Initial mold temperature
CVV = 0.07
#coolant velocity liters/sec
DV = 4.75*10**-4
#coolant dynamic viscosity
WDV = 0.0009775
#coolant dynamic viscosity when near wall
KC = 0.5797
#thermal conductivity of coolant
PC = 993
#coolant density
CC = 4187
#specific heat capacity of coolant
L = 1.508
#coolant line length

moldmatname1 = "316 Steel" 
#name of first mold material
moldmatname2 = "6061 Aluminum"
#name of second mold material
moldmatname3 = "Copper"
#name of third mold material
mat1PM = 7750.
#First comparison Mold density kg/m^3: 316 steel
mat2PM = 2700
#Second comparison Mold density kg/m^3: aluminum 6061
mat3PM = 8960
#Third comparison Mold density kg/m^3: copper
mat1CM = 440
#First comparison Mold specific heat 316 steel
mat2CM = 896
#Second comparison Mold specific heat aluminum
mat3CM = 380
#Third comparison Mold specific heat copper
mat1fancye = 65*10**-6
#First comparison average height of pipe surface irregularities (m) 316 steel
mat2fancye =  0.000001
#Second comparison average height of pipe surface irregularities (m) aluminum
mat3fancye = 0.000001
#Third comparison average height of pipe surface irregularities (m) copper
mat1KM = 20
#First comparison thermal conductivity of mold: 316 steel
mat2KM = 180
#Second comparison thermal conductivity of mold: aluminum 6061
mat3KM = 402
#Third comparison thermal conductivity of mold: copper