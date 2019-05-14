
import mc_automata
import time
import threading


mc = mc_automata.MinecraftAFKSubstitute("1.14")

def remove_leaves():
	mc.press_and_release("Hotbar Slot 1")
	mc.press("Attack")
	while mc.get_targetedBlock()[1] == "minecraft:birch_leaves":
		continue
	mc.release("Attack")


def remove_log():
	mc.press_and_release("Hotbar Slot 2")
	mc.press("Attack")
	while mc.get_targetedBlock()[1] == "minecraft:birch_log":
		continue
	mc.release("Attack")


dur = 0

mc.continue_when_key("inicio")

while True:



	# Sapling
	mc.set_angles(0,60)
	mc.press_and_release("Hotbar Slot 1")
	mc.press_and_release("Use Item/Place Block")


	# Wait for grow
	mc.set_angles(0,45)
	while mc.get_targetedBlock()[1] != "minecraft:birch_log":
		time.sleep(0.5)

	# Chop first two
	remove_log()

	# Chop the rest
	mc.set_angles(0,-77.5)
	remove_leaves()
	remove_log()

	# Remove leaves
	mc.set_angles(60.5,-41.3)
	remove_leaves()
	mc.set_angles(-60.5,-41.3)
	remove_leaves()
	mc.set_angles(148.4,-56.1)
	remove_leaves()
	mc.set_angles(180,-90)
	remove_leaves()

	dur += 6

	if dur > 125:
		dur = 0
		mc.set_angles(180,0)
		mc.press_and_release("Use Item/Place Block")
		time.sleep(3)
		mc.cursor_to_ui_dispenser(0)
		mc.press_and_release("Hotbar Slot 2")
		mc.press_and_release("Drop")
		mc.press_and_release("Open/Close Inventory")
