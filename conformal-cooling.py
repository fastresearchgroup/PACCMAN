import matplotlib.pyplot as plt


import math
import numpy as np

programfunction = input('What would you like to use this program for? M for mold material comparison, H for heat transfer coefficient comparison, N for simple data from a single mold material and user choice of heat transfer coefficient: ' )


if programfunction == "N" or programfunction == "n": 
    heat_coefficient_correlation = input("Please choose a heat transfer correllation. D for Dittus-Boelter, G for Gnielinski, S for Sieder-Tate: ")

savegraphs = input ("Would you like to save an image of the graphs? Y for yes, N for no: ")



#general note: when programfunction = N or H, the first choice of mold material properties is used (KM1, PM1, etc.)

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
PM1 = 7930.
#First comparison Mold density kg/m^3: 316 steel
PM2 = 2700
#Second comparison Mold density kg/m^3: aluminum 6061
PM3 = 8960
#Third comparison Mold density kg/m^3: copper
CM1 = 510.
#First comparison Mold specific heat 316 steel
CM2 = 896
#Second comparison Mold specific heat aluminum
CM3 = 380
#Third comparison Mold specific heat copper
fancye1 = 0.00015
#First comparison average height of pipe surface irregularities (m) 316 steel
fancye2 =  0.000001
#Second comparison average height of pipe surface irregularities (m) aluminum
fancye3 = 0.000001
#Third comparison average height of pipe surface irregularities (m) copper
KM1 = 16.5
#First comparison thermal conductivity of mold: 316 steel
KM2 = 180
#Second comparison thermal conductivity of mold: aluminum 6061
KM3 = 402
#Third comparison thermal conductivity of mold: copper




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





DF1 = (1/(-1.8*np.log(((fancye1/(3.7*D))**1.11)+(6.9/RE))))**2

DF2 = (1/(-1.8*np.log(((fancye2/(3.7*D))**1.11)+(6.9/RE))))**2

DF3 = (1/(-1.8*np.log(((fancye3/(3.7*D))**1.11)+(6.9/RE))))**2
#Darcy friction factor





print ("Darcy friction factor (",moldmatname1,"):", DF1)

if programfunction == "M" or programfunction == "m":
    print ("Darcy friction factor (",moldmatname2,"):", DF2)
    print ("Darcy friction factor (",moldmatname3,"):", DF3)





if programfunction == "N" or programfunction == "n":
    if heat_coefficient_correlation == "D":
        chosenNU1 = (0.023*RE**0.8)*PR**0.4
    elif heat_coefficient_correlation == "G":
        chosenNU1 = ((DF1/8)*(RE-1000)*PR)/(1+(12.7*((DF1/8)**0.5)*(PR**(2/3)-1)))
    elif heat_coefficient_correlation == "S":
        chosenNU1 = 0.027*(RE**(4/5))*(PR**(1/3))*((DV/WDV)**0.14)
elif programfunction == "M" or programfunction == "m":
    chosenNU1 = ((DF1/8)*(RE-1000)*PR)/(1+(12.7*((DF1/8)**0.5)*(PR**(2/3)-1)))
    chosenNU2 = ((DF2/8)*(RE-1000)*PR)/(1+(12.7*((DF2/8)**0.5)*(PR**(2/3)-1)))
    chosenNU3 = ((DF3/8)*(RE-1000)*PR)/(1+(12.7*((DF3/8)**0.5)*(PR**(2/3)-1)))
elif programfunction == "H" or programfunction == "h":
    chosenNU1 = (0.023*RE**0.8)*PR**0.4
    chosenNU2 = ((DF1/8)*(RE-1000)*PR)/(1+(12.7*((DF1/8)**0.5)*(PR**(2/3)-1)))
    chosenNU3 = 0.027*(RE**(4/5))*(PR**(1/3))*((DV/WDV)**0.14)
else: 
    print ("false")
#chosen correlation to Nusselt number



h1 = (KC/D)* chosenNU1

if programfunction == "M" or programfunction == "m" or programfunction == "H" or programfunction == "h":
    h2 = (KC/D)* chosenNU2
    h3 = (KC/D)* chosenNU3
#Heat transfer coefficient



if programfunction == "M" or programfunction == "m": 
    print ("heat transfer coefficient (",moldmatname1,"):", h1)
    print ("heat transfer coefficient (",moldmatname2,"):", h2)
    print ("heat transfer coefficient (",moldmatname3,"):", h3)
elif programfunction == "H" or programfunction == "h":
    print ("heat transfer coefficient (Ditus-Boelter):", h1)
    print ("heat transfer coefficient (Gnielinski):", h2)
    print ("heat transfer coefficient (Sieder-Tate):", h3)
elif programfunction == "N" or programfunction == "n":
    print ("heat transfer coefficient", h1)



if programfunction == "M" or programfunction == "m": 
    ATM1 = PP*CP*LP*(2.0*KM1*W + h1*D*LM*np.pi)*(TMelt - TEject)
    ATM2 = PP*CP*LP*(2.0*KM2*W + h2*D*LM*np.pi)*(TMelt - TEject)
    ATM3 = PP*CP*LP*(2.0*KM3*W + h3*D*LM*np.pi)*(TMelt - TEject)
    
    ATM1 = ATM1/(h1*D*KM1*TCycle*np.pi)
    ATM2 = ATM2/(h2*D*KM2*TCycle*np.pi)
    ATM3 = ATM3/(h3*D*KM3*TCycle*np.pi)
    
    ATM1 = ATM1 + TC
    ATM2 = ATM2 + TC
    ATM3 = ATM3 + TC
    
    print ("temperature of the mold (",moldmatname1,"):", ATM1)
    print ("temperature of the mold (",moldmatname2,"):", ATM2)
    print ("temperature of the mold (",moldmatname3,"):", ATM3)
elif programfunction == "H" or programfunction == "h":
    ATM1 = PP*CP*LP*(2.0*KM1*W + h1*D*LM*np.pi)*(TMelt - TEject)
    ATM2 = PP*CP*LP*(2.0*KM1*W + h2*D*LM*np.pi)*(TMelt - TEject)
    ATM3 = PP*CP*LP*(2.0*KM1*W + h3*D*LM*np.pi)*(TMelt - TEject)
    
    ATM1 = ATM1/(h1*D*KM1*TCycle*np.pi) + TC
    ATM2 = ATM2/(h2*D*KM1*TCycle*np.pi) + TC
    ATM3 = ATM3/(h3*D*KM1*TCycle*np.pi) + TC
    
    print ("temperature of the mold (Ditus-Boelter):", ATM1)
    print ("temperature of the mold (Gnielinski):", ATM2)
    print ("temperature of the mold (Sieder-Tate):", ATM3)
elif programfunction == "N" or programfunction == "n":
    ATM1 = PP*CP*LP*(2.0*KM1*W + h1*D*LM*np.pi)*(TMelt - TEject)
    
    ATM1 = ATM1/(h1*D*KM1*TCycle*np.pi)
    
    ATM1 = ATM1 + TC
    
    print ("temperature of the mold:", ATM1)
#Average temperature of the mold



if programfunction == "M" or programfunction == "m":
    TConstant1 = ((PM1*CM1*LM**2)/KM1)*(1+(2.0*W*KM1)/(h1*D*LM*np.pi))
    TConstant2 = ((PM2*CM2*LM**2)/KM2)*(1+(2.0*W*KM2)/(h2*D*LM*np.pi))
    TConstant3 = ((PM3*CM3*LM**2)/KM3)*(1+(2.0*W*KM3)/(h3*D*LM*np.pi))
elif programfunction == "H" or programfunction == "h":
    TConstant1 = ((PM1*CM1*LM**2)/KM1)*(1+(2.0*W*KM1)/(h1*D*LM*np.pi))
    TConstant2 = ((PM1*CM1*LM**2)/KM1)*(1+(2.0*W*KM1)/(h2*D*LM*np.pi))
    TConstant3 = ((PM1*CM1*LM**2)/KM1)*(1+(2.0*W*KM1)/(h3*D*LM*np.pi))
elif programfunction == "N" or programfunction == "n":
    TConstant1 = ((PM1*CM1*LM**2)/KM1)*(1+(2.0*W*KM1)/(h1*D*LM*np.pi))

if programfunction == "M" or programfunction == "m": 
    print ("time constant (",moldmatname1,"):", TConstant1)
    print ("time constant (",moldmatname2,"):", TConstant2)
    print ("time constant (",moldmatname3,"):", TConstant3)
elif programfunction == "H" or programfunction == "h":
    print ("time constant (Ditus-Boelter):", TConstant1)
    print ("time constant (Gnielinski):", TConstant2)
    print ("time constant (Sieder-Tate):", TConstant3)
elif programfunction == "N" or programfunction == "n":
    print ("time constant", TConstant1)
#Time constant




x = np.linspace(0,100)




y1 = ATM1 + ((TMO-ATM1)*np.e**(-x/TConstant1))
if programfunction == "M" or programfunction == "m" or programfunction == "H" or programfunction == "h":
    y2 = ATM2 + ((TMO-ATM2)*np.e**(-x/TConstant2))
if programfunction == "M" or programfunction == "m" or programfunction == "H" or programfunction == "h":
    y3 = ATM3 + ((TMO-ATM3)*np.e**(-x/TConstant3))




if programfunction == "M" or programfunction == "m":
    plt.plot(x,y1,'r', ls=('dotted'), label=moldmatname1)
    plt.plot(x,y2,'black', ls=('dotted'), label=moldmatname2)
    plt.plot(x,y3,'b', ls=('dotted'), label=moldmatname3)

elif programfunction == "H" or programfunction == "h":
    plt.plot(x,y1,'r', ls=('dotted'), label='Ditus-Boelter')
    plt.plot(x,y2,'black', ls=('dotted'), label='Gnielinski')
    plt.plot(x,y3,'b', ls=('dotted'), label='Sieder-Tate')
elif programfunction == "N" or programfunction == "n":
    plt.plot(x,y1,'r', ls=('dotted'), label=moldmatname1)
    
plt.axis([0,25,13,20])
plt.xlabel("Time (s) from beginning of heat cycling")
plt.ylabel("Average heat cycle temperature (C)")
plt.grid('both')
plt.legend()




if savegraphs == "Y" or savegraphs == "y":
    plt.savefig("conformal-cooling-comparison.png")
    plt.savefig("conformal-cooling-comparison.eps")




if programfunction == "M" or programfunction == "m":
    pdrop1 = (DF1*L/D)*(PC/2)*CVV**2
    print ("coolant pressure drop (",moldmatname1,"):", pdrop1)
    pdrop2 = (DF2*L/D)*(PC/2)*CVV**2
    print ("coolant pressure drop (",moldmatname2,"):", pdrop2)
    pdrop3 = (DF3*L/D)*(PC/2)*CVV**2
    print ("coolant pressure drop (",moldmatname3,"):", pdrop3)
elif programfunction == "H" or programfunction == "h" or programfunction == "N" or programfunction == "n":
    pdrop1 = (DF1*L/D)*(PC/2)*CVV**2
    print ("coolant pressure drop:", pdrop1)

#coolant pressure drop




#unit testing:
#def testATM1():
	#global ATM1
	#ATM1Test = ATM1
	#ATM1 = PP*CP*LP*(2.0*KM1*W + h1*D*LM*np.pi)*(TMelt - TEject)
	#ATM1 = (ATM1/(h1*D*KM1*TCycle*np.pi)) + TC
	#assert ATM1Test == ATM1
#def testATM2():
	#global ATM2
	#ATM2Test = ATM2
	#ATM2 = PP*CP*LP*(2.0*KM2*W + h2*D*LM*np.pi)*(TMelt - TEject)
	#ATM2 = (ATM2/(h2*D*KM2*TCycle*np.pi)) + TC
#	assert ATM2Test == ATM2
#def testATM3():
	#global ATM3
	#ATM3Test = ATM3
	#ATM3 = PP*CP*LP*(2.0*KM3*W + h3*D*LM*np.pi)*(TMelt - TEject)
	#ATM3 = (ATM3/(h3*D*KM3*TCycle*np.pi)) + TC
	#assert ATM3Test == ATM3
#testATM1()
#testATM2()
#testATM3()