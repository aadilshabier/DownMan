from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return RedirectResponse("/static/index.html")

app.mount("/static", StaticFiles(directory="static"), name="static")
