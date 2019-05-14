
import mc_automata
import time


mc = mc_automata.MinecraftAFKSubstitute("1.14")


mc.continue_when_key("inicio")


while True:

	# Fortune pickaxe
	for i in range(5):
		mc.press_and_release("Attack")

	# Put potatoes
	for i in range(5):
		mc.press_and_release("Use Item/Place Block")

	# Wait 1750 ms
	time.sleep(2)
