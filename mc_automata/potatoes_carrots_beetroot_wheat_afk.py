
import mc_automata
import time


mc = mc_automata.MinecraftAFKSubstitute("1.14")


mc.continue_when_key("inicio")


while True:

	for i in [2,2,2,3,2,3,4,5]:

		# Select crop
		mc.press_and_release("Hotbar Slot " + str(i))

		# Plant it!
		mc.press_and_release("Use Item/Place Block")

		# Wait 1750 ms
		time.sleep(1.75)

		# Fortune pickaxe
		mc.press_and_release("Hotbar Slot 1")
		mc.press_and_release("Attack")
