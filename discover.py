import asyncio
from bleak import discover

def extractAddress(mac):
    address = mac.replace(':', '')
    return address

def printDetails(device):
    if option == 1:
        print("({})    {}    {}".format(extractAddress(device.address), device.address, device.name))
    if option == 2:
        if "IFS4205" in device.name:
            print("({})    {}    {}".format(extractAddress(device.address), device.address, device.name))

async def run():
    devices = await discover()
    print("(copy)            address              name")
    print("========================================================")
    for d in devices:
        printDetails(d)

option = 0
while (option != 1 and option != 2):
    print("(1) Display all nearby devices")
    print("(2) Display only IFS4205 devices")
    option = int(input())
    print()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
