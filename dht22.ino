//sigfox declarations


#include <SigFox.h>
#include <ArduinoLowPower.h>
#include <RTCZero.h>
#define SLEEPTIME     5 * 60 * 1000   // Delay: X minutes (X min x 60 seconds x 1000 milliseconds)
int moduleTemp;

volatile int alarm_source = 0;  //variable for sleep mode

//moisture sensor definations
int dryValue = 0;
int wetValue = 1023;
int friendlyDryValue = 0;
int friendlyWetValue = 100;

int rawValue ;
//humidity sensor
#include <DHT.h>
#include <DHT_U.h>
#define DHTPIN 1   // Digital pin connected to the DHT sensor 
#define DHTTYPE    DHT22     // DHT 22 (AM2302)
DHT_Unified dht(DHTPIN, DHTTYPE);

void read_DHT(void);
void readMoisture(void);

float temp = 0.0, hum = 0.0;
uint32_t delayMS;


void setup() {
  dht.begin();
  Serial.begin(115200);
  LowPower.attachInterruptWakeup(RTC_ALARM_WAKEUP, alarmEvent0, CHANGE);  //interrupt for wake-up from sleep
  SigFox.begin();
  if (!SigFox.begin()) {
    Serial.println("Something is wrong, try rebooting device");
    SigFox.reset();
    while (1);
  }
}
void alarmEvent0() // Interrupt to wake-up Device from SLEEP
{
  alarm_source = 0;
}
void loop() {
  ReadDHT();
  LowPower.sleep(SLEEPTIME);
  // put your main code here, to run repeatedly:

}

void ReadDHT()
{
  float Mkr_temp = 0.0;
  // Delay between measurements.
  delay(delayMS);
  // Get temperature event and print its value.
  sensors_event_t event;
  dht.temperature().getEvent(&event);
  temp = event.temperature;
  if (isnan(temp)) {
    Serial.println(F("Error reading temperature!"));
  }
  else {
    //Serial.print(F("Temperature: "));
    Serial.println(temp);
    //Serial.println(F("°C"));
  }
  // Get humidity event and print its value.
  dht.humidity().getEvent(&event);
  hum = event.relative_humidity;
  if (isnan(hum)) {
    Serial.println(F("Error reading humidity!"));
  }
  else {
    // Serial.print(F("Humidity: "));
    Serial.println(hum);
    //Serial.println(F("%"));
  }
  delay(100);

  //measuring internal temperature
  moduleTemp = SigFox.internalTemperature();
  if (isnan(moduleTemp)) {   // Check if reading T/H was okay
    Serial.println("Failed to read the internal temperature!");
    return;
  }
  // SigFox.write(moduleTemp);  // Send the temperature to backend.sigfox.com
  //SigFox.end();

 //int rawValue = analogRead(A0);
 //int friendlyValue = map(rawValue, dryValue, wetValue, friendlyDryValue, friendlyWetValue);
 //delay(50);
  
  float packed[75] = {temp, hum, moduleTemp};
  SigFox.begin();
  SigFox.beginPacket();
  SigFox.write((uint8_t*)&packed, 12);
  int ret = SigFox.endPacket();

}