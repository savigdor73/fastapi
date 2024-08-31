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
    return JSONResponse(content={}, headers={"Allow": "GET, POST, OPTIONS"}, status_code=200)

@app.get("/")
def handle_root():
    return {"message": "Hello, World!"}

@app.post("/pabbly")
async def handle_pabbly(request: Request):
    body = await request.json()
    print(f"Received data: {body}")
    return {"message": f"Pabbly just sent you a message with data: {body}"}
