#include <RFduinoBLE.h>

const char* device_name = "IFS4205";
const char* device_address = "<REPLACE WITH DEVICE MAC ADDRESS IN FORMAT xx:xx:xx:xx:xx:xx>";

void setup() {
  RFduinoBLE.deviceName = device_name;
  RFduinoBLE.begin();
}

void RFduinoBLE_onConnect() {
}

void loop() {
  RFduino_ULPDelay(SECONDS(1));
  RFduinoBLE.send(device_address, 17);
}
