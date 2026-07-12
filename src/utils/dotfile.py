from pathlib import Path
import tomlkit
from utils.config import DOTFILE_NAME


def resolve_dotfile_path() -> Path:
    """Returns path to .sisyphus dotfile in current directory."""
    return Path.cwd() / DOTFILE_NAME

def dotfile_exists(dotfile_path: Path) -> bool:
    """Checks if a .sisyphus dotfile already exists at the given path."""
    return dotfile_path.exists()

def create_dotfile(path: Path, project_name: str) -> None:
    """Creates the .sisyphus dotfile with initial project data."""
    dotfile_path = path / DOTFILE_NAME

    doc = tomlkit.document()
    project_table = tomlkit.table()
    project_table["name"] = project_name
    project_table["url"] = ""
    doc["project"] = project_table

    with open(dotfile_path, "w") as f:
        tomlkit.dump(doc, f)

def load_dotfile(path: Path) -> tomlkit.TOMLDocument:
    """Reads and parses the dotfile."""
    with open(path, "r") as f:
        return tomlkit.load(f)

def write_dotfile(path: Path, doc: tomlkit.TOMLDocument) -> None:
    """Writes the updated document back to the dotfile."""
    with open(path, "w") as f:
        tomlkit.dump(doc, f)
