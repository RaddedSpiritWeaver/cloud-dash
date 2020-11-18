from fastapi import FastAPI
import vboxapi
import virtualbox
import os

app = FastAPI()
vbox = virtualbox.VirtualBox()

base_vms = {
            "vm1": "192.168.1.56",
            "vm2": "192.168.1.57"
           }

v_command = 'vboxmanage '

@app.get("/")
async def root():
    return [m.name for m in vbox.machines]


# vms controller basically
@app.get("/vms")
async def command():
    return [m.name for m in vbox.machines]
#return names of vms as a list of strings

@app.get("/power")
def stop_start(stop: bool, vm_name: str):
    # todo: start and stop vms and keep track of their sessions soo you can interact with them
    stream = None
    if stop:
        command = "controlvm "
        subcommand = " poweroff"
        stream = os.popen(v_command + command + vm_name + subcommand)
    else:
        command = "startvm "
        stream = os.popen(v_command + command + vm_name)

    return stream.readlines()
# no return

@app.get("/status")
def status(vm_name: str):
    machine = vbox.find_machine(vm_name)
    return machine.state

# sample return value
# {
#   "_value": 5, # this seems to mean online
#   "__doc__": "Pseudo-state: first online state (for use in relational expressions)."
# }

@app.get("/deep")
def depInf(vm_name: str):
    # todo: idk how to use the main api for this
    stream = os.popen(v_command + 'showvminfo ' + vm_name)
    return stream.readlines()
# retrons a list of strings that, a sample output is provided

def modify(): pass

def delete_vm(): pass

def clone_vm(): pass

def pass_command(): pass