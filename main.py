from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def get_datetime():
    return {"datetime": datetime.now()}

