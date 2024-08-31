from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/pabbly")
async def handle_pabbly(request: Request):
    body = await request.json()
    data = body.get("data")
    return {"message": f"pabbly just sent you a message with data: {data}"}
