from fastapi import FastAPI
from typing import Union
import re
from helpers import *
app = FastAPI()


@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/on/{light_name}")
def turn_on(light_name: str):
    light_name = re.sub("_", " ", light_name)
    val = toggle_light_on(light_name)
    return val

@app.get("/off/{light_name}")
def turn_off(light_name: str):
    light_name = re.sub("_", " ", light_name)
    val = toggle_light_off(light_name)
    return val

@app.get("/to_work")
def to_work():
    toggle_light_off("Bed light")
    toggle_light_on("Desk light")
    return list_lights()

@app.get("/to_bed")
def to_work():
    toggle_light_on("Bed light")
    toggle_light_off("Desk light")
    return list_lights()


@app.get("/lights")
def all_lights():
    return list_lights()

@app.get("/all_off")
def all_off():
    return toggle_all_off()