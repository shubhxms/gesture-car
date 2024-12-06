# gesture-car
Code, demo and report for ECE504: Internet Of Things at [Ahmedabad University](https://ahduni.edu.in/).


## Brief
In this project we developed a robotic car that was controlled using hand gestures.

The robotic car had a raspberry pi (model 3) mounted on it which controlled four motors attached to four different wheels through two H-bridges.

The user has a glove which has a MPU6050 (accelerometer + gyrosope) attached on it and attached to an esp8266 microcontroller.

The esp8266 and the pi communicate using the [MQTT Protocol](https://mqtt.org/) - the pi simultaenously acts as both a broker and a subscriber client. The esp8266 publishes translated actions to the broker which is then subscribed to by the pi.


## Demo
https://github.com/user-attachments/assets/1cb01c62-5ef6-41f1-9199-5d7717a43cb2



## Group Members:
- Aarya Parekh
- Preksha Morbia
- Shubham Shah (me)

This repository is only an archive; as such the commit history does not accurately represent the contributions of the members.
