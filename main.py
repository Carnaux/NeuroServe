import os
import glob
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/handshake")
def handshake():
    return {"status": "OK"}

@app.get("/listFiles")
def read_item():
    files = []
    for file in glob.glob("./static/*"):
        files.append(os.path.basename(file))
    return { "files": files}