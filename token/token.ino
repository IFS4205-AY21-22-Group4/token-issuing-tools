#include <RFduinoBLE.h>
#include <time.h>

const char* device_name = "IFS4205-E9FCCD620A49";
const char* device_address = "e9:fc:cd:62:0a:49";

void setup() {
  RFduinoBLE.deviceName = device_name;
  RFduinoBLE.begin();
}

void RFduinoBLE_onConnect() {
   Serial.println("Start connection..."); 
}

void loop() {
  RFduino_ULPDelay(SECONDS(1));
  RFduinoBLE.send(device_address, 17);
}
