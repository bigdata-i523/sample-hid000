import paho.mqtt.client as mqtt 
import time


def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

def on_log(client, userdata, level, buf):
    print("log: ",buf)

broker_address="localhost"    
# broker_address="test.mosquitto.org"
# broker_address="broker.hivemq.com"
# broker_address="iot.eclipse.org"

print("creating new instance")
client = mqtt.Client("i523") #create new instance
client.on_log=on_log
client.on_message=on_message #attach function to callback

print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop

print("Subscribing to topic","robot/leds/led1")
client.subscribe("robot/leds/led1")

print("Publishing message to topic","robot/leds/led1")
client.publish("robot/leds/led1","OFF")

time.sleep(4) # wait
client.loop_stop() #stop the loop
