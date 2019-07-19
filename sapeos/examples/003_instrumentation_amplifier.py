
import sapeos

n00 = sapeos.Node("GND", v=0)
ni1 = sapeos.Node("Input1")
ni2 = sapeos.Node("Input2")
nA1_n = sapeos.Node("n(n-)_A1")
nA1_o = sapeos.Node("n(no)_A1")
nA2_n = sapeos.Node("n(n-)_A2")
nA2_o = sapeos.Node("n(no)_A2")
nA3_p = sapeos.Node("n(n+)_A3")
nA3_n = sapeos.Node("n(n-)_A3")
no = sapeos.Node("Output")

s01 = sapeos.Source("S1", ni1, n00)
s02 = sapeos.Source("S2", ni2, n00)
a01 = sapeos.IdealOpAmp("A1", ni1, nA1_n, nA1_o)
a02 = sapeos.IdealOpAmp("A2", ni2, nA2_n, nA2_o)
a03 = sapeos.IdealOpAmp("A3", nA3_p, nA3_n, no)
r01_1 = sapeos.Impedance("R1_1", nA1_o, nA1_n)
r01_2 = sapeos.Impedance("R1_2", nA2_o, nA2_n)
rg = sapeos.Impedance("RG", nA1_n, nA2_n)
r02_1 = sapeos.Impedance("R2_1", nA1_o, nA3_n)
r02_2 = sapeos.Impedance("R2_2", nA2_o, nA3_p)
r03_1 = sapeos.Impedance("R3_1", nA3_p, n00)
r03_2 = sapeos.Impedance("R3_2", nA3_n, no)






ckt = sapeos.Circuit([s01,s02,a01,a02,a03,r01_1,r01_2,rg,r02_1,r02_2,r03_1,r03_2], [n00,ni1,ni2,nA1_n,nA1_o,nA2_n,nA2_o,nA3_p,nA3_n,no])
sol = ckt.solve([s01.V,s02.V], no.v)

print(sol)
