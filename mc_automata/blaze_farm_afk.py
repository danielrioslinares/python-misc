import mc_automata
import time


mc = mc_automata.MinecraftAFKSubstitute("1.14")

mc.continue_when_key("inicio")

while True:

	mc.press("Hotbar Slot 1")
	mc.press_and_release("Attack")

	time.sleep(1)
