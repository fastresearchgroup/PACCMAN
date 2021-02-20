import matplotlib.pyplot as plt
import numpy as np

programfunction = input('What would you like to use this program for? M for mold material comparison, H for heat transfer coefficient comparison, N for simple data from a single mold material and user choice of heat transfer coefficient, T for initializing unit testing: ' )


if programfunction == "N" or programfunction == "n": 
    heat_coefficient_correlation = input("Please choose a heat transfer correllation. D for Dittus-Boelter, G for Gnielinski, S for Sieder-Tate: ")





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

def FVfunc(CVV, D): 
	FV = (CVV*0.001)/(np.pi*(D/2)**2)
	return FV
#flow velocity of coolant m/s

def KVfunc(DV,PC):
	KV = DV/PC
	return KV
#coolant kinematic viscosity

def REfunc(FV,D,KV):
	RE = FV*D/KV
	return RE
#Reynolds number of coolant

def PRfunc(DV,CC,KC):
	PR = DV*CC/KC
	return PR
#Prandl number of coolant

def DFfunc(fancye,D,RE):
	DF = (1/(-1.8*np.log(((fancye/(3.7*D))**1.11)+(6.9/RE))))**2
	return DF
#Darcy friction factor

def DBNU(RE,PR):
	NU = (0.023*RE**0.8)*PR**0.4
	return NU
def GNU(DF,RE,PR):
	NU = ((DF/8)*(RE-1000)*PR)/(1+(12.7*((DF/8)**0.5)*(PR**(2/3)-1)))
	return NU
def STNU(RE,PR,DV,WDV):
	NU = 0.027*(RE**(4/5))*(PR**(1/3))*((DV/WDV)**0.14)
	return NU
	
def htc(KC,D,NU):
	h = (KC/D)* NU
	return h
#Heat transfer coefficient

def ATMfunc(PP,CP,LP,KM,W,h,D,LM,TMelt,TEject,TCycle,TC):
	ATM = PP*CP*LP*(2.0*KM*W + h*D*LM*np.pi)*(TMelt - TEject)
	ATM = ATM/(h*D*KM*TCycle*np.pi) + TC
	return ATM
	
def TConstantfunc(PM,CM,LM,KM,W,h,D):
	TConstant = ((PM*CM*LM**2)/KM)*(1+(2.0*W*KM)/(h*D*LM*np.pi))
	return TConstant
		
def pdropfunc(DF,L,D,PC,CVV):
	pdrop = (DF*L/D)*(PC/2)*CVV**2
	return pdrop

	
if programfunction == "M" or programfunction == "m" or programfunction == "N" or programfunction == "n" or programfunction == "H" or programfunction == "h":
	savegraphs = input ("Would you like to save an image of the graphs? Y for yes, N for no: ")

	FV = FVfunc(CVV, D)
	print ("flow velocity:", FV)

	KV = KVfunc(DV,PC)
	print ("kinematic viscosity:", KV)

	RE = REfunc(FV,D,KV)
	print ("Reynolds number:", RE)

	PR = PRfunc(DV,CC,KC)
	print ("Prandl number:", PR)

	DF1 = DFfunc(mat1fancye,D,RE)
	print ("Darcy friction factor (",moldmatname1,"):", DF1)

	if programfunction == "M" or "m":
		DF2 = DFfunc(mat2fancye,D,RE)
		print ("Darcy friction factor (",moldmatname2,"):", DF2)
	if programfunction == "M" or "m":
		DF3 = DFfunc(mat3fancye,D,RE)   
		print ("Darcy friction factor (",moldmatname3,"):", DF3)
   
   
	if programfunction == "M" or "m": 
		h1 = htc(KC,D,GNU(DF1,RE,PR))
		print ("heat transfer coefficient (",moldmatname1,"):", h1)
		h2 = htc(KC,D,GNU(DF2,RE,PR))
		print ("heat transfer coefficient (",moldmatname2,"):", h2)
		h3 = htc(KC,D,GNU(DF3,RE,PR))
		print ("heat transfer coefficient (",moldmatname3,"):", h3)

		
	elif programfunction == "H" or "h":
		h1 = htc(KC,D,DBNU(RE,PR))
		print ("heat transfer coefficient (Ditus-Boelter):", h1)
		h2 = htc(KC,D,GNU(DF1,RE,PR))
		print ("heat transfer coefficient (Gnielinski):", h2)
		h3 = htc(KC,D,STNU(RE,PR,DV,WDV))
		print ("heat transfer coefficient (Sieder-Tate):", h3)
	
	
	elif programfunction == "N" or "n":
		if heat_coefficient_correlation == "D":
			h1 = htc(KC,D,DBNU(RE,PR))
			print ("heat transfer coefficient", h1)
		elif heat_coefficient_correlation == "G":
			h2 = htc(KC,D,GNU(DF1,RE,PR))
			print ("heat transfer coefficient", h2)
		elif heat_coefficient_correlation == "S":
			h3 = htc(KC,D,DBNU(RE,PR,DV,WDV))
			print ("heat transfer coefficient", h3)
	

	if programfunction == "M" or "m": 
		ATM1 = ATMfunc(PP,CP,LP,mat1KM,W,h1,D,LM,TMelt,TEject,TCycle,TC)
		print ("temperature of the mold (",moldmatname1,"):", ATM1)
		ATM2 = ATMfunc(PP,CP,LP,mat2KM,W,h2,D,LM,TMelt,TEject,TCycle,TC)
		print ("temperature of the mold (",moldmatname2,"):", ATM2)
		ATM3 = ATMfunc(PP,CP,LP,mat3KM,W,h3,D,LM,TMelt,TEject,TCycle,TC)
		print ("temperature of the mold (",moldmatname3,"):", ATM3)

		
	elif programfunction == "H" or "h":
		ATM1 = ATMfunc(PP,CP,LP,mat1KM,W,h1,D,LM,TMelt,TEject,TCycle,TC)
		print ("temperature of the mold (Ditus-Boelter):", ATM1)
		ATM2 = ATMfunc(PP,CP,LP,mat1KM,W,h2,D,LM,TMelt,TEject,TCycle,TC)
		print ("temperature of the mold (Gnielinski):", ATM2)
		ATM3 = ATMfunc(PP,CP,LP,mat1KM,W,h3,D,LM,TMelt,TEject,TCycle,TC)
		print ("temperature of the mold (Sieder-Tate):", ATM3)
    
	
	elif programfunction == "N" or "n":
		ATM1 = ATMfunc(PP,CP,LP,mat1KM,W,h1,D,LM,TMelt,TEject,TCycle,TC)
		print ("temperature of the mold:", ATM1)
	#Average temperature of the mold
	

	if programfunction == "M" or "m":
		TConstant1 = TConstantfunc(mat1PM,mat1CM,LM,mat1KM,W,h1,D)
		TConstant2 = TConstantfunc(mat2PM,mat2CM,LM,mat2KM,W,h2,D)
		TConstant3 = TConstantfunc(mat3PM,mat3CM,LM,mat3KM,W,h3,D)
		print ("time constant (",moldmatname1,"):", TConstant1)
		print ("time constant (",moldmatname2,"):", TConstant2)
		print ("time constant (",moldmatname3,"):", TConstant3)
		
	elif programfunction == "H" or "h":
		TConstant1 = TConstantfunc(mat1PM,mat1CM,LM,mat1KM,W,h1,D)
		TConstant2 = TConstantfunc(mat1PM,mat1CM,LM,mat1KM,W,h2,D)
		TConstant3 = TConstantfunc(mat1PM,mat1CM,LM,mat1KM,W,h3,D)
		print ("time constant (Ditus-Boelter):", TConstant1)
		print ("time constant (Gnielinski):", TConstant2)
		print ("time constant (Sieder-Tate):", TConstant3)
		
	elif programfunction == "N" or "n":
		TConstant1 = TConstantfunc(mat1PM,mat1CM,LM,mat1KM,W,h1,D)
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

	if programfunction == "M" or "m":
		pdrop1 = pdropfunc(DF1,L,D,PC,CVV)
		pdrop2 = pdropfunc(DF2,L,D,PC,CVV)
		pdrop3 = pdropfunc(DF3,L,D,PC,CVV)

		print ("coolant pressure drop (",moldmatname1,"):", pdrop1)
		print ("coolant pressure drop (",moldmatname2,"):", pdrop2)
		print ("coolant pressure drop (",moldmatname3,"):", pdrop3)

	elif programfunction == "H" or "h" or "N" or "n":
		pdrop1 = pdropfunc(DF1,L,D,PC,CVV)
		print ("coolant pressure drop:", pdrop1)

	#coolant pressure drop

	
	
	
	
#testing
elif programfunction == "T" or programfunction == "t": 
	testFV = FVfunc(test.testCVV, test.testD)
	assert testFV == 11.561015066195278
	testKV = KVfunc(test.testDV,test.testPC)
	assert testKV == 1.0038068523342016e-06
	testRE = REfunc(testFV,test.testD,testKV)
	assert testRE == 57585.854486407814
	testPR = PRfunc(test.testDV,test.testCC,test.testKC)
	assert testPR == 7.089175397093613
	testDF = DFfunc(test.testfancye,test.testD,testRE)
	assert testDF == 0.010906214575733224
	testh = htc(test.testKC,test.testD,GNU(testDF,testRE,testPR))
	assert testh == 28621.292587276246
	testATM = ATMfunc(test.testPP,test.testCP,test.testLP,test.testKM,test.testW,testh,test.testD,test.testLM,test.testTMelt,test.testTEject,test.testTCycle,test.testTC)
	assert testATM == 19.207173469816603
	testTConstant = TConstantfunc(test.testPM,test.testCM,test.testLM,test.testKM,test.testW,testh,test.testD)
	assert testTConstant == 4.641400260500878
	testpdrop = pdropfunc(testDF,test.testL,test.testD,test.testPC,test.testCVV)
	assert testpdrop == 64.51209687989939
	print("Testing complete")
else:
	print("invalid input")
	
