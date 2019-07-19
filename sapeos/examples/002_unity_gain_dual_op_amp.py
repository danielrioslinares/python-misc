
import sapeos

n00 = sapeos.Node("GND", v=0)
n01 = sapeos.Node("Input")
n02 = sapeos.Node("OA1(n-)")
n03 = sapeos.Node("OA1(no)")
n04 = sapeos.Node("OA2(n-)")
n05 = sapeos.Node("Output")

a01 = sapeos.IdealOpAmp("A1", n00, n02, n03)
a02 = sapeos.IdealOpAmp("A2", n00, n04, n05)
s01 = sapeos.Source("S1", n01, n00)
r01 = sapeos.Impedance("R1", n01, n02)
r02 = sapeos.Impedance("R2", n03, n04)
l01 = sapeos.Impedance("L1", n02, n03)
c01 = sapeos.Impedance("C1", n04, n05)

ckt = sapeos.Circuit([a01,a02,s01,r01,r02,l01,c01], [n00,n01,n02,n03,n04,n05])
sol = ckt.solve([s01.V], n05.v)

print(sol)
