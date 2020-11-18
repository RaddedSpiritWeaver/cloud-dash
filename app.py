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
    stream = os.popen(v_command + 'list vms')
    output = stream.readlines()
    return output

@app.get("/power")
def stop_start(stop: bool, vm_name: str):
    stream = None
    if stop:
        command = "controlvm "
        subcommand = " poweroff"
        stream = os.popen(v_command + command + vm_name + subcommand)
    else:
        command = "startvm "
        stream = os.popen(v_command + command + vm_name)

    return stream.readlines()

@app.get("status")
def status():
    # return a list of vm names and their status
    pass


def depInf(): pass # if the v command was as same as thes status one, handle with adding a flag not endpoints

def modify(): pass

def delete_vm(): pass

def clone_vm(): pass

def pass_command(): pass