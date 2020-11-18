import virtualbox

vbox = virtualbox.VirtualBox()

session = virtualbox.Session()
machine = vbox.find_machine("vm2")
print(machine.q)