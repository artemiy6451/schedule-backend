"""Main fastapi app"""
from fastapi import FastAPI

app = FastAPI(title="Schedule backend")


@app.get("/")
def hello():
    return {"status": "succes"}
