from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# הוסף את ה-CORSMiddleware כדי לאפשר CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ניתן לשנות כדי לאפשר דומיינים ספציפיים בלבד
    allow_credentials=True,
    allow_methods=["*"],  # מאפשר את כל שיטות ה-HTTP
    allow_headers=["*"],  # מאפשר את כל הכותרות
)

@app.options("/")
def options_root():
    return JSONResponse(headers={"Allow": "GET, POST, OPTIONS"}, status_code=200)

@app.options("/pabbly")
def options_pabbly():
    return JSONResponse(headers={"Allow": "POST, OPTIONS"}, status_code=200)

@app.post("/pabbly")
async def handle_pabbly(request: Request):
    try:
        body = await request.json()
        data = body.get("data")
        if data is None:
            return JSONResponse(status_code=400, content={"error": "Missing 'data' field"})
        return {"message": f"pabbly just sent you a message with data: {data}"}
    except ValueError:
        return JSONResponse(status_code=400, content={"error": "Invalid JSON"})
