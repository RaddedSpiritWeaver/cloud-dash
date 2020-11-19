from fastapi import FastAPI
import time
import vboxapi
import virtualbox
import os
from datetime import datetime
import subprocess

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
    vm_name = '\'{}\''.format(vm_name)
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
    # vm_name = '\'{}\''.format(vm_name)
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
    vm_name = '\'{}\''.format(vm_name)
    stream = os.popen(v_command + 'showvminfo ' + vm_name)
    return stream.readlines()
# retrons a list of strings that, a sample output is provided

@app.get("/modify")
def modify(vm_name: str, cpus: int = None, memory: int = None):
    # vm_name = '\'{}\''.format(vm_name)
    process = subprocess.Popen(["vboxmanage", 'modifyvm', vm_name, "--cpus", str(cpus), "--memory", str(memory)])
    stdout, stderr = process.communicate()
    return None

def delete_vm(): pass

@app.get("/clone")
def clone_vm(vm_name: str):
    old_dir = os.getcwd()
    os.chdir("/home/spiritweaver/VirtualBox VMs/")
    base_store = "clones/"
    current_time = datetime.now()
    name = "{}{}_{}.ova".format(base_store, vm_name, current_time)
    # name = 
    process = subprocess.Popen(['vboxmanage', 'export', vm_name, '-o', name])
    stdout, stderr = process.communicate()
    print("starting wait")
    time.sleep(5)
    os.popen(v_command + "import " + '\''+ name + '\'')
    os.chdir(old_dir)
    return name
    

def pass_command(): pass