import network 
import time 
import dht 
from machine import Pin 
from umqtt.simple import MQTTClient 
import json 
 
# Thông tin WiFi 
SSID = "Wokwi-GUEST" 
PASSWORD = "" 
 
# Thông tin MQTT 
MQTT_BROKER = "broker.hivemq.com" 
MQTT_PORT = 1883 
MQTT_CLIENT_ID = "esp32_khdl" 
MQTT_TOPIC = "iot/khdl/esp32" 
 
# Kết nối Wi-Fi 
def connect_wifi(): 
    wlan = network.WLAN(network.STA_IF) 
    wlan.active(True) 
    if not wlan.isconnected(): 
        print("Đang kết nối WiFi...") 
        wlan.connect(SSID, PASSWORD) 
        while not wlan.isconnected(): 
            time.sleep(1) 
    print("Kết nối WiFi thành công. IP:", wlan.ifconfig()[0]) 
 
# Đọc dữ liệu từ DHT22 
def read_sensor(): 
    d = dht.DHT22(Pin(15)) 
    d.measure() 
    temp = d.temperature() 
    hum = d.humidity() 
    return temp, hum 
 
# Kết nối và gửi MQTT 
def connect_mqtt(): 
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT) 
    client.connect() 
    print("Kết nối MQTT thành công!") 
    return client 
# Main 
connect_wifi() 
mqtt_client = connect_mqtt() 
from collections import OrderedDict 
while True: 
  temp, hum = read_sensor() 
  '''data = { 
  "temperature": temp, 
  "humidity": hum, 
  "timestamp": time.time() # thời gian hiện tại (giây UNIX) 
  }''' 
  data = OrderedDict() 
  data["temperature"] = temp 
  data["humidity"] = hum 
  data["timestamp"] = time.time() 
  json_data = json.dumps(data) 
  mqtt_client.publish(MQTT_TOPIC, json_data) 
  print("Đã gửi:", json_data) 
  time.sleep(2) 