from pathlib import Path
import tomlkit
from utils.dotfile import dotfile_exists, resolve_dotfile_path, load_dotfile, write_dotfile


def update_url(doc: tomlkit.TOMLDocument, url: str) -> tomlkit.TOMLDocument:
    """Updates the url field in the parsed dotfile document."""
    doc["project"]["url"] = url
    return doc

def assign_url(url: str) -> Path:
    """Assigning function for updating dotfile with url."""
    path = resolve_dotfile_path()

    if not dotfile_exists(path):
        raise FileNotFoundError(str(path))

    doc = load_dotfile(path)
    doc = update_url(doc, url)
    write_dotfile(path, doc)

    return path
