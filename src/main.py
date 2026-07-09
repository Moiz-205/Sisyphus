from pathlib import Path


def resolve_project_path(name: str | None = None) -> Path:
    """Returns the target project path.

    If a name is given, returns cwd/name (new subdir).
    If no name is given, returns cwd (use current dir).
    """
    current_dir = Path.cwd()

    if name:
        return current_dir / name
    else:
        return current_dir


if __name__ == "__main__":
    print(resolve_project_path())
    print(resolve_project_path("test-project"))
