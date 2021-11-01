# Tools for token issuing

### [discover.py](https://github.com/IFS4205-AY21-22-Group4/token-issuing-tools/blob/master/discover/discover.py)

This is used to view MAC address of your BLE token. 

Upload token.ino to BLE token before using this script to find out MAC address of token, then use MAC address shown to update token.ino.

> Take note:
> This only works on Windows/Linux
> For this project, MacOS users can use a randomly generated MAC address and assume the MAC address entered into token.ino is physical token MAC address

#### Prerequisites:
 - Python
 - adafruit-blinka-bleio
 - adafruit-circuitpython-ble
 - gmsservice.py in python ble service area

#### To install packages:
```
pip install --upgrade adafruit-blinka-bleio adafruit-circuitpython-ble
```
Placing [gmsservice.py](https://github.com/IFS4205-AY21-22-Group4/token-issuing-tools/blob/master/discover/gmsservice.py) in the python ble service directory.

> On Windows:
>
> Place `gmsservice.py` in directory `C:\...........\Python38\site-packages\adafruit_ble\services`
>
> On macOS:
>
> Place `gmsservice.py` in directory `/opt/homebrew/lib/python3.8/site-packages/adafruit_ble/services/`
>
> On Linux:
>
> Place `gmsservice.py` in directory `~/.local/lib/python3.8/site-packages/adafruit_ble/services`


#### To run script:
```
python discover.py
```

### [token.ino](https://github.com/IFS4205-AY21-22-Group4/token-issuing-tools/blob/master/token/token.ino)

This is uploaded to the BLE dongle via Arduino IDE

```
const char* device_address = "<REPLACE WITH DEVICE MAC ADDRESS IN FORMAT xx:xx:xx:xx:xx:xx>";
```
Enter your device MAC ADDRESS before uploading to BLE token for use with gateway client.
