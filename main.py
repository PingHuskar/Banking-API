from typing import Union

from fastapi import FastAPI, Body, Request
import json
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/users")
def alluser():
    with open("userdb.json", "r") as jsonFile:
        jsonData = json.load(jsonFile)
    return jsonData

@app.get("/users/{head}")
def headuser(head: int):
    with open("userdb.json", "r") as jsonFile:
        jsonData = json.load(jsonFile)
    return jsonData[0:head]

@app.get("/user/{id}")
def find_user(id: int):
    with open("userdb.json", "r") as jsonFile:
        jsonData = json.load(jsonFile)
    for user in jsonData:
        if user["id"] == id:
            return user["name"]
    return "Bank Account Not Found"

@app.put("/deposit/{id}/{amount}")
def deposit_user(id: int,amount: int):
    with open("userdb.json", "r") as jsonFile:
        jsonData = json.load(jsonFile)
    for user in jsonData:
        if user["id"] == id:
            return user["balance"]
            # return user["name"] + user["balance"]