from pathlib import Path
import tomlkit
from utils.config import DOTFILE_NAME


def resolve_project_path(name: str | None = None) -> Path:
    """Returns the target project path."""
    current_dir = Path.cwd()

    if name:
        return current_dir / name
    else:
        return current_dir

def create_project_dir(path: Path) -> None:
    """Create the project directory if it doesn't already exist."""
    path.mkdir(parents=True, exist_ok=True)

def dotfile_exists(path: Path) -> bool:
    """Checks if a .sisyphus dotfile already exists at the given path."""
    dotfile_path = path / DOTFILE_NAME
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

def init_project(name: str | None = None) -> None:
    """Initialization function for project directory and dotfile creation."""
    path = resolve_project_path(name)
    create_project_dir(path)

    if dotfile_exists(path):
        raise FileExistsError(f"Project already initialized at {path}")

    create_dotfile(path, project_name=name or path.name)
    print(f"Initialized sisyphus project at {path}")
