from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

@app.get("/")
async def get_index():
    return FileResponse("index.html")

@app.get("/logo")
async def get_logo():
    return FileResponse("logo.jpg")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)