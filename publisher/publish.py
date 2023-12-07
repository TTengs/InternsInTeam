import random
import time
import paho.mqtt.publish as publish

filename = "publisher/tools.txt"
with open(filename, "r") as f:
   lines = f.readlines()
host = "localhost"

if __name__ == '__main__':
   starttime = time.monotonic()
   while True:
      result = random.choice(["accepted", "rejected"]).strip()
      tool = random.choice(lines).strip() if result == "rejected" else "null"
      timestamp = time.time_ns()
      machine = random.choice(["machine1", "machine2"])

      topicName = f"{machine}/lid/{result}"
      message = f"lid reason='{tool}',result='{result}' {timestamp}"
      print(f"Publishing message {message} to topic {topicName}")
      # publish a single message
      publish.single(topic=topicName, payload=message, hostname=host)

      time.sleep(1.0 - ((time.monotonic() - starttime) % 1.0))