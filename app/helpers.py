import requests
import json
import os

# key = os.environ["KEY"]

def list_lights():
    
    url = "https://developer-api.govee.com/v1/devices"

    payload={}
    headers = {
    'Govee-API-Key': key
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    val = response.text
    
    # print(response.text)
    return json.loads(val)

def toggle_light_on(light):
    config = list_lights()

    # val = 0 if action == "off" else action
    for device in config["data"]["devices"]:
        print(device)
        if device["deviceName"] == light:
            focus = device
    url = "https://developer-api.govee.com/v1/devices/control?="

    payload = json.dumps({
    "device": focus["device"],
    "model": focus["model"],
    "cmd": {
        "name": "turn", 
        "value": "on"
    }
    })
    headers = {
    'Govee-API-Key': key,
    'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    # print(response.text)
    return response.text

def toggle_light_off(light):
    config = list_lights()

    # val = 0 if action == "off" else action
    for device in config["data"]["devices"]:
        if device["deviceName"] == light:
            focus = device
    
    url = "https://developer-api.govee.com/v1/devices/control?="

    payload = json.dumps({
    "device": focus["device"],
    "model": focus["model"],
    "cmd": {
        "name": "turn", 
        "value": "off"
    }
    })
    headers = {
    'Govee-API-Key': key,
    'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    # print(response.text)
    return response.text

def toggle_all_off():
    config = list_lights()
    
    for device in config["data"]["devices"]:
        toggle_light_off(device["deviceName"])
    
    return "success"