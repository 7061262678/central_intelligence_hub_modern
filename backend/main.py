from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Central Intelligence Hub API Running"}

@app.get("/insights")
def insights():
    with open("../data/insights.json") as f:
        data = json.load(f)
    return data
