import random
import time
from paho.mqtt import client as mqtt_client


filename = "./tools.txt"

host = "mqtt"
broker = 'mqtt'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

if __name__ == '__main__':

   with open(filename, "r") as f:
      lines = f.readlines()

   client = connect_mqtt()

   starttime = time.monotonic()
   while True:
      result = random.choice(["accepted", "rejected"]).strip()
      tool = random.choice(lines).strip()
      timestamp = int(time.time() * 1_000_000_000)
      machine = random.choice(["machine1", "machine2"])

      topicName = f"{machine}/lid"
      message = f'lid reason="{tool}",result="{result}" {timestamp}'

      # print(f"Publishing message {message} to topic {topicName}")
      # publish a single message
      client.publish(topicName, message)

      time.sleep(1.0 - ((time.monotonic() - starttime) % 1.0))