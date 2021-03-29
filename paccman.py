import matplotlib.pyplot as plt
import numpy as np

programfunction = input('What would you like to use this program for? M for mold material comparison, H for heat transfer coefficient comparison, N for simple data from a single mold material and user choice of heat transfer coefficient: ' )

if programfunction == "N" or programfunction == "n": 
    heat_coefficient_correlation = input("Please choose a heat transfer correllation. D for Dittus-Boelter, G for Gnielinski, S for Sieder-Tate: ")

#general note: when programfunction = N or H, the first choice of mold material properties is used (KM1, PM1, etc.)

#the name of the import can be changed to use other data
import basedata as data

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
#Dittus-Boelter heat transfer coefficent correlation
	return NU
def GNU(DF,RE,PR):
	NU = ((DF/8)*(RE-1000)*PR)/(1+(12.7*((DF/8)**0.5)*(PR**(2/3)-1)))
	return NU
#Gnielinski heat transfer coefficent correlation
def STNU(RE,PR,DV,WDV):
	NU = 0.027*(RE**(4/5))*(PR**(1/3))*((DV/WDV)**0.14)
	return NU
#Sieder-Tate heat transfer coefficent correlation
	
def htc(KC,D,NU):
	h = (KC/D)* NU
	return h
#Heat transfer coefficient

def ATMfunc(PP,CP,LP,KM,W,h,D,LM,TMelt,TEject,TCycle,TC):
	ATM = PP*CP*LP*(2.0*KM*W + h*D*LM*np.pi)*(TMelt - TEject)
	ATM = ATM/(h*D*KM*TCycle*np.pi) + TC
	return ATM
#Average temperature of the mold

def TConstantfunc(PM,CM,LM,KM,W,h,D):
	TConstant = ((PM*CM*LM**2)/KM)*(1+(2.0*W*KM)/(h*D*LM*np.pi))
	return TConstant
#Time constant
def pdropfunc(DF,L,D,PC,CVV):
	pdrop = (DF*L/D)*(PC/2)*CVV**2
	return pdrop
#Pressure drop
	
if programfunction == "M" or programfunction == "m" or programfunction == "N" or programfunction == "n" or programfunction == "H" or programfunction == "h":
	savegraphs = input ("Would you like to save an image of the graphs? Y for yes, N for no: ")

	FV = FVfunc(data.CVV, data.D)
	print ("flow velocity:", FV)

	KV = KVfunc(data.DV,data.PC)
	print ("kinematic viscosity:", KV)
    
	RE = RE = REfunc(FV,data.D,KV)
    
	print ("Reynolds number:", RE)

	PR = PRfunc(data.DV,data.CC,data.KC)
	print ("Prandl number:", PR)

	DF1 = DFfunc(data.mat1fancye,data.D,RE)
	print ("Darcy friction factor (",data.moldmatname1,"):", DF1)

	if programfunction == "M" or programfunction == "m":
		DF2 = DFfunc(data.mat2fancye,data.D,RE)
		print ("Darcy friction factor (",data.moldmatname2,"):", DF2)
	if programfunction == "M" or programfunction == "m":
		DF3 = DFfunc(data.mat3fancye,data.D,RE)   
		print ("Darcy friction factor (",data.moldmatname3,"):", DF3)
   
   
	if programfunction == "M" or programfunction == "m": 
		h1 = htc(data.KC,data.D,GNU(DF1,RE,PR))
		print ("heat transfer coefficient (",data.moldmatname1,"):", h1)
		h2 = htc(data.KC,data.D,GNU(DF2,RE,PR))
		print ("heat transfer coefficient (",data.moldmatname2,"):", h2)
		h3 = htc(data.KC,data.D,GNU(DF3,RE,PR))
		print ("heat transfer coefficient (",data.moldmatname3,"):", h3)

		
	elif programfunction == "H" or programfunction == "h":
		h1 = htc(data.KC,data.D,DBNU(RE,PR))
		print ("heat transfer coefficient (Ditus-Boelter):", h1)
		h2 = htc(data.KC,data.D,GNU(DF1,RE,PR))
		print ("heat transfer coefficient (Gnielinski):", h2)
		h3 = htc(data.KC,data.D,STNU(RE,PR,data.DV,data.WDV))
		print ("heat transfer coefficient (Sieder-Tate):", h3)
	
	
	elif programfunction == "N" or programfunction == "n":
		if heat_coefficient_correlation == "D":
			h1 = htc(data.KC,data.D,DBNU(RE,PR))
			print ("heat transfer coefficient", h1)
		elif heat_coefficient_correlation == "G":
			h2 = htc(data.KC,data.D,GNU(DF1,RE,PR))
			print ("heat transfer coefficient", h2)
		elif heat_coefficient_correlation == "S":
			h3 = htc(data.KC,data.D,DBNU(RE,PR,data.DV,data.WDV))
			print ("heat transfer coefficient", h3)
	

	if programfunction == "M" or programfunction == "m": 
		ATM1 = ATMfunc(data.PP,data.CP,data.LP,data.mat1KM,data.W,h1,data.D,data.LM,data.TMelt,data.TEject,data.TCycle,data.TC)
		print ("temperature of the mold (",data.moldmatname1,"):", ATM1)
		ATM2 = ATMfunc(data.PP,data.CP,data.LP,data.mat2KM,data.W,h2,data.D,data.LM,data.TMelt,data.TEject,data.TCycle,data.TC)
		print ("temperature of the mold (",data.moldmatname2,"):", ATM2)
		ATM3 = ATMfunc(data.PP,data.CP,data.LP,data.mat3KM,data.W,h3,data.D,data.LM,data.TMelt,data.TEject,data.TCycle,data.TC)
		print ("temperature of the mold (",data.moldmatname3,"):", ATM3)

		
	elif programfunction == "H" or programfunction == "h":
		ATM1 = ATMfunc(data.PP,data.CP,data.LP,data.mat1KM,data.W,h1,data.D,data.LM,data.TMelt,data.TEject,data.TCycle,data.TC)
		print ("temperature of the mold (Ditus-Boelter):", ATM1)
		ATM2 = ATMfunc(data.PP,data.CP,data.LP,data.mat1KM,data.W,h2,data.D,data.LM,data.TMelt,data.TEject,data.TCycle,data.TC)
		print ("temperature of the mold (Gnielinski):", ATM2)
		ATM3 = ATMfunc(data.PP,data.CP,data.LP,data.mat1KM,data.W,h3,data.D,data.LM,data.TMelt,data.TEject,data.TCycle,data.TC)
		print ("temperature of the mold (Sieder-Tate):", ATM3)
    
	
	elif programfunction == "N" or programfunction == "n":
		ATM1 = ATMfunc(data.PP,data.CP,data.LP,data.mat1KM,data.W,h1,data.D,data.LM,data.TMelt,data.TEject,data.TCycle,data.TC)
		print ("temperature of the mold:", ATM1)
	#Average temperature of the mold
	

	if programfunction == "M" or programfunction == "m":
		TConstant1 = TConstantfunc(data.mat1PM,data.mat1CM,data.LM,data.mat1KM,data.W,h1,data.D)
		TConstant2 = TConstantfunc(data.mat2PM,data.mat2CM,data.LM,data.mat2KM,data.W,h2,data.D)
		TConstant3 = TConstantfunc(data.mat3PM,data.mat3CM,data.LM,data.mat3KM,data.W,h3,data.D)
		print ("time constant (",data.moldmatname1,"):", TConstant1)
		print ("time constant (",data.moldmatname2,"):", TConstant2)
		print ("time constant (",data.moldmatname3,"):", TConstant3)
		
	elif programfunction == "H" or programfunction == "h":
		TConstant1 = TConstantfunc(data.mat1PM,data.mat1CM,data.LM,data.mat1KM,data.W,h1,data.D)
		TConstant2 = TConstantfunc(data.mat1PM,data.mat1CM,data.LM,data.mat1KM,data.W,h2,data.D)
		TConstant3 = TConstantfunc(data.mat1PM,data.mat1CM,data.LM,data.mat1KM,data.W,h3,data.D)
		print ("time constant (Ditus-Boelter):", TConstant1)
		print ("time constant (Gnielinski):", TConstant2)
		print ("time constant (Sieder-Tate):", TConstant3)
		
	elif programfunction == "N" or programfunction == "n":
		TConstant1 = TConstantfunc(data.mat1PM,data.mat1CM,data.LM,data.mat1KM,data.W,h1,data.D)
		print ("time constant", TConstant1)

	#Time constant
	
	if programfunction == "M" or programfunction == "m":
		pdrop1 = pdropfunc(DF1,data.L,data.D,data.PC,data.CVV)
		pdrop2 = pdropfunc(DF2,data.L,data.D,data.PC,data.CVV)
		pdrop3 = pdropfunc(DF3,data.L,data.D,data.PC,data.CVV)

		print ("coolant pressure drop (",data.moldmatname1,"):", pdrop1)
		print ("coolant pressure drop (",data.moldmatname2,"):", pdrop2)
		print ("coolant pressure drop (",data.moldmatname3,"):", pdrop3)

	elif programfunction == "H" or programfunction == "h" or programfunction == "N" or programfunction == "n":
		pdrop1 = pdropfunc(DF1,data.L,data.D,data.PC,data.CVV)
		print ("coolant pressure drop:", pdrop1)

		#coolant pressure drop
		
	x = np.linspace(0,1000)

	y1 = ATM1 + ((data.TMO-ATM1)*np.e**(-x/TConstant1))
	if programfunction == "M" or programfunction == "m" or programfunction == "H" or programfunction == "h":
		y2 = ATM2 + ((data.TMO-ATM2)*np.e**(-x/TConstant2))
	if programfunction == "M" or programfunction == "m" or programfunction == "H" or programfunction == "h":
		y3 = ATM3 + ((data.TMO-ATM3)*np.e**(-x/TConstant3))

	if programfunction == "M" or programfunction == "m":
		plt.plot(x,y1,'r', ls=('dotted'), label=data.moldmatname1)
		plt.plot(x,y2,'black', ls=('dotted'), label=data.moldmatname2)
		plt.plot(x,y3,'b', ls=('dotted'), label=data.moldmatname3)

	elif programfunction == "H" or programfunction == "h":
		plt.plot(x,y1,'r', ls=('dotted'), label='Ditus-Boelter')
		plt.plot(x,y2,'black', ls=('dotted'), label='Gnielinski')
		plt.plot(x,y3,'b', ls=('dotted'), label='Sieder-Tate')
	elif programfunction == "N" or programfunction == "n":
		plt.plot(x,y1,'r', ls=('dotted'), label=data.moldmatname1)
    
	plt.axis([0,300,0,100])
	plt.xlabel("Time (s) from beginning of heat cycling")
	plt.ylabel("Average heat cycle temperature (C)")
	plt.grid('both')
	plt.legend()

	if savegraphs == "Y" or savegraphs == "y":
		plt.savefig("paccman.png")
		plt.savefig("paccman.eps")

else:
		print ("invalid program function selection")


	
