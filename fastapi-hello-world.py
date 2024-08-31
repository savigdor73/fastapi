from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/pabbly")
def read_pabbly():
    return {"message": "pabbly just sent you a message"}
