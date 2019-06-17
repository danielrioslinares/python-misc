
import mc_automata
import time


mc = mc_automata.MinecraftAFKSubstitute("1.14")


mc.continue_when_key("inicio")

x0,y0,z0 = -28.5,1.0,-23.5
max_height = 101
min_height = 1


XZ = [
	(-8,+2),(-8,+1),(-8,0), # (-8,-2),(-8,-1),
	(-7,-3),(-7,-2),(-7,-1),(-7,+3),(-7,+2),(-7,+1),(-7,0),
	(-6,-4),(-6,-3),(-6,-2),(-6,-1),(-6,+4),(-6,+3),(-6,+2),(-6,+1),(-6,0),
	(-5,-4),(-5,-3),(-5,-2),(-5,-1),(-5,+4),(-5,+3),(-5,+2),(-5,+1),(-5,0),
	(-4,-4),(-4,-3),(-4,-2),(-4,-1),(-4,+4),(-4,+3),(-4,+2),(-4,+1),(-4,0),
	(-3,-4),(-3,-3),(-3,-2),(-3,-1),(-3,+4),(-3,+3),(-3,+2),(-3,+1),(-3,0),
	(-2,-4),(-2,-3),(-2,-2),(-2,-1),(-2,+4),(-2,+3),(-2,+2),(-2,+1),(-2,0),
	(-1,-3),(-1,-2),(-1,-1),(-1,+3),(-1,+2),(-1,+1),(-1,0),
	(-0,-2),(-0,-1),(-0,+2),(-0,+1),(-0,0),
]


for dx,dz in XZ:

	mc.go_straight_xz( (x0,y0,z0) )
	mc.set_angles(0,0)

	for i in range(2,9):
		mc.press_and_release("Hotbar Slot " + str(i))
		time.sleep(0.1)
		for i in range(64):
			mc.press_and_release("Drop")

	mc.set_angles(90,90)
	mc.press("Walk Backwards")
	while mc.get_XYZ()[1][1] < max_height:
		continue
	mc.release("Walk Backwards")

	mc.go_straight_xz( (x0+dx,y0,z0+dz) )

	mc.press_and_release("Hotbar Slot 1")
	mc.press("Attack")
	while mc.get_XYZ()[1][1] > min_height+1:
		continue
	mc.release("Attack")











#
