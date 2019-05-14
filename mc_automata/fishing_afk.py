
import mc_automata
import time


mc = mc_automata.MinecraftAFKSubstitute("1.14")


mc.continue_when_key("inicio")


while True:

	# Throw the rod
	mc.press_and_release("Use Item/Place Block")

	# Wait 200 ms
	time.sleep(0.2)
