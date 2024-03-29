import matplotlib.pyplot as plt
import numpy as np

#the name of the import can be changed to use other data
import basedata as data

if data.pipetype == "straight":
    programfunction = input('Would you like to select a single heat transfer coefficient or view the results from multiple? Enter "N" to choose or "H" to compare: ' )
    if programfunction == "N" or programfunction == "n": 
        heat_coefficient_correlation = input("Please choose a heat transfer correllation. D for Dittus-Boelter, G for Gnielinski, S for Sieder-Tate: ")
else:
    programfunction = "N"

allvariables = [data.TC, data.PP, data.CP, data.LP, data.W, data.D, data.LM, data.TMelt, data.TEject, data.TCycle, data.TMO, data.CVV, data.DV, data.WDV, data.CP, data.KC, data.CC, data.PC, data.L]

arrayvariables = [vname for vname, i in vars(data).items() if isinstance(i, np.ndarray)]

for i in arrayvariables:
    global xvariable
    xvariable = i

arraynumber = 0
if len(arrayvariables) == 1:
    arraynumber = 1
elif len(arrayvariables) > 1:
    arraynumber = 2

ATMPoint = 1000
#long enough time at which the average temperature of the mold has stabilized, not used when there are no arrays in the data

def FVfunc(CVV, D): 
    FV = (CVV*0.001)/(np.pi*((D/2)**2))
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

def DFfunc(eps,D,RE):
    DF = (1/(-1.8*np.log(((eps/(3.7*D))**1.11)+(6.9/RE))))**2
    return DF
#Darcy friction factor

def helicalDFfunc_lam(RE):
    DF = 64/RE
    return DF
#Friction factor for helical coil with laminar flow

def helicalDFfunc_lam_bigv(RE,D,CD):
    DF = (1+(0.015*(RE**(0.75))*((D/CD)**0.4)))*(64/RE)
    return DF
#Friction factor for helical coil with laminar flow and big vortex

def helicalDFfunc_turb(eps,RE,D,CD):
    DF = (0.1*(1.46*eps+100/RE)**0.25)*(1+0.11*RE**0.23*(D/CD)**0.14)
    return DF
#Friction factor for helical coil with turbulent flow

def DEfunc(RE,D,CD):
    DE = RE*(D/CD)**0.5
    return DE
#Dean number

def DBNU(RE,PR):
    NU = (0.023*RE**0.8)*PR**0.4
#Dittus-Boelter nusselt number
    return NU
def GNU(DF,RE,PR):
    NU = ((DF/8)*(RE-1000)*PR)/(1+(12.7*((DF/8)**0.5)*(PR**(2/3)-1)))
    return NU
#Gnielinski nusselt number
def STNU(RE,PR,DV,WDV):
    NU = 0.027*(RE**(4/5))*(PR**(1/3))*((DV/WDV)**0.14)
    return NU
#Sieder-Tate nusselt number

def helicalNU_lam(DE,PR):
    NU = (2.153+0.318*DE**0.643)*PR**0.177
    return NU
#Helical nusselt number

def helicalNU_turb(RE,PR,D,CD):
    NU = 0.00619*RE**0.92*PR**0.4*(1+3.455*(D/CD))
    return NU
#Helical nusselt number, reynolds number between 5000 and 100,000)
    
def htc(KC,D,NU):
    h = (KC/D)* NU
    return h
#Heat transfer coefficient

def ATMfunc(PP,CP,LP,KM,W,h,D,LM,TMelt,TEject,TCycle,TC):
    ATM = PP*CP*LP*(2.0*KM*W + h*D*LM*np.pi)*(TMelt - TEject)
    ATM = ATM/(h*D*KM*TCycle*np.pi) + TC
    return ATM
#Average temperature of the mold

def TConstantfunc(rho_m,Cp_m,LM,KM,W,h,D):
    TConstant = ((rho_m*Cp_m*LM**2)/KM)*(1+(2.0*W*KM)/(h*D*LM*np.pi))
    return TConstant
#Time constant
def pdropfunc(DF,L,D,PC,FV):
    pdrop = DF*(L/D)*(PC/2)*FV**2
    return pdrop
#Pressure drop
    
if programfunction == "N" or programfunction == "n" or programfunction == "H" or programfunction == "h":
    savegraphs = input ("Would you like to save an image of the graphs? Y for yes, N for no: ")

    FV = FVfunc(data.CVV, data.D)
    print ("flow velocity:", FV)

    KV = KVfunc(data.DV,data.PC)
    print ("kinematic viscosity:", KV)
    
    RE = REfunc(FV,data.D,KV)
    print ("Reynolds number:", RE)

    PR = PRfunc(data.DV,data.CC,data.KC)
    print ("Prandl number:", PR)
    
    if data.pipetype == "straight":
        DF = DFfunc(data.eps,data.D,RE)
        print ("Darcy friction factor (",data.moldmatname,"):", DF) 
       
        if programfunction == "H" or programfunction == "h":
            h1 = htc(data.KC,data.D,DBNU(RE,PR))
            print ("heat transfer coefficient (Ditus-Boelter):", h1)
            h2 = htc(data.KC,data.D,GNU(DF,RE,PR))
            print ("heat transfer coefficient (Gnielinski):", h2)
            h3 = htc(data.KC,data.D,STNU(RE,PR,data.DV,data.WDV))
            print ("heat transfer coefficient (Sieder-Tate):", h3)
    
        elif programfunction == "N" or programfunction == "n":
            if heat_coefficient_correlation == "D":
                h1 = htc(data.KC,data.D,DBNU(RE,PR))
                print ("heat transfer coefficient", h1)
            elif heat_coefficient_correlation == "G":
                h1 = htc(data.KC,data.D,GNU(DF,RE,PR))
                print ("heat transfer coefficient", h1)
            elif heat_coefficient_correlation == "S":
                h1 = htc(data.KC,data.D,STNU(RE,PR,data.DV,data.WDV))
                print ("heat transfer coefficient", h1)
            #heat transfer coefficient
        
        if programfunction == "H" or programfunction == "h":
            ATM1 = ATMfunc(data.PP,data.CP,data.LP,data.KM,data.W,h1,data.D,data.LM,data.TMelt,data.TEject,data.TCycle,data.TC)
            print ("temperature of the mold (Ditus-Boelter):", ATM1)
            ATM2 = ATMfunc(data.PP,data.CP,data.LP,data.KM,data.W,h2,data.D,data.LM,data.TMelt,data.TEject,data.TCycle,data.TC)
            print ("temperature of the mold (Gnielinski):", ATM2)
            ATM3 = ATMfunc(data.PP,data.CP,data.LP,data.KM,data.W,h3,data.D,data.LM,data.TMelt,data.TEject,data.TCycle,data.TC)
            print ("temperature of the mold (Sieder-Tate):", ATM3)
    
        elif programfunction == "N" or programfunction == "n":
            ATM1 = ATMfunc(data.PP,data.CP,data.LP,data.KM,data.W,h1,data.D,data.LM,data.TMelt,data.TEject,data.TCycle,data.TC)
            print ("temperature of the mold:", ATM1)
        #Average temperature of the mold
        
        if programfunction == "H" or programfunction == "h":
            TConstant1 = TConstantfunc(data.rho_m,data.Cp_m,data.LM,data.KM,data.W,h1,data.D)
            TConstant2 = TConstantfunc(data.rho_m,data.Cp_m,data.LM,data.KM,data.W,h2,data.D)
            TConstant3 = TConstantfunc(data.rho_m,data.Cp_m,data.LM,data.KM,data.W,h3,data.D)
            print ("time constant (Ditus-Boelter):", TConstant1)
            print ("time constant (Gnielinski):", TConstant2)
            print ("time constant (Sieder-Tate):", TConstant3)
        
        elif programfunction == "N" or programfunction == "n":
            TConstant1 = TConstantfunc(data.rho_m,data.Cp_m,data.LM,data.KM,data.W,h1,data.D)
            print ("time constant", TConstant1)
        #Time constant

        pdrop = pdropfunc(DF,data.L,data.D,data.PC,FV)
        print ("coolant pressure drop:", pdrop)
    #coolant pressure drop
    
    elif data.pipetype == "helical":
        DE = DEfunc(RE,data.D,data.CD)
        print ("Dean number:", DE)
        
        if 20 < DE < 2000 and 0.7 < PR < 175 and 0.0267 < data.D/data.CD < 0.0884:
            h1 = htc(data.KC,data.D,helicalNU_lam(DE,PR))
        elif 5000 < RE < 100000 and 0.7 < PR < 5 and 0.0267 < data.D/data.CD < 0.0884:
            h1 = htc(data.KC,data.D,helicalNU_turb(DE,PR,data.D,data.CD))
        else:
            print ("Helical coil geometry invalid")
        
        print ("heat transfer coefficient", h1)
        #heat transfer coefficient
        
        ATM1 = ATMfunc(data.PP,data.CP,data.LP,data.KM,data.W,h1,data.D,data.LM,data.TMelt,data.TEject,data.TCycle,data.TC)
        print ("temperature of the mold:", ATM1)
        #Average temperature of the mold
        
        TConstant1 = TConstantfunc(data.rho_m,data.Cp_m,data.LM,data.KM,data.W,h1,data.D)
        print ("time constant", TConstant1)
        #Time constant
        
        if DE < 11.6:
            DF = helicalDFfunc_lam(RE)
            
        elif DE > 11.6 and RE < 10000:
            DF = helicalDFfunc_lam_bigv(RE,data.D,data.CD)
            
        elif DE > 11.6 and RE > 10000:
            DF = helicalDFfunc_turb(data.eps,RE,data.D,data.CD)
        
        print ("Darcy friction factor (",data.moldmatname,"):", DF)
        #Darcy friction factor
        
        pdrop = pdropfunc(DF,data.L,data.D,data.PC,FV)
        print ("coolant pressure drop:", pdrop)
        #Pressure drop
        
    if arraynumber == 1:
        x = eval("data." + xvariable)
    elif arraynumber == 2:
        x = np.arange(1, len(eval("data." + xvariable))+1)
    else:
        x = np.linspace(0,200)
        ATMPoint = x
    
    y1 = ATM1 + ((data.TMO-ATM1)*np.e**(-ATMPoint/TConstant1))
    if programfunction == "H" or programfunction == "h":
        y2 = ATM2 + ((data.TMO-ATM2)*np.e**(-ATMPoint/TConstant2))
        y3 = ATM3 + ((data.TMO-ATM3)*np.e**(-ATMPoint/TConstant3))

    if programfunction == "H" and arraynumber == 0 or programfunction == "h" and arraynumber == 0:
        plt.plot(x,y1,'r', ls=('dotted'), label='Ditus-Boelter')
        plt.plot(x,y2,'black', ls=('dotted'), label='Gnielinski')
        plt.plot(x,y3,'b', ls=('dotted'), label='Sieder-Tate')
        plt.xlabel("Time (s) from beginning of heat cycling")

    elif programfunction == "H" or programfunction == "h":
        plt.plot(x,y1,'r', ls=('none'), marker="o", markersize=7, label='Ditus-Boelter')
        plt.plot(x,y2,'black', ls=('none'), marker="o", markersize=7, label='Gnielinski')
        plt.plot(x,y3,'b', ls=('none'), marker="o", markersize=7, label='Sieder-Tate')
        if arraynumber == 1:
            plt.xlabel("Values for array variable in SI units")
        else:
            plt.xlabel("Variables' position in array")
        plt.locator_params(axis="x", integer=True, tight=True)
    elif programfunction == "N" and arraynumber == 0 or programfunction == "n" and arraynumber == 0:
        plt.plot(x,y1,'r', ls=('dotted'))
        plt.xlabel("Time (s) from beginning of heat cycling")
    elif programfunction == "N" or programfunction == "n":
        plt.plot(x,y1,'r', ls=('none'), marker="o", markersize=7)
        plt.xlabel("Variable(s) position in array")
        plt.locator_params(axis="x", integer=True, tight=True)
    
    plt.ylabel("Average heat cycle temperature (C)")
    plt.grid('both')
    plt.legend()

    if savegraphs == "Y" or savegraphs == "y":
        plt.savefig("paccman.png")
        plt.savefig("paccman.eps")

else:
        print ("invalid program function selection")
