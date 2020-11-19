import virtualbox
import vboxapi

vbox = virtualbox.VirtualBox()
vbox_manager = vboxapi.VirtualBoxManager

session = virtualbox.Session()
machine = vbox.find_machine("vm2")
