import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    data = message.payload.decode()
    print(f"Received: {data} on topic {message.topic}")
    if float(data) > 24.0:
        print("ALERT: Temperature high! Activating cooling...")

# 1. Setup Client
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

# 2. Connect and Subscribe
client.connect("test.mosquitto.org", 1883)
client.subscribe("home/livingroom/temp")

print("Subscribed to 'home/livingroom/temp'. Waiting for data...")
client.loop_forever()
