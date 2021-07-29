from math import isclose
from _pytest.monkeypatch import MonkeyPatch

def test_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "M")
test_input(MonkeyPatch())

testTC = 15.
#coolant temperature celsius
testPP = 980.
#density of plastic part kg/m^3
testCP = 1300.
#specific heat capacity of plastic part J/KG*K
testLP = 0.001
#half the plastic part thickness m
testW = 0.010
#cooling line pitch distance m
testD = 0.005
#cooling line diameter m
testLM = 0.004
#distance from cooling line to mold wall
testTMelt = 180.
#Part melted temperature
testTEject = 64.9
#Part ejection temperature
testTCycle = 10.
#Cycle time seconds
testTMO = 13.
#Initial mold temperature
testCVV = 0.227
#coolant velocity liters/sec
testDV = 1.002 * 10**-3
#coolant dynamic viscosity
tesWDV = 0.0009775
#coolant dynamic viscosity when near wall
testKC = 0.5918
#thermal conductivity of coolant
testPC = 998.2
#coolant density
testCC = 4187
#specific heat capacity of coolant
testL = 1.15
#coolant line length
testrho_m = 7930.
#First comparison Mold density kg/m^3: 316 steel
testCp_m = 510.
#First comparison Mold specific heat 316 steel
testeps = 0.00015
#First comparison average height of pipe surface irregularities (m) 316 steel
testKM = 16.5
#First comparison thermal conductivity of mold: 316 steel
testPR = 7.089175397093613
testCD = 0.057

from ..paccman import FVfunc
from ..paccman import KVfunc
from ..paccman import REfunc
from ..paccman import PRfunc
from ..paccman import DFfunc
from ..paccman import htc
from ..paccman import GNU
from ..paccman import ATMfunc
from ..paccman import TConstantfunc
from ..paccman import pdropfunc
from ..paccman import helicalDFfunc_lam_bigv
from ..paccman import helicalDFfunc_turb
from ..paccman import helicalNU_lam
from ..paccman import helicalNU_turb

class TestClass:

    def testFV(self):
        testFV = FVfunc(testCVV, testD)
        assert testFV == 11.561015066195278
        return testFV

    def testKV(self):
        testKV = KVfunc(testDV,testPC)
        assert testKV == 1.0038068523342016e-06
        return testKV
        
    def testRE(self):
        testRE = REfunc(11.561015066195278,testD,1.0038068523342016e-06)
        assert testRE == 57585.854486407814
        return testRE
        
    def testPR(self):
        testPR = PRfunc(testDV,testCC,testKC)
        assert testPR == 7.089175397093613
        return testPR
    
    def testDF(self):
        testDF = DFfunc(testeps,testD,57585.854486407814)
        assert testDF == 0.010906214575733224
        return testDF
    
    def testhtc(self):
        testh = htc(testKC,testD,GNU(0.010906214575733224,57585.854486407814,7.089175397093613))
        assert testh == 28621.292587276246
        return testh
    
    def testATM(self):
        testATM = ATMfunc(testPP,testCP,testLP,testKM,testW,28621.292587276246,testD,testLM,testTMelt,testTEject,testTCycle,testTC)
        assert testATM == 19.207173469816603
        return testATM
    
    def testTConstant(self):
        testTConstant = TConstantfunc(testrho_m,testCp_m,testLM,testKM,testW,28621.292587276246,testD)
        assert testTConstant == 4.641400260500878
        return testTConstant
    
    def testpdrop(self):
        testpdrop = pdropfunc(0.010906214575733224,testL,testD,testPC,11.561015066195278)
        assert testpdrop == 167332.91558708664
        return testpdrop
    
    def testhelicalDFfunc_lam(self):
        testhelicalDF_lam = helicalDFfunc_lam_bigv(2492,12/112,1)
        testhelicalDF_lam2 = helicalDFfunc_lam_bigv(7912,12/112,1)
        assert isclose(testhelicalDF_lam, 0.07922, abs_tol=2.1e-3)
        assert isclose(testhelicalDF_lam2, 0.04899, abs_tol=1e-3)
#data from Hydraulic Performance... (2001) by Xu, et al. pulled with WebPlotDigitizer
        
    def testhelicalDFfunc_turb(self):
        testhelicalDF_turb = helicalDFfunc_turb(0,10394,12/112,1)
        testhelicalDF_turb2 = helicalDFfunc_turb(0,21310,12/112,1)
        assert isclose(testhelicalDF_turb, 0.05457, abs_tol=2.5e-3)
        assert isclose(testhelicalDF_turb2, 0.05246, abs_tol=5.5e-3)
#data from Hydraulic Performance... (2001) by Xu, et al. pulled with WebPlotDigitizer
        
    def testhelicalNU_lam(self):
        testhelicalNU_lam = helicalNU_lam(765.17,testPR)
        testhelicalNU_lam2 = helicalNU_lam(15.227,testPR)
        assert isclose(testhelicalNU_lam, 23.751*testPR**0.175, abs_tol=3)
        assert isclose(testhelicalNU_lam2, 3.9104*testPR**0.175, abs_tol=1.4e-1)
#data from The Effects of... (1997) by Xin, et al. pulled with WebPlotDigitizer and tested using generic Prandtl
        
    def testhelicalNU_turb(self):
        testhelicalNU_turb = helicalNU_turb(18152.641,testPR,testD,testCD)
        testhelicalNU_turb2 = helicalNU_turb(112074.9,testPR,testD,testCD)
        assert isclose(testhelicalNU_turb, 51.304*(testPR**0.4*(1+3.455*(testD/testCD))), abs_tol=1e-1)
        assert isclose(testhelicalNU_turb2, 279.538*(testPR**0.4*(1+3.455*(testD/testCD))), abs_tol=17)
#data from The Effects of... (1997) by Xin, et al. pulled with WebPlotDigitizer and tested using generic Prandtl, Diameter, Coil Diameter


