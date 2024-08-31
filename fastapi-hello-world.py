from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.options("/")
def options_root():
    return JSONResponse(headers={"Allow": "GET, POST, OPTIONS"}, status_code=200)
    
@app.post("/pabbly")
async def handle_pabbly(request: Request):
    body = await request.json()
    data = body.get("data")
    return {"message": f"pabbly just sent you a message with data: {data}"}
