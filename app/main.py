from fastapi import FastAPI

app = FastAPI(title="OnsiteWash Backend")

@app.get("/")
def health():
    return {"status": "running"}
