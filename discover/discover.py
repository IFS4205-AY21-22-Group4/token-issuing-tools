from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.gmsservice import GMS
import platform

def connect_token(entry, radio):
    if GMS in entry.services:
        GMS_connection = radio.connect(entry)
        if GMS_connection and GMS_connection.connected:
            response = GMS_connection[GMS].readline().decode("utf-8")
    GMS_connection.disconnect()
    return response

def scan():
    radio = BLERadio()
    found = set()
    for entry in radio.start_scan(ProvideServicesAdvertisement, timeout=10, minimum_rssi=-80):
        addr = entry.address.string
        name = entry.complete_name
        if addr not in found and name != None and "IFS4205" in name:
            if platform.system() == 'Darwin':
                addr = connect_token(entry, radio)
                found.add(addr)
            else:
                found.add(addr)
            print("{} | {}".format(addr.lower(), name))
            
    return found

if __name__ == "__main__":
    print("address           | name")
    print("==================|================")
    tokens = scan()
    