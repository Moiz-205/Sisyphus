import tomlkit
from utils.dotfile import resolve_dotfile_path, dotfile_exists, load_dotfile


def reveal_project() -> tomlkit.TOMLDocument:
    """Reveal function for displaying the content of the dotfile."""
    path = resolve_dotfile_path()

    if not dotfile_exists(path):
        raise FileNotFoundError(str(path))

    doc = load_dotfile(path)
    return doc
