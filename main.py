from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def index():
    return {"message": "Hello, World"}

@app.get("/home/{name}")
def print_name(name: str, q: Union[str,None] = None):
    return {"message": f"Hello, {name}, q: {q}"}