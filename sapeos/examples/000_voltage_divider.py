
import sapeos

n00 = sapeos.Node("GND", v=0)
n01 = sapeos.Node("Input")
n02 = sapeos.Node("Output")

s01 = sapeos.Source("S1", n01, n00)
r01 = sapeos.Impedance("R1", n01, n02)
r02 = sapeos.Impedance("R2", n02, n00)

ckt = sapeos.Circuit([s01,r01,r02], [n00,n01,n02])
sol = ckt.solve([s01.I], n02.v)

print(sol)
