from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from . import models

app = FastAPI()
items: list[models.DownloadItem] = models.get_items_from_file("file.db")

DB_FILE = "file.db"

# Return index.html
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def root():
    return RedirectResponse("/static/index.html")

# API endpoints
@app.get("/status")
async def status() -> list[models.DownloadItem]:
    return models.items

app.mount("/static", StaticFiles(directory="static"), name="static")
