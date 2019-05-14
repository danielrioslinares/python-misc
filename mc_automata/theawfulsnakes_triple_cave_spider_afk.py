
import mc_automata
import time
from datetime import datetime
import mouse

# Minecraft instance
mc = mc_automata.MinecraftAFKSubstitute("1.14")

# Wait for "inicio" key
mc.continue_when_key("inicio")

mouse.press(button='right')
time.sleep(1)
mouse.release(button='right')


# While required
while True:

	# DEBUG
	print( "[{}] I'm working :D".format( datetime.now().strftime("%m/%d/%Y, %H:%M:%S") ) )

	# Sword (or hand)
	mc.press_and_release("Hotbar Slot 1")

	# Look at the lever and pull it
	mc.go_straight_xz( (279.5,20,-132.5) )
	mc.set_angles( 166, 19.5 )
	mc.press_and_release("Use Item/Place Block")

	# Go to the crushing point
	mc.go_straight_xz( (278.80,20,-135.2) )

	# Look at the button and push it
	mc.set_angles( -115, -59 )
	mc.press_and_release("Use Item/Place Block")

	# Look at the spiders
	mc.set_angles( -164.5, -6.7 )

	# Wait 20 seconds
	time.sleep(10)

	# Swing the sword
	for i in range(7):
		mc.press_and_release("Attack")
		time.sleep(2)

	# Move closer (get xp)
	mc.go_straight_xz( (278.5,20,-136) )
	time.sleep(5)

	# Look at the lever and pull it
	mc.go_straight_xz( (279.5,20,-132.5) )
	mc.set_angles( 166, 19.5 )
	mc.press_and_release("Use Item/Place Block")

	# Go to start position (AFK zone)
	mc.go_straight_xz( (279.5,20,-116.5) )

	# Try to eat
	mc.set_angles( -180, 0 )
	mc.press_and_release("Hotbar Slot 8")
	mouse.press(button='right')

	# Wait time (2 minutes)
	time.sleep(240)
	mc.release("Use Item/Place Block")

	mouse.release(button='right')
