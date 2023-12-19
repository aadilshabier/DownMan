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
    items = models.get_items_from_file(DB_FILE)
    return items

@app.put("/add")
async def add(extra_items: list[models.DownloadItem]):
    items.extend(extra_items)
    print("Added:", extra_items)
    models.write_items_to_file(items, DB_FILE)

app.mount("/static", StaticFiles(directory="static"), name="static")
