import virtualbox

vbox = virtualbox.VirtualBox()

session = virtualbox.Session()
machine = vbox.find_machine("vm2")
machine.state
progress = machine.launch_vm_process(session, "gui", [])
progress.wait_for_completion()