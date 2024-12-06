// ------------- MQTT Imports -----------------


#include "PubSubClient.h" // Connect and publish to the MQTT broker
#include "ESP8266WiFi.h"  // Enables the ESP8266 to connect to the local network (via WiFi)


// ------------- MQTT Imports -----------------
// ------------- Hand Imports -----------------


#include <MPU6050.h>


// ------------- Hand Imports -----------------


// ------------- MQTT Helpers -----------------


String currState = "";


// WiFi
const char* ssid = "aarya";                 // Your personal network SSID
const char* wifi_password = "12345678"; // Your personal network password


// MQTT
const char* mqtt_server = "172.20.10.3";  // IP of the MQTT broker
const char* hand_topic = "esp8266/hand";
// const char* head_topic = "esp8266/head";
const char* mqtt_username = "admin"; // MQTT username
const char* mqtt_password = "admin"; // MQTT password
const char* clientID = "esp8266"; // MQTT client ID


// Initialise the WiFi and MQTT Client objects
WiFiClient wifiClient;
// 1883 is the listener port for the Broker
PubSubClient client(mqtt_server, 1883, wifiClient);


void connect_MQTT() {
 Serial.print("Connecting to ");
 Serial.println(ssid);


 // Connect to the WiFi
 WiFi.begin(ssid, wifi_password);


 // Wait until the connection has been confirmed before continuing
 while (WiFi.status() != WL_CONNECTED) {
   delay(50);
   Serial.print(".");
 }


 // Debugging - Output the IP Address of the ESP8266
 Serial.println("WiFi connected");
 Serial.print("IP address: ");
 Serial.println(WiFi.localIP());


 // Connect to MQTT Broker
 // client.connect returns a boolean value to let us know if the connection was successful.
 // If the connection is failing, make sure you are using the correct MQTT Username and Password (Setup Earlier in the Instructable)
 if (client.connect(clientID)) {
   Serial.println("Connected to MQTT Broker!");
 }


 else {
   Serial.println("Connection to MQTT Broker failed...");
 }
}


// ------------- MQTT Helpers -----------------
// ------------- Hand Helpers -----------------


MPU6050 mpu;
String readCommand() {
  Vector normAccel = mpu.readNormalizeAccel();


 if (normAccel.XAxis < -5) {
   return "Forward";
 } else if (normAccel.XAxis > 5) {
   return "Backward";
 } else if (normAccel.YAxis > 5) {
   return "Right";
 } else if (normAccel.YAxis < -5) {
   return "Left";
 } else {
   return "Halt";
 }
}


// ------------- Hand Helpers -----------------


void setup() {
  // ------------- MQTT Setup ---------------


 connect_MQTT();


 // ------------- MQTT Setup -----------------
 // ------------- Hand Setup -----------------
  // put your setup code here, to run once:
 Serial.begin(115200);


 Serial.println("Initialize MPU6050");


 while(!mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G))
 {
   Serial.println("Could not find a valid MPU6050 sensor, check wiring!");
   delay(500);
 }


 // ------------- Hand Setup -----------------
}


void loop() {
 // put your main code here, to run repeatedly:
 while (WiFi.status() != WL_CONNECTED) {
   connect_MQTT();
 }


 String newState = readCommand();
 if (newState != currState) {
   if (client.publish(hand_topic, newState.c_str())) {
     Serial.print("State Updated to ");
     Serial.println(newState);
     currState = newState;
   }
 }
 delay(10);
}
