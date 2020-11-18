from fastapi import FastAPI
import os
# import virtualbox

app = FastAPI()
# vbox = virtualbox.VirtualBox()

base_vms = ["192.168.1.56", "192.168.1.56"]

v_command = 'vboxmanage'

@app.get("/")
async def root():
    stream = os.popen(v_command + 'list vms')
    output = stream.readlines()
    return output


@app.get("/vms")
async def command():
    stream = os.popen(v_command + 'list vms')
    output = stream.readlines()
    return output

def stop_start():
    pass

def status(): pass

def depInf(): pass # if the v command was as same as thes status one, handle with adding a flag not endpoints

def modify(): pass

def delete_vm(): pass

def clone_vm(): pass

def pass_command(): pass