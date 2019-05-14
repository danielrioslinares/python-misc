
import mc_automata
import time


mc = mc_automata.MinecraftAFKSubstitute("1.14")


mc.continue_when_key("inicio")

pumpkin_melon_cycles = 128
sugar_canne = 128
resupply_cycles = 60

i = 0

while True:

	# Crop no.1
	mc.set_angles(-36.5,29.1)
	mc.press_and_release("Hotbar Slot 9") # Fortune
	mc.press_and_release("Attack")
	mc.press_and_release("Hotbar Slot 1")
	mc.press_and_release("Use Item/Place Block")


	# Crop no.2
	mc.set_angles(-15,33.5)
	mc.press_and_release("Hotbar Slot 9") # Fortune
	mc.press_and_release("Attack")
	mc.press_and_release("Hotbar Slot 2")
	mc.press_and_release("Use Item/Place Block")

	# Crop no.3
	mc.set_angles(15,33.5)
	mc.press_and_release("Hotbar Slot 9") # Fortune
	mc.press_and_release("Attack")
	mc.press_and_release("Hotbar Slot 3")
	mc.press_and_release("Use Item/Place Block")

	# Crop no.4
	mc.set_angles(36.5,29.1)
	mc.press_and_release("Hotbar Slot 9") # Fortune
	mc.press_and_release("Attack")
	mc.press_and_release("Hotbar Slot 4")
	mc.press_and_release("Use Item/Place Block")

	# Pumpkin and melon
	if i % pumpkin_melon_cycles == 0:
		mc.press_and_release("Hotbar Slot 8") # Axe
		mc.set_angles(-90,10)
		mc.press("Attack")
		while mc.get_targetedBlock()[1] == "minecraft:pumpkin":
			continue
		mc.release("Attack")
		mc.set_angles(90,10)
		mc.press("Attack")
		while mc.get_targetedBlock()[1] == "minecraft:melon":
			continue
		mc.release("Attack")

	# Sugar canne
	if i % sugar_canne == 0:
		mc.set_angles(124.7,-4.6)
		mc.press_and_release("Attack")
		mc.press_and_release("Attack")
		mc.set_angles(146.9,-2.8)
		mc.press_and_release("Attack")
		mc.press_and_release("Attack")
		mc.set_angles(-124.7,-4.6)
		mc.press_and_release("Attack")
		mc.press_and_release("Attack")
		mc.set_angles(-146.9,-2.8)
		mc.press_and_release("Attack")
		mc.press_and_release("Attack")

	# Resupply
	if i % resupply_cycles == 0:
		mc.set_angles(0,-90)
		mc.press_and_release("Use Item/Place Block")
		mc.cursor_to_ui_dispenser(0)
		mc.press_and_release("Hotbar Slot 1")
		mc.press_and_release("Open/Close Inventory")

		mc.press_and_release("Use Item/Place Block")
		mc.cursor_to_ui_dispenser(1)
		mc.press_and_release("Hotbar Slot 2")
		mc.press_and_release("Open/Close Inventory")
		mc.press_and_release("Use Item/Place Block")

		mc.cursor_to_ui_dispenser(2)
		mc.press_and_release("Hotbar Slot 3")
		mc.press_and_release("Open/Close Inventory")

		mc.press_and_release("Use Item/Place Block")
		mc.cursor_to_ui_dispenser(3)
		mc.press_and_release("Hotbar Slot 4")
		mc.press_and_release("Open/Close Inventory")

	i += 1
