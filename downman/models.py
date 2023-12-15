from pydantic import BaseModel

class DownloadItem(BaseModel):
    url: str
    name: str | None
    completed: bool = False

items: list[DownloadItem] = [
    DownloadItem(url="hello/world1.txt", name="world1.txt"),
    DownloadItem(url="hello/world2.txt", name="world2.txt"),
]
