
import sapeos

n00 = sapeos.Node("GND", v=0)
n01 = sapeos.Node("Input")
n02 = sapeos.Node("Output")
n03 = sapeos.Node("OA(n-)")
n04 = sapeos.Node("OA(n+)")

a01 = sapeos.IdealOpAmp("A1", n04, n03, n02)
s01 = sapeos.Source("S1", n01, n00)
s02 = sapeos.Source("S2", n04, n00)
r01 = sapeos.Impedance("R1", n01, n03)
r02 = sapeos.Impedance("R2", n03, n02)


ckt = sapeos.Circuit([a01,s01,s02,r01,r02], [n00,n01,n02,n03,n04])
sol = ckt.solve([s01.V, s02.V], n02.v)

print(sol)
