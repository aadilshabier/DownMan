from pydantic import BaseModel
import os

class DownloadItem(BaseModel):
    url: str
    name: str | None
    completed: bool = False


def get_items_from_file(file: str) -> list[DownloadItem]:
    result: list[DownloadItem] = []
    with open(file, "r") as f:
        for line in f.readlines():
            split = line.split(',')
            if len(split) > 1:
                result.append(DownloadItem(url=split[0], name=split[1].rstrip()))
            elif len(split) == 1 and split[0]: # case for empty line
                result.append(DownloadItem(url=split[0]))
    return result

def write_items_to_file(items: list[DownloadItem], file: str):
    with open(file, "w") as f:
        for item in items:
            f.write(f"{item.url},{item.name}\n")
