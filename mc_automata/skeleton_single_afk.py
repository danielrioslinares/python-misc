
import mc_automata
import time
import threading


mc = mc_automata.MinecraftAFKSubstitute("1.14")








is_server_on = True
def check_server_on():
	global is_server_on
	while True:
		a = mc.push_button("Back to server list")
		if a[0]:
			is_server_on = False
		time.sleep(50)



def return_from_back_to_server_list(server_ip):

	global is_server_on
	global mc

	while not is_server_on:

		mc.push_button("Direct Connect")[0]

		mc._app.send_keystrokes("{END}")
		for i in range(100):
			mc._app.send_keystrokes("{BACKSPACE}")

		mc.type(server_ip)

		if mc.push_button("Join Server")[0]:
			is_server_on = True



mc.continue_when_key("inicio")

t = threading.Thread(target=check_server_on)
try:
	t.start()
except (KeyboardInterrupt, SystemExit):
    t.join()
    sys.exit()




while True:

	mc.press("Hotbar Slot 1")
	mc.press_and_release("Attack")

	try:
		hungry = mc.get_hungry()[1]
		health = mc.get_health()[1]
		if hungry is not None:
			while hungry < 20 or health < 20:
				hungry = mc.get_hungry()[1]
				health = mc.get_health()[1]
				mc.press("Hotbar Slot 8")
				mc.press("Use Item/Place Block")
			mc.release("Use Item/Place Block")
	except:
		pass

	time.sleep(30)

	if not is_server_on:
		return_from_back_to_server_list("158.69.185.95:25566")
		time.sleep(15)
