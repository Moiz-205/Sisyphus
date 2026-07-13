from pathlib import Path
from utils.dotfile import dotfile_exists, create_dotfile
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

def init_project(name: str | None = None) -> Path:
    """Initialization function for project directory and dotfile creation."""
    path = resolve_project_path(name)
    create_project_dir(path)

    dotfile_path = path / DOTFILE_NAME
    if dotfile_exists(dotfile_path):
        raise FileExistsError(str(path))

    create_dotfile(path, project_name=name or path.name)
    return path
